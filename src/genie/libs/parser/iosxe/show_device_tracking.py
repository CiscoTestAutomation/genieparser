import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


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

# ========================
# Schema for:
#   * 'show device-tracking database details'
# ========================
class ShowDeviceTrackingDatabaseDetailsSchema(MetaParser):
    '''Schema for:
        * 'show device-tracking database details'
    '''

    schema = {
        "binding_table_configuration": {
            "max/box": str,
            "max/port": str,
            "max/vlan": str,
            "max/mac": str,
        },
        "binding_table_count": {
            "dynamic": int,
            "local": int,
            "total": int,
        },
        "binding_table_state_count": {
            Optional("verify"): int,
            Optional("reachable"): int,
            Optional("stale"): int,
            Optional("down"): int,
            Optional("total"): int,
        },
        "device": {
            int: {
                "dev_code": str,
                "network_layer_address": str,
                "link_layer_address": str,
                "interface": str,
                "mode": str,
                "vlan_id": int,
                "pref_level_code": int,
                "age": str,
                "state": str,
                Optional("time_left"): str,
                "filter": str,
                "in_crimson": str,
                "client_id": str,
                Optional("policy"): str,
            },
        },
    }


# ========================
# Parser for:
#   * 'show device-tracking database details'
# ========================
class ShowDeviceTrackingDatabaseDetails(ShowDeviceTrackingDatabaseDetailsSchema):
    '''Parser for:
        * 'show device-tracking database details'
    '''

    cli_command = 'show device-tracking database details'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        device_tracking_database_details_dict = {}
        device_index = 0
        last_key = ''

        #  Binding table configuration:
        #  ----------------------------
        #  max/box  : no limit
        #  max/vlan : no limit
        #  max/port : no limit
        #  max/mac  : no limit

        #  Binding table current counters:
        #  ------------------------------
        #  dynamic  : 1
        #  local    : 1
        #  total    : 4

        #  Binding table counters by state:
        #  ----------------------------------
        #  REACHABLE  : 1
        #  STALE      : 2
        #  DOWN       : 1
        #    total    : 4

        # Codes: L - Local, S - Static, ND - Neighbor Discovery, ARP - Address Resolution Protocol, DH4 - IPv4 DHCP, DH6 - IPv6 DHCP, PKT - Other Packet, API - API created
        # Preflevel flags (prlvl):
        # 0001:MAC and LLA match     0002:Orig trunk            0004:Orig access
        # 0008:Orig trusted trunk    0010:Orig trusted access   0020:DHCP assigned
        # 0040:Cga authenticated     0080:Cert authenticated    0100:Statically assigned


        #     Network Layer Address                    Link Layer Address     Interface  mode       vlan(prim)   prlvl      age        state      Time left        Filter     In Crimson   Client ID          Policy (feature)
        # ND  100.100.100.1                            dead.beef.0001(S)      Twe1/0/42  access     39  (  39)      0024       92mn       STALE      83192 s          no         no           0000.0000.0000     test (Device-tracking)
        # L   39.39.39.1                               5c5a.c791.d69f(R)      Vl39       svi        39  (  39)      0100       11591mn    REACHABLE                   no         yes          0000.0000.0000
        # S   10.10.10.10                              dead.beef.0001(S)      Twe1/0/42  access     39  (  39)      0100       59mn       STALE      N/A              no         yes          0000.0000.0000
        # S   1000::1                                  000a.000b.000c(D)      Twe1/0/1   trunk      100 ( 100)      0100       30565mn    DOWN       N/A              no         yes          0000.0000.0000

        #  Binding table configuration:
        binding_table_configuration_capture = re.compile(r'^Binding\s+table\s+configuration:$')
        #  Binding table current counters:
        binding_table_counter_capture = re.compile(r'^Binding\s+table\s+current\s+counters:$')
        #  Binding table counters by state:
        binding_table_state_capture = re.compile(r'^Binding\s+table\s+counters\s+by\s+state:$')

        #  max/box  : no limit
        #  max/vlan : no limit
        #  max/port : no limit
        #  max/mac  : no limit
        #  dynamic  : 1
        #  local    : 1
        #  total    : 4
        #  REACHABLE  : 1
        #  STALE      : 2
        #  DOWN       : 1
        #    total    : 4
        binding_table_info = re.compile(r'^(?P<parameter>(\S+))\s+:\s+(?P<info>(\S+)|(\S+\s+\S+))$')

        #     Network Layer Address                    Link Layer Address     Interface  mode       vlan(prim)   prlvl      age        state      Time left        Filter     In Crimson   Client ID          Policy (feature)
        device_header_capture = re.compile(r'^Network\s+Layer\s+Address\s+Link\s+Layer\s+Address\s+Interface\s+mode\s+vlan\(prim\)\s+prlvl\s+age\s+state\s+Time\s+left\s+Filter\s+In\s+Crimson\s+Client\s+ID\s+Policy\s+\(feature\)$')

        # ND  100.100.100.1                            dead.beef.0001(S)      Twe1/0/42  access     39  (  39)      0024       92mn       STALE      83192 s          no         no           0000.0000.0000     test (Device-tracking)
        # L   39.39.39.1                               5c5a.c791.d69f(R)      Vl39       svi        39  (  39)      0100       11591mn    REACHABLE                   no         yes          0000.0000.0000
        # S   10.10.10.10                              dead.beef.0001(S)      Twe1/0/42  access     39  (  39)      0100       59mn       STALE      N/A              no         yes          0000.0000.0000
        # S   1000::1                                  000a.000b.000c(D)      Twe1/0/1   trunk      100 ( 100)      0100       30565mn    DOWN       N/A              no         yes          0000.0000.0000
        device_info_capture = re.compile(r'^(?P<dev_code>(\S+))\s+(?P<network_layer_address>(\S+))'
                                         r'\s+(?P<link_layer_address>(\S+))\s+(?P<interface>(\S+))'
                                         r'\s+(?P<mode>(\S+))\s+(?P<vlan_id>(\d+))\s+\(\s+\d+\)'
                                         r'\s+(?P<pref_level_code>(\d+))\s+(?P<age>(\S+))'
                                         r'\s+(?P<state>(\S+))\s+(?P<time_left>(try\s\d\s\d+\ss)|(N\/A)|(\d+\ss\stry\s\d)|(\d+\ss))?'
                                         r'\s+(?P<filter>(yes|no))\s+(?P<in_crimson>(\S+))'
                                         r'\s+(?P<client_id>(\S+))(\s+(?P<policy>(\S+)|(\S+\s+\S+)))?$')

        optional_parameters = [
            'time_left',
            'policy',
        ]

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            #  Binding table configuration:
            match = binding_table_configuration_capture.match(line)
            if match:
                last_key = "binding_table_configuration"
                device_tracking_database_details_dict.setdefault(last_key, {})
                continue

            #  Binding table current counters:
            match = binding_table_counter_capture.match(line)
            if match:
                last_key = "binding_table_count"
                device_tracking_database_details_dict.setdefault(last_key, {})
                continue

            #  Binding table counters by state:
            match = binding_table_state_capture.match(line)
            if match:
                last_key = "binding_table_state_count"
                device_tracking_database_details_dict.setdefault(last_key, {})
                continue

            #     Network Layer Address                    Link Layer Address     Interface  mode       vlan(prim)   prlvl      age        state      Time left        Filter     In Crimson   Client ID          Policy (feature)
            match = device_header_capture.match(line)
            if match:
                last_key = "device"
                device_tracking_database_details_dict.setdefault(last_key, {})
                continue

            if last_key:
                #  max/box  : no limit
                #  max/vlan : no limit
                #  max/port : no limit
                #  max/mac  : no limit
                #  dynamic  : 1
                #  local    : 1
                #  total    : 4
                #  REACHABLE  : 1
                #  STALE      : 2
                #  DOWN       : 1
                #    total    : 4
                match = binding_table_info.match(line)
                if match:
                    groups = match.groupdict()
                    key = groups['parameter'].lower()
                    value = groups['info']
                    if value.isdigit():
                        device_tracking_database_details_dict[last_key][key] = int(value)
                    else:
                        device_tracking_database_details_dict[last_key][key] = value
                    continue

                # ND  100.100.100.1                            dead.beef.0001(S)      Twe1/0/42  access     39  (  39)      0024       92mn       STALE      83192 s          no         no           0000.0000.0000     test (Device-tracking)
                # L   39.39.39.1                               5c5a.c791.d69f(R)      Vl39       svi        39  (  39)      0100       11591mn    REACHABLE                   no         yes          0000.0000.0000
                # S   10.10.10.10                              dead.beef.0001(S)      Twe1/0/42  access     39  (  39)      0100       59mn       STALE      N/A              no         yes          0000.0000.0000
                # S   1000::1                                  000a.000b.000c(D)      Twe1/0/1   trunk      100 ( 100)      0100       30565mn    DOWN       N/A              no         yes          0000.0000.0000
                match = device_info_capture.match(line)
                if match:
                    device_index += 1
                    groups = match.groupdict()
                    for parameter in optional_parameters:
                        if groups[parameter] == None:
                            groups[parameter] = ''

                    if not device_tracking_database_details_dict.get(last_key, {}):
                        device_tracking_database_details_dict.setdefault(last_key, {})

                    device_dict = device_tracking_database_details_dict.setdefault(last_key, {}) \
                                                                    .setdefault(device_index, {})

                    for key, value in groups.items():
                        if value.isdigit():
                            device_dict[key] = int(value)
                        else:
                            device_dict[key] = value

        return device_tracking_database_details_dict


