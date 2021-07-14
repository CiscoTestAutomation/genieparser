import re
import pprint

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

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
            cmd = self.cli_command
            out = self.device.execute(cmd)

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
            if entry_capture.match(line):
                device_index += 1
                entry_capture_match = entry_capture.match(line)
                groups = entry_capture_match.groupdict()
                lla = groups['link_layer_address']
                interface = groups['interface']
                vlan_id = int(groups['vlan_id'])
                pre_level = groups['pre_level']
                state = groups['state']
                policy = groups['policy']

                if not device_tracking_database_mac_dict.get('device', {}):
                    device_tracking_database_mac_dict['device'] = {}
                device_tracking_database_mac_dict['device'][device_index] = {}
                device_tracking_database_mac_dict['device'][device_index]['link_layer_address'] = lla
                device_tracking_database_mac_dict['device'][device_index]['interface'] = interface
                device_tracking_database_mac_dict['device'][device_index]['vlan_id'] = vlan_id
                device_tracking_database_mac_dict['device'][device_index]['pref_level_code'] = pre_level
                device_tracking_database_mac_dict['device'][device_index]['state'] = state
                device_tracking_database_mac_dict['device'][device_index]['policy'] = policy

                if groups['time_left'] is not None:
                    time_left = groups['time_left']
                    device_tracking_database_mac_dict['device'][device_index]['time_left'] = time_left
                if groups['input_index'] is not None:
                    input_index = int(groups['input_index'])
                    device_tracking_database_mac_dict['device'][device_index]['input_index'] = input_index
                continue
        return device_tracking_database_mac_dict


# ==================================
# Schema for:
#  * 'show device-tracking database mac <mac>'
# ==================================
class ShowDeviceTrackingDatabaseMacMacSchema(MetaParser):
    """Schema for show device-tracking database mac <mac>."""

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

            if table_info_capture.match(line):
                match = table_info_capture.match(line)
                groups = match.groupdict()

                entries = int(groups['entries'])
                vlan_id = int(groups['vlan_id'])
                dynamic_count = int(groups['dynamic_count'])

                device_tracking_database_mac_dict['macDB_count'] = entries
                device_tracking_database_mac_dict['vlan'] = vlan_id
                device_tracking_database_mac_dict['dynamic_count'] = dynamic_count

                continue
            elif entry_capture.match(line):
                entry_num += 1
                match = entry_capture.match(line)
                groups = match.groupdict()

                code = groups['code']
                ip = groups['network_layer_address']
                lla = groups['link_layer_address']
                interface = groups['interface']
                vlan = int(groups['vlan_id'])
                prlvl = int(groups['prlvl'])
                age = groups['age']
                state = groups['state']

                if not device_tracking_database_mac_dict.get('entries', {}):
                    device_tracking_database_mac_dict['entries'] = {}
                device_tracking_database_mac_dict['entries'][entry_num] = {}
                device_tracking_database_mac_dict['entries'][entry_num]['dev_code'] = code
                device_tracking_database_mac_dict['entries'][entry_num]['network_layer_address'] = ip
                device_tracking_database_mac_dict['entries'][entry_num]['link_layer_address'] = lla
                device_tracking_database_mac_dict['entries'][entry_num]['interface'] = interface
                device_tracking_database_mac_dict['entries'][entry_num]['vlan_id'] = vlan
                device_tracking_database_mac_dict['entries'][entry_num]['pref_level_code'] = prlvl
                device_tracking_database_mac_dict['entries'][entry_num]['age'] = age
                device_tracking_database_mac_dict['entries'][entry_num]['state'] = state

                if groups['time_left'] is not None:
                    time_left = groups['time_left']
                    device_tracking_database_mac_dict['entries'][entry_num]['time_left'] = time_left

                continue
        return device_tracking_database_mac_dict


