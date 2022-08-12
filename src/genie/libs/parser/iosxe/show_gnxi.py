"""show_gnxi.py

IOSXE parsers for the following commands
    * 'show gnxi state'
    * 'show gnxi state detail'
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Or


class ShowGnxiStateSchema(MetaParser):
    """ Schema for:
            show gnxi state
    """
    schema = {
        'state': str,
        'status': str
    }


class ShowGnxiState(ShowGnxiStateSchema):
    """ Parser for:
            show gnxi state
    """
    cli_command = "show gnxi state"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Disabled         Down
        # Enabled          Up
        p_full = re.compile(r"^(?P<state>Disabled|Enabled)\s*(?P<status>Down|Up)$")

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            m = p_full.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

        return ret_dict


class ShowGnxiStateDetailSchema(MetaParser):
    """ Schema for:
            show gnxi state detail
    """
    schema = {
        'settings': {
            'server': str,
            'server_port': int,
            'secure_server': str,
            'secure_server_port': int,
            'secure_client_authentication': str,
            'secure_trustpoint': Or(str, None),
            'secure_client_trustpoint': Or(str, None),
            'secure_password_authentication': str
        },
        'gnmi': {
            'admin_state': str,
            'oper_status': str,
            'state': str,
            'grpc_server': {
                'admin_state': str,
                'oper_status': str
            },
            'configuration_service': {
                'admin_state': str,
                'oper_status': str
            },
            'telemetry_service': {
                'admin_state': str,
                'oper_status': str
            }
        },
        'gnoi': {
            'cert_management_service': {
                'admin_state': str,
                'oper_status': str
            },
            Optional('os_image_service'): {
                'admin_state': str,
                'oper_status': str,
                'supported': str
            },
            Optional('factory_reset_service'): {
                'admin_state': str,
                'oper_status': str,
                'supported': str
            }
        }
    }


class ShowGnxiStateDetail(ShowGnxiStateDetailSchema):
    """ Parser for:
            show gnxi state detail
    """
    cli_command = "show gnxi state detail"
    sections = {
        'SETTINGS': "settings",
        'GNMI': "gnmi",
        'GNOI': "gnoi"
    }
    subsections = {
        'GNMI_GRPC': "grpc_server",
        'GNMI_CONF': "configuration_service",
        'GNMI_TELEMETRY': "telemetry_service",
        'GNOI_CERT': "cert_management_service",
        'GNOI_OS': "os_image_service",
        'GNOI_RESET': "factory_reset_service"
    }

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # sections
        p_settings = re.compile(r"^Settings$")
        p_gnmi = re.compile(r"^GNMI$")
        p_gnoi = re.compile(r"^GNOI$")

        # subsections
        p_grpc_section = re.compile(r"^gRPC Server$")
        p_conf_section = re.compile(r"^Configuration service$")
        p_telemetry_section = re.compile(r"^Telemetry service$")
        p_cert_section = re.compile(r"^Cert Management service$")
        p_os_section = re.compile(r"^OS Image service$")
        p_reset_section = re.compile(r"^Factory Reset service$")

        # Server: Enabled
        # Server: Disabled
        p_server = re.compile(r"^Server: (?P<server>Disabled|Enabled)$")

        # Server port: 50052
        p_server_port = re.compile(r"^Server port: (?P<server_port>\d+)$")

        # Secure server: Enabled
        # Secure server: Disabled
        p_secure_server = re.compile(r"^Secure server: (?P<secure_server>Disabled|Enabled)$")

        # Secure server port: 9399
        p_secure_server_port = re.compile(r"^Secure server port: (?P<secure_server_port>\d+)$")

        # Secure client authentication: Disabled
        # Secure client authentication: Enabled
        p_secure_client_auth = re.compile(r"^Secure client authentication: "
                                          r"(?P<secure_client_authentication>Disabled|Enabled)$")

        # Secure trustpoint: Trustpoint_name_here
        p_secure_tp = re.compile(r"^Secure trustpoint:( +)?(?P<secure_trustpoint>\S+)?$")

        # Secure client trustpoint: Trustpoint_name_here
        p_secure_client_tp = re.compile(r"^Secure client trustpoint:( +)?(?P<secure_client_trustpoint>\S+)?$")

        # Secure password authentication: Disabled
        # Secure password authentication: Enabled
        p_secure_pwd_auth = re.compile(r"^Secure password authentication: "
                                       r"(?P<secure_password_authentication>Disabled|Enabled)$")

        # State: Provisioned
        # State: Default
        p_bs_state = re.compile(r"^State: (?P<state>Provisioned|Default)$")

        # Admin state: Enabled
        # Admin state: Disabled
        p_admin_state = re.compile(r"^Admin state: (?P<admin_state>Disabled|Enabled)$")

        # Oper status: Up
        # Oper status: Down
        p_oper_status = re.compile(r"^Oper status: (?P<oper_status>Down|Up)$")

        # Supported: Supported
        # Supported: Not supported on this platform
        p_supported = re.compile(r"^Supported: (?P<supported>Not supported on this platform|Supported)$")

        ret_dict = {}
        current_section = None
        current_subsection = None
        for line in output.splitlines():
            line = line.strip()

            # section matches

            # Settings
            # ========
            m = p_settings.match(line)
            if m:
                current_section = self.sections['SETTINGS']
                continue
            # GNMI
            # ====
            m = p_gnmi.match(line)
            if m:
                current_section = self.sections['GNMI']
                continue
            # GNOI
            # ====
            m = p_gnoi.match(line)
            if m:
                current_section = self.sections['GNOI']
                continue

            # subsection matches

            #   gRPC Server
            #   -----------
            m = p_grpc_section.match(line)
            if m:
                current_subsection = self.subsections['GNMI_GRPC']
                continue
            #   Configuration service
            #   ---------------------
            m = p_conf_section.match(line)
            if m:
                current_subsection = self.subsections['GNMI_CONF']
                continue
            #   Telemetry service
            #   -----------------
            m = p_telemetry_section.match(line)
            if m:
                current_subsection = self.subsections['GNMI_TELEMETRY']
                continue

            m = p_cert_section.match(line)
            #   Cert Management service
            #   -----------------
            if m:
                current_subsection = self.subsections['GNOI_CERT']
                continue
            #   OS Image service
            #   ----------------
            m = p_os_section.match(line)
            if m:
                current_subsection = self.subsections['GNOI_OS']
                continue
            #   Factory Reset service
            #   ---------------------
            m = p_reset_section.match(line)
            if m:
                current_subsection = self.subsections['GNOI_RESET']
                continue

            # settings exclusive matches

            # Server: Enabled
            # Server: Disabled
            m = p_server.match(line)
            if m:
                settings_dict = ret_dict.setdefault('settings', {})
                settings_dict.update(m.groupdict())
                continue

            # Server port: 50052
            m = p_server_port.match(line)
            if m:
                settings_dict.update({'server_port': int(m.groupdict()['server_port'])})
                continue

            # Secure server: Enabled
            # Secure server: Disabled
            m = p_secure_server.match(line)
            if m:
                settings_dict.update(m.groupdict())
                continue

            # Secure server port: 9399
            m = p_secure_server_port.match(line)
            if m:
                settings_dict.update({'secure_server_port': int(m.groupdict()['secure_server_port'])})
                continue

            # Secure client authentication: Disabled
            # Secure client authentication: Enabled
            m = p_secure_client_auth.match(line)
            if m:
                settings_dict.update(m.groupdict())
                continue

            # Secure trustpoint: Trustpoint_name_here
            m = p_secure_tp.match(line)
            if m:
                group = m.groupdict()
                if group['secure_trustpoint'] is not None:
                    settings_dict.update(m.groupdict())
                else:
                    settings_dict.update({'secure_trustpoint': None})
                continue

            # Secure client trustpoint: Trustpoint_name_here
            m = p_secure_client_tp.match(line)
            if m:
                group = m.groupdict()
                if group['secure_client_trustpoint'] is not None:
                    settings_dict.update(m.groupdict())
                else:
                    settings_dict.update({'secure_client_trustpoint': None})
                continue

            # Secure password authentication: Disabled
            # Secure password authentication: Enabled
            m = p_secure_pwd_auth.match(line)
            if m:
                settings_dict.update(m.groupdict())
                continue

            # GNMI exclusive matches

            # State: Provisioned
            # State: Default
            m = p_bs_state.match(line)
            if m:
                gnmi_dict = ret_dict.setdefault('gnmi', {})
                gnmi_dict.update(m.groupdict())
                continue

            # generic matches

            # Admin state: Enabled
            # Admin state: Disabled
            m = p_admin_state.match(line)
            if m:
                groups = m.groupdict()
                if current_subsection is None:
                    ret_dict.setdefault(current_section, {})['admin_state'] = groups['admin_state']
                else:
                    ret_dict.setdefault(current_section, {}).setdefault(current_subsection, {})['admin_state'] = \
                        groups["admin_state"]
                continue

            # Oper status: Up
            # Oper status: Down
            m = p_oper_status.match(line)
            if m:
                groups = m.groupdict()
                if current_subsection is None:
                    ret_dict.setdefault(current_section, {})['oper_status'] = groups['oper_status']
                else:
                    ret_dict.setdefault(current_section, {}).setdefault(current_subsection, {})['oper_status'] = \
                        groups["oper_status"]
                continue

            # Supported: Supported
            # Supported: Not supported on this platform
            m = p_supported.match(line)
            if m:
                groups = m.groupdict()
                if current_subsection is None:
                    ret_dict.setdefault(current_section, {})['supported'] = groups['supported']
                else:
                    ret_dict.setdefault(current_section, {}).setdefault(current_subsection, {})['supported'] = \
                        groups["supported"]
                continue

        return ret_dict
