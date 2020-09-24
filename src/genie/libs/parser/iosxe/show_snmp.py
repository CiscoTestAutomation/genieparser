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

