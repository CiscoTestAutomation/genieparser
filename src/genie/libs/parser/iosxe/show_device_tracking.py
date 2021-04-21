import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==================================
# Schema for:
#  * 'show device-tracking database'
# ==================================
class ShowDeviceTrackingDatabaseSchema(MetaParser):
    """Schema for show device-tracking database."""

    schema = {
        "binding_table_count": int,
        "dynamic_entry_count": int,
        "binding_table_limit": int,
        "device": {
            int: {
                "dev_code": str,
                "network_layer_address": str,
                "link_layer_address": str,
                "interface": str,
                "vlan_id": int,
                "pref_level_code": int,
                "age": str,
                "state": str
            }
        }
    }   


# ==================================
# Parser for:
#  * 'show device-tracking database'
# ==================================
class ShowDeviceTrackingDatabase(ShowDeviceTrackingDatabaseSchema):
    """Parser for show device-tracking database"""

    cli_command = 'show device-tracking database'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        device_tracking_database_dict = {}

        # Binding Table has 10 entries, 0 dynamic (limit 200000)
        # Codes: L - Local, S - Static, ND - Neighbor Discovery, ARP - Address Resolution Protocol, DH4 - IPv4 DHCP, DH6 - IPv6 DHCP, PKT - Other Packet, API - API created
        # Preflevel flags (prlvl):
        # 0001:MAC and LLA match     0002:Orig trunk            0004:Orig access
        # 0008:Orig trusted trunk    0010:Orig trusted access   0020:DHCP assigned
        # 0040:Cga authenticated     0080:Cert authenticated    0100:Statically assigned
        #
        #
        #     Network Layer Address                   Link Layer Address Interface  vlan  prlvl age    state     Time left
        # L   10.22.66.10                            7081.05ff.eb40     Vl230      230   0100  10194mn REACHABLE
        # L   10.22.28.10                            7081.05ff.eb40     Vl238      238   0100  10255mn REACHABLE
        # L   10.22.24.10                            7081.05ff.eb40     Vl236      236   0100  10330mn REACHABLE
        # L   10.22.20.10                            7081.05ff.eb40     Vl234      234   0100  10329mn REACHABLE
        # L   10.22.16.10                            7081.05ff.eb40     Vl232      232   0100  10330mn REACHABLE
        # L   10.22.12.10                            7081.05ff.eb40     Vl228      228   0100  10330mn REACHABLE
        # L   10.22.8.10                             7081.05ff.eb40     Vl226      226   0100  10329mn REACHABLE
        # L   10.22.4.10                             7081.05ff.eb40     Vl224      224   0100  10329mn REACHABLE
        # L   10.22.0.10                             7081.05ff.eb40     Vl222      222   0100  10329mn REACHABLE
        # L   10.10.68.10                            7081.05ff.eb40     Vl243      243   0100  10330mn REACHABLE

        # Binding Table has 10 entries, 0 dynamic (limit 200000)
        binding_table_capture = re.compile(
            r"^Binding\s+Table\s+has\s+(?P<binding_table_count>\d+)\s+entries,\s+(?P<dynamic_entry_count>\d+)\s+dynamic\s+\(limit\s+(?P<binding_table_limit>\d+)\)$")
        # Codes: L - Local, S - Static, ND - Neighbor Discovery, ARP - Address Resolution Protocol, DH4 - IPv4 DHCP, DH6 - IPv6 DHCP, PKT - Other Packet, API - API created
        codes_capture = re.compile(
            r"^Codes:\s+L\s+-\s+Local,\s+S\s+-\s+Static,\s+ND\s+-\s+Neighbor\s+Discovery,\s+ARP\s+-\s+Address\s+Resolution\s+Protocol,\s+DH4\s+-\s+IPv4\s+DHCP,\s+DH6\s+-\s+IPv6\s+DHCP,\s+PKT\s+-\s+Other\s+Packet,\s+API\s+-\s+API\s+created$")
        # Preflevel flags (prlvl):
        pref_level_flag_codes_capture = re.compile(r"^Preflevel\s+flags\s+\(prlvl\):$")
        # 0001:MAC and LLA match     0002:Orig trunk            0004:Orig access
        pref_level_flags_2_capture = re.compile(
            r"^0001:MAC\s+and\s+LLA\s+match\s+0002:Orig\s+trunk\s+0004:Orig\s+access$")
        # 0008:Orig trusted trunk    0010:Orig trusted access   0020:DHCP assigned
        _capture = re.compile(r"^0008:Orig\s+trusted\s+trunk\s+0010:Orig\s+trusted\s+access\s+0020:DHCP\s+assigned$")
        # 0040:Cga authenticated     0080:Cert authenticated    0100:Statically assigned
        _capture = re.compile(r"^0040:Cga\s+authenticated\s+0080:Cert\s+authenticated\s+0100:Statically\s+assigned$")
        #     Network Layer Address                   Link Layer Address Interface  vlan  prlvl age    state     Time left
        device_info_header_capture = re.compile(
            r"^Network\s+Layer\s+Address\s+Link\s+Layer\s+Address\s+Interface\s+vlan\s+prlvl\s+age\s+state\s+Time\s+left$")
        # L   10.22.66.10                            7081.05ff.eb40     Vl230      230   0100  10194mn REACHABLE
        device_info_capture = re.compile(
            r"^(?P<dev_code>\S+)\s+(?P<network_layer_address>\S+)\s+(?P<link_layer_address>\S+)\s+(?P<interface>\S+)\s+(?P<vlan_id>\d+)\s+(?P<pref_level_code>\d+)\s+(?P<age>\S+)\s+(?P<state>\S+)$")

        device_index = 0

        for line in out.splitlines():
            line = line.strip()
            # Binding Table has 10 entries, 0 dynamic (limit 200000)
            if binding_table_capture.match(line):
                binding_table_capture_match = binding_table_capture.match(line)
                groups = binding_table_capture_match.groupdict()
                binding_table_count = int(groups['binding_table_count'])
                dynamic_entry_count = int(groups['dynamic_entry_count'])
                binding_table_limit = int(groups['binding_table_limit'])
                device_tracking_database_dict['binding_table_count'] = binding_table_count
                device_tracking_database_dict['dynamic_entry_count'] = dynamic_entry_count
                device_tracking_database_dict['binding_table_limit'] = binding_table_limit
                continue
            # Codes: L - Local, S - Static, ND - Neighbor Discovery, ARP - Address Resolution Protocol, DH4 - IPv4 DHCP, DH6 - IPv6 DHCP, PKT - Other Packet, API - API created
            elif codes_capture.match(line):
                codes_capture_match = codes_capture.match(line)
                groups = codes_capture_match.groupdict()
                continue
            # Preflevel flags (prlvl):
            elif pref_level_flag_codes_capture.match(line):
                pref_level_flag_codes_capture_match = pref_level_flag_codes_capture.match(line)
                groups = pref_level_flag_codes_capture_match.groupdict()
                continue
            # 0001:MAC and LLA match     0002:Orig trunk            0004:Orig access
            elif pref_level_flags_2_capture.match(line):
                pref_level_flags_2_capture_match = pref_level_flags_2_capture.match(line)
                groups = pref_level_flags_2_capture_match.groupdict()
                continue
            # 0008:Orig trusted trunk    0010:Orig trusted access   0020:DHCP assigned
            elif _capture.match(line):
                _capture_match = _capture.match(line)
                groups = _capture_match.groupdict()
                continue
            # 0040:Cga authenticated     0080:Cert authenticated    0100:Statically assigned
            elif _capture.match(line):
                _capture_match = _capture.match(line)
                groups = _capture_match.groupdict()
                continue
            #     Network Layer Address                   Link Layer Address Interface  vlan  prlvl age    state     Time left
            elif device_info_header_capture.match(line):
                device_info_header_capture_match = device_info_header_capture.match(line)
                groups = device_info_header_capture_match.groupdict()
                continue
            # L   10.22.66.10                            7081.05ff.eb40     Vl230      230   0100  10194mn REACHABLE
            elif device_info_capture.match(line):
                device_index = device_index + 1
                device_info_capture_match = device_info_capture.match(line)
                groups = device_info_capture_match.groupdict()
                dev_code = groups['dev_code']
                network_layer_address = groups['network_layer_address']
                link_layer_address = groups['link_layer_address']
                interface = groups['interface']
                vlan_id = int(groups['vlan_id'])
                pref_level_code = int(groups['pref_level_code'])
                age = groups['age']
                state = groups['state']
                if not device_tracking_database_dict.get('device', {}):
                    device_tracking_database_dict['device'] = {}
                device_tracking_database_dict['device'][device_index] = {}
                device_tracking_database_dict['device'][device_index].update({'dev_code': dev_code})
                device_tracking_database_dict['device'][device_index]['network_layer_address'] = network_layer_address
                device_tracking_database_dict['device'][device_index]['link_layer_address'] = link_layer_address
                device_tracking_database_dict['device'][device_index]['interface'] = interface
                device_tracking_database_dict['device'][device_index]['vlan_id'] = vlan_id
                device_tracking_database_dict['device'][device_index]['pref_level_code'] = pref_level_code
                device_tracking_database_dict['device'][device_index]['age'] = age
                device_tracking_database_dict['device'][device_index]['state'] = state
                continue

        return device_tracking_database_dict


