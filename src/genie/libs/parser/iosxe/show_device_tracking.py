import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or

from genie.libs.parser.utils.common import Common

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
                "state": str,
                Optional("time_left"): str,
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
        # S   10.22.12.10                            7081.05ff.eb41     E0/0       228   0100  10330mn REACHABLE  N/A
        # ND  10.22.8.10                             7081.05ff.eb42     E0/1       226   0005  235mn   STALE      try 0 73072 s
        # ND  10.22.4.10                             7081.05ff.eb43     E0/2       224   0005  60s     REACHABLE  250 s
        # ND  10.22.0.10                             7081.05ff.eb40     E0/3       222   0005  3mn     REACHABLE  83 s try 0
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
        # DH4 10.160.43.197                           94d4.69ff.e606  Te8/0/37       1023  0025  116s  REACHABLE  191 s try 0(557967 s)
        device_info_capture_database = re.compile(
            r"^(?P<dev_code>\S+)\s+"
            r"(?P<network_layer_address>\S+)\s+(?P<link_layer_address>\S+)\s+"
            r"(?P<interface>\S+)\s+(?P<vlan_id>\d+)\s+"
            r"(?P<pref_level_code>\d+)\s+(?P<age>\S+)\s+(?P<state>\S+)\s+(?P<time_left>(try\s\d\s\d+\ss)|(N/A)|(\d+.*)|(\d+\ss\stry\d))$")

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
            # DH4 10.160.43.197                           94d4.69ff.e606  Te8/0/37       1023  0025  116s  REACHABLE  191 s try 0(557967 s)
            elif device_info_capture_database.match(line):
                device_index += 1
                device_info_capture_database_match = device_info_capture_database.match(line)
                groups = device_info_capture_database_match.groupdict()
                dev_code = groups['dev_code']
                network_layer_address = groups['network_layer_address']
                link_layer_address = groups['link_layer_address']
                interface = groups['interface']
                vlan_id = int(groups['vlan_id'])
                pref_level_code = int(groups['pref_level_code'])
                age = groups['age']
                state = groups['state']
                time_left = groups['time_left']
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
                device_tracking_database_dict['device'][device_index]['time_left'] = time_left
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
        "binding_table": {
            "dynamic": int,
            "entries": int,
            Optional("limit"): int
        },
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
        # portDB has 2 entries for interface Gi0/1/1, 2 dynamic
        p1 = re.compile(
            r"^(.+) +has +(?P<entries>\d+) +entries"
            r"( +for +interface +\S+)?"
            r", +(?P<dynamic>\d+) +dynamic( +\(limit +(?P<limit>\d+)\))?$"
        )

        # DH4 10.160.43.197                           94d4.69ff.e606  Te8/0/37       1023  0025  116s  REACHABLE  191 s try 0(557967 s)
        # L   10.160.48.1                             0000.0cff.94fe  Vl1024         1024  0100 42473mn REACHABLE
        # ND  FE80::E6C7:22FF:FEFF:8239               e4c7.22ff.8239  Gi1/0/24       1023  0005   34s  REACHABLE  268 s
        p2 = re.compile(
            r"^(?P<code>\S+)\s+(?P<network_layer_address>"
            r"\d+\.\d+\.\d+\.\d+|\S+\:\:\S+\:\S+\:\S+\:\S+)"
            r"\s+(?P<link_layer_address>\S+\.\S+\.\S+)"
            r"\s+(?P<interface>\S+)\s+(?P<vlan>\d+)"
            r"\s+(?P<prlvl>\d+)\s+(?P<age>\d+\S+)"
            r"\s+(?P<state>\S+)(\s+(?P<time_left>\d+.*))?$"
        )

        device_info_obj = {}

        for line in out.splitlines():
            line = line.strip()

            # Binding Table has 87 entries, 75 dynamic (limit 100000)
            # portDB has 2 entries for interface Gi0/1/1, 2 dynamic
            m = p1.match(line)
            if m:
                group = m.groupdict()

                # convert str to int
                binding_table_dict = {
                    k: int(v) for k, v in group.items() if v is not None
                }

                device_info_obj["binding_table"] = binding_table_dict
                continue

            # DH4 10.160.43.197                           94d4.69ff.e606  Te8/0/37       1023  0025  116s  REACHABLE  191 s try 0(557967 s)
            m = p2.match(line)
            if m:
                group = m.groupdict()

                network_layer_address = group["network_layer_address"]
                # pull a key from dict to use as new_key
                network_layer_addresses_dict = device_info_obj.setdefault(
                    "network_layer_address", {})

                network_layer_address_dict = network_layer_addresses_dict.\
                    setdefault(network_layer_address, {})

                network_layer_address_dict.update({
                    "age": group["age"],
                    "code": group["code"],
                    "interface": group["interface"],
                    "link_layer_address": group["link_layer_address"],
                    "prlvl": group["prlvl"],
                    "state": group["state"],
                    "vlan": int(group["vlan"]),
                })

                if group["time_left"]:
                    network_layer_address_dict["time_left"] = \
                        group["time_left"]

                continue

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
            "total": int,
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

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        device_tracking_database_details_dict = {}
        device_index = 0
        binding_key = ''

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
        binding_table_info = re.compile(r'^(?P<parameter>(\S+))\s+:\s+(?P<info>(.*))$')

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
                                         r'\s+(?P<client_id>(\S+))(\s+(?P<policy>(.*)))?$')

        optional_parameters = [
            'time_left',
            'policy',
        ]

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            match = binding_table_configuration_capture.match(line)
            if match:
                binding_key = "binding_table_configuration"
                device_tracking_database_details_dict.setdefault(binding_key, {})
                continue

            match = binding_table_counter_capture.match(line)
            if match:
                binding_key = "binding_table_count"
                device_tracking_database_details_dict.setdefault(binding_key, {})
                continue

            match = binding_table_state_capture.match(line)
            if match:
                binding_key = "binding_table_state_count"
                device_tracking_database_details_dict.setdefault(binding_key, {})
                continue

            match = device_header_capture.match(line)
            if match:
                device_tracking_database_details_dict.setdefault('device', {})
                continue

            match = binding_table_info.match(line)
            if match:
                groups = match.groupdict()
                key = groups['parameter'].lower()
                value = groups['info']
                binding_table_dict = device_tracking_database_details_dict.setdefault(binding_key, {})
                if value.isdigit():
                    binding_table_dict[key] = int(value)
                else:
                    binding_table_dict[key] = value
                continue

            match = device_info_capture.match(line)
            if match:
                device_index += 1
                groups = match.groupdict()
                for parameter in optional_parameters:
                    if groups[parameter] is None:
                        groups[parameter] = ''

                if not device_tracking_database_details_dict.get('device', {}):
                    device_tracking_database_details_dict.setdefault('device', {})

                device_dict = device_tracking_database_details_dict.setdefault('device', {}) \
                                                                .setdefault(device_index, {})

                for key, value in groups.items():
                    if value.isdigit():
                        device_dict[key] = int(value)
                    else:
                        device_dict[key] = value

        return device_tracking_database_details_dict


