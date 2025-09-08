import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional

from genie.libs.parser.utils.common import Common


# ==================================
# Schema for:
#  * 'show device-tracking database mac details'
# ==================================
class ShowDeviceTrackingDatabaseMacDetailsSchema(MetaParser):
    """Schema for show device-tracking database mac details"""

    schema = {
        "device": {
            int: {
                "dev_code": str,
                "link_layer_address": str,
                "interface": str,
                "vlan_id": int,
                "prim_vlan_id": int,
                "pref_level": str,
                "state": str,
                Optional("time_left"): str,
                "policy": str,
                Optional("input_index"): int,
                Optional("attached"): {
                    int: {
                        "ip": str,
                    }
                }
            }
        }
    }

# ==================================
# Parser for:
#  * 'show device-tracking database mac details'
# ==================================
class ShowDeviceTrackingDatabaseMacDetails(ShowDeviceTrackingDatabaseMacDetailsSchema):
    """Parser for show device-tracking database mac details"""

    cli_command = 'show device-tracking database mac details'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)

        else:
            out = output

        device_tracking_database_mac_details_dict = {}

        #      MAC                    Interface  vlan(prim) prlvl      state            Time left        Policy           Input_index
        # AUT  dead.beef.0001         Gi1/0/1    20  (  20) TRUSTED    MAC-REACHABLE    235 s            LISP-DT-GUARD-VLAN 9       
        # 	 Attached IP: 20.0.0.1        
        # L    cc70.edae.dd56         Vl20       20  (  20) TRUSTED    MAC-REACHABLE    N/A              LISP-DT-GUARD-VLAN 53      
        # L    ba25.cdf4.ad38         Vl20       20  (  20) TRUSTED    MAC-REACHABLE    N/A              LISP-DT-GUARD-VLAN 53      
        # 	 Attached IP: 20.0.0.254      
        # 	 Attached IP: FE80::B825:CDFF:FEF4:AD38
        # 	 Attached IP: 2001::100   

        p0 = re.compile(
            r"^(?P<dev_code>\S+)"
            r"\s+(?P<link_layer_address>(\S+\.\S+\.\S+))"
            r"\s+(?P<interface>\S+)"
            r"\s+(?P<vlan_id>\d+)"
            r"(\s*\(\s*(?P<prim_vlan_id>\d+)\))?"
            r"\s+(?P<prlvl>\S+|\S+\s?\S+)"
            r"\s+(?P<state>\S+)"
            r"(\s+(?P<time_left>\S+\ss|N\/A))?"
            r"\s+(?P<policy>\S+)"
            r"(\s+(?P<input_index>\d+))?$"
        )
        attached_capture = re.compile(
            r"^Attached IP: (?P<ip>\S+)$"
        )
        device_index = 0
        attached_counter = 0
        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # L    cc70.edae.dd56         Vl20       20  (  20) TRUSTED    MAC-REACHABLE    N/A              LISP-DT-GUARD-VLAN 53      
            m = p0.match(line)
            if m:
                device_index += 1
                attached_counter = 0
                groups = m.groupdict()
                index_dict = device_tracking_database_mac_details_dict.setdefault('device', {}).setdefault(device_index, {})
                index_dict['dev_code'] = groups['dev_code']
                index_dict['link_layer_address'] = groups['link_layer_address']
                index_dict['interface'] = groups['interface']
                index_dict['vlan_id'] = int(groups['vlan_id'])
                index_dict['prim_vlan_id'] = int(groups['prim_vlan_id'])
                index_dict['pref_level'] = groups['prlvl']
                index_dict['state'] = groups['state']
                index_dict["policy"] = groups['policy']

                if groups['time_left']:
                    index_dict['time_left'] = groups['time_left']
                if groups['input_index']:
                    index_dict['input_index'] = int(groups['input_index'])
                continue

            # 	 Attached IP: 20.0.0.1        
            m = attached_capture.match(line)
            if m:
                attached_counter += 1
                groups = m.groupdict()
                attached_dict = device_tracking_database_mac_details_dict['device'][device_index].setdefault('attached', {}).setdefault(attached_counter, {})
                attached_dict['ip'] = groups['ip']
                continue

        return device_tracking_database_mac_details_dict