# ======================================
# Schema for:
#  * 'show device-tracking database interface {interface}'
# ======================================
class ShowDeviceTrackingDatabaseInterfaceSchema(MetaParser):
    """Schema for show device-tracking database interface {interface}."""

    schema = {
        "binding_table": {"dynamic": int, "entries": int, "limit": int},
        "network_layer_address": {
            Any(): {
                "age": str,
                "code": str,
                "interface": str,
                "link_layer_address": str,
                "prlvl": str,
                "state": str,
                Optional("time_left"): str,
                "vlan": int,
            }
        },
    }


# ======================================
# Parser for:
#  * show device-tracking database interface {interface}'
# ======================================
class ShowDeviceTrackingDatabaseInterface(ShowDeviceTrackingDatabaseInterfaceSchema):
    """Parser for show device-tracking database interface {interface}"""

    cli_command = 'show device-tracking database interface {interface}'

    def cli(self, interface, output=None):
        if output is None:
            cmd = self.cli_command.format(interface=interface)
            out = self.device.execute(cmd)

        else:
            out = output

        # Binding Table has 87 entries, 75 dynamic (limit 100000)
        # Codes: L - Local, S - Static, ND - Neighbor Discovery, ARP - Address Resolution Protocol, DH4 - IPv4 DHCP, DH6 - IPv6 DHCP, PKT - Other Packet, API - API created
        # Preflevel flags (prlvl):
        # 0001:MAC and LLA match     0002:Orig trunk            0004:Orig access
        # 0008:Orig trusted trunk    0010:Orig trusted access   0020:DHCP assigned
        # 0040:Cga authenticated     0080:Cert authenticated    0100:Statically assigned

        # Network Layer Address               Link Layer Address Interface        vlan prlvl  age   state     Time left
        # L   10.160.48.1                             0000.0cff.94fe  Vl1024         1024  0100 42473mn REACHABLE
        # DH4 10.160.43.197                           94d4.69ff.e606  Te8/0/37       1023  0025  116s  REACHABLE  191 s try 0(557967 s)
        # DH4 10.160.42.157                           0896.adff.899b  Gi7/0/11       1023  0025   33s  REACHABLE  271 s try 0(447985 s)
        # DH4 10.160.42.124                           00b1.e3ff.c71d  Te2/0/39       1023  0025   30s  REACHABLE  272 s try 0(450251 s)
        #
        # ...OUTPUT OMMITTED...
        #
        # L   2001:db8:350b:919::1                    0000.0cff.94fd  Vl1023         1023  0100 42475mn REACHABLE
        # L   2001:db8:350b:411::1                         0000.0cff.94fc  Vl1022         1022  0100 42473mn REACHABLE

        # Binding Table has 87 entries, 75 dynamic (limit 100000)
        binding_table_capture = re.compile(
            r"^Binding Table has (?P<entries>\d+) entries, (?P<dynamic>\d+) dynamic \(limit (?P<limit>\d+)\)$"
            )

        # DH4 10.160.43.197                           94d4.69ff.e606  Te8/0/37       1023  0025  116s  REACHABLE  191 s try 0(557967 s)
        tracking_database_capture = re.compile(
            r"^(?P<code>\S+)\s+(?P<network_layer_address>\d+\.\d+\.\d+\.\d+|\S+\:\:\S+\:\S+\:\S+\:\S+)\s+(?P<link_layer_address>\S+\.\S+\.\S+)\s+(?P<interface>\S+)\s+(?P<vlan>\d+)\s+(?P<prlvl>\d+)\s+(?P<age>\d+\S+)\s+(?P<state>\S+)\s+(?P<time_left>\d+.*)$"
            )

        # L   10.160.48.1                             0000.0cff.94fe  Vl1024         1024  0100 42473mn REACHABLE
        local_database_capture = re.compile(
            r"^(?P<code>L)\s+(?P<network_layer_address>\d+\.\d+\.\d+\.\d+|\S+\:\:\S+\:\S+\:\S+\:\S+)\s+(?P<link_layer_address>\S+\.\S+\.\S+)\s+(?P<interface>\S+)\s+(?P<vlan>\d+)\s+(?P<prlvl>\d+)\s+(?P<age>\d+\S+)\s+(?P<state>\S+)$"
            )

        device_info_obj = {}

        capture_list = [
            binding_table_capture,
            tracking_database_capture,
            local_database_capture,
        ]

        for capture in capture_list:
            for line in out.splitlines():
                line = line.strip()

                match = capture.match(line)
                if match:
                    group = match.groupdict()

                    if capture == binding_table_capture:
                        # convert str to int
                        for item in group:
                            group[item] = int(group[item])

                        new_group = {"binding_table": group}
                        device_info_obj.update(new_group)

                    if (
                        capture == tracking_database_capture
                        or capture == local_database_capture
                    ):
                        # convert str to int
                        group["vlan"] = int(group["vlan"])

                        # pull a key from dict to use as new_key
                        new_key = "network_layer_address"
                        new_group = {group[new_key]: {}}

                        # update then pop new_key from the dict
                        new_group[group[new_key]].update(group)
                        new_group[group[new_key]].pop(new_key)

                        if not device_info_obj.get(new_key):
                            device_info_obj[new_key] = {}

                        device_info_obj[new_key].update(new_group)

        return device_info_obj