# ========================
# Schema for:
#   * 'show device-tracking policy {policy_name}'
# ========================
class ShowDeviceTrackingPolicySchema(MetaParser):
    '''Schema for:
        * 'show device-tracking policy {policy_name}'
    '''

    schema = {
        "configuration": {
            Optional("trusted_port"): str,
            "security_level": str,
            "device_role": str,
            Optional("data_glean"): str,
            Optional("prefix_glean"): str,
            Any(): {
                "is_gleaning": str,
                Optional("protecting_prefix_list"): str,
            },
            Optional("limit_address_count"): {
                Optional('ipv4'): int,
                Optional('ipv6'): int,
            },
            Optional("cache_guard"): str,
            Optional("tracking"): str,
        },
        Optional("device"): {
            Optional(int): {
                "target": str,
                "policy_type": str,
                "policy_name": str,
                "feature": str,
                "tgt_range": str,
            },
        },
    }


# ========================
# Parser for:
#   * 'show device-tracking policy {policy_name}'
# ========================
class ShowDeviceTrackingPolicy(ShowDeviceTrackingPolicySchema):
    '''Parser for:
        * 'show device-tracking policy {policy_name}'
    '''

    cli_command = 'show device-tracking policy {policy_name}'

    def cli(self, policy_name, output=None):

        if output is None:
            cmd = self.cli_command.format(policy_name=policy_name)
            output = self.device.execute(cmd)

        device_tracking_policy_dict = {}
        device_index = 0
        last_key = ''

        # Device-tracking policy test configuration:
        #   trusted-port
        #   security-level guard
        #   device-role node
        #   data-glean log-only
        #   prefix-glean only
        #   gleaning from Neighbor Discovery protecting prefix-list qux
        #   gleaning from DHCP6 protecting prefix-list baz
        #   gleaning from ARP protecting prefix-list foo
        #   gleaning from DHCP4 protecting prefix-list bar
        #   gleaning from protocol unkn protecting prefix-list quux
        #   limit address-count for IPv4 per mac 5
        #   limit address-count for IPv6 per mac 1
        #   cache poisoning guard enabled all
        #   tracking disable
        # Policy test is applied on the following targets:
        # Target               Type  Policy               Feature        Target range
        # Twe1/0/42            PORT  test                 Device-tracking vlan all

        # Device-tracking policy test configuration:
        device_tracking_policy_configuration_header_capture = re.compile(r'^Device-tracking\s+policy\s+\S+\s+configuration:$')

        #   trusted-port
        device_tracking_policy_trusted_port_capture = re.compile(r'^(?P<trusted_port>(trusted-port))$')

        #   security-level guard
        device_tracking_policy_security_level_capture = re.compile(r'^security-level\s+(?P<security_level>(\S+))$')

        #   device-role node
        device_tracking_policy_device_role_capture = re.compile(r'^device-role\s+(?P<device_role>(\S+))$')

        #   data-glean log-only
        device_tracking_policy_data_glean_capture = re.compile(r'^data-glean\s+(?P<data_glean>(\S+))$')

        #   prefix-glean only
        device_tracking_policy_prefix_glean_capture = re.compile(r'^prefix-glean\s+(?P<prefix_glean>(\S+))$')


        #   gleaning from Neighbor Discovery protecting prefix-list qux
        #   gleaning from DHCP6 protecting prefix-list baz
        #   gleaning from ARP protecting prefix-list foo
        #   gleaning from DHCP4 protecting prefix-list bar
        #   gleaning from protocol unkn protecting prefix-list quux
        device_tracking_policy_gleaning_capture = re.compile(
            r'^(?P<is_gleaning>((NOT\s+)?gleaning))\s+from\s+(?P<protocol>(\S+\s+\S+|\S+))'
            r'\s+protecting\s+prefix-list\s+(?P<protecting_prefix_list>(\S+))$'
        )

        #   limit address-count for IPv4 per mac 5
        #   limit address-count for IPv6 per mac 1
        device_tracking_policy_limit_address_count_capture = re.compile(
            r'^limit\s+address-count\s+for\s+(?P<version>(IPv\d))\s+per\s+mac\s+(?P<limit_address_count>(\d+))$')

        #   cache poisoning guard enabled all
        device_tracking_policy_cache_guard_capture = re.compile(
            r'^cache\s+poisoning\s+guard\s+enabled\s+(?P<cache_guard>(\S+))$')

        #   tracking disable
        device_tracking_policy_tracking_capture = re.compile(r'^tracking\s(\(.*\)\s)?(?P<tracking>(\S+))$')

        # Target               Type  Policy               Feature        Target range
        device_tracking_policy_targets_header_capture = re.compile(r'^Target\s+Type\s+Policy\s+Feature\s+Target\s+range$')

        # Twe1/0/42            PORT  test                 Device-tracking vlan all
        device_tracking_policy_capture = re.compile(r'^(?P<target>(\S+|vlan\s+\d+))\s+(?P<policy_type>(\S+))'
                                                    r'\s+(?P<policy_name>(\S+))\s+(?P<feature>(\S+))'
                                                    r'\s+(?P<tgt_range>vlan\s+\S+)$')

        capture_list = [
            device_tracking_policy_trusted_port_capture,
            device_tracking_policy_security_level_capture,
            device_tracking_policy_device_role_capture,
            device_tracking_policy_data_glean_capture,
            device_tracking_policy_prefix_glean_capture,
            device_tracking_policy_gleaning_capture,
            device_tracking_policy_limit_address_count_capture,
            device_tracking_policy_cache_guard_capture,
            device_tracking_policy_tracking_capture,
            device_tracking_policy_capture
        ]

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Device-tracking policy test configuration:
            match = device_tracking_policy_configuration_header_capture.match(line)
            if match:
                last_key = 'configuration'
                device_tracking_policy_dict.setdefault(last_key, {})
                continue

            # Target               Type  Policy               Feature        Target range
            match = device_tracking_policy_targets_header_capture.match(line)
            if match:
                last_key = 'device'
                device_tracking_policy_dict.setdefault(last_key, {})
                continue

            if last_key:
                for capture in capture_list:
                    match = capture.match(line)
                    if match:
                        groups = match.groupdict()

                        if capture == device_tracking_policy_trusted_port_capture:
                            for key, _ in groups.items():
                                device_tracking_policy_dict[last_key][key] = 'yes'
                        elif capture == device_tracking_policy_limit_address_count_capture:
                            limit_key = 'limit_address_count'
                            limit_value = groups[limit_key]
                            version = groups['version'].lower()

                            device_dict = device_tracking_policy_dict.setdefault(last_key, {}) \
                                                                     .setdefault(limit_key, {})
                            device_dict[version] = int(limit_value)
                        elif capture == device_tracking_policy_gleaning_capture:
                            protocol = groups['protocol']
                            if protocol == 'Neighbor Discovery':
                                protocol = 'nd'
                            elif protocol == 'protocol unkn':
                                protocol = 'protocol_unkn'
                            protocol = protocol.lower()
                            del groups['protocol']

                            device_dict = device_tracking_policy_dict.setdefault(last_key, {}) \
                                                                     .setdefault(protocol, {})

                            for key, value in groups.items():
                                device_dict[key] = value
                        elif capture == device_tracking_policy_capture:
                            device_index += 1
                            device_dict = device_tracking_policy_dict.setdefault(last_key, {}) \
                                                                     .setdefault(device_index, {})

                            for key, value in groups.items():
                                device_dict[key] = value
                        else:
                            for key, value in groups.items():
                                device_tracking_policy_dict[last_key][key] = value

        return device_tracking_policy_dict