# =========================================
# Schema for:
#  * 'show device-tracking policies'
# ==========================================


class ShowDeviceTrackingPoliciesSchema(MetaParser):

    """Schema for show device-tracking policies"""

    schema = {
        "policies": {
            int: {
                "target": str,
                "policy_type": str,
                "policy_name": str,
                "feature": str,
                "tgt_range": str,
            }
        }
    }

# ======================================
# Parser for:
#  * 'show device-tracking policies'
# ======================================


class ShowDeviceTrackingPolicies(ShowDeviceTrackingPoliciesSchema):
    """ Parser for show device-tracking policies """

    cli_command = ['show device-tracking policies',
                   'show device-tracking policies interface {interface}',
                   'show device-tracking policies vlan {vlan}',
    ]

    def cli(self, interface='', vlan='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            elif vlan:
                cmd = self.cli_command[2].format(vlan=vlan)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        device_tracking_policies_dict = {}
        policy_index = 0

        policy_info_header_capture = re.compile(r'^Target\s+Type\s+Policy\s+Feature\s+Target\s+range$')
        policy_info_capture = re.compile(
            r"^(?P<target>(\S+)|(vlan\s+\S+))\s+(?P<policy_type>[a-zA-Z]+)\s+"
            r"(?P<policy_name>\S+)\s+(?P<feature>(\S+\s?)+)\s+(?P<tgt_range>vlan\s+\S+)$")

        lines = out.splitlines()

        if len(lines) == 0:
            return device_tracking_policies_dict

        #Target     Type   Policy     Feature        Target range
        policy_info_header_capture_match = policy_info_header_capture.match(lines[0].strip())
        if policy_info_header_capture_match:
            group = policy_info_header_capture_match.groupdict()
        else:
            return device_tracking_policies_dict

        for line in lines[1:]:
            line = line.strip()

            # vlan 39    VLAN   test1    Device-tracking  vlan all
            policy_info_capture_match = policy_info_capture.match(line)
            if policy_info_capture_match:
                policy_index += 1
                group = policy_info_capture_match.groupdict()

                target = group['target']
                policy_type = group['policy_type']
                policy_name = group['policy_name']
                feature = group['feature'].strip()
                tgt_range = group['tgt_range']

                if not device_tracking_policies_dict.get('policies', {}):
                    device_tracking_policies_dict['policies'] = {}
                device_tracking_policies_dict['policies'][policy_index] = {}
                device_tracking_policies_dict['policies'][policy_index]['target'] = target
                device_tracking_policies_dict['policies'][policy_index]['policy_type'] = policy_type
                device_tracking_policies_dict['policies'][policy_index]['policy_name'] = policy_name
                device_tracking_policies_dict['policies'][policy_index]['feature'] = feature
                device_tracking_policies_dict['policies'][policy_index]['tgt_range'] = tgt_range

        return device_tracking_policies_dict


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
            Optional("destination_glean"): str,
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
            Optional("origin"): str,
            Optional("tracking"): str,
        },
        "device": {
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
            out = self.device.execute(cmd)
        else:
            out = output

        device_tracking_policy_dict = {}
        device_index = 0

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

        #   destination-glean log-only
        device_tracking_policy_destination_glean_capture = re.compile(r'^destination-glean\s+(?P<destination_glean>(\S+))$')

        #   prefix-glean only
        device_tracking_policy_prefix_glean_capture = re.compile(r'^prefix-glean\s+(?P<prefix_glean>(\S+))$')


        #   gleaning from Neighbor Discovery protecting prefix-list qux
        #   gleaning from DHCP6 protecting prefix-list baz
        #   gleaning from ARP protecting prefix-list foo
        #   gleaning from DHCP4 protecting prefix-list bar
        #   gleaning from protocol unkn protecting prefix-list quux
        device_tracking_policy_gleaning_capture = re.compile(
            r'^(?P<is_gleaning>((NOT\s+)?gleaning))\s+from\s+(?P<protocol>(\S+\s+\S+|\S+))'
            r'(\s+protecting\s+prefix-list\s+(?P<protecting_prefix_list>(\S+)))?$'
        )

        #   limit address-count for IPv4 per mac 5
        #   limit address-count for IPv6 per mac 1
        device_tracking_policy_limit_address_count_capture = re.compile(
            r'^limit\s+address-count\s+for\s+(?P<version>(IPv\d))\s+per\s+mac\s+(?P<limit_address_count>(\d+))$')

        #   cache poisoning guard enabled all
        device_tracking_policy_cache_guard_capture = re.compile(
            r'^cache\s+poisoning\s+guard\s+enabled\s+(?P<cache_guard>(\S+))$')

        #   origin fabric
        device_tracking_policy_origin_capture = re.compile(r'^origin\s+(?P<origin>(\S+))$')

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
            device_tracking_policy_destination_glean_capture,
            device_tracking_policy_prefix_glean_capture,
            device_tracking_policy_gleaning_capture,
            device_tracking_policy_limit_address_count_capture,
            device_tracking_policy_cache_guard_capture,
            device_tracking_policy_origin_capture,
            device_tracking_policy_tracking_capture,
            device_tracking_policy_capture,
        ]

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            match = device_tracking_policy_configuration_header_capture.match(line)
            if match:
                configuration_dict = device_tracking_policy_dict.setdefault('configuration', {})
                continue

            match = device_tracking_policy_targets_header_capture.match(line)
            if match:
                device_dict = device_tracking_policy_dict.setdefault('device', {})
                continue

            for capture in capture_list:
                match = capture.match(line)
                if match:
                    groups = match.groupdict()

                    if capture == device_tracking_policy_trusted_port_capture:
                        for key, _ in groups.items():
                            configuration_dict[key] = 'yes'
                    elif capture == device_tracking_policy_limit_address_count_capture:
                        limit_key = 'limit_address_count'
                        limit_value = groups[limit_key]
                        version = groups['version'].lower()

                        limit_dict = configuration_dict.setdefault(limit_key, {})
                        limit_dict[version] = int(limit_value)
                    elif capture == device_tracking_policy_gleaning_capture:
                        protocol = groups['protocol']
                        if protocol == 'Neighbor Discovery':
                            protocol = 'nd'
                        elif protocol == 'protocol unkn':
                            protocol = 'protocol_unkn'
                        protocol = protocol.lower()
                        del groups['protocol']

                        if groups['protecting_prefix_list'] is None:
                            del groups['protecting_prefix_list']

                        gleaning_dict = configuration_dict.setdefault(protocol, {})

                        for key, value in groups.items():
                            gleaning_dict[key] = value
                    elif capture == device_tracking_policy_capture:
                        device_index += 1
                        policy_dict = device_dict.setdefault(device_index, {})

                        for key, value in groups.items():
                            policy_dict[key] = value
                    else:
                        for key, value in groups.items():
                            configuration_dict[key] = value

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
        "device": {
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
            out = self.device.execute(cmd)
        else:
            out = output

        ipv6_nd_raguard_dict = {}
        device_index = 0

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
            ipv6_nd_raguard_target_capture,
        ]

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            match = ipv6_nd_raguard_configuration_header_capture.match(line)
            if match:
                configuration_dict = ipv6_nd_raguard_dict.setdefault('configuration', {})
                continue

            match = ipv6_nd_raguard_targets_header_capture.match(line)
            if match:
                ipv6_nd_raguard_dict.setdefault('device', {})
                continue

            for capture in capture_list:
                match = capture.match(line)
                if match:
                    if capture == ipv6_nd_raguard_target_capture:
                        groups = match.groupdict()
                        device_index += 1
                        device_dict = ipv6_nd_raguard_dict.setdefault('device', {}) \
                                                          .setdefault(device_index, {})

                        for key, value in groups.items():
                            device_dict[key] = value
                    else:
                        groups = match.groupdict()
                        for key, value in groups.items():
                            if key == 'trusted_port':
                                configuration_dict[key] = 'yes'
                                continue

                            if value.isdigit():
                                configuration_dict[key] = int(value)
                            else:
                                configuration_dict[key] = value

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
        "device": {
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
            out = self.device.execute(cmd)
        else:
            out = output

        ipv6_source_guard_dict = {}
        device_index = 0

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
            ipv6_source_guard_target_capture
        ]

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            match = ipv6_source_guard_configuration_header_capture.match(line)
            if match:
                configuration_dict = ipv6_source_guard_dict.setdefault('configuration', {})
                continue

            match = ipv6_source_guard_targets_header_capture.match(line)
            if match:
                ipv6_source_guard_dict.setdefault('device', {})
                continue

            for capture in capture_list:
                match = capture.match(line)
                if match:
                    if capture == ipv6_source_guard_target_capture:
                        groups = match.groupdict()
                        device_index += 1

                        device_dict = ipv6_source_guard_dict.setdefault('device', {}) \
                                                            .setdefault(device_index, {})

                        for key, value in groups.items():
                            device_dict[key] = value
                    else:
                        groups = match.groupdict()

                        for key, value in groups.items():
                            if capture == ipv6_source_guard_trusted_capture or \
                                capture == ipv6_source_guard_prefix_capture:
                                configuration_dict[key] = 'yes'
                            elif capture == ipv6_source_guard_address_capture:
                                description = 'yes'
                                if "NOT" in value:
                                    description = 'no'
                                configuration_dict[key] = description
                            else:
                                configuration_dict[key] = value

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
                    Optional("acd&dad"): int,
                    Optional(Or("ndp","dhcpv6","arp","dhcpv4","probe_send","probe_reply")): {
                        Any(): int,
                    },
                    Any(): {
                        "protocol": str,
                        "message": str,
                        "dropped": int,
                    },
                },
                "faults": list,
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
            out = self.device.execute(cmd)
        else:
            out = output

        device_tracking_counters_vlanid_dict = {}
        message_key = ''

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
        dhcp6_info = re.compile(r'^(?P<protocol>(DHCPv6))\s+(?P<message>(.*))?$')
        arp_info = re.compile(r'^(?P<protocol>(ARP))\s+(?P<message>(.*))?$')
        dhcp4_info = re.compile(r'^(?P<protocol>(DHCPv4))\s+(?P<message>(.*))?$')
        acd_dad_info = re.compile(r'^(?P<protocol>(ACD&DAD))\s+\S+\[(?P<message>(\d+))\]?$')

        # PROBE_SEND      NS[3128]
        # PROBE_REPLY     NA[10]
        probe_info = re.compile(r'^(?P<protocol>(PROBE_\S+))\s+(?P<message>(.*))?')

        # Device-tracking:    NDP      NS  [10]
        # Flooding Suppress:  NDP      NS  [36]
        dropped_message_info = re.compile(r'^(?P<feature>((?!reason).*)):\s+(?P<protocol>(\S+))'
                                          r'\s+(?P<message>(\S+))\s+\[(?P<dropped>(\d+))\]$')

        #   DHCPv6_REQUEST_NAK[1]
        fault_info = re.compile(r'^(?P<fault>(FAULT_CODE_INVALID|DHCPv\d_\S+_(TIMEOUT|NAK|ERROR))).*$')

        capture_list = [
            ndp_info,
            dhcp6_info,
            arp_info,
            dhcp4_info,
            acd_dad_info,
            probe_info,
            dropped_message_info,
            fault_info,
        ]

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            if not device_tracking_counters_vlanid_dict:
                message_dict = device_tracking_counters_vlanid_dict.setdefault('vlanid', {}) \
                                                                   .setdefault(int(vlanid), {})

            match = received_messages_capture.match(line)
            if match:
                message_key = "received"
                message_dict.setdefault(message_key, {})
                continue

            match = received_broadcast_multicast_messages_capture.match(line)
            if match:
                message_key = "received_broadcast_multicast"
                message_dict.setdefault(message_key, {})
                continue

            match = bridged_messages_capture.match(line)
            if match:
                message_key = "bridged"
                message_dict.setdefault(message_key, {})
                continue

            match = broadcast_multicast_to_unicast_messages_capture.match(line)
            if match:
                message_key = "broadcast_multicast_to_unicast"
                message_dict.setdefault(message_key, {})
                continue

            match = probe_message_capture.match(line)
            if match:
                message_key = "probe"
                message_dict.setdefault(message_key, {})
                continue

            match = limited_broadcast_to_local_messages_capture.match(line)
            if match:
                message_key = "limited_broadcast_to_local"
                message_dict.setdefault(message_key, {})
                continue

            match = dropped_messages_capture.match(line)
            if match:
                dropped_dict = message_dict.setdefault('dropped', {})
                continue

            match = faults_capture.match(line)
            if match:
                faults_list = message_dict.setdefault('faults', [])
                continue

            for capture in capture_list:
                match = capture.match(line)
                if match:
                    groups = match.groupdict()
                    if capture == dropped_message_info:
                        feature = groups['feature']
                        dropped_dict.setdefault(feature, {})
                        del groups['feature']

                        for key, value in groups.items():
                            if value.isdigit():
                                dropped_dict[feature][key] = int(value)
                            else:
                                dropped_dict[feature][key] = value.lower()
                    elif capture == fault_info:
                        message = groups['fault']
                        faults_list.append(message)
                    elif capture == acd_dad_info:
                        protocol = groups['protocol'].lower()
                        message = groups['message']
                        packet_dict = message_dict.setdefault(message_key, {})
                        packet_dict[protocol] = int(message)
                    else:
                        protocol = groups['protocol'].lower()
                        messages = groups['message'].split()
                        packet_dict = message_dict.setdefault(message_key, {}).setdefault(protocol, {})
                        packet_capture = re.compile(r'^(?P<packet>(\S+))\[(?P<num>(\d+))\]$')
                        for message in messages:
                            packet_match = packet_capture.match(message)
                            if packet_match:
                                packet_groups = packet_match.groupdict()
                                packet = packet_groups['packet']
                                num = packet_groups['num']
                                packet_dict[packet] = int(num)

        return device_tracking_counters_vlanid_dict

