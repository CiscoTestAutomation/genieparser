import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


# =====================================
# Schema for:
#  * 'show avc sd-service info summary'
# =====================================
class ShowAvcSdServiceInfoSummarySchema(MetaParser):
    """Schema for show avc sd-service info summary."""

    schema = {
        Optional("active_controller"): {
            "ip": str,
            "last_connection": str,
            "status": str,
            "type": str
        },
        Optional("standby_controller"): {
            "ip": str,
            "last_connection": str,
            "status": str,
            "type": str
        },
        Optional("device"): {
            Optional("id"): str,
            "address": str,
            "segment_name": str,
            Optional("dev_os_ver"): str,
            Optional("dev_type"): str
        },
        Optional("status"): str,
        Optional("sd_vac_status"): str,
    }


# =====================================
# Parser for:
#  * 'show avc sd-service info summary'
# =====================================
class ShowAvcSdServiceInfoSummary(ShowAvcSdServiceInfoSummarySchema):
    """Parser for show avc sd-service info summary"""

    cli_command = ["show avc sd-service info summary"]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        ret_dict = {}

        # Status: DISCONNECTED|CONNECTED
        p1 = re.compile(r'^Status:\s+(?P<status>(\w+))$')

        # Device ID: WLC.one-1_1
        # Device ID:
        p2 = re.compile(r'^Device ID:\s+(?P<id>([\w_\-.]+))$|Device ID:')

        # Device segment name: global (default)
        p3 = re.compile(r'^Device segment name:\s+(?P<segment_name>([\w\s\-()]*))$')

        # Device address: 1.0.0.1
        # Device address: 2001:bebe::1
        p4 = re.compile(r'^Device address:\s+(?P<address>((\d{1,3}\.){3}\d{1,3}|([a-fA-F\d]{1,4}:*:?){1,7}[a-fA-F\d]{1,4}))$')

        # Device OS version: 17.9.2
        p5 = re.compile(r'^Device OS version:\s+(?P<dev_os_ver>([\w.:_]*))$')

        # Device type: C9800-L-C-K9
        p6 = re.compile(r'^Device type:\s+(?P<dev_type>([\w-]*))$')

        #   Type: Primary
        p7 = re.compile(r'^\s+Type\s+:\s+(?P<type>(\w+))$')

        #   Address|IP : 1.0.0.1
        #   Address|IP : 2001:bebe::1
        p8 = re.compile(r'^(\s+Address|\s+IP)\s+:\s+(?P<ip>((\d{1,3}\.){3}\d{1,3}|([a-fA-F\d]{1,4}:*:?){1,7}[a-fA-F\d]{1,4}))$')

        #   Status  : Disconnected
        p9 = re.compile(r'^\s+Status\s?:\s+(?P<status>(\w+))$')

        #   Last connection: Never
        #   Last connection: 18:42:02.000 UTC Fri Oct 2 2020
        p10 = re.compile(r'^\s+Last connection\s*:\s+(?P<last_connection>\d{2}:\d{2}:\d{2}\.\d{3,6} \w{2,3}[A-Z] \w{3} \w{3}\s\d{1,2}\s\d{4}|Never)$')

        # SD-AVC is disabled
        p11 = re.compile(r'^SD-AVC is disabled$')

        # Active controller:
        p_active = re.compile(r'^Active controller:$')
        # Standby controller:
        p_standby = re.compile(r'^Standby controller:$')

        for line in output.splitlines():
            line = line.rstrip()
            # Status: DISCONNECTED|CONNECTED
            m = re.match(p1, line)
            if m:
                ret_dict.update({'status': m.groupdict()['status']})
                continue
            # Device ID: WLC.one-1_1
            # Device ID:
            m = re.match(p2, line)
            if m:
                device_dict = ret_dict.setdefault('device', {})
                id_name = m.groupdict().get('id')
                device_dict.update({'id': id_name if id_name else ""})
                continue
            # Device segment name: global (default)
            m = re.match(p3, line)
            if m:
                # To make it backwards compatible and return
                # only 'global' when 'global (default) appears'
                segment = m.groupdict()['segment_name']
                segment = segment.split('(')[0].strip()
                device_dict.update({'segment_name': segment})
                continue
            # Address : 1.0.0.1
            # IP : 2001:bebe::1
            m = re.match(p4, line)
            if m:
                device_dict.update({'address': m.groupdict()['address']})
                continue
            # Device OS version: 17.9.2
            m = re.match(p5, line)
            if m:
                device_dict.update({'dev_os_ver': m.groupdict()['dev_os_ver']})
                continue
            # Device type: C9800-L-C-K9
            m = re.match(p6, line)
            if m:
                device_dict.update({'dev_type': m.groupdict()['dev_type']})
                continue
            # Active controller:
            m = re.match(p_active, line)
            if m:
                ctrl_dict = ret_dict.setdefault('active_controller', {})
                continue
            # Standby controller:
            m = re.match(p_standby, line)
            if m:
                ctrl_dict = ret_dict.setdefault('standby_controller', {})
                continue
            #   Type  : Primary|Secondary
            m = re.match(p7, line)
            if m:
                ctrl_dict.update({'type': m.groupdict()['type']})
                continue
            #   IP|Address    : 10.11.236.21
            m = re.match(p8, line)
            if m:
                ctrl_dict.update({'ip': m.groupdict()['ip']})
                continue
            #   Status: Connected
            m = re.match(p9, line)
            if m:
                ctrl_dict.update({'status': m.groupdict()['status']})
                continue
            #   Last connection: Never
            #   Last connection: 18:42:02.000 UTC Fri Oct 2 2020
            m = re.match(p10, line)
            if m:
                ctrl_dict.update({'last_connection': m.groupdict()['last_connection']})
                continue

        m = re.match(p11, output.strip())
        if m:
            ret_dict = {"sd_vac_status": "disabled"}

        return ret_dict
