import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, And, Default, Use


class ShowModuleSchema(MetaParser):
    """Schema for show module"""

    schema = {
        "slot": {
            Optional("rp"): {
                Any(): {
                    Any(): {
                        "ports": str,
                        "slot": str,
                        Optional("model"): str,
                        "status": str,
                        Optional("software"): str,
                        Optional("hardware"): str,
                        Optional("mac_address"): str,
                        Optional("serial_number"): str,
                        Optional("online_diag_status"): str,
                        Optional("slot/world_wide_name"): str,
                    }
                },
            },
            Optional("lc"): {
                Optional(Any()): {
                    Optional(Any()): {
                        Optional("ports"): str,
                        "slot": str,
                        Optional("model"): str,
                        Optional("status"): str,
                        Optional("software"): str,
                        Optional("hardware"): str,
                        Optional("mac_address"): str,
                        Optional("serial_number"): str,
                        Optional("online_diag_status"): str,
                        Optional("slot/world_wide_name"): str,
                    }
                },
            },
        },
        Optional("xbar"): {
            Optional(Any()): {
                Optional("ports"): str,
                "slot": str,
                Optional("module_type"): str,
                Optional("model"): str,
                Optional("status"): str,
                Optional("software"): str,
                Optional("hardware"): str,
                Optional("mac_address"): str,
                Optional("serial_number"): str,
            }
        },
        Optional("lem"): {
            Optional(Any()): {
                Optional("ports"): str,
                "slot": str,
                Optional("module_type"): str,
                Optional("model"): str,
                Optional("status"): str,
                Optional("software"): str,
                Optional("hardware"): str,
                Optional("mac_address"): str,
                Optional("online_diag_status"): str,
                Optional("slot/world_wide_name"): str,
                Optional("serial_number"): str,
            }
        },
        Optional("sam"): {
            Optional(Any()): #Module
            {
                Optional(Any()): # SAM
                {
                Optional("module_type"): str,
                Optional("model"): str,
                Optional("status"): str,
                Optional("software"): str,
                Optional("hardware"): str,
                Optional("online_diag_status"): str,
                Optional("serial_number"): str
                }
            }
        },
    }


