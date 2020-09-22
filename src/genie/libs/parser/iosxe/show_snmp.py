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

    ''' Schema for "show snmp mib" '''

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
            "input_queue_drops": int
        },
        "snmp_output": {
            "packet_count": int,
            "too_big_errors": int,
            "no_such_name_errors": int,
            "bad_value_errors": int,
            "general_errors": int,
            "response_pdus": int,
            "trap_pdus": int
        },
        Optional("snmp_input_queue"): Optional(int),
        Optional("snmp_global_trap"): Optional(str),
        "snmp_logging" : {
            "status": str,
            Optional("endpoints") : {
                Optional("ip_address"): {
                    Optional(Any()) : {
                        Optional("port") : Optional(int),
                        Optional("buffer"): Optional(str),
                        Optional("sent"): Optional(int),
                        Optional("dropped"): Optional(int)
                    }
                }
            }
        }
    }

# ==========================
# Parser for 'show snmp'
# ==========================
class ShowSnmp(ShowSnmpSchema):

    ''' Parser for "show snmp" '''

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
        #     Logging to 13.43.1.12.151, 0/10, 102045 sent, 3065 dropped.
        #     Logging to 12.44.133.10.111, 0/10, 102045 sent, 3065 dropped.
        #     Logging to 116.75.154.186.169, 0/10, 201075 sent, 11383 dropped.
        #     Logging to 126.35.67.19.108, 0/10, 102045 sent, 3065 dropped.

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
        p_input_drops = re.compile(r"^(?P<input_drops>\d+)\s+Input\s+queue\s+packet\s+drops\s+\(Maximum\s+queue\s+size\s+1000\)$")

        # 35598123 SNMP packets output
        p_output_count = re.compile(r"^(?P<output_count>\d+)\s+SNMP\s+packets\s+output$")

        # 0 Too big errors (Maximum packet size 1500)
        p_output_big = re.compile(r"^(?P<output_big>\d+)\s+Too\s+big\s+errors\s+\(Maximum\s+packet\s+size\s+1500\)$")

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
        p_global_trap = re.compile(r"^SNMP\s+global\s+trap:\s+enabled")

        # SNMP logging: enabled
        p_logging = re.compile(r"^SNMP\s+logging:\s+(?P<logging_status>(enabled|disabled))$")

        # Logging to 13.43.1.12.151, 0/10, 102045 sent, 3065 dropped.
        p_logging_endpoint = re.compile(r"^Logging\s+to\s+(?P<endpoint_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\.(?P<endpoint_port>\d+),\s+(?P<endpoint_buffer>\d+\/\d+),\s+(?P<endpoint_sent>\d+)\s+sent,\s+(?P<endpoint_dropped>\d+)\s+dropped.$")

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
                snmp_obj["snmp_input"].update({ "packet_count": int(match.group("input_count"))})
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
                snmp_obj["snmp_global_trap"] = "enabled"
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
                    snmp_obj.update({"snmp_logging" : {"status" : "disabled"}})
                else:
                    snmp_obj.update({"snmp_logging" : {"status" : "enabled"}})
                continue
            # Logging to 13.43.1.12.151, 0/10, 102045 sent, 3065 dropped.
            elif p_logging_endpoint.match(line):
                match = p_logging_endpoint.match(line)
                if not snmp_obj["snmp_logging"].get("endpoints"):
                    snmp_obj["snmp_logging"]["endpoints"] = {"ip_address" : {}}
                snmp_obj["snmp_logging"]["endpoints"]["ip_address"].update({ match.group("endpoint_ip") : {"port" : int(match.group("endpoint_port")), "buffer" : match.group("endpoint_buffer"), 
                                                                                                        "sent" : int(match.group("endpoint_sent")), "dropped" : int(match.group("endpoint_dropped"))} })

        return snmp_obj