# ========================
# Schema for:
#   * 'show ipv6 nd raguard policy {policy_name}'
# ========================
class ShowIpv6RaGuardPolicySchema(MetaParser):
    '''Schema for:
        * 'show ipv6 nd raguard policy {policy_name}'
    '''

    schema = {
        "configuration": {
            "device_role": str,
            Optional("max_hop_limit"): int,
            Optional("min_hop_limit"): int,
            Optional("managed_config_flag"): str,
            Optional("other_config_flag"): str,
            Optional("max_router_preference"): str,
            Optional("match_ra_prefix"): str,
            Optional("match_ipv6_access_list"): str,
            Optional("trusted_port"): str
        },
        Optional("device"): {
            Optional(int): {
                "target": str,
                "policy_type": str,
                "policy_name": str,
                "feature": str,
                "tgt_range": str,
            },
        },
    }


# ========================
# Parser for:
#   * 'show ipv6 nd raguard policy {policy_name}'
# ========================
class ShowIpv6RaGuardPolicy(ShowIpv6RaGuardPolicySchema):
    '''Parser for:
        * 'show ipv6 nd raguard policy {policy_name}'
    '''

    cli_command = 'show ipv6 nd raguard policy {policy_name}'

    def cli(self, policy_name, output=None):

        if output is None:
            cmd = self.cli_command.format(policy_name=policy_name)
            output = self.device.execute(cmd)

        ipv6_nd_raguard_dict = {}
        device_index = 0
        last_key = ''

        # RA guard policy asdf configuration:
        #   trusted-port
        #   device-role router
        #   hop-limit minimum 1
        #   hop-limit maximum 3
        #   managed-config-flag on
        #   other-config-flag on
        #   router-preference maximum high
        #   match ra prefix-list bar
        #   match ipv6 access-list foo
        # Policy asdf is applied on the following targets:
        # Target               Type  Policy               Feature        Target range
        # Twe1/0/42            PORT  asdf                 RA guard       vlan all

        # RA guard policy asdf configuration:
        ipv6_nd_raguard_configuration_header_capture = re.compile(r'^RA\s+guard\s+policy\s+\S+\s+configuration:$')

        #   trusted-port
        ipv6_nd_ragaurd_trusted_port_capture = re.compile(r'^(?P<trusted_port>(trusted-port))$')

        #   device-role router
        ipv6_nd_ragaurd_device_role_capture = re.compile(r'^device-role\s+(?P<device_role>(\S+))$')

        #   hop-limit minimum 1
        ipv6_nd_ragaurd_min_hop_limit_capture = re.compile(r'^hop-limit\s+minimum\s+(?P<min_hop_limit>(\d+))$')

        #   hop-limit maximum 3
        ipv6_nd_ragaurd_max_hop_limit_capture = re.compile(r'^hop-limit\s+maximum\s+(?P<max_hop_limit>(\d+))$')

        #   managed-config-flag on
        ipv6_nd_ragaurd_managed_config_flag_capture = re.compile(r'^managed-config-flag\s+(?P<managed_config_flag>(\S+))$')

        #   other-config-flag on
        ipv6_nd_ragaurd_other_config_flag_capture = re.compile(r'^other-config-flag\s+(?P<other_config_flag>(\S+))$')

        #   router-preference maximum high
        ipv6_nd_ragaurd_max_router_preference_capture = re.compile(r'^router-preference\s+maximum\s+(?P<max_router_preference>(\S+))$')

        #   match ra prefix-list bar
        ipv6_nd_ragaurd_match_ra_prefix_list_capture = re.compile(r'^match\s+ra\s+prefix-list\s+(?P<match_ra_prefix>(\S+))$')

        #   match ipv6 access-list foo
        ipv6_nd_ragaurd_match_ipv6_access_list_capture = re.compile(r'^match\s+ipv6\s+access-list\s+(?P<match_ipv6_access_list>(\S+))$')

        # Target               Type  Policy               Feature        Target range
        ipv6_nd_raguard_targets_header_capture = re.compile(r'^Target\s+Type\s+Policy\s+Feature\s+Target\s+range$')

        # Twe1/0/42            PORT  asdf                 RA guard       vlan all
        ipv6_nd_raguard_target_capture = re.compile(r'^(?P<target>(\S+|vlan\s+\d+))\s+(?P<policy_type>(\S+))'
                                                    r'\s+(?P<policy_name>(\S+))\s+(?P<feature>(\S+|\S+\s\S+))'
                                                    r'\s+(?P<tgt_range>vlan\s+\S+)$')

        capture_list = [
            ipv6_nd_ragaurd_device_role_capture,
            ipv6_nd_ragaurd_trusted_port_capture,
            ipv6_nd_ragaurd_max_hop_limit_capture,
            ipv6_nd_ragaurd_min_hop_limit_capture,
            ipv6_nd_ragaurd_managed_config_flag_capture,
            ipv6_nd_ragaurd_other_config_flag_capture,
            ipv6_nd_ragaurd_max_router_preference_capture,
            ipv6_nd_ragaurd_match_ra_prefix_list_capture,
            ipv6_nd_ragaurd_match_ipv6_access_list_capture,
        ]

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Source guard policy test configuration:
            match = ipv6_nd_raguard_configuration_header_capture.match(line)
            if match:
                last_key = "configuration"
                ipv6_nd_raguard_dict.setdefault(last_key, {})
                continue

            # Target               Type  Policy               Feature        Target range
            match = ipv6_nd_raguard_targets_header_capture.match(line)
            if match:
                last_key = 'device'
                ipv6_nd_raguard_dict.setdefault(last_key, {})
                continue

            # Add all subsequent lines to the last parsed key
            if last_key == 'configuration':
                for capture in capture_list:
                    match = capture.match(line)
                    if match:
                        groups = match.groupdict()
                        for key, value in groups.items():
                            if key == 'trusted_port':
                                ipv6_nd_raguard_dict[last_key][key] = 'yes'
                                continue

                            if value.isdigit():
                                ipv6_nd_raguard_dict[last_key][key] = int(value)
                            else:
                                ipv6_nd_raguard_dict[last_key][key] = value


            if last_key == 'device':
                match = ipv6_nd_raguard_target_capture.match(line)
                if match:
                    groups = match.groupdict()
                    device_index += 1
                    device_dict = ipv6_nd_raguard_dict.setdefault('device', {}).setdefault(device_index, {})

                    for key, value in groups.items():
                        device_dict[key] = value

        return ipv6_nd_raguard_dict


