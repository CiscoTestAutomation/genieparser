''' show_snmp.py

IOSXR parsers for the following show commands:
    * show snmp 
    * show snmp host
'''

# Python regex module
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# ==========================
# Schema for 'show snmp'
# ==========================

class ShowSnmpSchema(MetaParser):

    ''' Schema for "show snmp" on IOSXR'''

    schema = {
        "chassis": str,
        "snmp_packets_input": {
            "packet_count": int,
            "bad_snmp_version_errors": int,
            "unknown_community_name": int,
            "illegal_operation_for_community": int,
            "encoding_errors": int,
            "number_of_requested_variables": int,
            "number_of_altered_variables": int,
            "get_request_pdus": int,
            "get_next_pdus": int,
            "set_request_pdus": int,
        },
        "snmp_packets_output": {
            "packet_count": int,
            "too_big_errors": int,
            "maximum_packet_size": int,
            "no_such_name_errors": int,
            "bad_value_errors": int,
            "general_errors": int,
            "response_pdus": int,
            "trap_pdus": int
        },
        "snmp_logging" : {
            "status": str,
            Optional("logging_hosts") : {
                Optional(Any()) : {
                    Optional("udp_port") : int,
                    Optional("host_statistics") : {
                        Optional("notification_type"): str,
                        Optional("pkts_in_trap_queue"): int,
                        Optional("max_len_trap_queue"): int,
                        Optional("pkts_sent"): int,
                        Optional("pkts_dropped"): int
                    }
                }
            },
            Optional("inform_statistics"): {
                Optional("informs_sent") : int,
                Optional("informs_retries"): int,
                Optional("informs_pending"): int,
                Optional("informs_dropped"): int
                }
            }
        }


# ==========================
# Parser for 'show snmp'
# ==========================