# ==================================
# Schema for:
#  * 'show device-tracking database mac <mac> details'
# ==================================
class ShowDeviceTrackingDatabaseMacMacDetailsSchema(MetaParser):
    """Schema for show device-tracking database mac <mac> details."""

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
#  * 'show device-tracking database mac <mac> details'
# ==================================
class ShowDeviceTrackingDatabaseMacMacDetails(ShowDeviceTrackingDatabaseMacMacDetailsSchema):
    """Parser for show device-tracking database mac <mac> details."""

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

            if binding_table_config_capture.match(line):
                key = 'binding_table_configuration'
                device_tracking_database_mac_details_dict[key] = {}
                continue
            elif binding_table_current_counters_capture.match(line):
                key = 'binding_table_count'
                device_tracking_database_mac_details_dict[key] = {}
                continue
            elif binding_table_counters_by_state_capture.match(line):
                key = 'binding_table_state_count'
                device_tracking_database_mac_details_dict[key] = {}
                continue
            elif table_entry_capture.match(line):
                match = table_entry_capture.match(line)
                groups = match.groupdict()

                name = groups['parameter'].lower()
                value = groups['info']
                if key == 'binding_table_state_count' or key == 'binding_table_count':
                    value = int(value)
                device_tracking_database_mac_details_dict[key][name] = value
                continue
            elif table_info_capture.match(line):
                match = table_info_capture.match(line)
                groups = match.groupdict()

                entry_count = int(groups['entries'])
                vlan_id = int(groups['vlan_id'])
                dynamic_count = int(groups['dynamic_count'])

                device_tracking_database_mac_details_dict['entry_count'] = entry_count
                device_tracking_database_mac_details_dict['vlan_id'] = vlan_id
                device_tracking_database_mac_details_dict['dynamic_count'] = dynamic_count
                continue
            elif entry_capture.match(line):
                match = entry_capture.match(line)
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

                if not device_tracking_database_mac_details_dict.get('entries', {}):
                    device_tracking_database_mac_details_dict['entries'] = {}
                device_tracking_database_mac_details_dict['entries'][(entry_counter)] = {}
                device_tracking_database_mac_details_dict['entries'][entry_counter]['dev_code'] = dev_code
                device_tracking_database_mac_details_dict['entries'][entry_counter]['network_layer_address'] = network_layer_address
                device_tracking_database_mac_details_dict['entries'][entry_counter]['link_layer_address'] = lla
                device_tracking_database_mac_details_dict['entries'][entry_counter]['interface'] = interface
                device_tracking_database_mac_details_dict['entries'][entry_counter]['mode'] = mode
                device_tracking_database_mac_details_dict['entries'][entry_counter]['vlan_id'] = vlan
                device_tracking_database_mac_details_dict['entries'][entry_counter]['pref_level_code'] = prlvl
                device_tracking_database_mac_details_dict['entries'][entry_counter]['age'] = age
                device_tracking_database_mac_details_dict['entries'][entry_counter]['state'] = state
                device_tracking_database_mac_details_dict['entries'][entry_counter]['filter'] = filter
                device_tracking_database_mac_details_dict['entries'][entry_counter]['in_crimson'] = in_crimson
                device_tracking_database_mac_details_dict['entries'][entry_counter]['client_id'] = client_id

                if groups['time_left'] is not None:
                    time_left = groups['time_left']
                    device_tracking_database_mac_details_dict['entries'][entry_counter]['time_left'] = time_left
                if groups['policy'] is not None:
                    policy = groups['policy']
                    device_tracking_database_mac_details_dict['entries'][entry_counter]['policy'] = policy

                continue
        return device_tracking_database_mac_details_dict


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
            cmd = self.cli_command
            out = self.device.execute(cmd)

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

            if device_capture.match(line):
                device_index += 1
                attached_counter = 0
                match = device_capture.match(line)
                groups = match.groupdict()

                dev_code = groups['dev_code']
                lla = groups['link_layer_address']
                interface = groups['interface']
                vlan = int(groups['vlan_id'])
                pref_level = groups['prlvl']
                state = groups['state']
                policy = groups['policy']

                if not device_tracking_database_mac_details_dict.get('device', {}):
                    device_tracking_database_mac_details_dict['device'] = {}
                device_tracking_database_mac_details_dict['device'][device_index] = {}
                device_tracking_database_mac_details_dict['device'][device_index]['dev_code'] = dev_code
                device_tracking_database_mac_details_dict['device'][device_index]['link_layer_address'] = lla
                device_tracking_database_mac_details_dict['device'][device_index]['interface'] = interface
                device_tracking_database_mac_details_dict['device'][device_index]['vlan_id'] = vlan
                device_tracking_database_mac_details_dict['device'][device_index]['pref_level'] = pref_level
                device_tracking_database_mac_details_dict['device'][device_index]['state'] = state
                device_tracking_database_mac_details_dict['device'][device_index]["policy"] = policy

                if groups['time_left'] is not None:
                    time_left = groups['time_left']
                    device_tracking_database_mac_details_dict['device'][device_index]['time_left'] = time_left
                if groups['input_index'] is not None:
                    input_index = int(groups['input_index'])
                    device_tracking_database_mac_details_dict['device'][device_index]['input_index'] = input_index
                continue
            elif attached_capture.match(line):
                attached_counter += 1
                match = attached_capture.match(line)
                groups = match.groupdict()

                ip = groups['ip']
                if not device_tracking_database_mac_details_dict['device'][device_index].get('attached', {}):
                    device_tracking_database_mac_details_dict['device'][device_index]['attached'] = {}
                device_tracking_database_mac_details_dict['device'][device_index]['attached'][attached_counter] = {}
                device_tracking_database_mac_details_dict['device'][device_index]['attached'][attached_counter]['ip'] = ip
                continue

        return device_tracking_database_mac_details_dict