# ========================
# Schema for:
#   * 'show ipv6 source-guard policy {policy_name}'
# ========================
class ShowIpv6SourceGuardPolicySchema(MetaParser):
    '''Schema for:
        * 'show ipv6 source-guard policy {policy_name}'
    '''

    schema = {
        "configuration": {
            "validate_address": str,
            Optional("validate_prefix"): str,
            Optional("permit"): str,
            Optional("trusted"): str,
            Optional("deny"): str,
        },
        Optional("device"): {
            Optional(int): {
                "target": str,
                "policy_type": str,
                "policy_name": str,
                "feature": str,
                "tgt_range": str,
            },
        },
    }


# ========================
# Parser for:
#   * 'show ipv6 source-guard policy {policy_name}'
# ========================
class ShowIpv6SourceGuardPolicy(ShowIpv6SourceGuardPolicySchema):
    '''Parser for:
        * 'show ipv6 source-guard policy {policy_name}'
    '''

    cli_command = 'show ipv6 source-guard policy {policy_name}'

    def cli(self, policy_name, output=None):

        if output is None:
            cmd = self.cli_command.format(policy_name=policy_name)
            output = self.device.execute(cmd)

        ipv6_source_guard_dict = {}
        device_index = 0
        last_key = ''

        # Source guard policy test1 configuration:
        #   trusted
        #   validate prefix
        #   validate address
        #   permit link-local
        #   deny global-autoconf
        # Policy test1 is applied on the following targets:
        # Target               Type  Policy               Feature        Target range
        # Twe1/0/42            PORT  test1                Source guard   vlan all

        # Source guard policy test1 configuration:
        ipv6_source_guard_configuration_header_capture = re.compile(r'^Source\s+guard\s+policy\s+\S+\s+configuration:$')

        #   trusted
        ipv6_source_guard_trusted_capture = re.compile(r'^(?P<trusted>(trusted))$')

        #   validate prefix
        ipv6_source_guard_prefix_capture = re.compile(r'^(?P<validate_prefix>(validate\s+prefix))$')

        #   validate address
        ipv6_source_guard_address_capture = re.compile(r'^(?P<validate_address>((NOT\s)?validate\s+address))$')

        #   permit link-local
        ipv6_source_guard_permit_capture = re.compile(r'^permit\s+(?P<permit>(\S+))$')

        #   deny global-autoconf
        ipv6_source_guard_deny_capture = re.compile(r'^deny\s+(?P<deny>(\S+))$')

       # Target               Type  Policy               Feature        Target range
        ipv6_source_guard_targets_header_capture = re.compile(r'^Target\s+Type\s+Policy\s+Feature\s+Target\s+range$')

        # Twe1/0/42            PORT  test1                Source guard   vlan all
        ipv6_source_guard_target_capture = re.compile(r'^(?P<target>(\S+|vlan\s+\d+))\s+(?P<policy_type>(\S+))'
                                                      r'\s+(?P<policy_name>(\S+))\s+(?P<feature>(\S+|\S+\s\S+))'
                                                      r'\s+(?P<tgt_range>vlan\s+\S+)$')

        capture_list = [
            ipv6_source_guard_trusted_capture,
            ipv6_source_guard_prefix_capture,
            ipv6_source_guard_address_capture,
            ipv6_source_guard_permit_capture,
            ipv6_source_guard_deny_capture,
        ]

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Source guard policy test1 configuration:
            match = ipv6_source_guard_configuration_header_capture.match(line)
            if match:
                last_key = 'configuration'
                ipv6_source_guard_dict.setdefault(last_key, {})
                continue

            # Policy test1 is applied on the following targets:
            match = ipv6_source_guard_targets_header_capture.match(line)
            if match:
                last_key = 'device'
                ipv6_source_guard_dict.setdefault(last_key, {})
                continue

            # Add all subsequent lines to the last parsed key
            if last_key == "configuration":
                for capture in capture_list:
                    match = capture.match(line)
                    if match:
                        groups = match.groupdict()

                        for key, value in groups.items():
                            if capture == ipv6_source_guard_trusted_capture or \
                                capture == ipv6_source_guard_prefix_capture:
                                ipv6_source_guard_dict[last_key][key] = 'yes'
                            elif capture == ipv6_source_guard_address_capture:
                                description = 'yes'
                                if "NOT" in value:
                                    description = 'no'
                                ipv6_source_guard_dict[last_key][key] = description
                            else:
                                ipv6_source_guard_dict[last_key][key] = value

            if last_key == 'device':
                match = ipv6_source_guard_target_capture.match(line)
                if match:
                    groups = match.groupdict()
                    device_index += 1
                    device_dict = ipv6_source_guard_dict.setdefault(last_key, {}).setdefault(device_index, {})

                    for key, value in groups.items():
                        device_dict[key] = value

        return ipv6_source_guard_dict