# ==================================
# Schema for:
#  * 'show device-tracking database mac'
# ==================================
class ShowDeviceTrackingDatabaseMacSchema(MetaParser):
    """Schema for show device-tracking database mac."""

    schema = {
        "device": {
            int: {
                "link_layer_address": str,
                "interface": str,
                "vlan_id": int,
                "pref_level_code": str,
                "state": str,
                "policy": str,
                Optional("time_left"): str,
                Optional("input_index"): int,
            }
        }
    }

# ==================================
# Parser for:
#  * 'show device-tracking database mac'
# ==================================
class ShowDeviceTrackingDatabaseMac(ShowDeviceTrackingDatabaseMacSchema):
    """Parser for show device-tracking database mac."""

    cli_command = 'show device-tracking database mac'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)

        else:
            out = output
        device_tracking_database_mac_dict = {}

        # MAC                    Interface  vlan       prlvl      state            Time left        Policy           Input_index
        # dead.beef.0001         Twe1/0/42  39         NO TRUST   MAC-STALE        N/A              49      
        # 5c5a.c791.d69f         Vl39       39         TRUSTED    MAC-REACHABLE    N/A              dna_policy       108     
        # 0050.56b0.babc         Twe1/0/42  39         NO TRUST   MAC-REACHABLE    41 s             test1            49      
        # 0050.56b0.afed         Twe1/0/42  39         NO TRUST   MAC-REACHABLE    21 s             test1            49      
        # 000a.000b.000c         Twe1/0/1   100        NO TRUST   MAC-DOWN         N/A              8       

        # dead.beef.0001         Twe1/0/42  39         NO TRUST   MAC-STALE        N/A              49
        entry_capture = re.compile(
            r"^(?P<link_layer_address>\S+)"
            r"\s+(?P<interface>\S+)"
            r"\s+(?P<vlan_id>\d+)"
            r"\s+(?P<pre_level>(\S+\s\S+)|(\S+))"
            r"\s+(?P<state>\S+)"
            r"\s+((N/A)|(?P<time_left>(\d+\ss)))"
            r"\s+(?P<policy>\S+)"
            r"(\s+(?P<input_index>\d+))?"
        )

        device_index = 0
        for line in out.splitlines():
            line = line.strip()
            entry_capture_match = entry_capture.match(line)
            if entry_capture_match:
                device_index += 1
                groups = entry_capture_match.groupdict()
                lla = groups['link_layer_address']
                interface = groups['interface']
                vlan_id = int(groups['vlan_id'])
                pre_level = groups['pre_level']
                state = groups['state']
                policy = groups['policy']

                index_dict = device_tracking_database_mac_dict.setdefault('device', {}).setdefault(device_index, {})

                index_dict['link_layer_address'] = lla
                index_dict['interface'] = interface
                index_dict['vlan_id'] = vlan_id
                index_dict['pref_level_code'] = pre_level
                index_dict['state'] = state
                index_dict['policy'] = policy

                if groups['time_left']:
                    time_left = groups['time_left']
                    index_dict['time_left'] = time_left
                if groups['input_index']:
                    input_index = int(groups['input_index'])
                    index_dict['input_index'] = input_index

                continue
        return device_tracking_database_mac_dict


