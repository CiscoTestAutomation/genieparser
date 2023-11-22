"""show_device.py

IOSXE parsers for the following show commands:
    * show device-sensor cache interface {interface}
    * show device-sensor cache all
    * show device-sensor cache mac {mac_address}
    * show device-sensor details
    * show device classifier attached interface {intf}
    * show device classifier attached mac-address {mac_address}
    * show device classifier attached interface <interface> detail
    * show device classifier profile type custom
    * show device classifier attached detail   

"""

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Default

# parser utils
from genie.libs.parser.utils.common import Common

# =================
# Schema for:
#  * 'show device-sensor cache interface {interface}'
#  * show device-sensor cache mac {mac_address}
#  * show device-sensor cache all
# =================

class ShowDeviceSensorSchema(MetaParser):
    """Schema for show device-sensor cache interface {interface}"""
    schema = {
        'device':{
            # device mac address
            Any(): {
                'port': {
                    Any(): {
                        'proto': {
                            # Protocol - DHCP or CDP
                            Any(): {
                                'type': {
                                    # Protocol Type - integer
                                    Any(): {  
                                        'name': str,
                                        'length': int,
                                        'value': str,
                                        'text': str,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# =================
# Parser for:
#  * 'show device-sensor'
# =================
class ShowDeviceSensor(ShowDeviceSensorSchema):
    '''Parser for show device-sensor cache interface {interface}     

    '''

    cli_command = ['show device-sensor cache interface {interface}',
                   'show device-sensor cache {cache_all}',
                   'show device-sensor cache mac {mac_address}']

    def cli(self, interface=None, mac_address=None, cache_all=None, output=None):
        if output is None:            
            if interface:
                cmd = "show device-sensor cache interface {interface}".format(interface=interface)
                output = self.device.execute(cmd)
            elif mac_address:
                cmd = "show device-sensor cache mac {mac_address}".format(mac_address=mac_address)
                output = self.device.execute(cmd)
            elif cache_all:
                cmd = "show device-sensor cache {cache_all}".format(cache_all=cache_all)
                output = self.device.execute(cmd)
        else:
            output = output

        # initial variables
        ret_dict = {'device': {}}

        if output:
            if "No elements found in cache" in output:
                ret_dict = {}
                return ret_dict

        # Device: 0050.56ae.de2e on port TenGigabitEthernet1/1/6
        p0 = re.compile(r'^Device: +(?P<mac>\S+) +on port (?P<port>\S+)$')

        # DHCP    60:class-identifier            10 3C 08 63 69 73 63 6F 70 6E  <.ciscopn
        # DHCP    60:class-identifier            38 3C 24 43 69 73 63 6F 20 73  <$Cisco s
        p1 = re.compile(r'^(?P<protocol>\S+)\s+(?P<proto_type>\d+):(?P<name>\S+)\s+(?P<length>\d+)\s(?P<value>[0-9A-F\d ]{27})\s(?P<text>.+)$')

        #                                           30 63 37 35 2E 62 64 30 32  0c75.bd02
        #                                           79 73 74 65 6D 73 2C 20 49  ystems, I
        p2 = re.compile(r'^\s+(?P<value>[0-9A-F\d ]{27})\s(?P<text>.+)$')

        for line in output.splitlines():
            line_strip = line.strip()

            m = p0.match(line)
            if m:
                mac = m.groupdict()['mac']
                mac_dict = ret_dict['device'].setdefault(mac, {})
                mac_dict['port'] = {}
                interface = m.groupdict()['port']
                port_dict = mac_dict['port'].setdefault(interface, {})
                port_dict.setdefault('proto', {})
                continue

            m = p1.match(line)
            if m:
                protocol = m.groupdict()['protocol']
                prot_dict = port_dict['proto'].setdefault(protocol, {})
                prot_dict.setdefault('type', {})
                proto_type = m.groupdict()['proto_type']
                # cast to integer
                proto_type_dict = prot_dict['type'].setdefault(int(proto_type), {})
                
                proto_type_dict['name'] = m.groupdict()['name']
                proto_type_dict['length'] = int(m.groupdict()['length'])
                # strip blankspace from the end of the string
                proto_type_dict['value'] = m.groupdict()['value'].rstrip()
                proto_type_dict['text'] = m.groupdict()['text']
                continue

            m = p2.match(line)
            if m:
                value = m.groupdict()['value']
                text = m.groupdict()['text']                
                if value:
                    # Add to existing string
                    proto_type_dict['value'] = proto_type_dict['value'] +" " +value.rstrip()
                if text:
                    # Add to existing string
                    proto_type_dict['text']+=text
                continue

        return ret_dict


class ShowDeviceClassifierAttachedDetailSchema(MetaParser):
    '''Schema for show device classifier attached detail'''

    schema = {
        'mac_address': {
            Any(): {
                'port_id': str,
                'cert': int,
                'parent': int,
                'proto': list,
                'profile_type': str,
                'profile_name': str,
                'device_name': str
            }
        }
    }


class ShowDeviceClassifierAttachedDetail(ShowDeviceClassifierAttachedDetailSchema):
    '''Parser for show device classifier attached detail'''

    cli_command = 'show device classifier attached detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # 0016.47cd.9ab1  GigabitEthernet2/0/48 10   0      M   Built-in Cisco-Device                 CISCO SYSTEMS, INC
        p1 = re.compile(r'^(?P<mac_address>[a-f0-9\.]+)\s+(?P<port_id>\S+)\s+(?P<cert>\d+)\s+'
        r'(?P<parent>\d+)\s+(?P<proto>[A-Z][\sA-Z]*)\s{3}(?P<profile_type>\S+)\s+(?P<profile_name>\S+)\s+(?P<device_name>.+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # 5006.0484.5b1d  GigabitEthernet2/0/48 20   1   C  M   Default  Cisco-Switch                 cisco WS-C3850-48P
            m = p1.match(line)
            if m:
                out_dict = m.groupdict()
                mac_dict = ret_dict.setdefault('mac_address', {}).setdefault(out_dict['mac_address'], {})
                mac_dict['port_id'] = Common.convert_intf_name(out_dict['port_id'])
                mac_dict['cert'] = int(out_dict['cert'])
                mac_dict['parent'] = int(out_dict['parent'])
                mac_dict['proto'] = list(filter(None, out_dict['proto'].split(' ')))
                mac_dict['profile_type'] = out_dict['profile_type']
                mac_dict['profile_name'] = out_dict['profile_name']
                mac_dict['device_name'] = out_dict['device_name']
                continue

        return ret_dict


class ShowDeviceClassifierAttachedInterfaceDetail(ShowDeviceClassifierAttachedDetail):
    '''Parser for show device classifier attached interface {interface} detail'''

    cli_command = 'show device classifier attached interface {interface} detail'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        return super().cli(output=output)


# ======================================================
# Parser for 'show device classifier attached interface <intf>
# ======================================================

class ShowDeviceClassifierAttachedInterfaceSchema(MetaParser):
    """Schema for show device classifier attached interface"""

    schema = {
        'port_id': {
            Any(): {
                'mac_address': str,
                'profile_name': str,
                'device_name': str,
            },
        },
    }

class ShowDeviceClassifierAttachedInterface(ShowDeviceClassifierAttachedInterfaceSchema):
    """Parser for show device classifier attached interface"""

    cli_command = 'show device classifier attached interface {intf}'

    def cli(self, intf=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(intf=intf))

        # 001b.0c18.918d  GigabitEthernet1/0/24 Cisco-IP-Phone-7970          Cisco IP Phone 7970
        p1 = re.compile(r"^(?P<mac_address>\w+\.\w+\.\w+)\s+(?P<port_id>[\w\/\.\-\:]+)\s+(?P<profile_name>\S+)\s+(?P<device_name>.+)$")

        ret_dict = {}

        for line in output.splitlines():

            # 001b.0c18.918d  GigabitEthernet1/0/24 Cisco-IP-Phone-7970          Cisco IP Phone 7970
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                port_id_var = dict_val['port_id']
                if 'port_id' not in ret_dict:
                    port_id = ret_dict.setdefault('port_id', {})
                if port_id_var not in ret_dict['port_id']:
                    port_id_dict = ret_dict['port_id'].setdefault(port_id_var, {})
                port_id_dict['mac_address'] = dict_val['mac_address']
                port_id_dict['profile_name'] = dict_val['profile_name']
                port_id_dict['device_name'] = dict_val['device_name']
                continue

        return ret_dict

# ======================================================
# Parser for 'show device classifier attached mac-address '
# ======================================================

class ShowDeviceClassifierAttachedMacAddressSchema(MetaParser):
    """Schema for show device classifier attached mac-address <mac_address>"""

    schema = {
        'mac_address': {
            Any(): {
                'port_id': str,
                'profile_name': str,
                'device_name': str,
            },
        },
    }

class ShowDeviceClassifierAttachedMacAddress(ShowDeviceClassifierAttachedMacAddressSchema):
    """Parser for show device classifier attached mac-address <mac_address>"""

    cli_command = 'show device classifier attached mac-address {mac_address}'

    def cli(self, mac_address=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mac_address=mac_address))

        # 001b.0c18.918d  GigabitEthernet1/0/24 Cisco-IP-Phone-7970          Cisco IP Phone 7970
        p1 = re.compile(r"^(?P<mac_address>\w+\.\w+\.\w+)\s+(?P<port_id>[\w\/\.\-\:]+)\s+(?P<profile_name>\S+)\s+(?P<device_name>.+)$")

        ret_dict = {}

        for line in output.splitlines():

            # 001b.0c18.918d  GigabitEthernet1/0/24 Cisco-IP-Phone-7970          Cisco IP Phone 7970
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                mac_address_var = dict_val['mac_address']
                if 'mac_address' not in ret_dict:
                    mac_address = ret_dict.setdefault('mac_address', {})
                if mac_address_var not in ret_dict['mac_address']:
                    mac_address_dict = ret_dict['mac_address'].setdefault(mac_address_var, {})
                mac_address_dict['port_id'] = dict_val['port_id']
                mac_address_dict['profile_name'] = dict_val['profile_name']
                mac_address_dict['device_name'] = dict_val['device_name']
                continue

        return ret_dict


class ShowDeviceClassifierProfileTypeCustomSchema(MetaParser):
    """Schema for show device classifier profile type custom"""

    schema = {
        'profile': {
            Any(): {
                'valid': str,
                'type': str,
                'profile_name': str,
                'ncon': int,
                'id': int,
            },
        },
    }

class ShowDeviceClassifierProfileTypeCustom(ShowDeviceClassifierProfileTypeCustomSchema):
    """Parser for show device classifier profile type custom"""

    cli_command = 'show device classifier profile type custom'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Valid     Custom      DEVICE_TYPE_A                               0     0
        p1 = re.compile(r"^(?P<valid>\w+)\s+(?P<type>\w+)\s+(?P<profile_name>\S+)\s+(?P<ncon>\d+)\s+(?P<id>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Valid     Custom      DEVICE_TYPE_A                               0     0
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                profile_name_var = dict_val['profile_name']
                profile = ret_dict.setdefault('profile', {})
                profile_name_dict = ret_dict['profile'].setdefault(profile_name_var, {})
                profile_name_dict['valid'] = dict_val['valid']
                profile_name_dict['type'] = dict_val['type']
                profile_name_dict['profile_name'] = dict_val['profile_name']
                profile_name_dict['ncon'] = int(dict_val['ncon'])
                profile_name_dict['id'] = int(dict_val['id'])
                continue
        return ret_dict 


# ======================================================
# Schema for 'show device-sensor details '
# ======================================================

class ShowDeviceSensorDetailsSchema(MetaParser):
    """Schema for show device-sensor details"""

    schema = {
        'status': str,
        'protocols': {
            Any(): {
                'name': str,
                'status': str,
                'tlv_limit': str,
            },
        },
        'protocol_filter': {
            Any(): {
                'name': str,
                'filter_type': str,
            },
        },
    }

# ======================================================
# Parser for 'show device-sensor details '
# ======================================================
class ShowDeviceSensorDetails(ShowDeviceSensorDetailsSchema):
    """Parser for show device-sensor details"""

    cli_command = 'show device-sensor details'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Status = Enabled 
        p1 = re.compile(r"^Status\s+=\s+(?P<status>\w+)$")
        # CDP            registered  Proto Tlv Limit = 128
        p2 = re.compile(r"^(?P<name>\w+)\s+(?P<status>\w+)\s+(?P<tlv_limit>\S+\s+\S+\s+\S+\s+\S+\s+\S+)$")
        # CDP             None
        p3 = re.compile(r"^(?P<name>\w+)\s+(?P<filter_type>\w+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            # Status = Enabled 
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['status'] = dict_val['status']
                continue

            # CDP            registered  Proto Tlv Limit = 128
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                name_var = dict_val['name']
                protocols = ret_dict.setdefault('protocols', {})
                name_dict = ret_dict['protocols'].setdefault(name_var, {})
                name_dict['name'] = dict_val['name']
                name_dict['status'] = dict_val['status']
                name_dict['tlv_limit'] = dict_val['tlv_limit']
                continue

            # CDP             None
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                name_var = dict_val['name']
                protocol_filter = ret_dict.setdefault('protocol_filter', {})
                name_dict = ret_dict['protocol_filter'].setdefault(name_var, {})
                name_dict['name'] = dict_val['name']
                name_dict['filter_type'] = dict_val['filter_type']
                continue

        return ret_dict


        
        