# ========================
# Schema for:
#   * 'show device-tracking counters vlan {vlanid}'
# ========================
class ShowDeviceTrackingCountersVlanSchema(MetaParser):
    '''Schema for:
        * 'show device-tracking counters vlan {vlanid}'
    '''

    schema = {
        "vlanid": {
            int: {
                Any(): {
                    Optional("protocol"): str,
                    Optional("acd&dad"): int,
                    Optional("type"): str,
                    Optional(Or("ndp","dhcpv6","arp","dhcpv4","probe_send","probe_reply")): {
                        Optional(Any()): int,
                    },
                    Any(): {
                        Optional("protocol"): str,
                        Optional("message"): str,
                        Optional("dropped"): int,
                        },
                },
                Optional("faults"): list,
            },
        },
    }


# ========================
# Parser for:
#   * 'show device-tracking counters vlan {vlanid}'
# ========================
class ShowDeviceTrackingCountersVlan(ShowDeviceTrackingCountersVlanSchema):
    '''Parser for:
        * 'show device-tracking counters vlan {vlanid}'
    '''

    cli_command = 'show device-tracking counters vlan {vlanid}'

    def cli(self, vlanid, output=None):

        if output is None:
            cmd = self.cli_command.format(vlanid=vlanid)
            output = self.device.execute(cmd)

        device_tracking_counters_vlanid_dict = {}
        last_key = ''

        # Received messages on vlan 39   :
        # Protocol        Protocol message
        # NDP             RS[15543] NS[5181] NA[10]
        # DHCPv6
        # ARP
        # DHCPv4
        # ACD&DAD         --[5181]

        # Received Broadcast/Multicast messages on vlan 39   :
        # Protocol        Protocol message
        # NDP             RS[15543] NS[5181] NA[10]
        # DHCPv6
        # ARP
        # DHCPv4

        # Bridged messages from vlan 39   :
        # Protocol        Protocol message
        # NDP             RS[15543] NS[8299]
        # DHCPv6
        # ARP
        # DHCPv4
        # ACD&DAD         --[5171]

        # Broadcast/Multicast converted to unicast messages from vlan 39   :
        # Protocol        Protocol message
        # NDP
        # DHCPv6
        # ARP
        # DHCPv4
        # ACD&DAD

        # Probe message on vlan 39   :
        # Type            Protocol message
        # PROBE_SEND      NS[3128]
        # PROBE_REPLY     NA[10]

        # Limited Broadcast to Local message on vlan 39   :
        # Type            Protocol message
        # NDP
        # DHCPv6
        # ARP
        # DHCPv4

        # Dropped messages on vlan 39   :
        # Feature             Protocol Msg [Total dropped]
        # Device-tracking:    NDP      NS  [10]
        #                     reason:  Silent drop [10]

        #                             NA  [10]
        #                     reason:  Silent drop [10]

        # ACD&DAD:            --       --  [10]


        # Faults on vlan 39   :
        #   DHCPv6_REQUEST_NAK[1]

        # Received messages on vlan 39   :
        received_messages_capture = re.compile(r'^Received\s+messages\s+on\s+vlan\s+\d+\s+:$')

        # Received Broadcast/Multicast messages on vlan 39   :
        received_broadcast_multicast_messages_capture = re.compile(r'^Received\s+Broadcast/Multicast\s+messages\s+on\s+vlan\s+\d+\s+:$')

        # Bridged messages from vlan 39   :
        bridged_messages_capture = re.compile(r'^Bridged\s+messages\s+from\s+vlan\s+\d+\s+:$')

        # Broadcast/Multicast converted to unicast messages from vlan 39   :
        broadcast_multicast_to_unicast_messages_capture = re.compile(r'^Broadcast/Multicast\s+converted\s+to\s+unicast\s+messages\s+from\s+vlan\s+\d+\s+:$')

       # Probe message on vlan 39   :
        probe_message_capture = re.compile(r'^Probe\s+message\s+on\s+vlan\s+\d+\s+:$')

        # Limited Broadcast to Local message on vlan 39   :
        limited_broadcast_to_local_messages_capture = re.compile(r'^Limited\s+Broadcast\s+to\s+Local\s+message\s+on\s+vlan\s+\d+\s+:$')

        # Dropped messages on vlan 39   :
        dropped_messages_capture = re.compile(r'^Dropped\s+messages\s+on\s+vlan\s+\d+\s+:$')

        # Faults on vlan 39   :
        faults_capture = re.compile(r'^Faults\s+on\s+vlan\s+\d+\s+:$')

        # Protocol        Protocol message
        # NDP             RS[15543] NS[5181] NA[10]
        # DHCPv6
        # ARP
        # DHCPv4
        # ACD&DAD         --[5181]
        protocol_info = re.compile(r'^(?P<protocol>(Protocol))\s+(?P<message>(.*))$')
        ndp_info = re.compile(r'^(?P<protocol>(NDP))\s+(?P<message>(.*))?')
        dpch6_info = re.compile(r'^(?P<protocol>(DHCPv6))\s+(?P<message>(.*))?$')
        arp_info = re.compile(r'^(?P<protocol>(ARP))\s+(?P<message>(.*))?$')
        dhcp4_info = re.compile(r'^(?P<protocol>(DHCPv4))\s+(?P<message>(.*))?$')
        acd_dad_info = re.compile(r'^(?P<protocol>(ACD&DAD))\s+\S+\[(?P<message>(\d+))\]?$')

        # PROBE_SEND      NS[3128]
        # PROBE_REPLY     NA[10]
        probe_info = re.compile(r'^(?P<protocol>(PROBE_\S+))\s+(?P<message>(.*))?')

        # Device-tracking:    NDP      NS  [10]
        dropped_message_info = re.compile(r'^(?P<feature>((?!reason)\S+)):\s+(?P<protocol>(\S+))'
                                          r'\s+(?P<message>(\S+))\s+\[(?P<dropped>(\d+))\]$')

        #   DHCPv6_REQUEST_NAK[1]
        fault_info = re.compile(r'^(?P<fault>(FAULT_CODE_INVALID|DHCPv\d_\S+_(TIMEOUT|NAK|ERROR)))$')

        capture_list = [
            ndp_info,
            dpch6_info,
            arp_info,
            dhcp4_info,
            acd_dad_info,
            probe_info,
            dropped_message_info,
        ]

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            if not device_tracking_counters_vlanid_dict:
                message_dict = device_tracking_counters_vlanid_dict.setdefault('vlanid', {}) \
                                                                   .setdefault(int(vlanid), {})
            # Received messages on vlan 39   :
            match = received_messages_capture.match(line)
            if match:
                last_key = "received"
                message_dict.setdefault(last_key, {})
                continue

            # Received Broadcast/Multicast messages on vlan 39   :
            match = received_broadcast_multicast_messages_capture.match(line)
            if match:
                last_key = "received_broadcast_multicast"
                message_dict.setdefault(last_key, {})
                continue

            # Bridged messages from vlan 39   :
            match = bridged_messages_capture.match(line)
            if match:
                last_key = "bridged"
                message_dict.setdefault(last_key, {})
                continue

            # Broadcast/Multicast converted to unicast messages from vlan 39   :
            match = broadcast_multicast_to_unicast_messages_capture.match(line)
            if match:
                last_key = "broadcast_multicast_to_unicast"
                message_dict.setdefault(last_key, {})
                continue

            # Probe message on vlan 39   :
            match = probe_message_capture.match(line)
            if match:
                last_key = "probe"
                message_dict.setdefault(last_key, {})
                continue

            # Limited Broadcast to Local message on vlan 39   :
            match = limited_broadcast_to_local_messages_capture.match(line)
            if match:
                last_key = "limited_broadcast_to_local"
                message_dict.setdefault(last_key, {})
                continue

            # Dropped messages on vlan 39   :
            match = dropped_messages_capture.match(line)
            if match:
                last_key = "dropped"
                message_dict.setdefault(last_key, {})
                continue

            # Faults on vlan 39   :
            match = faults_capture.match(line)
            if match:
                last_key = "faults"
                message_dict.setdefault(last_key, [])
                continue

            # Add all subsequent lines to the last parsed key
            if last_key:
                for capture in capture_list:
                    match = capture.match(line)
                    if match:
                        groups = match.groupdict()
                        if capture == dropped_message_info:
                            feature = groups['feature']
                            message_dict.setdefault(last_key, {}).setdefault(feature, {})
                            del groups['feature']

                            for key, value in groups.items():
                                if value.isdigit():
                                    message_dict[last_key][feature][key] = int(value)
                                else:
                                    message_dict[last_key][feature][key] = value.lower()
                        elif capture == fault_info:
                            message = groups['fault']
                            message_dict[last_key].append(message)
                        elif capture == acd_dad_info:
                            protocol = groups['protocol'].lower()
                            message = groups['message']
                            message_dict[last_key][protocol] = int(message)
                        else:
                            protocol = groups['protocol'].lower()
                            messages = groups['message'].split()
                            message_dict.setdefault(last_key, {}).setdefault(protocol, {})
                            packet_capture = re.compile(r'^(?P<packet>(\S+))\[(?P<num>(\d+))\]$')
                            for message in messages:
                                packet_match = packet_capture.match(message)
                                if packet_match:
                                    packet_groups = packet_match.groupdict()
                                    packet = packet_groups['packet']
                                    num = packet_groups['num']
                                    message_dict[last_key][protocol][packet] = int(num)

        return device_tracking_counters_vlanid_dict