# ==================================
# Schema for:
#  * 'show device-tracking database mac {mac}'
# ==================================
class ShowDeviceTrackingDatabaseMacMacSchema(MetaParser):
    """Schema for show device-tracking database mac {mac}."""

    schema = {
        "macDB_count": int,
        "vlan": int,
        "dynamic_count": int,
        "entries": {
            int: {
                "dev_code": str,
                "network_layer_address": str,
                "link_layer_address": str,
                "interface": str,
                "vlan_id": int,
                "pref_level_code": int,
                "age": str,
                "state": str,
                Optional("time_left"): str,
            }
        }
    }

# ==================================
# Parser for:
#  * 'show device-tracking database mac {mac}'
# ==================================
class ShowDeviceTrackingDatabaseMacMac(ShowDeviceTrackingDatabaseMacMacSchema):
    """Parser for show device-tracking database mac {mac}."""

    cli_command = 'show device-tracking database mac {mac}'

    def cli(self, mac, output=None):
        if output is None:
            cmd = self.cli_command.format(mac=mac)
            out = self.device.execute(cmd)

        else:
            out = output

        device_tracking_database_mac_dict = {}
        # Codes: L - Local, S - Static, ND - Neighbor Discovery, ARP - Address Resolution Protocol, DH4 - IPv4 DHCP, DH6 - IPv6 DHCP, PKT - Other Packet, API - API created
        # Preflevel flags (prlvl):
        # 0001:MAC and LLA match     0002:Orig trunk            0004:Orig access           
        # 0008:Orig trusted trunk    0010:Orig trusted access   0020:DHCP assigned         
        # 0040:Cga authenticated     0080:Cert authenticated    0100:Statically assigned   


        #     Network Layer Address                    Link Layer Address     Interface  vlan       prlvl      age        state      Time left       
        # macDB has 2 entries for mac dead.beef.0001,vlan 38, 0 dynamic 
        # S   10.10.10.11                              dead.beef.0001         Twe1/0/41  38         0100       4s         REACHABLE  308 s           
        # S   10.10.10.10                              dead.beef.0001         Twe1/0/41  38         0100       77s        REACHABLE  226 s   

        # macDB has 2 entries for mac dead.beef.0001,vlan 38, 0 dynamic
        table_info_capture = re.compile(
            r"^macDB has (?P<entries>\d+) entries for mac \S+,vlan (?P<vlan_id>\d+), (?P<dynamic_count>\d+) dynamic$"
        )
        # S   10.10.10.11                              dead.beef.0001         Twe1/0/41  38         0100       4s         REACHABLE  308 s
        entry_capture = re.compile(
            r"^(?P<code>\S+)\s+"
            r"(?P<network_layer_address>\S+)\s+"
            r"(?P<link_layer_address>\S+)\s+"
            r"(?P<interface>\S+)\s+"
            r"(?P<vlan_id>\d+)\s+"
            r"(?P<prlvl>\d+)\s+"
            r"(?P<age>\S+)\s+"
            r"(?P<state>\S+)\s+"
            r"((try\s\d\sN/A)|(?P<time_left>\S+\s\S+))$"
        )

        entry_num = 0
        for line in out.splitlines():
            line = line.strip()

            # macDB has 2 entries for mac dead.beef.0001,vlan 38, 0 dynamic
            match = table_info_capture.match(line)
            if match:
                groups = match.groupdict()

                entries = int(groups['entries'])
                vlan_id = int(groups['vlan_id'])
                dynamic_count = int(groups['dynamic_count'])

                device_tracking_database_mac_dict['macDB_count'] = entries
                device_tracking_database_mac_dict['vlan'] = vlan_id
                device_tracking_database_mac_dict['dynamic_count'] = dynamic_count
                continue

            # S   10.10.10.11                              dead.beef.0001         Twe1/0/41  38         0100       4s         REACHABLE  308 s
            match = entry_capture.match(line)
            if match:
                entry_num += 1
                groups = match.groupdict()

                code = groups['code']
                ip = groups['network_layer_address']
                lla = groups['link_layer_address']
                interface = groups['interface']
                vlan = int(groups['vlan_id'])
                prlvl = int(groups['prlvl'])
                age = groups['age']
                state = groups['state']

                index_dict = device_tracking_database_mac_dict.setdefault('entries', {}).setdefault(entry_num, {})

                index_dict['dev_code'] = code
                index_dict['network_layer_address'] = ip
                index_dict['link_layer_address'] = lla
                index_dict['interface'] = interface
                index_dict['vlan_id'] = vlan
                index_dict['pref_level_code'] = prlvl
                index_dict['age'] = age
                index_dict['state'] = state

                if groups['time_left']:
                    time_left = groups['time_left']
                    index_dict['time_left'] = time_left
                continue

        return device_tracking_database_mac_dict


