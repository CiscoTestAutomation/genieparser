"""show_gnxi.py

IOSXE parsers for the following commands
    * 'show gnxi state'
    * 'show gnxi state detail'
"""

import re

from genie.metaparser import MetaParser


def enabled_disabled_to_bool(value : str):
    ''' Returns True if argument string is "Enabled"
        else False
    '''
    if value == "Enabled":
        return True

    return False

def up_down_to_bool(value : str):
    ''' Returns True if argument string is "Up"
        else False
    '''
    if value == "Up":
        return True

    return False


class ShowGnxiStateSchema(MetaParser):
    ''' Schema for:
            show gnxi state
    '''
    schema = {
            "oper_state": {
                "admin_enabled": bool,
                "oper_up": bool
                }
            }


class ShowGnxiState(ShowGnxiStateSchema):
    ''' Parser for:
            show gnxi state
    '''
    cli_command = "show gnxi state"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        gnxi_state_dict = { "oper_state": {} }

        p_full = re.compile(r"(?P<admin_state>Disabled|Enabled)\s*(?P<oper_status>Down|Up)")

        matches = p_full.search(out)

        if matches:
            groups = matches.groupdict()

            gnxi_state_dict["oper_state"]["admin_enabled"] = enabled_disabled_to_bool(groups["admin_state"])
            gnxi_state_dict["oper_state"]["oper_up"] = up_down_to_bool(groups["oper_status"])

        else:
            gnxi_state_dict = {}

        return gnxi_state_dict


class ShowGnxiStateDetailSchema(MetaParser):
    ''' Schema for:
            show gnxi state detail
    '''
    schema = {
                "settings": {
                        "insecure_server": bool,
                        "insecure_port": int,
                        "secure_server": bool,
                        "secure_port": int,
                        "secure_client_authentication": bool,
                        "secure_trustpoint": str,
                        "secure_client_trustpoint": str,
                        "secure_password_authentication": bool
                    },

                "oper_state": {
                    "admin_enabled": bool,
                    "oper_up": bool,
                    "provisioned": bool,

                    "grpc": {
                        "admin_enabled": bool,
                        "oper_up": bool
                        },
                    "config_svc": {
                        "admin_enabled": bool,
                        "oper_up": bool
                        },
                    "telemetry_svc": {
                        "admin_enabled": bool,
                        "oper_up": bool
                        },
                    "cert_mgmt_svc": {
                        "admin_enabled": bool,
                        "oper_up": bool
                        },
                    "os_image_svc": {
                        "admin_enabled": bool,
                        "oper_up": bool,
                        "supported": bool
                        },
                    "factory_reset_svc": {
                        "admin_enabled": bool,
                        "oper_up": bool,
                        "supported": bool
                        }
                }
        }


