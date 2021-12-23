''' show_snmp.py

IOSXE parsers for the following show commands:
    * show snmp mib
    * show snmp
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common

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



# ==========================
# Schema for 'show snmp'
# ==========================
class ShowSnmpSchema(MetaParser):

    ''' Schema for "show snmp" '''

    schema = {
        "chassis": str,
        "contact": str,
        Optional("location"): Optional(str),
        "snmp_input": {
            "packet_count": int,
            "bad_snmp_version_errors": int,
            "unknown_community_name": int,
            "illegal_operation_for_community_name_supplied": int,
            "encoding_errors": int,
            "number_of_requested_variables": int,
            "number_of_altered_variables": int,
            "get_request_pdus": int,
            "get_next_pdus": int,
            "set_request_pdus": int,
            "input_queue_drops": int,
            "maximum_queue_size": int
        },
        "snmp_output": {
            "packet_count": int,
            "too_big_errors": int,
            "maximum_packet_size": int,
            "no_such_name_errors": int,
            "bad_value_errors": int,
            "general_errors": int,
            "response_pdus": int,
            "trap_pdus": int
        },
        Optional("snmp_input_queue"): int,
        Optional("snmp_global_trap"): str,
        "snmp_logging" : {
            "status": str,
            Optional("endpoints") : {
                Optional(Any()) : {
                    Optional("port") : int,
                    Optional("queue"): int,
                    Optional("queue_size"): int,
                    Optional("sent"): int,
                    Optional("dropped"): int
                }
            }
        }
    }

# ==========================
# Parser for 'show snmp'
# ==========================
class ShowSnmp(ShowSnmpSchema):

    ''' Parser for "show snmp" '''

    exclude = ["buffer"]

    cli_command = 'show snmp'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        # Chassis: FCE2310A48M
        # Contact: "something@cisco.com"
        # Location: "To be filled in"
        # 35072424 SNMP packets input
        #     0 Bad SNMP version errors
        #     2089 Unknown community name
        #     68 Illegal operation for community name supplied
        #     0 Encoding errors
        #     341796946 Number of requested variables
        #     7328 Number of altered variables
        #     954173 Get-request PDUs
        #     31072480 Get-next PDUs
        #     3878 Set-request PDUs
        #     0 Input queue packet drops (Maximum queue size 1000)
        # 35598123 SNMP packets output
        #     0 Too big errors (Maximum packet size 1500)
        #     1 No such name errors
        #     0 Bad values errors
        #     0 General errors
        #     322899 Response PDUs
        #     527788 Trap PDUs
        # Packets currently in SNMP process input queue: 0
        # SNMP global trap: enabled
        #
        # SNMP logging: enabled
        #     Logging to 10.76.1.12.151, 0/10, 102045 sent, 3065 dropped.
        #     Logging to 10.76.133.10.111, 0/10, 102045 sent, 3065 dropped.
        #     Logging to 10.16.154.186.169, 0/10, 201075 sent, 11383 dropped.
        #     Logging to 10.166.67.19.108, 0/10, 102045 sent, 3065 dropped.

        # Chassis: FCE2310A48M
        p_chassis = re.compile(r"Chassis:\s+(?P<chassis>\S+)$")

        # Contact: "something@cisco.com"
        p_contact = re.compile(r"Contact:\s+(?P<contact>\S+)")

        # Location: "To be filled in"
        p_location_not_filled = re.compile(r"Location:\s+\"To\s+be\s+filled\s+in\"$")
        p_location = re.compile(r"Location:\s+(?P<location>.*)$")

        # 35072424 SNMP packets input
        p_input_count = re.compile(r"^(?P<input_count>\d+)\s+SNMP\s+packets\s+input$")

        # 0 Bad SNMP version errors
        p_input_bad = re.compile(r"^(?P<input_bad>\d+)\s+Bad\s+SNMP\s+version\s+errors$")

        # 2089 Unknown community name
        p_input_unknown = re.compile(r"^(?P<input_unknown>\d+)\s+Unknown\s+community\s+name$")

        # 68 Illegal operation for community name supplied
        p_input_illegal = re.compile(r"(?P<input_illegal>\d+)\s+Illegal\s+operation\s+for\s+community\s+name\s+supplied$")

        # 0 Encoding errors
        p_input_encode = re.compile(r"^(?P<input_encode>\d+)\s+Encoding\s+errors")

        # 341796946 Number of requested variables
        p_input_requested = re.compile(r"^(?P<input_requested>\d+)\s+Number\s+of\s+requested\s+variables$")

        # 7328 Number of altered variables
        p_input_altered = re.compile(r"^(?P<input_altered>\d+)\s+Number\s+of\s+altered\s+variables$")

        # 954173 Get-request PDUs
        p_input_get_pdu = re.compile(r"^(?P<input_get_pdu>\d+)\s+Get-request\s+PDUs$")

        # 31072480 Get-next PDUs
        p_input_next_pdu = re.compile(r"^(?P<input_next_pdu>\d+)\s+Get-next\s+PDUs$")

        # 3878 Set-request PDUs
        p_input_set_pdu = re.compile(r"^(?P<input_set_pdu>\d+)\s+Set-request\s+PDUs$")

        # 0 Input queue packet drops (Maximum queue size 1000)
        p_input_drops = re.compile(r"^(?P<input_drops>\d+)\s+Input\s+queue\s+packet\s+drops\s+\(Maximum\s+queue\s+size\s+(?P<size>\d+)\)$")

        # 35598123 SNMP packets output
        p_output_count = re.compile(r"^(?P<output_count>\d+)\s+SNMP\s+packets\s+output$")

        # 0 Too big errors (Maximum packet size 1500)
        p_output_big = re.compile(r"^(?P<output_big>\d+)\s+Too\s+big\s+errors\s+\(Maximum\s+packet\s+size\s+(?P<size>\d+)\)$")

        # 1 No such name errors
        p_output_name = re.compile(r"^(?P<output_name>\d+)\s+No\s+such\s+name\s+errors$")

        # 0 Bad values errors
        p_output_bad = re.compile(r"^(?P<output_bad>\d+)\s+Bad\s+values\s+errors$")

        # 0 General errors
        p_output_general = re.compile(r"^(?P<output_general>\d+)\s+General\s+errors$")

        # 322899 Response PDUs
        p_output_response_pdu = re.compile(r"^(?P<output_response_pdu>\d+)\s+Response\s+PDUs$")

        # 527788 Trap PDUs
        p_output_trap_pdu = re.compile(r"^(?P<output_trap>\d+)\s+Trap\s+PDUs")

        # Packets currently in SNMP process input queue: 0
        p_packet_queue = re.compile(r"^Packets\s+currently\s+in\s+SNMP\s+process\s+input\s+queue:\s+(?P<queue>\d+)")

        # SNMP global trap: enabled
        p_global_trap = re.compile(r"^SNMP\s+global\s+trap:\s+(?P<global_status>enabled|disabled)")

        # SNMP logging: enabled
        p_logging = re.compile(r"^SNMP\s+logging:\s+(?P<logging_status>enabled|disabled)$")

        # Logging to 10.76.1.12.151, 0/10, 102045 sent, 3065 dropped.
        p_logging_endpoint = re.compile(r"^Logging\s+to\s+(?P<endpoint_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\.(?P<endpoint_port>\d+),\s+(?P<endpoint_queue>\d+)\/(?P<endpoint_queue_size>\d+),\s+(?P<endpoint_sent>\d+)\s+sent,\s+(?P<endpoint_dropped>\d+)\s+dropped.$")

        snmp_obj = {}

        for line in output.splitlines():
            line = line.strip()
            # Chassis: FCE2310A48M
            if p_chassis.match(line):
                match = p_chassis.match(line)
                snmp_obj["chassis"] = match.group("chassis")
                continue
            # Contact: "something@cisco.com"
            elif p_contact.match(line):
                line = line.replace('"', '')
                match = p_contact.match(line)
                snmp_obj["contact"] = match.group("contact")
                continue
            # Location: "To be filled in"
            elif p_location_not_filled.match(line):
                match = p_location_not_filled.match(line)
                snmp_obj["location"] = "To be filled in"
                continue
            # Location: SJCT
            elif p_location.match(line):
                match = p_location.match(line)
                snmp_obj["location"] = match.group("location")
                continue
            # 35072424 SNMP packets input
            elif p_input_count.match(line):
                match = p_input_count.match(line)
                if not snmp_obj.get("snmp_input"):
                    snmp_obj["snmp_input"] = {}
                snmp_obj.setdefault("snmp_input", {})["packet_count"] = int(match.group("input_count"))
                continue
            # 0 Bad SNMP version errors
            elif p_input_bad.match(line):
                match = p_input_bad.match(line)
                snmp_obj["snmp_input"].update({ "bad_snmp_version_errors": int(match.group("input_bad"))})
                continue
            # 2089 Unknown community name
            elif p_input_unknown.match(line):
                match = p_input_unknown.match(line)
                snmp_obj["snmp_input"].update({ "unknown_community_name": int(match.group("input_unknown"))})
                continue
            # 68 Illegal operation for community name supplied
            elif p_input_illegal.match(line):
                match = p_input_illegal.match(line)
                snmp_obj["snmp_input"].update({ "illegal_operation_for_community_name_supplied": int(match.group("input_illegal"))})
                continue
            # 0 Encoding errors
            elif p_input_encode.match(line):
                match = p_input_encode.match(line)
                snmp_obj["snmp_input"].update({ "encoding_errors": int(match.group("input_encode"))})
                continue
            # 341796946 Number of requested variables
            elif p_input_requested.match(line):
                match = p_input_requested.match(line)
                snmp_obj["snmp_input"].update({"number_of_requested_variables": int(match.group("input_requested"))})
                continue
            # 7328 Number of altered variables
            elif p_input_altered.match(line):
                match = p_input_altered.match(line)
                snmp_obj["snmp_input"].update({"number_of_altered_variables": int(match.group("input_altered"))})
                continue
            # 954173 Get-request PDUs
            elif p_input_get_pdu.match(line):
                match = p_input_get_pdu.match(line)
                snmp_obj["snmp_input"].update({"get_request_pdus": int(match.group("input_get_pdu"))})
                continue
            # 954173 Get-next PDUs
            elif p_input_next_pdu.match(line):
                match = p_input_next_pdu.match(line)
                snmp_obj["snmp_input"].update({"get_next_pdus": int(match.group("input_next_pdu"))})
                continue
            # 3878 Set-request PDUs
            elif p_input_set_pdu.match(line):
                match = p_input_set_pdu.match(line)
                snmp_obj["snmp_input"].update({"set_request_pdus": int(match.group("input_set_pdu"))})
                continue
            # 0 Input queue packet drops (Maximum queue size 1000)
            elif p_input_drops.match(line):
                match = p_input_drops.match(line)
                snmp_obj["snmp_input"].update({"input_queue_drops": int(match.group("input_drops"))})
                snmp_obj["snmp_input"].update({"maximum_queue_size": int(match.group("size"))})
                continue
            # 35598123 SNMP packets output
            elif p_output_count.match(line):
                match = p_output_count.match(line)
                if not snmp_obj.get("snmp_output"):
                    snmp_obj["snmp_output"] = {}
                snmp_obj["snmp_output"].update({ "packet_count": int(match.group("output_count"))})
                continue
            # 0 Too big errors (Maximum packet size 1500)
            elif p_output_big.match(line):
                match = p_output_big.match(line)
                snmp_obj["snmp_output"].update({"too_big_errors": int(match.group("output_big"))})
                snmp_obj["snmp_output"].update({"maximum_packet_size": int(match.group("size"))})
                continue
            # 1 No such name errors
            elif p_output_name.match(line):
                match = p_output_name.match(line)
                snmp_obj["snmp_output"].update({"no_such_name_errors": int(match.group("output_name"))})
                continue
            # 0 Bad values errors
            elif p_output_bad.match(line):
                match = p_output_bad.match(line)
                snmp_obj["snmp_output"].update({"bad_value_errors": int(match.group("output_bad"))})
                continue
            # 0 General errors
            elif p_output_general.match(line):
                match = p_output_general.match(line)
                snmp_obj["snmp_output"].update({"general_errors": int(match.group("output_general"))})
                continue
            # 322899 Response PDUs
            elif p_output_response_pdu.match(line):
                match = p_output_response_pdu.match(line)
                snmp_obj["snmp_output"].update({"response_pdus": int(match.group("output_response_pdu"))})
                continue
            # 527788 Trap PDUs
            elif p_output_trap_pdu.match(line):
                match = p_output_trap_pdu.match(line)
                snmp_obj["snmp_output"].update({"trap_pdus": int(match.group("output_trap"))})
                continue
            # SNMP global trap: enabled
            elif p_global_trap.match(line):
                match = p_global_trap.match(line)
                global_trap = match.group("global_status")
                if global_trap == "enabled":
                    snmp_obj["snmp_global_trap"] = "enabled"
                else:
                    snmp_obj["snmp_global_trap"] = "disabled"
                continue
            # Packets currently in SNMP process input queue: 0
            elif p_packet_queue.match(line):
                match = p_packet_queue.match(line)
                snmp_obj["snmp_input_queue"] = int(match.group("queue"))
                continue
            # SNMP logging: enabled
            elif p_logging.match(line):
                match = p_logging.match(line)
                logging_status = match.group("logging_status")
                if logging_status == "disabled":
                    snmp_obj.setdefault("snmp_logging", {}).update({ "status": "disabled" })
                else:
                    snmp_obj.setdefault("snmp_logging", {}).update({ "status": "enabled" })
                continue
            # Logging to 10.76.1.12.151, 0/10, 102045 sent, 3065 dropped.
            elif p_logging_endpoint.match(line):
                match = p_logging_endpoint.match(line)
                if not snmp_obj["snmp_logging"].get("endpoints"):
                    snmp_obj["snmp_logging"].update({ "endpoints": {} })
                snmp_obj["snmp_logging"]["endpoints"].update({ match.group("endpoint_ip") : {"port" : int(match.group("endpoint_port")), "queue" : int(match.group("endpoint_queue")), 
                                                                                                        "queue_size" : int(match.group("endpoint_queue_size")), "sent" : int(match.group("endpoint_sent")), 
                                                                                                        "dropped" : int(match.group("endpoint_dropped"))} })

        return snmp_obj


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

# ==========================================================
#  Parser for snmp mib ifmib ifindex
# ==========================================================
class ShowSnmpMibIfmibIfindexSchema(MetaParser):
    """Schema for:
        * show snmp mib ifmib ifindex
        * show snmp mib ifmib ifindex | include {interface}
    """

    schema = {
        'interface': {
            Any(): { 
                'ifIndex': str 
            },
        }
    }


class ShowSnmpMibIfmibIfindex(ShowSnmpMibIfmibIfindexSchema):
    """
    parser for
        * show snmp mib ifmib ifindex
        * show snmp mib ifmib ifindex | include {interface}
    """

    cli_command = ['show snmp mib ifmib ifindex | include {interface}', 
                   'show snmp mib ifmib ifindex']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output
			
        interface_dict = {}

        #GigabitEthernet3/0/28: Ifindex = 36
        #unrouted VLAN 1003: Ifindex = 7
        p1 =  re.compile(r'^(?P<interface_index>(unrouted\sVLAN\s)?\S+) +Ifindex = +(?P<ifIndex>\d+)$')

        for line in out.splitlines():
            #GigabitEthernet3/0/28: Ifindex = 36
            #unrouted VLAN 1003: Ifindex = 7
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('interface_index'))
                intf = (intf.split(':'))[0]
                interface_dict.setdefault('interface',{}).setdefault(intf, group)

        return interface_dict
