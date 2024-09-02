""" show_isis.py

IOSXE parsers for the following show commands:
    * show isis node locators
    * show isis node locators {level}
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, ListOf
from genie.libs.parser.utils.common import Common


class ShowIsisNodeLocatorsSchema(MetaParser):
    """schema for show isis node locators"""
    schema = {
        "tag": {
            Any(): {
                "level": {
                    Any(): {
                        "host": {
                            Any(): {
                                "ipv6prefix": {
                                    Any(): {
                                        Optional("topology"): str,
                                        Optional("pfx_algo"): int,
                                        "lsp": {
                                                Optional("lsp_id"): int,
                                                Optional("lsp_index"): int,
                                                Optional("lsp_seq_no"): str,
                                        },
                                        Optional("metric"): int,
                                        Optional("algorithm"): int,
                                        Optional("srv6_end_sid"): str,
                                        Optional("srv6_sid_behavior"): str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIsisNodeLocators(ShowIsisNodeLocatorsSchema):
    """Parser for show isis node locators"""

    cli_command = ["show isis node locators","show isis node locators {level}"]

 
    def cli(self, level="", output=None):
        if output is None:
            if level:
                output = self.device.execute(self.cli_command[1].format(level=level))
            else:
                output = self.device.execute(self.cli_command[0])

        print(output) 
        # initial return dictionary
        ret_dict = {}
        host_dict = {}
        v6pfx_dict = {}
        # Tag 1:
        p1 = re.compile(r"^Tag (?P<tag>\S+):$")
 
        # ISIS level-1 node information for R1.00
        p2 = re.compile(r"^ISIS\s+(?P<level>\S+)\s+node information for\s+(?P<host>\S+)$")

        # (MT-2) FCCC:CCC1:A1::/48, Algorithm: 128
        p3 = re.compile(r"\((?P<topology>MT-[2|0])\)\s+(?P<ipv6prefix>[0-9a-fA-F:/]+)\,\s+Algorithm:\s+(?P<pfx_algo>\d+)")

        #LSP 0, Index 1, Seq 0xB8
        p4 = re.compile(r"LSP\s+(?P<lsp_id>\d+)\,\s+Index\s+(?P<lsp_index>\d+)\,\s+Seq\s+(?P<lsp_seq_no>[0-9a-fA-Fx]+)")

        #Metric: 0, Algoritm: 128
        p5 = re.compile(r"Metric:\s+(?P<metric>\d+)\,\s+Algoritm:\s+(?P<algorithm>\d+)")

        #End SID: FCCC:CCC1:A1:: uN (PSP/USD)
        p6 = re.compile(r"End SID:\s+(?P<srv6_end_sid>[0-9a-fA-F:/]+)\s+(?P<srv6_sid_behavior>[\w\W\s()/]+)")

        for line in output.splitlines():
            line = line.strip()

            # Tag 1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag = group["tag"]
                root_dict = ret_dict.setdefault("tag", {}).setdefault(group["tag"], {})
                continue

            # ISIS level-1 node information for R1.00      
            m = p2.match(line)
            if m:
                group = m.groupdict()
                level = group["level"]
                host = group["host"]
                host_dict = ret_dict["tag"][tag].setdefault("level", {}).setdefault(
                    level, {}
                ).setdefault("host", {}).setdefault(host, {})
                continue

            # (MT-2) FCCC:CCC1:A1::/48, Algorithm: 128     
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ipv6prefix = group["ipv6prefix"]
                v6pfx_dict = host_dict.setdefault("ipv6prefix", {}).setdefault(
                    ipv6prefix, {}
                )
                v6pfx_dict["topology"] = (
                    group["topology"]
                )
                v6pfx_dict["pfx_algo"] = (
                    int(group["pfx_algo"])
                )
                continue

            #LSP 0, Index 1, Seq 0xB8
            m = p4.match(line)
            if m:
                group = m.groupdict()
                lsp_data = {
                    "lsp_id": int(group['lsp_id']),
                    "lsp_index": int(group['lsp_index']),
                    "lsp_seq_no": group['lsp_seq_no'],
                }
                v6pfx_dict[
                    "lsp"
                ] = lsp_data
                continue

            #Metric: 0, Algoritm: 128
            m = p5.match(line)
            if m:
                group = m.groupdict()
                v6pfx_dict["metric"] = (
                    int(group["metric"])
                )
                v6pfx_dict["algorithm"] = (
                    int(group["algorithm"])
                )
                continue

            #End SID: FCCC:CCC1:A1:: uN (PSP/USD)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                v6pfx_dict["srv6_end_sid"] = (
                    group["srv6_end_sid"]
                )
                v6pfx_dict["srv6_sid_behavior"] = (
                    group["srv6_sid_behavior"]
                )
                continue

        return ret_dict