class ShowGnxiStateDetail(ShowGnxiStateDetailSchema):
    ''' Parser for:
            show gnxi state detail
    '''
    cli_command = "show gnxi state detail"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        gnxi_state_detail_dict = {"settings": {},
                "oper_state": {
                    "grpc": {},
                    "config_svc": {},
                    "telemetry_svc": {},
                    "cert_mgmt_svc": {},
                    "os_image_svc": {},
                    "factory_reset_svc": {}
                    }
                }

        p_full = re.compile(r"Settings\n"
                r"=*\n"
                r"\s\sServer: (?P<insecure_server>Disabled|Enabled)\n"
                r"\s\sServer port: (?P<insecure_port>\d+)\n"
                r"\s\sSecure server: (?P<secure_server>Disabled|Enabled)\n"
                r"\s\sSecure server port: (?P<secure_port>\d+)\n"
                r"\s\sSecure client authentication: (?P<secure_client_auth>Disabled|Enabled)\n"
                r"\s\sSecure trustpoint:\s?(?P<secure_trustpoint>.*)\n"
                r"\s\sSecure client trustpoint:\s?(?P<secure_client_trustpoint>.*)\n"
                r"\s\sSecure password authentication: (?P<secure_pass_auth>Disabled|Enabled)\n\n"
                r"GNMI\n"
                r"====\n"
                r"\s\sAdmin state: (?P<admin_state>Disabled|Enabled)\n"
                r"\s\sOper status: (?P<oper_status>Down|Up)\n"
                r"\s\sState: (?P<bootstrapping_state>Provisioned|Default)\n\n"
                r"\s\sgRPC Server\n"
                r"\s\s-*\n"
                r"\s\s\s\sAdmin state: (?P<grpc_admin_state>Disabled|Enabled)\n"
                r"\s\s\s\sOper status: (?P<grpc_oper_status>Down|Up)\n\n"
                r"\s\sConfiguration service\n"
                r"\s\s-*\n"
                r"\s\s\s\sAdmin state: (?P<config_svc_admin_state>Disabled|Enabled)\n"
                r"\s\s\s\sOper status: (?P<config_svc_oper_status>Down|Up)\n\n"
                r"\s\sTelemetry service\n"
                r"\s\s-*\n"
                r"\s\s\s\sAdmin state: (?P<telemetry_svc_admin_state>Disabled|Enabled)\n"
                r"\s\s\s\sOper status: (?P<telemetry_svc_oper_status>Down|Up)\n\n"
                r"GNOI\n"
                r"====\n\n"
                r"\s\sCert Management service\n"
                r"\s\s-*\n"
                r"\s\s\s\sAdmin state: (?P<cert_svc_admin_state>Disabled|Enabled)\n"
                r"\s\s\s\sOper status: (?P<cert_svc_oper_status>Down|Up)\n\n"
                r"\s\sOS Image service\n"
                r"\s\s-*\n"
                r"\s\s\s\sAdmin state: (?P<os_svc_admin_state>Disabled|Enabled)\n"
                r"\s\s\s\sOper status: (?P<os_svc_oper_status>Down|Up)\n"
                r"\s\s\s\sSupported: (?P<os_svc_supported>Not supported on this platform|Supported)\n\n"
                r"\s\sFactory Reset service\n"
                r"\s\s-*\n"
                r"\s\s\s\sAdmin state: (?P<reset_svc_admin_state>Disabled|Enabled)\n"
                r"\s\s\s\sOper status: (?P<reset_svc_oper_status>Down|Up)\n"
                r"\s\s\s\sSupported: (?P<reset_svc_supported>Not supported on this platform|Supported)")

        out = "\n".join(out.splitlines())

        matches = p_full.match(out)

        if matches:
            groups = matches.groupdict()

            # gnmib settings and configuration
            gnxi_state_detail_dict["settings"]["insecure_server"] = enabled_disabled_to_bool(groups["insecure_server"])
            gnxi_state_detail_dict["settings"]["insecure_port"] = int(groups["insecure_port"])
            gnxi_state_detail_dict["settings"]["secure_server"] = enabled_disabled_to_bool(groups["secure_server"])
            gnxi_state_detail_dict["settings"]["secure_port"] = int(groups["secure_port"])
            gnxi_state_detail_dict["settings"]["secure_client_authentication"] = enabled_disabled_to_bool(groups["secure_client_auth"])
            gnxi_state_detail_dict["settings"]["secure_trustpoint"] = str(groups["secure_trustpoint"])
            gnxi_state_detail_dict["settings"]["secure_client_trustpoint"] = str(groups["secure_client_trustpoint"])
            gnxi_state_detail_dict["settings"]["secure_password_authentication"] = enabled_disabled_to_bool(groups["secure_pass_auth"])

            # gnmi broker information
            gnxi_state_detail_dict["oper_state"]["admin_enabled"] = enabled_disabled_to_bool(groups["admin_state"])
            gnxi_state_detail_dict["oper_state"]["oper_up"]       = up_down_to_bool(groups["oper_status"])
            gnxi_state_detail_dict["oper_state"]["provisioned"]   = groups["bootstrapping_state"] == "Provisioned"

            # grpc server information
            gnxi_state_detail_dict["oper_state"]["grpc"]["admin_enabled"] = enabled_disabled_to_bool(groups["grpc_admin_state"])
            gnxi_state_detail_dict["oper_state"]["grpc"]["oper_up"] = up_down_to_bool(groups["grpc_oper_status"])

            # configuration interface information
            gnxi_state_detail_dict["oper_state"]["config_svc"]["admin_enabled"] = enabled_disabled_to_bool(groups["config_svc_admin_state"])
            gnxi_state_detail_dict["oper_state"]["config_svc"]["oper_up"] = up_down_to_bool(groups["config_svc_oper_status"])

            # telemetry interface information
            gnxi_state_detail_dict["oper_state"]["telemetry_svc"]["admin_enabled"] = enabled_disabled_to_bool(groups["telemetry_svc_admin_state"])
            gnxi_state_detail_dict["oper_state"]["telemetry_svc"]["oper_up"] = up_down_to_bool(groups["telemetry_svc_oper_status"])

            # certificate management interface information
            gnxi_state_detail_dict["oper_state"]["cert_mgmt_svc"]["admin_enabled"] = enabled_disabled_to_bool(groups["cert_svc_admin_state"])
            gnxi_state_detail_dict["oper_state"]["cert_mgmt_svc"]["oper_up"] = up_down_to_bool(groups["cert_svc_oper_status"])

            # os image interface information
            gnxi_state_detail_dict["oper_state"]["os_image_svc"]["admin_enabled"] = enabled_disabled_to_bool(groups["os_svc_admin_state"])
            gnxi_state_detail_dict["oper_state"]["os_image_svc"]["oper_up"] = up_down_to_bool(groups["os_svc_oper_status"])
            gnxi_state_detail_dict["oper_state"]["os_image_svc"]["supported"] = groups["os_svc_supported"] == "Supported"

            # factory reset interface information
            gnxi_state_detail_dict["oper_state"]["factory_reset_svc"]["admin_enabled"] = enabled_disabled_to_bool(groups["reset_svc_admin_state"])
            gnxi_state_detail_dict["oper_state"]["factory_reset_svc"]["oper_up"] = up_down_to_bool(groups["reset_svc_oper_status"])
            gnxi_state_detail_dict["oper_state"]["factory_reset_svc"]["supported"] = groups["reset_svc_supported"] == "Supported"

        else:
            gnxi_state_detail_dict = {}

        return gnxi_state_detail_dict
