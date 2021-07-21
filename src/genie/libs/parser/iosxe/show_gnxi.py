"""show_gnxi.py

IOSXE parsers for the following commands
    * 'show gnxi state'
    * 'show gnxi state detail'
"""

from collections import defaultdict
import re
from enum import Enum

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


def _enabled_disabled_to_bool(value : str):
    ''' Returns True if argument string is "Enabled"
        else False
    '''
    return value == "Enabled"

def _up_down_to_bool(value : str):
    ''' Returns True if argument string is "Up"
        else False
    '''
    return value == "Up"


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

        ret_dict = {}

        # Disabled         Down
        # Enabled          Up
        p_full = re.compile(r"(?P<admin_state>Disabled|Enabled)\s*(?P<oper_status>Down|Up)")

        matches = p_full.search(out)

        if matches:
            groups = matches.groupdict()

            ret_dict = { "oper_state": {} }

            ret_dict["oper_state"]["admin_enabled"] = _enabled_disabled_to_bool(groups["admin_state"])
            ret_dict["oper_state"]["oper_up"] = _up_down_to_bool(groups["oper_status"])

        return ret_dict


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
                    Optional("os_image_svc"): {
                        "admin_enabled": bool,
                        "oper_up": bool,
                        "supported": bool
                        },
                    Optional("factory_reset_svc"): {
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

    class GnmibSection(Enum):
        SETTINGS = "settings"
        GNMI_GRPC = "grpc"
        GNMI_CONF = "config_svc"
        GNMI_TELEMETRY = "telemetry_svc"
        GNOI_CERT = "cert_mgmt_svc"
        GNOI_OS = "os_image_svc"
        GNOI_RESET = "factory_reset_svc"


    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        current_gnmib_section = self.GnmibSection.SETTINGS

        # Server: Enabled
        # Server: Disabled
        p_server = re.compile(r"Server: (?P<insecure_server>Disabled|Enabled)")

        # Server port: 50052
        p_server_port = re.compile(r"Server port: (?P<insecure_port>\d+)")

        # Secure server: Enabled
        # Secure server: Disabled
        p_secure_server = re.compile(r"Secure server: (?P<secure_server>Disabled|Enabled)")

        # Secure server port: 9399
        p_secure_server_port = re.compile(r"Secure server port: (?P<secure_port>\d+)")

        # Secure client authentication: Disabled
        # Secure client authentication: Enabled
        p_secure_client_auth = re.compile(r"Secure client authentication: (?P<secure_client_auth>Disabled|Enabled)")

        # Secure trustpoint: Trustpoint_name_here
        p_secure_tp = re.compile(r"Secure trustpoint:\s?(?P<secure_trustpoint>.*)")

        # Secure client trustpoint: Trustpoint_name_here
        p_secure_client_tp = re.compile(r"Secure client trustpoint:\s?(?P<secure_client_trustpoint>.*)")

        # Secure password authentication: Disabled
        # Secure password authentication: Enabled
        p_secure_pwd_auth = re.compile(r"Secure password authentication: (?P<secure_pass_auth>Disabled|Enabled)")

        # State: Provisioned
        # State: Default
        p_bs_state = re.compile(r"State: (?P<bootstrapping_state>Provisioned|Default)")

        p_grpc_section = re.compile(r"gRPC Server")
        p_conf_section = re.compile(r"Configuration service")
        p_telemetry_section = re.compile(r"Telemetry service")
        p_cert_section = re.compile(r"Cert Management service")
        p_os_section = re.compile(r"OS Image service")
        p_reset_section = re.compile(r"Factory Reset service")

        # Admin state: Enabled
        # Admin state: Disabled
        p_admin_state = re.compile(r"Admin state: (?P<admin_state>Disabled|Enabled)")

        # Oper status: Up
        # Oper status: Down
        p_oper_status = re.compile(r"Oper status: (?P<oper_status>Down|Up)")

        # Supported: Supported
        # Supported: Not supported on this platform
        p_supported = re.compile(r"Supported: (?P<supported>Not supported on this platform|Supported)")

        ret_dict = defaultdict(dict)

        for line in out.splitlines():

            line = line.strip()

            match = p_server.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["settings"]["insecure_server"] = _enabled_disabled_to_bool(groups["insecure_server"])


            match = p_server_port.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["settings"]["insecure_port"] = int(groups["insecure_port"])


            match = p_secure_server.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["settings"]["secure_server"] = _enabled_disabled_to_bool(groups["secure_server"])


            match = p_secure_server_port.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["settings"]["secure_port"] = int(groups["secure_port"])


            match = p_secure_client_auth.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["settings"]["secure_client_authentication"] = _enabled_disabled_to_bool(groups["secure_client_auth"])


            match = p_secure_tp.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["settings"]["secure_trustpoint"] = str(groups["secure_trustpoint"])


            match = p_secure_client_tp.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["settings"]["secure_client_trustpoint"] = str(groups["secure_client_trustpoint"])


            match = p_secure_pwd_auth.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["settings"]["secure_password_authentication"] = _enabled_disabled_to_bool(groups["secure_pass_auth"])


            match = p_bs_state.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["oper_state"]["provisioned"] = groups["bootstrapping_state"] == "Provisioned"


            match = p_grpc_section.match(line)
            if match:
                groups = match.groupdict()
                current_gnmib_section = self.GnmibSection.GNMI_GRPC


            match = p_conf_section.match(line)
            if match:
                groups = match.groupdict()
                current_gnmib_section = self.GnmibSection.GNMI_CONF


            match = p_telemetry_section.match(line)
            if match:
                groups = match.groupdict()
                current_gnmib_section = self.GnmibSection.GNMI_TELEMETRY


            match = p_cert_section.match(line)
            if match:
                groups = match.groupdict()
                current_gnmib_section = self.GnmibSection.GNOI_CERT


            match = p_os_section.match(line)
            if match:
                groups = match.groupdict()
                current_gnmib_section = self.GnmibSection.GNOI_OS


            match = p_reset_section.match(line)
            if match:
                groups = match.groupdict()
                current_gnmib_section = self.GnmibSection.GNOI_RESET


            match = p_admin_state.match(line)
            if match:
                groups = match.groupdict()
                if current_gnmib_section == self.GnmibSection.SETTINGS:
                    ret_dict["oper_state"]["admin_enabled"] = _enabled_disabled_to_bool(groups["admin_state"])
                else:
                    ret_dict["oper_state"].setdefault(current_gnmib_section.value, {})["admin_enabled"] = _enabled_disabled_to_bool(groups["admin_state"])


            match = p_oper_status.match(line)
            if match:
                groups = match.groupdict()
                if current_gnmib_section == self.GnmibSection.SETTINGS:
                    ret_dict["oper_state"]["oper_up"] = _up_down_to_bool(groups["oper_status"])
                else:
                    ret_dict["oper_state"].setdefault(current_gnmib_section.value, {})["oper_up"] = _up_down_to_bool(groups["oper_status"])


            match = p_supported.match(line)
            if match:
                groups = match.groupdict()
                ret_dict["oper_state"].setdefault(current_gnmib_section.value, {})["supported"] = groups["supported"] == "Supported"


        return dict(ret_dict)