class ShowSnmp(ShowSnmpSchema):

    ''' Parser for "show snmp" on IOSXR '''

    cli_command = 'show snmp'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        # Chassis: ABC0123A19Z
        p0 = re.compile(r"^Chassis:\s?(?P<chassis>\S+|z{0,})$")

        # 34854563 SNMP packets input
        p1 = re.compile(r"^(?P<input_pkts>\d+)\s+SNMP\s+packets\s+input$")

        # 0 Bad SNMP version errors
        p2 = re.compile(r"^(?P<bad_version>\d+)\s+Bad\s+SNMP\s+version\s+errors$")

        # 105 Unknown community name
        p3 = re.compile(r"^(?P<unknown_community>\d+)\s+Unknown\s+community\s+name$")

        # 45 Illegal operation for community name supplied
        p4 = re.compile(r"(?P<illegal_oper>\d+)\s+Illegal\s+operation\s+for\s+community\s+name\s+supplied$")

        # 0 Encoding errors
        p5 = re.compile(r"^(?P<encoding_errors>\d+)\s+Encoding\s+errors")

        # 2415368 Number of requested variables
        p6= re.compile(r"^(?P<requested_variables>\d+)\s+Number\s+of\s+requested\s+variables$")

        # 68954 Number of altered variables
        p7 = re.compile(r"^(?P<altered_variables>\d+)\s+Number\s+of\s+altered\s+variables$")

        # 22102104 Get-request PDUs
        p8 = re.compile(r"^(?P<get_request_pdus>\d+)\s+Get-request\s+PDUs$")

        # 972411 Get-next PDUs
        p9 = re.compile(r"^(?P<get_next_pdus>\d+)\s+Get-next\s+PDUs$")

        # 3878 Set-request PDUs
        p10 = re.compile(r"^(?P<set_request_pdus>\d+)\s+Set-request\s+PDUs$")

        # 42531179 SNMP packets output
        p11 = re.compile(r"^(?P<output_pkts>\d+)\s+SNMP\s+packets\s+output$")

        # 0 Too big errors (Maximum packet size 1500)
        p12 = re.compile(r"^(?P<big_errors>\d+)\s+Too\s+big\s+errors\s+\(Maximum\s+packet\s+size\s+(?P<max_pkt_size>\d+)\)$")

        # 160671 No such name errors
        p13 = re.compile(r"^(?P<name_errors>\d+)\s+No\s+such\s+name\s+errors$")

        # 0 Bad values errors
        p14 = re.compile(r"^(?P<value_errors>\d+)\s+Bad\s+values\s+errors$")

        # 0 General errors
        p15 = re.compile(r"^(?P<general_errors>\d+)\s+General\s+errors$")

        # 34854547 Response PDUs
        p16 = re.compile(r"^(?P<response_pdus>\d+)\s+Response\s+PDUs$")

        # 7676632 Trap PDUs
        p17 = re.compile(r"^(?P<trap_pdus>\d+)\s+Trap\s+PDUs$")

        # SNMP logging: Enabled
        p18 = re.compile(r"^SNMP\s+logging:\s+(?P<logging_status>Enabled|Disabled)$")

        # Logging to Notification host: 10.0.0.1, udp-port: 162
        p19 = re.compile(r"^Logging\sto\sNotification\shost:\s(?P<logging_host>[a-fA-F\d.:]+),\sudp-port:\s(?P<udp_port>\d+)$")

        # Trap Host Statistics
        p20 = re.compile(r"^(?P<notification_type>(Trap|Inform))\sHost\sStatistics$")

        # Number of pkts in Trap Queue: 0
        p21 = re.compile(r"^Number\sof\spkts\sin\sTrap\sQueue:\s(?P<pkts_in_trap_queue>\d+)$")

        # Maximum length of Trap Queue: 100
        p22 = re.compile(r"^Maximum\slength\sof\sTrap\sQueue:\s(?P<max_len_trap_queue>\d+)$")

        # Number of pkts sent: 0
        p23 = re.compile(r"^Number\sof\spkts\ssent:\s(?P<pkts_sent>\d+)$")

        # Number of pkts dropped: 0
        p24 = re.compile(r"^Number\sof\spkts\sdropped:\s(?P<pkts_dropped>\d+)$")

        # Number of Informs sent: 0
        p25 = re.compile(r"^Number\sof\sInforms\ssent:\s(?P<informs_sent>\d+)$")

        # Number of Informs retries: 0
        p26 = re.compile(r"^Number\sof\sInforms\sretries:\s(?P<informs_retries>\d+)$")

        # Number of Informs pending: 0
        p27 = re.compile(r"^Number\sof\sInforms\spending:\s(?P<informs_pending>\d+)")

        # Number of Informs dropped: 0 
        p28 = re.compile(r"^Number\sof\sInforms\sdropped:\s(?P<informs_dropped>\d+)$")

        snmp_dict = {}

        for line in output.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # Chassis: ABC0123A19Z
            m = p0.match(line)
            if m:
                group = m.groupdict()
                chassis = group["chassis"]
                
                snmp_dict["chassis"] = chassis
                continue

            # 34854563 SNMP packets input
            m = p1.match(line)
            if m:
                group = m.groupdict()
                input_pkts = int(group["input_pkts"])

                if not snmp_dict.get("snmp_packets_input"):
                    snmp_dict.setdefault("snmp_packets_input", {})

                snmp_dict["snmp_packets_input"].update({"packet_count": input_pkts})
                continue

            # 0 Bad SNMP version errors
            m = p2.match(line)
            if m:
                group = m.groupdict()
                bad_version = int(group["bad_version"])

                snmp_dict["snmp_packets_input"].update({"bad_snmp_version_errors": bad_version})
                continue

            # 105 Unknown community name
            m = p3.match(line)
            if m:
                group = m.groupdict()
                unknown_community = int(group["unknown_community"])

                snmp_dict["snmp_packets_input"].update({"unknown_community_name": unknown_community})
                continue

            # 45 Illegal operation for community name supplied
            m = p4.match(line)
            if m:
                group = m.groupdict()
                illegal_oper = int(group["illegal_oper"])

                snmp_dict["snmp_packets_input"].update({"illegal_operation_for_community": illegal_oper})
                continue

            # 0 Encoding errors
            m = p5.match(line)
            if m:
                group = m.groupdict()
                encoding_errors = int(group["encoding_errors"])

                snmp_dict["snmp_packets_input"].update({"encoding_errors": encoding_errors})
                continue

            # 2415368 Number of requested variables
            m = p6.match(line)
            if m:
                group = m.groupdict()
                requested_variables = int(group["requested_variables"])

                snmp_dict["snmp_packets_input"].update({"number_of_requested_variables": requested_variables})
                continue

            # 68954 Number of altered variables
            m = p7.match(line)
            if m:
                group = m.groupdict()
                altered_variables = int(group["altered_variables"])

                snmp_dict["snmp_packets_input"].update({"number_of_altered_variables": altered_variables})
                continue

            # 22102104 Get-request PDUs
            m = p8.match(line)
            if m:
                group = m.groupdict()
                get_request_pdus = int(group["get_request_pdus"])

                snmp_dict["snmp_packets_input"].update({"get_request_pdus": get_request_pdus})
                continue

            # 972411 Get-next PDUs
            m = p9.match(line)
            if m:
                group = m.groupdict()
                get_next_pdus = int(group["get_next_pdus"])

                snmp_dict["snmp_packets_input"].update({"get_next_pdus": get_next_pdus})
                continue

            # 3878 Set-request PDUs
            m = p10.match(line)
            if m:
                group = m.groupdict()
                set_request_pdus = int(group["set_request_pdus"])

                snmp_dict["snmp_packets_input"].update({"set_request_pdus": set_request_pdus})
                continue

            # 42531179 SNMP packets output
            m = p11.match(line)
            if m:
                group = m.groupdict()
                output_pkts = int(group["output_pkts"])

                if not snmp_dict.get("snmp_packets_output"):
                    snmp_dict.setdefault("snmp_packets_output", {})

                snmp_dict["snmp_packets_output"].update({"packet_count": output_pkts})
                continue

            # 0 Too big errors (Maximum packet size 1500)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                big_errors = int(group["big_errors"])
                max_pkt_size = int(group["max_pkt_size"])

                snmp_dict["snmp_packets_output"].update({"too_big_errors": big_errors})
                snmp_dict["snmp_packets_output"].update({"maximum_packet_size": max_pkt_size})
                continue

            # 160671 No such name errors
            m = p13.match(line)
            if m:
                group = m.groupdict()
                name_errors = int(group["name_errors"])

                snmp_dict["snmp_packets_output"].update({"no_such_name_errors": name_errors})
                continue

            # 0 Bad values errors
            m = p14.match(line)
            if m:
                group = m.groupdict()
                value_errors = int(group["value_errors"])

                snmp_dict["snmp_packets_output"].update({"bad_value_errors": value_errors})
                continue

            # 0 General errors
            m = p15.match(line)
            if m:
                group = m.groupdict()
                general_errors = int(group["general_errors"])

                snmp_dict["snmp_packets_output"].update({"general_errors": general_errors})
                continue

            # 34854547 Response PDUs
            m = p16.match(line)
            if m:
                group = m.groupdict()
                response_pdus = int(group["response_pdus"])

                snmp_dict["snmp_packets_output"].update({"response_pdus": response_pdus})
                continue

            # 7676632 Trap PDUs
            m = p17.match(line)
            if m:
                group = m.groupdict()
                trap_pdus = int(group["trap_pdus"])

                snmp_dict["snmp_packets_output"].update({"trap_pdus": trap_pdus})
                continue

            # SNMP logging: Enabled
            m = p18.match(line)
            if m:
                group = m.groupdict()
                logging_status = group["logging_status"]

                if logging_status == "Enabled":
                    snmp_dict.setdefault("snmp_logging", {}).update({"status": "enabled"})
                else:
                    snmp_dict.setdefault("snmp_logging", {}).update({"status": "disabled"})
                continue

            # Logging to Notification host: 10.0.0.1, udp-port: 162
            m = p19.match(line)
            if m:
                group = m.groupdict()
                logging_host = group["logging_host"]
                udp_port = int(group["udp_port"])

                if not snmp_dict["snmp_logging"].get("logging_hosts"):
                    snmp_dict["snmp_logging"].update({"logging_hosts": {} })

                snmp_dict["snmp_logging"]["logging_hosts"].update({logging_host: {"udp_port": udp_port}})

                continue

            # Trap Host Statistics
            m = p20.match(line)
            if m:
                group = m.groupdict()
                notification_type = group["notification_type"]

                snmp_dict["snmp_logging"]["logging_hosts"][logging_host].update({"host_statistics": {}})
                host_statistics_dict = snmp_dict["snmp_logging"]["logging_hosts"][logging_host]["host_statistics"]
                host_statistics_dict["notification_type"] = notification_type
                continue

            # Number of pkts in Trap Queue: 0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                pkts_in_trap_queue = int(group["pkts_in_trap_queue"])

                host_statistics_dict.update({"pkts_in_trap_queue": pkts_in_trap_queue})
                continue

            # Maximum length of Trap Queue: 100
            m = p22.match(line)
            if m:
                group = m.groupdict()
                max_len_trap_queue = int(group["max_len_trap_queue"])

                host_statistics_dict.update({"max_len_trap_queue": max_len_trap_queue})
                continue

            # Number of pkts sent: 0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                pkts_sent = int(group["pkts_sent"])

                host_statistics_dict.update({"pkts_sent": pkts_sent})
                continue

            # Number of pkts dropped: 0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                pkts_dropped = int(group["pkts_dropped"])

                host_statistics_dict.update({"pkts_dropped": pkts_dropped})
                continue

            # Number of Informs sent: 0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                informs_sent = int(group["informs_sent"])

                if not snmp_dict["snmp_logging"].get("inform_statistics"):
                    snmp_dict["snmp_logging"].update({"inform_statistics": {} })

                snmp_dict["snmp_logging"]["inform_statistics"].update({"informs_sent": informs_sent})
                continue

            # Number of Informs retries: 0
            m = p26.match(line)
            if m:
                group = m.groupdict()
                informs_retries = int(group["informs_retries"])

                snmp_dict["snmp_logging"]["inform_statistics"].update({"informs_retries": informs_retries})
                continue

            # Number of Informs pending: 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                informs_pending = int(group["informs_pending"])

                snmp_dict["snmp_logging"]["inform_statistics"].update({"informs_pending": informs_pending})
                continue

            # Number of Informs dropped: 0 
            m = p28.match(line)
            if m:
                group = m.groupdict()
                informs_dropped = int(group["informs_dropped"])

                snmp_dict["snmp_logging"]["inform_statistics"].update({"informs_dropped": informs_dropped})
                continue

        return snmp_dict



