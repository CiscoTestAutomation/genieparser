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



# ====================
# Schema for:
#  * 'show snmp group'
# ====================
class ShowSnmpGroupSchema(MetaParser):
    """Schema for show snmp group."""

    schema = {
        Optional(int): {
            "groupname": str,
            "sec_model": str,
            Optional("contextname"): str,
            Optional("storage_type"): str,
            "readview": str,
            "writeview": str,
            "notifyview": str,
            "row_status": {
                "status": str,
                Optional("access_list"): str
            }
        }
        
    }


# ====================
# Parser for:
#  * 'show snmp group'
# ====================
class ShowSnmpGroup(ShowSnmpGroupSchema):
    """Parser for show snmp group"""

    cli_command = 'show snmp group'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        else:
            output = output

        # groupname: 2c                               security model:v1 
        # contextname: <no context specified>         storage-type: volatile
        # readview : <no readview specified>          writeview: <no writeview specified>        
        # notifyview: *tv.FFFF58bf.eaFF58bf.eaFFFFFF.F
        # row status: active
        #
        # groupname: ag-ro                           security model:v1 
        # contextname: <no context specified>         storage-type: volatile
        # readview : v1default                        writeview: <no writeview specified>        
        # notifyview: *tv.FFFF58bf.eaFF58bf.eaFFFFFF.F
        # row status: active
        #
        # groupname: AlfaV                    security model:v2c 
        # contextname: <no context specified>         storage-type: permanent
        # readview : v1default                        writeview: <no writeview specified>        
        # notifyview: <no notifyview specified>       
        # row status: active	access-list: 90

        # groupname: 2c                               security model:v1
        p_group = re.compile(r"^groupname:\s+(?P<group>\S+)\s+security model:(?P<security>.*)$")

        # contextname: <no context specified>         storage-type: permanent
        p_context_none = re.compile(r"^contextname:\s+<no context specified>\s+storage-type:\s+(?P<storage>\S+)$")

        # contextname: Alfa         storage-type: permanent
        p_context = re.compile(r"^contextname:\s+(?P<context>\S+)\s+storage-type:\s+(?P<storage>\S+)$")

        # readview : <no readview specified>          writeview: <no writeview specified>   
        p_rw_none = re.compile(r"^readview :\s+<no readview specified>\s+writeview:\s+<no writeview specified>$")

        # readview : v1default                        writeview: <no writeview specified>
        p_r_wnone = re.compile(r"^readview :\s+(?P<read>\S+)\s+writeview:\s+<no writeview specified>$")

        # readview : v1default                        writeview: v1default
        p_rw = re.compile(r"^readview :\s+(?P<read>\S+)\s+writeview:\s+(?P<write>\S+)$")

        # notifyview: <no notifyview specified>
        p_notify_none = re.compile(r"^notifyview: <no notifyview specified>$")

        # notifyview: *tv.FFFF58bf.eaFF58bf.eaFFFFFF.F
        p_notify = re.compile(r"^notifyview:\s+(?P<notify>\S+)$")

        # row status: active	access-list: 90
        p_row = re.compile(r"^row\s+status:\s+active$")

        # row status: active	access-list: 90
        p_row_ac = re.compile(r"^row\s+status:\s+active\s+access-list:\s+(?P<access>\S+)$")


        index = 0
        show_snmp_groups_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # groupname: 2c                               security model:v1
            if p_group.match(line):
                match = p_group.match(line)
                index += 1
                groupname = match.group("group")
                security = match.group("security")
                show_snmp_groups_dict.update({index: {}})
                show_snmp_groups_dict[index].update({"groupname": groupname, "sec_model": security})
                continue
            # contextname: <no context specified>         storage-type: permanent
            elif p_context_none.match(line):
                match = p_context_none.match(line)
                storage = match.group("storage")
                show_snmp_groups_dict[index].update({"contextname" : "none", "storage_type" : storage})
                continue
            # contextname: context1         storage-type: volatile
            elif p_context.match(line):
                match = p_context_none.match(line)
                context = match.group("context")
                storage = match.group("storage")
                show_snmp_groups_dict[index].update({"contextname" : context, "storage_type" : storage})
                continue
            # readview : <no readview specified>          writeview: <no writeview specified>  
            elif p_rw_none.match(line):
                show_snmp_groups_dict[index].update({"readview" : "none", "writeview" : "none"})
                continue
            # readview : v1default          writeview: <no writeview specified> 
            elif p_r_wnone.match(line):
                match = p_r_wnone.match(line)
                readview = match.group("read")
                show_snmp_groups_dict[index].update({"readview" : readview, "writeview": "none"})
                continue
            # readview : v1default                        writeview: v1default
            elif p_rw.match(line):
                match = p_rw.match(line)
                readview = match.group("read")
                writeview = match.group("write")
                show_snmp_groups_dict[index].update({"readview" : readview, "writeview": writeview})
                continue
            # notifyview: <no notifyview specified> 
            elif p_notify_none.match(line):
                show_snmp_groups_dict[index].update({"notifyview" : "none"})
                continue
            # notifyview: *tv.FFFF58bf.eaFF58bf.eaFFFFFF.F
            elif p_notify.match(line):
                match = p_notify.match(line)
                notify = match.group("notify")
                show_snmp_groups_dict[index].update({"notifyview" : notify})
                continue
            # row status: active	access-list: 90
            elif p_row_ac.match(line):
                match = p_row_ac.match(line)
                status = "active"
                access_list = match.group("access")
                show_snmp_groups_dict[index]["row_status"] = {"status" : status, "access_list": access_list}
                continue
            # row status: active	access-list: 90
            elif p_row.match(line):
                p_row.match(line)
                status = "active"
                show_snmp_groups_dict[index]["row_status"] = {"status" : status}
        return show_snmp_groups_dict
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
        p_user = re.compile(r"^User\s+name:\s+(?P<user>\S+)$")

        # Engine ID: 800000090300002790FBCF00
        p_engine = re.compile(r"^Engine\s+ID:\s+(?P<engine>\S+)$")

        # storage-type: nonvolatile   active access-list: 69
        p_storage_access = re.compile(r"^storage-type:\s(?P<storage>\S+)\s+active\s+access-list:\s+(?P<access>.*)$")

        # storage-type: nonvolatile         active
        p_storage = re.compile(r"^storage-type:\s(?P<storage>\S+)\s+active$")

        # Authentication Protocol: SHA
        p_auth = re.compile(r"^Authentication\s+Protocol:\s+(?P<auth>\S+)$")

        # Privacy Protocol: AES256
        p_priv = re.compile(r"^Privacy\s+Protocol:\s+(?P<priv>\S+)$")

        # Group-name: group1
        p_group = re.compile(r"^Group-name:\s+(?P<group>\S+)$")


        snmp_user_obj = {}
        current_loop_user = ""

        for line in output.splitlines():
            line = line.strip()
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