class ShowModule(ShowModuleSchema):
    """Parser for show module"""

    cli_command = "show module"

    def cli(self, output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        module_dict = {}
        table_header = None
        header_type = None
        lem_hit = False
        parse_status = False
        rp_list = []
        map_dic = {}

        # Mod  Ports  Module-Type                         Model              Status
        p1 = re.compile(r"^\s*Mod.*$")

        # Xbar Ports  Module-Type                         Model              Status
        p2 = re.compile(r"^\s*Xbar.*$")

        # Lem Ports             Module-Type                      Model           Status
        p2_1 = re.compile(r"^\s*Lem.*$")

        # 1    1     DPU                       DPU-PART-NUM          ok
        p2_3 = re.compile(r"^\s*(?P<module>\d+)\s+(?P<sam_number>\d+)\s+(?P<descr>Service Accelerator Module|DPU)\s+(?P<model>[A-Za-z0-9\-]+)\s+(?P<status>\S+)")

        # 1 18 1/10/25/40G IPS, 4/8/16/32G FC/Sup-4 DS-C9220I-K9-SUP active *
        # 8    36   36x400G QSFP56-DD Ethernet Module                N9K-X9836DM-A         ok
        # 27   0    Supervisor Module                                N9K-C9800-SUP-A       active *
        # 1    36   28x100/40G + 8x400G QSFP-DD Ethernet Module      N9K-C93600CD-GX
        p3 = re.compile(
            r"^(?P<number>[0-9]+)\s+(?P<ports>[0-9]+)\s+(?P<module_type>.+?)\s+"
            r"((?P<model>[A-Z0-9v\-\+]+))?((\s+(?P<status>[a-z\- ]+)(\s\*)?)?)$"
        )

        # 1 9.4(0)SK(0.135) 1.0 20:01:00:08:31:14:b7:60 to 20:10:00:08:31:14:b7:60
        # 7    10.3(2)IOV9(0.190)       1.0    LC7
        # 1    NA               3.1
        p4 = re.compile(
            r"^(?P<number>[\d]+)\s+(?P<software>[A-Z0-9\(\)\.]+)\s+"
            r"(?P<hardware>\d+\.\d+)(\s+(?P<slot>[A-Z]+\d+))?"
            r"(\s+(?P<world_wide_name>[\w\:\s-]+))?$"
        )

        # 1 e0-69-ba-60-02-00 to e0-69-ba-60-02-0f JAE26361EB4
        p5 = re.compile(
            r"^\s*(?P<number>[0-9]+) +(?P<mac_address>[a-zA-Z0-9\.\-\s]+) +(?P<serial_number>[A-Z0-9]+)$"
        )

        # 7    Pass
        p6 = re.compile(r"^\s*(?P<number>[0-9]+) +(?P<online_diag_status>[a-zA-Z]+)$")

        #  active *
        p7 = re.compile(r"^\s*(?P<status>\S+)")

        # 1    1    1.99.0-43                     FSJ2128000B      Pass
        p8 = re.compile(r"^(?P<module>\d+)\s+(?P<sam_number>\d+)\s+(?P<software>\S+)"
                        r"\s+(?P<hardware>\S+)?\s+(?P<serial_num>\S+)"
                        r"(\s+(?P<diag_status>\S+))$")

        for line in out.splitlines():
            line = line.rstrip()

            # Mod  Ports  Module-Type                         Model              Status
            m = p1.match(line)
            if m:
                table_header = "slot"
                if "slot" not in module_dict:
                    module_dict["slot"] = {}
                if ("Mod DPU" in line or "Mod SAM" in line) and "sam" not in module_dict:
                    module_dict['sam'] = {}
                continue

            # Xbar Ports  Module-Type                         Model              Status
            m = p2.match(line)
            if m:
                table_header = "xbar"
                if "xbar" not in module_dict:
                    module_dict["xbar"] = {}
                continue

            # Lem Ports             Module-Type                      Model           Status
            m = p2_1.match(line)
            if m:
                table_header = "lem"
                lem_hit = True
                if "lem" not in module_dict:
                    module_dict["lem"] = {}
                continue

            # 1    1     DPU                       N9324C-SE1U-DPU       ok
            m = p2_3.match(line)
            if m:
                match_dict = m.groupdict()
                mod = match_dict.get("module")
                sam_num = match_dict.get("sam_number")
                descr = match_dict.get("descr")
                model = match_dict.get("model")
                status = match_dict.get("status")
                sam_dict_module = module_dict["sam"].setdefault(mod, {})
                sam_dict_sam = sam_dict_module.setdefault(sam_num, {})
                sam_dict_sam.update({"module_type": descr, "model": model, "status": status})
                continue

            # 1 18 1/10/25/40G IPS, 4/8/16/32G FC/Sup-4 DS-C9220I-K9-SUP active *
            # 8    36   36x400G QSFP56-DD Ethernet Module                N9K-X9836DM-A         ok
            # 27   0    Supervisor Module                                N9K-C9800-SUP-A       active *
            # 1    36   28x100/40G + 8x400G QSFP-DD Ethernet Module      N9K-C93600CD-GX
            m = p3.match(line)
            if m:
                header_number = m.groupdict()["number"]
                module_type = m.groupdict()["module_type"]
                if "Supervisor" in module_type or "Sup" in module_type:
                    header_type = "rp"
                    if header_type not in module_dict["slot"]:
                        module_dict["slot"][header_type] = {}
                    rp_list.append(header_number)
                    rp_name = m.groupdict()["module_type"].strip()
                    map_dic[header_number] = rp_name
                else:
                    header_type = "lc"
                    lc_name = m.groupdict()["module_type"].strip()
                    map_dic[header_number] = lc_name

                if table_header == "slot":
                    if header_number in rp_list:
                        if header_number not in module_dict["slot"]["rp"]:
                            module_dict["slot"]["rp"][header_number] = {}
                        if rp_name not in module_dict["slot"]["rp"][header_number]:
                            module_dict["slot"]["rp"][header_number][rp_name] = {
                                "slot": header_number
                            }
                        module_dict["slot"]["rp"][header_number][rp_name][
                            "ports"
                        ] = m.groupdict()["ports"].strip()
                        if m.groupdict()["model"]:
                            module_dict["slot"]["rp"][header_number][rp_name][
                                "model"
                            ] = m.groupdict()["model"].strip()
                        if m.groupdict()["status"]:
                            module_dict["slot"]["rp"][header_number][rp_name][
                                "status"
                            ] = m.groupdict()["status"].strip()
                        else:
                            parse_status = True
                    else:
                        if header_type not in module_dict["slot"]:
                            module_dict["slot"][header_type] = {}
                        if header_number not in module_dict["slot"]["lc"]:
                            module_dict["slot"]["lc"][header_number] = {}
                        if lc_name not in module_dict["slot"]["lc"][header_number]:
                            module_dict["slot"]["lc"][header_number][lc_name] = {
                                "slot": header_number
                            }
                        module_dict["slot"]["lc"][header_number][lc_name][
                            "ports"
                        ] = m.groupdict()["ports"].strip()
                        if m.groupdict()["model"]:
                            module_dict["slot"]["lc"][header_number][lc_name][
                                "model"
                            ] = m.groupdict()["model"].strip()
                        if m.groupdict()["status"]:
                            module_dict["slot"]["lc"][header_number][lc_name][
                                "status"
                            ] = m.groupdict()["status"].strip()
                        else:
                            parse_status = True
                elif table_header == "xbar":
                    if header_number not in module_dict["xbar"]:
                        module_dict["xbar"][header_number] = {"slot": header_number}
                    module_dict["xbar"][header_number]["ports"] = m.groupdict()[
                        "ports"
                    ].strip()
                    module_dict["xbar"][header_number]["module_type"] = m.groupdict()[
                        "module_type"
                    ].strip()
                    if m.groupdict()["model"]:
                        module_dict["xbar"][header_number]["model"] = m.groupdict()[
                            "model"
                        ].strip()
                    module_dict["xbar"][header_number]["status"] = m.groupdict()[
                        "status"
                    ].strip()
                elif table_header == "lem":
                    if header_number not in module_dict["lem"]:
                        module_dict["lem"][header_number] = {"slot": header_number}
                    module_dict["lem"][header_number]["ports"] = m.groupdict()[
                        "ports"
                    ].strip()
                    module_dict["lem"][header_number]["module_type"] = m.groupdict()[
                        "module_type"
                    ].strip()
                    if m.groupdict()["model"]:
                        module_dict["lem"][header_number]["model"] = m.groupdict()[
                            "model"
                        ].strip()
                    module_dict["lem"][header_number]["status"] = m.groupdict()[
                        "status"
                    ].strip()
                continue

            # 1 9.4(0)SK(0.135) 1.0 20:01:00:08:31:14:b7:60 to 20:10:00:08:31:14:b7:60
            # 7    10.3(2)IOV9(0.190)       1.0    LC7
            # 1    NA               3.1
            m = p4.match(line)
            if m:
                header_number = m.groupdict()["number"]
                world_wide_name = (
                    m.groupdict()["world_wide_name"]
                    if m.groupdict()["world_wide_name"]
                    else m.groupdict()["slot"]
                )
                if table_header == "slot" and not lem_hit:
                    if header_number in rp_list:
                        rp_name = map_dic[header_number]
                        module_dict["slot"]["rp"][header_number][rp_name][
                            "software"
                        ] = m.groupdict()["software"].strip()
                        module_dict["slot"]["rp"][header_number][rp_name][
                            "hardware"
                        ] = m.groupdict()["hardware"].strip()
                    else:
                        lc_name = map_dic[header_number]
                        module_dict["slot"]["lc"][header_number][lc_name][
                            "software"
                        ] = m.groupdict()["software"].strip()
                        module_dict["slot"]["lc"][header_number][lc_name][
                            "hardware"
                        ] = m.groupdict()["hardware"].strip()
                    if world_wide_name:
                        if header_number in rp_list:
                            module_dict["slot"]["rp"][header_number][rp_name][
                                "slot/world_wide_name"
                            ] = (
                                m.groupdict()["world_wide_name"]
                                if m.groupdict()["world_wide_name"]
                                else m.groupdict()["slot"]
                            )
                        else:
                            module_dict["slot"]["lc"][header_number][lc_name][
                                "slot/world_wide_name"
                            ] = (
                                m.groupdict()["world_wide_name"]
                                if m.groupdict()["world_wide_name"]
                                else m.groupdict()["slot"]
                            )
                elif table_header == "xbar":
                    module_dict["xbar"][header_number]["software"] = m.groupdict()[
                        "software"
                    ].strip()
                    module_dict["xbar"][header_number]["hardware"] = m.groupdict()[
                        "hardware"
                    ].strip()
                    if world_wide_name:
                        module_dict["xbar"][header_number]["slot/world_wide_name"] = (
                            m.groupdict()["world_wide_name"]
                            if m.groupdict()["world_wide_name"]
                            else m.groupdict()["slot"]
                        )
                elif table_header == "lem" or lem_hit:
                    module_dict["lem"][header_number]["software"] = m.groupdict()[
                        "software"
                    ].strip()
                    module_dict["lem"][header_number]["hardware"] = m.groupdict()[
                        "hardware"
                    ].strip()
                    if world_wide_name:
                        module_dict["lem"][header_number]["slot/world_wide_name"] = (
                            m.groupdict()["world_wide_name"]
                            if m.groupdict()["world_wide_name"]
                            else m.groupdict()["slot"]
                        )
                continue

            # 1 e0-69-ba-60-02-00 to e0-69-ba-60-02-0f JAE26361EB4
            m = p5.match(line)
            if m:
                header_number = m.groupdict()["number"]
                if table_header == "slot":
                    if header_number in rp_list:
                        rp_name = map_dic[header_number]
                        module_dict["slot"]["rp"][header_number][rp_name][
                            "mac_address"
                        ] = m.groupdict()["mac_address"].strip()
                        module_dict["slot"]["rp"][header_number][rp_name][
                            "serial_number"
                        ] = m.groupdict()["serial_number"].strip()
                    else:
                        lc_name = map_dic[header_number]
                        module_dict["slot"]["lc"][header_number][lc_name][
                            "mac_address"
                        ] = m.groupdict()["mac_address"].strip()
                        module_dict["slot"]["lc"][header_number][lc_name][
                            "serial_number"
                        ] = m.groupdict()["serial_number"].strip()
                elif table_header == "xbar":
                    module_dict["xbar"][header_number]["mac_address"] = m.groupdict()[
                        "mac_address"
                    ].strip()
                    module_dict["xbar"][header_number]["serial_number"] = m.groupdict()[
                        "serial_number"
                    ].strip()
                elif table_header == "lem":
                    module_dict["lem"][header_number]["mac_address"] = m.groupdict()[
                        "mac_address"
                    ].strip()
                    module_dict["lem"][header_number]["serial_number"] = m.groupdict()[
                        "serial_number"
                    ].strip()
                continue

            # 7    Pass
            m = p6.match(line)
            if m:
                header_number = m.groupdict()["number"]
                if table_header == "slot":
                    if header_number in rp_list:
                        rp_name = map_dic[header_number]
                        module_dict["slot"]["rp"][header_number][rp_name][
                            "online_diag_status"
                        ] = m.groupdict()["online_diag_status"].strip()
                    else:
                        lc_name = map_dic[header_number]
                        module_dict["slot"]["lc"][header_number][lc_name][
                            "online_diag_status"
                        ] = m.groupdict()["online_diag_status"].strip()
                elif table_header == "lem":
                    module_dict["lem"][header_number][
                        "online_diag_status"
                    ] = m.groupdict()["online_diag_status"].strip()
                continue

            #  active *
            m = p7.match(line)
            if m and parse_status is True:
                if header_number in rp_list:
                    module_dict["slot"]["rp"][header_number][rp_name][
                        "status"
                    ] = m.groupdict()["status"].strip()
                else:
                    module_dict["slot"]["lc"][header_number][lc_name][
                        "status"
                    ] = m.groupdict()["status"].strip()
                parse_status = False

            #1    1    1.99.0-43                     FDO283707X4      Pass
            m = p8.match(line)
            if m:
                match_dict = m.groupdict()
                mod = match_dict.get("module")
                sam_num = match_dict.get("sam_number")
                software = match_dict.get("software")
                hardware = match_dict.get("hardware")
                sn = match_dict.get("serial_num")
                diag_status = match_dict.get("diag_status")
                sam_dict = module_dict["sam"]
                sam_dict[mod][sam_num].update({
                    "software": software,
                    "online_diag_status": diag_status,
                    "serial_number": sn
                    })
                if hardware: sam_dict[mod][sam_num].update({'hardware': hardware})

                continue

        # The case of n9k virtual device where no module was showing "supervisor" in the module type
        # if "slot" in module_dict:
        #     if "rp" not in module_dict["slot"].keys():
        #         for key in module_dict["slot"]["lc"].keys():
        #             rp_key = key
        #             break
        #         module_dict["slot"]["rp"] = {}
        #         module_dict["slot"]["rp"][rp_key] = module_dict["slot"]["lc"][rp_key]
        #         del module_dict["slot"]["lc"][rp_key]

        return module_dict