# ==================================
# Schema for:
#  * 'show device-tracking database mac {mac} details'
# ==================================
class ShowDeviceTrackingDatabaseMacMacDetailsSchema(MetaParser):
    """Schema for show device-tracking database mac {mac} details."""

    schema = {
        "entry_count": int,
        "vlan_id": int,
        "dynamic_count": int,
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
            "total": int,
        },
        "entries": {
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
            }
        }
    }

# ==================================
# Parser for:
#  * 'show device-tracking database mac {mac} details'
# ==================================
class ShowDeviceTrackingDatabaseMacMacDetails(ShowDeviceTrackingDatabaseMacMacDetailsSchema):
    """Parser for show device-tracking database mac {mac} details."""

    cli_command = 'show device-tracking database mac {mac} details'

    def cli(self, mac, output=None):
        if output is None:
            cmd = self.cli_command.format(mac=mac)
            out = self.device.execute(cmd)

        else:
            out = output
        device_tracking_database_mac_details_dict = {}

        # Binding table configuration:
        # ----------------------------
        # max/box  : no limit
        # max/vlan : no limit
        # max/port : no limit
        # max/mac  : no limit

        # Binding table current counters:
        # ------------------------------
        # dynamic  : 0
        # local    : 0
        # total    : 2

        # Binding table counters by state:
        # ----------------------------------
        # REACHABLE  : 2
        # total    : 2

        # Codes: L - Local, S - Static, ND - Neighbor Discovery, ARP - Address Resolution Protocol, DH4 - IPv4 DHCP, DH6 - IPv6 DHCP, PKT - Other Packet, API - API created
        # Preflevel flags (prlvl):
        # 0001:MAC and LLA match     0002:Orig trunk            0004:Orig access           
        # 0008:Orig trusted trunk    0010:Orig trusted access   0020:DHCP assigned         
        # 0040:Cga authenticated     0080:Cert authenticated    0100:Statically assigned   
        #
        #
        #     Network Layer Address                    Link Layer Address     Interface  mode       vlan(prim)   prlvl      age        state      Time left        Filter     In Crimson   Client ID          Policy (feature)
        # macDB has 2 entries for mac dead.beef.0001,vlan 38, 0 dynamic 
        # S   10.10.10.11                              dead.beef.0001(R)      Twe1/0/41  trunk      38  (  38)      0100       63s        REACHABLE  249 s            no         yes          0000.0000.0000    
        # S   10.10.10.10                              dead.beef.0001(R)      Twe1/0/41  trunk      38  (  38)      0100       136s       REACHABLE  167 s            no         yes          0000.0000.0000    

        # Binding table configuration:
        binding_table_config_capture = re.compile(r"^Binding table configuration:")
        # max/box  : no limit
        # REACHABLE  : 2
        # total    : 2
        table_entry_capture = re.compile(r"^(?P<parameter>\S+)\s+:\s+(?P<info>((\d+)|(no limit)))")
        # Binding table current counters:
        binding_table_current_counters_capture = re.compile(r"^Binding table current counters:")
        # Binding table counters by state:
        binding_table_counters_by_state_capture = re.compile(r"^Binding table counters by state:")
        # macDB has 2 entries for mac dead.beef.0001,vlan 38, 0 dynamic
        table_info_capture = re.compile(
            r"^macDB has (?P<entries>\d+) entries for mac \S+,vlan (?P<vlan_id>\d+), (?P<dynamic_count>\d+) dynamic$"
        )
        # S   10.10.10.11                              dead.beef.0001(R)      Twe1/0/41  trunk      38  (  38)      0100       63s        REACHABLE  249 s            no         yes          0000.0000.0000
        entry_capture = re.compile(
            r"^(?P<dev_code>\S+)"
            r"\s+(?P<network_layer_address>(\S\S\.\S\S\.\S\S\.\S\S))"
            r"\s+(?P<link_layer_address>\S+)"
            r"\s+(?P<interface>\S+)"
            r"\s+(?P<mode>\S+)"
            r"\s+(?P<vlan>\d+)\s+\(\s+\d+\)"
            r"\s+(?P<prlvl>\d+)"
            r"\s+(?P<age>\S+)"
            r"\s+(?P<state>\S+)"
            r"(\s+(?P<time_left>(\S+\ss)))?"
            r"\s+(?P<filter>\S+)"
            r"\s+(?P<in_crimson>\S+)"
            r"\s+(?P<client_id>\S+)"
            r"(\s+(?P<policy>(.*)))?$"
        )

        key = ""
        entry_counter = 0
        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Binding table configuration:
            match = binding_table_config_capture.match(line)
            if match:
                key = 'binding_table_configuration'
                device_tracking_database_mac_details_dict[key] = {}
                continue

            # Binding table current counters:
            match = binding_table_current_counters_capture.match(line)
            if match:
                key = 'binding_table_count'
                device_tracking_database_mac_details_dict[key] = {}
                continue

            # Binding table counters by state:
            match = binding_table_counters_by_state_capture.match(line)
            if match:
                key = 'binding_table_state_count'
                device_tracking_database_mac_details_dict[key] = {}
                continue

            # REACHABLE  : 2
            match = table_entry_capture.match(line)
            if match:
                groups = match.groupdict()

                name = groups['parameter'].lower()
                value = groups['info']
                if key == 'binding_table_state_count' or key == 'binding_table_count':
                    value = int(value)
                device_tracking_database_mac_details_dict[key][name] = value
                continue

            # macDB has 2 entries for mac dead.beef.0001,vlan 38, 0 dynamic
            match = table_info_capture.match(line)
            if match:
                groups = match.groupdict()

                entry_count = int(groups['entries'])
                vlan_id = int(groups['vlan_id'])
                dynamic_count = int(groups['dynamic_count'])

                device_tracking_database_mac_details_dict['entry_count'] = entry_count
                device_tracking_database_mac_details_dict['vlan_id'] = vlan_id
                device_tracking_database_mac_details_dict['dynamic_count'] = dynamic_count
                continue

            # S   10.10.10.11                              dead.beef.0001(R)      Twe1/0/41  trunk      38  (  38)      0100       63s        REACHABLE  249 s            no         yes          0000.0000.0000
            match = entry_capture.match(line)
            if match:
                groups = match.groupdict()
                entry_counter += 1

                dev_code = groups['dev_code']
                network_layer_address = groups['network_layer_address']
                lla = groups['link_layer_address']
                interface = groups['interface']
                mode = groups['mode']
                vlan = int(groups['vlan'])
                prlvl = int(groups['prlvl'])
                age = groups['age']
                state = groups['state']
                filter = groups['filter']
                in_crimson = groups['in_crimson']
                client_id = groups['client_id']

                index_dict = device_tracking_database_mac_details_dict.setdefault('entries', {}).setdefault(entry_counter, {})

                index_dict['dev_code'] = dev_code
                index_dict['network_layer_address'] = network_layer_address
                index_dict['link_layer_address'] = lla
                index_dict['interface'] = interface
                index_dict['mode'] = mode
                index_dict['vlan_id'] = vlan
                index_dict['pref_level_code'] = prlvl
                index_dict['age'] = age
                index_dict['state'] = state
                index_dict['filter'] = filter
                index_dict['in_crimson'] = in_crimson
                index_dict['client_id'] = client_id

                if groups['time_left']:
                    time_left = groups['time_left']
                    index_dict['time_left'] = time_left
                if groups['policy']:
                    policy = groups['policy']
                    index_dict['policy'] = policy
                continue

        return device_tracking_database_mac_details_dict

