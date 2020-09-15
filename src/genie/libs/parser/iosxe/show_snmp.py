''' show_snmp.py

IOSXE parsers for the following show commands:
    * show snmp mib
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ==========================
# Schema for 'show snmp mib'
# ==========================
class ShowSnmpMibSchema(MetaParser):

    ''' Schema for "show snmp mib" '''

    schema = {
        Any(): 
            {Optional(Any()): 
                {Optional(Any()): str,
                },
            },
        }


# ==========================
# Parser for 'show snmp mib'
# ==========================
class ShowSnmpMib(ShowSnmpMibSchema):

    ''' Parser for "show snmp mib" '''

    cli_command = 'show snmp mib'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # lldpLocalSystemData.1
        # dot3adAggPortDebugPartnerSyncTransitionCount
        p1 = re.compile(r'^(?P<snmp>([a-zA-Z0-9]+))(?:\.(?P<num>(\d+)))?$')

        # optIfObjects.1.1.1
        # mib-10.49.1.3.1.1.9
        # rmon.10.76.1.1
        # rmon.19.1
        p2 = re.compile(r'^(?P<snmp>([a-zA-Z0-9\-\.]+))$')

        for line in out.splitlines():
            line = line.strip()

            # lldpLocalSystemData.1
            # dot3adAggPortDebugPartnerSyncTransitionCount
            m = p1.match(line)
            if m:
                group = m.groupdict()
                item_dict = ret_dict.setdefault(group['snmp'], {})
                if group['num']:
                    num_dict = item_dict.setdefault(group['num'], {})
                continue

            # rmon.19.1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                item_dict = ret_dict.setdefault(group['snmp'], {})
                continue

        return ret_dict

# ===================
# Schema for:
#  * 'show snmp user'
# ===================
class ShowSnmpUserSchema(MetaParser):
    """Schema for show snmp user."""

    schema = { 
        "user_name" : {
             Any(): {
                Optional("access_list"): str,
                "auth_protocol": str,
                "engine_id": str,
                "group_name": str,
                "priv_protocol": str,
                "storage_type": str
            }
        }
    }


# ===================
# Parser for:
#  * 'show snmp user'
# ===================
class ShowSnmpUser(ShowSnmpUserSchema):
    """Parser for show snmp user"""

    cli_command = "show snmp user"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        else: 
            output = output

        # User name: SNMPv3-alfa
        # Engine ID: 800000090300002790FBCF00
        # storage-type: nonvolatile	 active
        # Authentication Protocol: SHA
        # Privacy Protocol: AES128
        # Group-name: ALFA
        #
        # User name: nmsops
        # Engine ID: 00000063000100A20A101B3E
        # storage-type: nonvolatile	 active	access-list: 69
        # Authentication Protocol: MD5
        # Privacy Protocol: DES
        # Group-name: nmcigroup

        # User name: SNMPv3-alfa
        user_capture = "(?P<user>\S+)"
        p_user = re.compile("User\s+name:\s+{user_capture}".format(user_capture=user_capture))

        # Engine ID: 800000090300002790FBCF00
        engine_capture = "(?P<engine>\S+)"
        p_engine = re.compile("Engine\s+ID:\s+{engine_capture}".format(engine_capture=engine_capture))

        # storage-type: nonvolatile   active access-list: 69
        storage_capture = "(?P<storage>\S+)"
        access_capture = "(?P<access>.*)"
        p_storage_access = re.compile("storage-type:\s{storage_capture}\s+active\s+access-list:\s+{access_capture}".format(storage_capture=storage_capture, access_capture=access_capture))

        # storage-type: nonvolatile         active
        p_storage = re.compile("storage-type:\s{storage_capture}\s+active".format(storage_capture=storage_capture))

        # Authentication Protocol: SHA
        auth_capture = "(?P<auth>\S+)"
        p_auth = re.compile("Authentication\s+Protocol:\s+{auth_capture}".format(auth_capture=auth_capture))

        # Privacy Protocol: AES256
        priv_capture = "(?P<priv>\S+)"
        p_priv = re.compile("Privacy\s+Protocol:\s+{priv_capture}".format(priv_capture=priv_capture))

        # Group-name: group1
        group_capture = "(?P<group>\S+)"
        p_group = re.compile("Group-name:\s+{group_capture}".format(group_capture=group_capture))


        snmp_user_obj = {}
        current_loop_user = ""

        for line in output.splitlines():
            # User name: SNMPv3-alfa
            if p_user.match(line):
                match = p_user.match(line)
                current_loop_user = match.group("user")
                if not snmp_user_obj.get("user_name", {}):
                    snmp_user_obj["user_name"] = {}
                snmp_user_obj["user_name"].update({current_loop_user: {}})
                continue
            # Engine ID: 800000090300002790FBCF00
            elif p_engine.match(line):
                match = p_engine.match(line)
                snmp_user_obj["user_name"][current_loop_user]["engine_id"] = match.group("engine")
                continue
            # storage-type: nonvolatile   active access-list: 69
            elif p_storage_access.match(line):
                match = p_storage_access.match(line)
                snmp_user_obj["user_name"][current_loop_user]["storage_type"] = match.group("storage")
                snmp_user_obj["user_name"][current_loop_user]["access_list"] = match.group("access")
                continue
            # storage-type: nonvolatile         active
            elif p_storage.match(line):
                match = p_storage.match(line)
                snmp_user_obj["user_name"][current_loop_user]["storage_type"] = match.group("storage")
                continue
            # Authentication Protocol: SHA
            elif p_auth.match(line):
                match = p_auth.match(line)
                snmp_user_obj["user_name"][current_loop_user]["auth_protocol"] = match.group("auth")
                continue
            # Privacy Protocol: AES256
            elif p_priv.match(line):
                match = p_priv.match(line)
                snmp_user_obj["user_name"][current_loop_user]["priv_protocol"] = match.group("priv")
                continue
            # Group-name: group1
            elif p_group.match(line):
                match = p_group.match(line)
                snmp_user_obj["user_name"][current_loop_user]["group_name"] = match.group("group")

        return snmp_user_obj