# ============================
# Schema for 'show snmp host'
# ============================

class ShowSnmpHostSchema(MetaParser):

    ''' Schema for "show snmp host" on IOSXR'''

    schema = {
        "snmp_notification_hosts" : {
                Optional(Any()) : {    
                    Optional("udp_port") : int, 
                    Optional("vrf") : str,
                    Optional("type") : str,
                    Optional("user"): str,
                    Optional("version"): str,
                    Optional("v3_sec_level"): str
                }
            }
        }



# ============================
# Parser for 'show snmp host'
# ============================

class ShowSnmpHost(ShowSnmpHostSchema):

    ''' Parser for "show snmp host" on IOSXR '''

    cli_command = 'show snmp host'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        snmp_host_dict = {}

        '''
        Notification host: 10.0.0.2 udp-port: 162  type: trap
        user: priv_comm      security model: v3 auth

        Notification host: 10.0.0.4 udp-port: 162-VRFA  type: trap
        user: priv_comm      security model: v3 noauth

        Notification host: 10.0.0.1 udp-port: 162  type: trap
        user: public      security model: v2c 

        Notification host: 10.0.0.3 udp-port: 162-VRF-A  type: trap
        user: public      security model: v2c 

        Notification host: 10.0.0.3 udp-port: 162  type: inform
        user: public2      security model: v2c 

        Notification host: 2001:ab8::1 udp-port: 162  type: trap
        user: public3      security model: v3 priv

        Notification host: 2001:0:ab00:1234:0:2552:7777:1313 udp-port: 162  type: trap
        user: public4      security model: v3 priv
        '''

        # Notification host: 10.0.0.2 udp-port: 162  type: trap
        # Notification host: 2001:ab8::1 udp-port: 162  type: trap
        # Notification host: 2001:0:ab00:1234:0:2552:7777:1313 udp-port: 162  type: trap
        p0 = re.compile(r"^Notification\shost:\s(?P<host>[a-fA-F\d.:]+)\sudp-port:\s(?P<udp_port>\d+)\s+type:\s(?P<type>\S+)$")

        # Notification host: 10.0.0.4 udp-port: 162-VRFA  type: trap
        p1 = re.compile(r"^Notification\shost:\s(?P<host>[a-fA-F\d.:]+)\sudp-port:\s(?P<udp_port>\d+)-(?P<vrf>\S+)\s*type:\s(?P<type>\S+)$")

        # user: public      security model: v2c
        p2 = re.compile(r"^user:\s(?P<user>\S+)\s+security\smodel:\s(?P<version>\S+)$")

        # user: public3      security model: v3 priv
        p3 = re.compile(r"^user:\s(?P<user>\S+)\s+security\smodel:\s(?P<version>\S+)\s(?P<v3_sec_level>\S+)$")


        for line in output.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # Notification host: 10.0.0.2 udp-port: 162  type: trap
            # Notification host: 2001:ab8::1 udp-port: 162  type: trap
            # Notification host: 2001:0:ab00:1234:0:2552:7777:1313 udp-port: 162  type: trap
            if p0.match(line):
                m = p0.match(line)
                logging_host = m.group("host")

                logging_host_dict = snmp_host_dict.setdefault('snmp_notification_hosts', {}).setdefault(logging_host, {})
                logging_host_dict["udp_port"] = int(m.group("udp_port"))
                logging_host_dict["type"] = m.group("type")
                continue

            # Notification host: 10.0.0.4 udp-port: 162-VRFA  type: trap
            elif p1.match(line):
                m = p1.match(line)
                logging_host = m.group("host")

                logging_host_dict = snmp_host_dict.setdefault('snmp_notification_hosts', {}).setdefault(logging_host, {})
                logging_host_dict["udp_port"] = int(m.group("udp_port"))
                logging_host_dict["vrf"] = m.group("vrf")
                logging_host_dict["type"] = m.group("type")
                continue

            # user: public      security model: v2c
            if p2.match(line):
                m = p2.match(line)
                logging_host_dict["user"] = m.group("user")
                logging_host_dict["version"] = m.group("version")
                continue

            # user: public3      security model: v3 priv
            elif p3.match(line):
                m = p3.match(line)
                logging_host_dict["user"] = m.group("user")
                logging_host_dict["version"] = m.group("version")
                logging_host_dict["v3_sec_level"] = m.group("v3_sec_level")
                continue

        return snmp_host_dict
