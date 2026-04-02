""" show_policy_map.py

IOSXE parsers for the following show commands:
    * 'show policy-map interface'
"""

# Python
import re
import xmltodict
import collections
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use, ListOf

# import parser utils
from genie.libs.parser.utils.common import Common

class ShowPolicyMapInterfaceSchema(MetaParser):
    schema = {
        "interface": {
            Any(): {
                "service_policy": {
                    "output": {
                        Any(): {
                            "class_map": {
                                Any(): {
                                    "match_mode": str,
                                    "packets": int,
                                    "bytes": int,
                                    "rate": {
                                        "interval_minutes": int,
                                        "offered_bps": int,
                                        "drop_bps": int
                                    },
                                    "match": str,
                                    Optional("queueing"): bool,
                                    Optional("queue_limit"): {
                                        Optional("packets"): int,
                                        Optional("bytes"): int,
                                        Optional("ms"): int
                                    },
                                    "queue_counters": {
                                        "queue_depth": int,
                                        "total_drops": int,
                                        "no_buffer_drops": int
                                    },
                                    "output_packets": int,
                                    "output_bytes": int,
                                    Optional("bandwidth_kbps"): int,
                                    Optional("shape"): {
                                        "type": str,
                                        "cir_bps": int,
                                        "bc_bytes": int,
                                        "be_bytes": int,
                                        Optional("target_rate_bps"): int
                                    },
                                    Optional("random_detect"): {
                                        "exp_weight_constant": int,
                                        "exp_weight_constant_fraction": str,
                                        "mean_queue_depth": {
                                            "ms": int,
                                            "bytes": int
                                        },
                                        "classes": {
                                            int: {
                                                "transmitted": {"pkts": int, "bytes": int},
                                                "random_drop": {"pkts": int, "bytes": int},
                                                "tail_drop": {"pkts": int, "bytes": int},
                                                "minimum_threshold": {"ms": int, "bytes": int},
                                                "maximum_threshold": {"ms": int, "bytes": int},
                                                "mark_prob": str
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowPolicyMapInterface(ShowPolicyMapInterfaceSchema):
    cli_command = ["show policy-map interface {interface}", "show policy-map interface"]

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}

        #  TenGigabitEthernet0/0/15 
        p1 = re.compile(r'^\s*(?P<interface>TenGigabitEthernet\d+/\d+/\d+)\s*$')

        #   Service-policy output: wred
        p2 = re.compile(r'^\s*Service-policy\s+output\s*:\s*(?P<policy>\S+)$')

        #     Class-map: prec1 (match-all)  
        p3 = re.compile(r'^\s*Class-map:\s+(?P<class_name>\S+)\s+\((?P<match_mode>[\w\-]+)\)\s*$')

        #       0 packets, 0 bytes
        p4 = re.compile(r'^\s*(?P<packets>\d+)\s+packets,\s+(?P<bytes>\d+)\s+bytes$')

        #       5 minute offered rate 0000 bps, drop rate 0000 bps
        p5 = re.compile(r'^\s*(?P<interval>\d+)\s+minute\s+offered\s+rate\s+(?P<offered>\d+)\s+bps,\s+drop\s+rate\s+(?P<drop>\d+)\s+bps$')

        #       Match:  precedence 1 
        p6 = re.compile(r'^\s*Match:\s*(?P<match>.+?)\s*$')

        #       Queueing
        p7 = re.compile(r'^\s*Queueing$')

        #       queue limit 640 packets
        p8 = re.compile(r'^\s*queue\s+limit\s+(?P<packets>\d+)\s+packets$')

        #       queue limit 5120 bytes
        p9 = re.compile(r'^\s*queue\s+limit\s+(?P<bytes>\d+)\s+bytes$')

        #       queue limit 10 ms/ 375000 bytes
        p10 = re.compile(r'^\s*queue\s+limit\s+(?P<ms>\d+)\s+ms/\s+(?P<bytes>\d+)\s+bytes$')

        #       (queue depth/total drops/no-buffer drops) 0/0/0
        p11 = re.compile(r'^\s*\(queue\s+depth/total\s+drops/no-buffer\s+drops\)\s+(?P<depth>\d+)/(?P<total>\d+)/(?P<no_buf>\d+)$')

        #       (pkts output/bytes output) 0/0
        p12 = re.compile(r'^\s*\(pkts\s+output/bytes\s+output\)\s+(?P<pkts>\d+)/(?P<out_bytes>\d+)$')

        #       shape (average) cir 1000000000, bc 10000000, be 10000000
        p13 = re.compile(r'^\s*shape\s+\((?P<stype>\w+)\)\s+cir\s+(?P<cir>\d+),\s+bc\s+(?P<bc>\d+),\s+be\s+(?P<be>\d+)$')

        #       target shape rate 1000000000
        p14 = re.compile(r'^\s*target\s+shape\s+rate\s+(?P<target>\d+)$')

        #       bandwidth 300000 kbps
        p15 = re.compile(r'^\s*bandwidth\s+(?P<kbps>\d+)\s+kbps$')

        #         Exp-weight-constant: 9 (1/512)
        p16 = re.compile(r'^\s*Exp-weight-constant:\s+(?P<exp>\d+)\s+\((?P<fraction>[^)]+)\)$')

        #         Mean queue depth: 0 ms/ 0 bytes
        p17 = re.compile(r'^\s*Mean\s+queue\s+depth:\s+(?P<ms>\d+)\s+ms/\s+(?P<bytes>\d+)\s+bytes$')

        #         0               0/0               0/0              0/0              2/93750       5/187500    1/10
        p18 = re.compile(
            r'^\s*(?P<cls>\d+)\s+'
            r'(?P<tx_pkts>\d+)/(?P<tx_bytes>\d+)\s+'
            r'(?P<rd_pkts>\d+)/(?P<rd_bytes>\d+)\s+'
            r'(?P<td_pkts>\d+)/(?P<td_bytes>\d+)\s+'
            r'(?P<min_ms>\d+)/(?P<min_bytes>\d+)\s+'
            r'(?P<max_ms>\d+)/(?P<max_bytes>\d+)\s+'
            r'(?P<mark_prob>\d+/\d+)$'
        )

        interface_name = None
        policy_name = None
        current_class = None
        class_dict = None

        for line in output.splitlines():
            line = line.rstrip()
            if not line:
                continue

            #  TenGigabitEthernet0/0/15 
            m = p1.match(line)
            if m:
                interface_name = m.group("interface")
                interface_dict = ret_dict.setdefault("interface", {}).setdefault(interface_name, {})
                continue

            #   Service-policy output: wred
            m = p2.match(line)
            if m and interface_name:
                policy_name = m.group("policy")
                service_policy = interface_dict.setdefault("service_policy", {})
                output_dict = service_policy.setdefault("output", {})
                policy_dict = output_dict.setdefault(policy_name, {})
                continue

            #     Class-map: prec1 (match-all)  
            m = p3.match(line)
            if m and policy_name:
                class_name = m.group("class_name")
                match_mode = m.group("match_mode")
                cm = policy_dict.setdefault("class_map", {})
                class_dict = cm.setdefault(class_name, {})
                class_dict["match_mode"] = match_mode
                current_class = class_name
                continue

            #       0 packets, 0 bytes
            m = p4.match(line)
            if m and class_dict is not None:
                class_dict["packets"] = int(m.group("packets"))
                class_dict["bytes"] = int(m.group("bytes"))
                continue

            #       5 minute offered rate 0000 bps, drop rate 0000 bps
            m = p5.match(line)
            if m and class_dict is not None:
                rate = class_dict.setdefault("rate", {})
                rate["interval_minutes"] = int(m.group("interval"))
                rate["offered_bps"] = int(m.group("offered"))
                rate["drop_bps"] = int(m.group("drop"))
                continue

            #       Match:  precedence 1 
            m = p6.match(line)
            if m and class_dict is not None:
                class_dict["match"] = m.group("match").strip()
                continue

            #       Queueing
            m = p7.match(line)
            if m and class_dict is not None:
                class_dict["queueing"] = True
                continue

            #       queue limit 640 packets
            m = p8.match(line)
            if m and class_dict is not None:
                ql = class_dict.setdefault("queue_limit", {})
                ql["packets"] = int(m.group("packets"))
                continue

            #       queue limit 5120 bytes
            m = p9.match(line)
            if m and class_dict is not None:
                ql = class_dict.setdefault("queue_limit", {})
                ql["bytes"] = int(m.group("bytes"))
                continue

            #       queue limit 10 ms/ 375000 bytes
            m = p10.match(line)
            if m and class_dict is not None:
                ql = class_dict.setdefault("queue_limit", {})
                ql["ms"] = int(m.group("ms"))
                ql["bytes"] = int(m.group("bytes"))
                continue

            #       (queue depth/total drops/no-buffer drops) 0/0/0
            m = p11.match(line)
            if m and class_dict is not None:
                qc = class_dict.setdefault("queue_counters", {})
                qc["queue_depth"] = int(m.group("depth"))
                qc["total_drops"] = int(m.group("total"))
                qc["no_buffer_drops"] = int(m.group("no_buf"))
                continue

            #       (pkts output/bytes output) 0/0
            m = p12.match(line)
            if m and class_dict is not None:
                class_dict["output_packets"] = int(m.group("pkts"))
                class_dict["output_bytes"] = int(m.group("out_bytes"))
                continue

            #       shape (average) cir 1000000000, bc 10000000, be 10000000
            m = p13.match(line)
            if m and class_dict is not None:
                shape = class_dict.setdefault("shape", {})
                shape["type"] = m.group("stype")
                shape["cir_bps"] = int(m.group("cir"))
                shape["bc_bytes"] = int(m.group("bc"))
                shape["be_bytes"] = int(m.group("be"))
                continue

            #       target shape rate 1000000000
            m = p14.match(line)
            if m and class_dict is not None:
                shape = class_dict.setdefault("shape", {})
                shape["target_rate_bps"] = int(m.group("target"))
                continue

            #       bandwidth 300000 kbps
            m = p15.match(line)
            if m and class_dict is not None:
                class_dict["bandwidth_kbps"] = int(m.group("kbps"))
                continue

            #         Exp-weight-constant: 9 (1/512)
            m = p16.match(line)
            if m and class_dict is not None:
                rd = class_dict.setdefault("random_detect", {})
                rd["exp_weight_constant"] = int(m.group("exp"))
                rd["exp_weight_constant_fraction"] = m.group("fraction")
                continue

            #         Mean queue depth: 0 ms/ 0 bytes
            m = p17.match(line)
            if m and class_dict is not None:
                rd = class_dict.setdefault("random_detect", {})
                mqd = rd.setdefault("mean_queue_depth", {})
                mqd["ms"] = int(m.group("ms"))
                mqd["bytes"] = int(m.group("bytes"))
                continue

            #         0               0/0               0/0              0/0              2/93750       5/187500    1/10
            m = p18.match(line)
            if m and class_dict is not None:
                rd = class_dict.setdefault("random_detect", {})
                classes = rd.setdefault("classes", {})
                idx = int(m.group("cls"))
                entry = classes.setdefault(idx, {})
                entry["transmitted"] = {"pkts": int(m.group("tx_pkts")), "bytes": int(m.group("tx_bytes"))}
                entry["random_drop"] = {"pkts": int(m.group("rd_pkts")), "bytes": int(m.group("rd_bytes"))}
                entry["tail_drop"] = {"pkts": int(m.group("td_pkts")), "bytes": int(m.group("td_bytes"))}
                entry["minimum_threshold"] = {"ms": int(m.group("min_ms")), "bytes": int(m.group("min_bytes"))}
                entry["maximum_threshold"] = {"ms": int(m.group("max_ms")), "bytes": int(m.group("max_bytes"))}
                entry["mark_prob"] = m.group("mark_prob")
                continue

        return ret_dict