# ========================
# Schema for:
#   * 'show device-tracking counters interface {interface}'
# ========================
class ShowDeviceTrackingCountersInterfaceSchema(MetaParser):
    '''Schema for:
        * 'show device-tracking counters interface {interface}'
    '''

    schema = {
        "interface": {
            str: {
                "message_type": {
                    str: {
                        Optional("protocols"): {
                            Optional("acd_dad"): int,
                            Optional(Or("ndp","dhcpv6","arp","dhcpv4","probe_send","probe_reply")): {
                                Any(): int,
                            },
                        },
                    },
                    "dropped": {
                        Optional("feature"): {
                            Any(): {
                                "protocol": str,
                                "message": str,
                                "dropped": int,
                            },
                        },
                    },
                    "faults": list,
                },
            },
        },
    }


# ========================
# Parser for:
#   * 'show device-tracking counters interface {interface}'
# ========================
class ShowDeviceTrackingCountersInterface(ShowDeviceTrackingCountersInterfaceSchema):
    '''Parser for:
        * 'show device-tracking counters interface {interface}'
    '''

    cli_command = 'show device-tracking counters interface {interface}'

    def cli(self, interface, output=None):

        if output is None:
            cmd = self.cli_command.format(interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        device_tracking_counters_interface_dict = {}
        message_key = ''

        # Received messages on Twe1/0/42:
        p1 = re.compile(r'^Received\s+messages\s+on\s+\S+:$')

        # Received Broadcast/Multicast messages on Twe1/0/42:
        p2 = re.compile(r'^Received\s+Broadcast/Multicast\s+messages\s+on\s+\S+:$')

        # Bridged messages from Twe1/0/42:
        p3 = re.compile(r'^Bridged\s+messages\s+from\s+\S+:$')

        # Broadcast/Multicast converted to unicast messages from Twe1/0/42:
        p4 = re.compile(r'^Broadcast/Multicast\s+converted\s+to\s+unicast\s+messages\s+from\s+\S+:$')

        # Probe message on Twe1/0/42:
        p5 = re.compile(r'^Probe\s+message\s+on\s+\S+:$')

        # Limited Broadcast to Local message on Twe1/0/42:
        p6 = re.compile(r'^Limited\s+Broadcast\s+to\s+Local\s+message\s+on\s+\S+:$')

        # Dropped messages on Twe1/0/42:
        p7 = re.compile(r'^Dropped\s+messages\s+on\s+\S+:$')

        # Faults on Twe1/0/42:
        p8 = re.compile(r'^Faults\s+on\s+\S+:$')

        # NDP             RS[70160] NS[20760] NA[14]
        # DHCPv6
        # ARP
        # DHCPv4
        # PROBE_SEND      NS[19935] REQ[3]
        # PROBE_REPLY     NA[14]
        p9 = re.compile(r'^(?P<protocol>(NDP|DHCPv6|ARP|DHCPv4|PROBE_\S+))\s+(?P<message>(.*))?')

        # ACD&DAD         --[20760]
        p10 = re.compile(r'^(?P<protocol>(ACD&DAD))\s+\S+\[(?P<message>(\d+))\]?$')

        # Flooding Suppress:  NDP      NS  [35]
        p11 = re.compile(r'^(?P<feature>((?!reason).*)):\s+(?P<protocol>(\S+))'
                                          r'\s+(?P<message>(\S+))\s+\[(?P<dropped>(\d+))\]$')

        # DHCPv6_REBIND_NAK[3]
        p12 = re.compile(r'^(?P<fault>(FAULT_CODE_INVALID|DHCPv\d_\S+_(TIMEOUT|NAK|ERROR))).*$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            if not device_tracking_counters_interface_dict:
                intf = Common.convert_intf_name(interface)
                message_dict = device_tracking_counters_interface_dict.setdefault('interface', {}) \
                                                                      .setdefault(intf, {}) \
                                                                      .setdefault('message_type', {})

            m = p1.match(line)
            if m:
                message_key = "received"
                message_dict.setdefault(message_key, {})
                continue

            m = p2.match(line)
            if m:
                message_key = "received_broadcast_multicast"
                message_dict.setdefault(message_key, {})
                continue

            m = p3.match(line)
            if m:
                message_key = "bridged"
                message_dict.setdefault(message_key, {})
                continue

            m = p4.match(line)
            if m:
                message_key = "broadcast_multicast_to_unicast"
                message_dict.setdefault(message_key, {})
                continue

            m = p5.match(line)
            if m:
                message_key = "probe"
                message_dict.setdefault(message_key, {})
                continue

            m = p6.match(line)
            if m:
                message_key = "limited_broadcast_to_local"
                message_dict.setdefault(message_key, {})
                continue

            m = p7.match(line)
            if m:
                dropped_dict = message_dict.setdefault('dropped', {})
                continue

            m = p8.match(line)
            if m:
                faults_list = message_dict.setdefault('faults', [])
                continue

            m = p9.match(line)
            if m:
                groups = m.groupdict()
                protocol = groups['protocol'].lower()
                messages = groups['message'].split()
                packet_dict = message_dict.setdefault(message_key, {}).setdefault('protocols', {}) \
                                          .setdefault(protocol, {})
                packet_capture = re.compile(r'^(?P<packet>(\S+))\[(?P<num>(\d+))\]$')
                for message in messages:
                    m1 = packet_capture.match(message)
                    if m1:
                        packet_groups = m1.groupdict()
                        packet = packet_groups['packet'].lower()
                        num = packet_groups['num']
                        packet_dict[packet] = int(num)
                continue

            m = p10.match(line)
            if m:
                groups = m.groupdict()
                protocol = groups['protocol'].lower().replace('&', '_')
                message = groups['message']
                packet_dict = message_dict.setdefault(message_key, {}).setdefault('protocols', {})
                packet_dict[protocol] = int(message)
                continue

            m = p11.match(line)
            if m:
                groups = m.groupdict()
                feature = groups['feature'].replace('&', '_')
                feature_dict = dropped_dict.setdefault('feature', {}).setdefault(feature, {})
                del groups['feature']

                for key, value in groups.items():
                    if value.isdigit():
                        feature_dict[key] = int(value)
                    else:
                        key = key.lower()
                        feature_dict[key] = value.lower()
                continue

            m = p12.match(line)
            if m:
                groups = m.groupdict()
                message = groups['fault']
                faults_list.append(message)
                continue

        return device_tracking_counters_interface_dict


# ====================================================
# Schema for 'show device-tracking events'
# ====================================================
class ShowDeviceTrackingEventsSchema(MetaParser):
    """ Schema for show device-tracking events """

    schema = {
        'ssid': {
              int:{
                "events": {
                    int: {
                    "event_type": str,
                    Optional('event_name'): str,
                    Optional('prev_state'): str,
                    Optional('state'): str,
                    Optional('fsm_name'): str,
                    Optional('ipv4'): str,
                    Optional('static_mac'): str,
                    Optional('ipv6'): str,
                    Optional('dynamic_mac'): str,
                    "ssid": int,
                    "timestamp": str
                    }
                }
              }
            }
        }


# =============================================
# Parser for 'show device-tracking events'
# =============================================
class ShowDeviceTrackingEvents(ShowDeviceTrackingEventsSchema):
    """ show device-tracking events """

    cli_command = 'show device-tracking events'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        #fsm_run event
        #[Fri Jun 18 22:14:40.000] SSID 0 FSM Feature Table running for event ACTIVE_REGISTER in state CREATING
        p1 = re.compile(r'^\[(?P<timestamp>.+)\]\s+SSID\s+(?P<ssid>\d+)\s+FSM\s+(?P<fsm_name>.*)\s+running\s+for\s+event\s+(?P<event_name>(?<=event\s{1})\S+)\s+in\s+state\s+(?P<event_state>.+)$')

        #fsm_transition event
        #[Fri Jun 18 22:14:40.000] SSID 0 Transition from CREATING to READY upon event ACTIVE_REGISTER
        p2 = re.compile(r'^\[(?P<timestamp>.+)\]\s+SSID\s+(?P<ssid>\d+)\s+Transition\s+from\s+(?P<prev_state>.+)\s+to\s+(?P<state>.+)\s+upon\s+event\s+(?P<event_name>.+)$')

        #bt_entry event
        #[Wed Jun 30 17:03:14.000] SSID 1 Created Entry origin Static MAC 000a.000a.000a IPV4 1.1.1.1
        #[Wed Jun 30 17:03:14.000] SSID 1 Entry State changed origin Static MAC 000a.000a.000a IPV4 1.1.1.1
        p3 = re.compile(r'^\[(?P<timestamp>.+)\]\s+SSID\s+(?P<ssid>\d+)\s(?P<entry_state>.+origin)\s+(?P<mac_addr_type>.+)\sMAC\s+(?P<mac_addr>([\w\d]{4}\.*){3})\s+(?P<ip_addr_type>\S+)\s+(?P<ip_addr>[\w\d\.:]+)$')

        parser_dict = {}
        ssid_event_no_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #[Fri Jun 18 22:14:40.000] SSID 0 FSM Feature Table running for event ACTIVE_REGISTER in state CREATING
            m1 = p1.match(line)
            if m1:
                ssids = parser_dict.setdefault('ssid', {})
                ssid = int(m1.groupdict()['ssid'])
                timestamp = m1.groupdict()['timestamp']

                ssid_obj = ssids.setdefault(ssid, {})
                events = ssid_obj.setdefault("events", {})
                ssid_event_no_dict.setdefault(ssid, 1)
                event_no = ssid_event_no_dict[ssid]

                event = {
                        'ssid': ssid,
                        'event_type': 'fsm_run',
                        'event_name': m1.groupdict()['event_name'],
                        'fsm_name': m1.groupdict()['fsm_name'],
                        'timestamp': timestamp
                    }

                events[event_no] = event
                ssid_event_no_dict[ssid]+=1
                continue

            #[Fri Jun 18 22:14:40.000] SSID 0 Transition from CREATING to READY upon event ACTIVE_REGISTER
            m2 = p2.match(line)
            if m2:
                ssids = parser_dict.setdefault('ssid', {})
                ssid = int(m2.groupdict()['ssid'])
                timestamp = m2.groupdict()['timestamp']

                ssid_obj = ssids.setdefault(ssid, {})
                events = ssid_obj.setdefault("events", {})

                ssid_event_no_dict.setdefault(ssid, 1)
                event_no = ssid_event_no_dict[ssid]

                event = {
                    'ssid': ssid,
                    'event_type': 'fsm_transition',
                    'event_name': m2.groupdict()['event_name'],
                    'state': m2.groupdict()['state'],
                    'prev_state': m2.groupdict()['prev_state'],
                    'timestamp': timestamp
                }

                events[event_no] = event
                ssid_event_no_dict[ssid]+=1
                continue

            #[Wed Jun 30 17:03:14.000] SSID 1 Created Entry origin Static MAC 000a.000a.000a IPV4 1.1.1.1
            #[Wed Jun 30 17:03:14.000] SSID 1 Entry State changed origin Static MAC 000a.000a.000a IPV4 1.1.1.1
            m3 = p3.match(line)
            if m3:
                ssids = parser_dict.setdefault('ssid', {})
                ssid = int(m3.groupdict()['ssid'])
                timestamp = m3.groupdict()['timestamp']

                ssid_obj = ssids.setdefault(ssid, {})
                events = ssid_obj.setdefault("events", {})

                ssid_event_no_dict.setdefault(ssid, 1)
                event_no = ssid_event_no_dict[ssid]

                mac_addr_type = (m3.groupdict()['mac_addr_type']).lower()
                mac_addr_type+="_mac"
                ip_addr_type = (m3.groupdict()['ip_addr_type']).lower()

                event = {
                    'ssid': ssid,
                    'event_type': 'bt_entry',
                    'state': m3.groupdict()['entry_state'],
                    mac_addr_type: m3.groupdict()['mac_addr'],
                    ip_addr_type: m3.groupdict()['ip_addr'],
                    'timestamp': timestamp
                    }

                events[event_no] = event
                ssid_event_no_dict[ssid]+=1
                continue

        return parser_dict


# ====================================================
# Schema for 'show device-tracking features
# ====================================================
class ShowDeviceTrackingFeaturesSchema(MetaParser):
    """ Schema for show device-tracking features """

    schema = {
        'features': {
            str: {
                'feature': str,
                'priority': int,
                'state': str
            }
        }
    }


# =============================================
# Parser for 'show device-tracking features'
# =============================================
class ShowDeviceTrackingFeatures(ShowDeviceTrackingFeaturesSchema):
    """ show device-tracking features """

    cli_command = 'show device-tracking features'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        # Feature name   priority state
        # RA guard          192   READY
        # Device-tracking   128   READY
        # Source guard       32   READY
        p1 = re.compile(r'(?P<feature>.+[^ ])\s+(?P<priority>\d+)\s+(?P<state>\w+)')

        parser_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Feature name   priority state
            # RA guard          192   READY
            # Device-tracking   128   READY
            # Source guard       32   READY
            m = p1.match(line)
            if m:
                features = parser_dict.setdefault('features', {})
                feature = features.setdefault(m.groupdict()['feature'], {})
                feature.update({'feature':  m.groupdict()['feature']})
                feature.update({'priority': int(m.groupdict()['priority'])})
                feature.update({'state':  m.groupdict()['state']})

        return parser_dict

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

        #     MAC                    Interface  vlan       prlvl      state            Time left        Policy           Input_index
        # S    dead.beef.0001         Twe1/0/41  38         TRUSTED    MAC-STALE        93013 s          47      
        #     Attached IP: 10.10.10.11     
        #     Attached IP: 10.10.10.10     
        # L    c4b2.39ae.51df         Vl1        1          TRUSTED    MAC-DOWN                          default          60      

        # S    dead.beef.0001         Twe1/0/41  38         TRUSTED    MAC-STALE        93013 s          47               60
        device_capture = re.compile(
            r"^(?P<dev_code>\S+)"
            r"\s+(?P<link_layer_address>(\S+\.\S+\.\S+))"
            r"\s+(?P<interface>\S+)"
            r"\s+(?P<vlan_id>\d+)"
            r"\s+(?P<prlvl>\S+)"
            r"\s+(?P<state>\S+)"
            r"(\s+(?P<time_left>\S+\ss))?"
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

            # S    dead.beef.0001         Twe1/0/41  38         TRUSTED    MAC-STALE        93013 s          47               60
            match = device_capture.match(line)
            if match:
                device_index += 1
                attached_counter = 0
                groups = match.groupdict()

                dev_code = groups['dev_code']
                lla = groups['link_layer_address']
                interface = groups['interface']
                vlan = int(groups['vlan_id'])
                pref_level = groups['prlvl']
                state = groups['state']
                policy = groups['policy']

                index_dict = device_tracking_database_mac_details_dict.setdefault('device', {}).setdefault(device_index, {})

                index_dict['dev_code'] = dev_code
                index_dict['link_layer_address'] = lla
                index_dict['interface'] = interface
                index_dict['vlan_id'] = vlan
                index_dict['pref_level'] = pref_level
                index_dict['state'] = state
                index_dict["policy"] = policy

                if groups['time_left']:
                    time_left = groups['time_left']
                    index_dict['time_left'] = time_left
                if groups['input_index']:
                    input_index = int(groups['input_index'])
                    index_dict['input_index'] = input_index
                continue

            #     Attached IP: 10.10.10.11
            match = attached_capture.match(line)
            if match:
                attached_counter += 1
                groups = match.groupdict()

                ip = groups['ip']
                attached_dict = device_tracking_database_mac_details_dict['device'][device_index].setdefault('attached', {}).setdefault(attached_counter, {})

                attached_dict['ip'] = ip
                continue

        return device_tracking_database_mac_details_dict

# ==================================
# Schema for:
#  * 'show device-tracking messages'
# ==================================
class ShowDeviceTrackingMessagesSchema(MetaParser):
    schema = {
        'entries': {
            int: {
                "timestamp": str,
                "vlan": int,
                "interface": str,
                Optional("mac"): str,
                "protocol": str,
                "ip": str,
                "ignored": bool,
                Optional("drop_reason"): str,
            }
        }
    }

# ==================================
# Parser for:
#  * 'show device-tracking messages'
# ==================================
class ShowDeviceTrackingMessages(ShowDeviceTrackingMessagesSchema):
    cli_command = "show device-tracking messages"

    def cli(self, output=None):
        if output == None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        device_tracking_messages_dict = {}

        # [Wed Jul 21 20:31:23.000] VLAN 1, From Et0/1 MAC aabb.cc00.0300: ARP::REP, 192.168.23.3, 
        # [Wed Jul 21 20:31:25.000] VLAN 1006, From Et0/1 MAC aabb.cc00.0300: ARP::REP, 192.168.23.3, Packet ignored. 
        # [Wed Jul 21 20:31:27.000] VLAN 10, From Et0/0 MAC aabb.cc00.0100: NDP::NA, FE80::A8BB:CCFF:FE00:100, Drop reason=Packet accepted but not forwarded

        message_capture = re.compile(
            r"^\[(?P<timestamp>(\S+\s\S+\s\d+\s\S+))\]"
            r"\s+VLAN (?P<vlan>\d+),"
            r"\s+From (?P<interface>\S+)"
            r"(\s+MAC (?P<mac>([a-f0-9]+\.[a-f0-9]+\.[a-f0-9]+)):)?"
            r"\s+(?P<protocol>([a-zA-Z]+::[a-zA-Z]+)),"
            r"\s+(?P<ip>(\d+\.\d+\.\d+\.\d+)|(([A-F0-9]+:+)+[A-F0-9]+)),"
            r"(\s+(?P<ignored>(Packet ignored))\.)?"
            r"(\s+Drop reason=(?P<drop_reason>.*))?$"
        )

        entry_counter = 0
        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # [Wed Jul 21 20:31:27.000] VLAN 10, From Et0/0 MAC aabb.cc00.0100: NDP::RA, FE80::A8BB:CCFF:FE00:100, Drop reason=Packet not authorized on port
            match = message_capture.match(line)
            if match:
                entry_counter += 1
                groups = match.groupdict()

                timestamp = groups['timestamp']
                vlan = int(groups['vlan'])
                interface = groups['interface']
                protocol = groups['protocol']
                ip = groups['ip']

                entry_dict = device_tracking_messages_dict.setdefault('entries', {}).setdefault(entry_counter, {})
                entry_dict['timestamp'] = timestamp
                entry_dict['vlan'] = vlan
                entry_dict['interface'] = interface
                entry_dict['protocol'] = protocol
                entry_dict['ip'] = ip

                if groups['mac']:
                    entry_dict['mac'] = groups['mac']
                if groups['ignored']:
                    entry_dict['ignored'] = True
                else:
                    entry_dict['ignored'] = False
                if groups['drop_reason']:
                    entry_dict['drop_reason'] = groups['drop_reason']
                continue

        return device_tracking_messages_dict
