"""show_platform_software_fed_matm.py
    * 'show platform software fed switch active matm macTable'
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And


# ======================================================
# Schema for 'show platform software fed switch active matm macTable'
# ======================================================
class ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema(MetaParser):
    """Schema for show platform software fed switch active matm macTable"""

    schema = {
        "vlan": {
            Any(): {
                "mac": {
                    Any(): {
                        "type": str,
                        "seq": int,
                        "ecbi": int,
                        "flags": int,
                        Optional("machandle"): str,
                        Optional("sihandle"): str,
                        Optional("rihandle"): str,
                        Optional("dihandle"): str,
                        "atime": int,
                        "etime": int,
                        "ports": str,
                        "con": str,
                    },
                },
            },
        },
        "number_of_address": int,
        "number_of_secure_address": int,
        "number_of_drop_address": int,
        "number_of_local_lisp_address": int,
        "number_of_remote_lisp_address": int,
    }


# ======================================================
# Parser for 'show platform software fed switch active matm macTable'
# ======================================================
class ShowPlatformSoftwareFedSwitchActiveMatmMactable(
    ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema
):
    """Parser for show platform software fed switch active matm macTable"""

    cli_command = ["show platform software fed switch active matm macTable",
                   "show platform software fed active matm macTable"]

    def cli(self, command=None, output=None, **kwargs):
        if output is None:
            output = self.device.execute(command)

        ret_dict = {}

        # VLAN   MAC                   Type  Seq#    EC_Bi  Flags  *a_time  *e_time  ports  Con
        # 1      c860.8fe7.a503       0x101    3673      0      0        300        0  FiftyGigE2/0/3  No
        p1 = re.compile(
            r"^(?P<vlan>[\d\-,]+)\s+"
            r"(?P<mac>(?:[a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+"
            r"(?P<type>0x[\w]+)\s+"
            r"(?P<seq>\d+)\s+"
            r"(?P<ecbi>\d+)\s+"
            r"(?P<flags>\d+)\s+"
            r"(?:(?P<machandle>0x[\w]+)\s+"
            r"(?P<sihandle>0x[\w]+)\s+"
            r"(?P<rihandle>0x[\w]+)\s+"
            r"(?P<dihandle>0x[\w]+)\s+)?"
            r"(?P<atime>\d+)\s+"
            r"(?P<etime>\d+)\s+"
            r"(?P<ports>[\w\/\.\-\:]+)\s+"
            r"(?P<con>\w+)$"
        )

        # Total Mac number of addresses:: 4
        p2 = re.compile(
            r"^Total Mac number of addresses:: (?P<number_of_address>(\d+))?"
        )

        # Total number of secure addresses:: 0
        p3 = re.compile(
            r"^Total number of secure addresses:: (?P<number_of_secure_address>(\d+))?"
        )

        # Total number of drop addresses:: 0
        p4 = re.compile(
            r"^Total number of drop addresses:: (?P<number_of_drop_address>(\d+))?"
        )

        # Total number of lisp local addresses:: 0
        p5 = re.compile(
            r"^Total number of lisp local addresses:: (?P<number_of_local_lisp_address>(\d+))?"
        )

        # Total number of lisp remote addresses:: 0
        p6 = re.compile(
            r"^Total number of lisp remote addresses:: (?P<number_of_remote_lisp_address>(\d+))?"
        )

        for line in output.splitlines():
            # Removes any trailing or leading spaces
            line = line.strip()

            # Checks for the table data
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan_dict = (
                    ret_dict.setdefault("vlan", {})
                    .setdefault(group["vlan"], {})
                    .setdefault("mac", {})
                    .setdefault(group["mac"], {})
                )
                vlan_dict.update(
                    {
                        "type": group["type"],
                        "seq": int(group["seq"]),
                        "ecbi": int(group["ecbi"]),
                        "flags": int(group["flags"]),
                        "atime": int(group["atime"]),
                        "etime": int(group["etime"]),
                        "ports": group["ports"],
                        "con": group["con"],
                    }
                )
                for handle_key in ["machandle", "sihandle", "rihandle", "dihandle"]:
                    if group.get(handle_key) is not None:
                        vlan_dict[handle_key] = group[handle_key]
                continue

            # Total Mac number of addresses:: 4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_address"] = int(group["number_of_address"])
                continue

            # Total number of secure addresses:: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_secure_address"] = int(
                    group["number_of_secure_address"]
                )
                continue

            # Total number of drop addresses:: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_drop_address"] = int(
                    group["number_of_drop_address"]
                )
                continue

            # Total number of lisp local addresses:: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_local_lisp_address"] = int(
                    group["number_of_local_lisp_address"]
                )
                continue

            # Total number of lisp remote addresses:: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_remote_lisp_address"] = int(
                    group["number_of_remote_lisp_address"]
                )
                continue

        return ret_dict
