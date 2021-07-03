''' show_port_security.py

IOSXE parsers for the following show commands:
    * show port-security
    * show por-security interface {interface}

'''
# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional, \
    Or, \
    And, \
    Default, \
    Use

# ==============================================
# Parser for 'show port-security'
# ==============================================
class ShowPortSecuritySchema(MetaParser):
    """Schema for show port-security
    """

    schema = {
        Optional('interfaces'): {
            Any(): {
                'max_secure_addr_cnt': int,
                'current_addr_cnt': int,
                'security_violation_cnt': int,
                'security_action': str,
            }
        },
        'total_addr_in_system': int,
        'max_addr_limit_in_system': int
    }


class ShowPortSecurity(ShowPortSecuritySchema):
    """Parser for 'show port-security'
    """

    cli_command = ['show port-security']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ''' Actual Output
        Device#show port-security                                  
        Secure Port  MaxSecureAddr  CurrentAddr  SecurityViolation  Security Action
                        (Count)       (Count)          (Count)
        ---------------------------------------------------------------------------
            Te4/0/4              2            1                  0         Shutdown
        ---------------------------------------------------------------------------
        Total Addresses in System (excluding one mac per port)     : 0
        Max Addresses limit in System (excluding one mac per port) : 4096
        #expected_output = {
        'interfaces': {
                'Te2/0/4': {
                    'max_secure_addr_cnt': 5,
                    'current_addr_cnt': 3,
                    'security_violation_cnt': 0,
                    'security_action': 'Shutdown'
                }
             },
            'total_addr_in_system': 0,
            'max_addr_limit_in_system': 4096
         }
        '''

        # initial return dictionary
        ret_dict = {}
        # initial regexp pattern

        # Matching patterns
        #     Te2/0/4              5            3                 0         Shutdown
        #     Tw3/0/4              4            2                 0         Shutdown
        #     Gi4/0/4              3            1                 0         Shutdown
        p1 = re.compile(r'((^(?P<interface>[\w\/]+)\s+)'
                        r'(?P<max_secure_addr_cnt>[\d]+)\s+'
                        r'(?P<current_addr_cnt>[\d]+)\s+'
                        r'(?P<security_violation_cnt>[\d]+)\s+'
                        r'(?P<security_action>[\w]+)$)')
        # Total Addresses in System (excluding one mac per port)     : 0
        p2 = re.compile(r'^Total +Addresses +in +System +\(excluding +one +mac +per +port\)\s+\:\s('
                        r'?P<total_addr_in_system>\d+)$')
        # Max Addresses limit in System (excluding one mac per port) : 4096
        p3 = re.compile(r'^Max +Addresses +limit +in +System +\(excluding +one +mac +per +port\)\s+\:\s('
                        r'?P<max_addr_limit_in_system>\d+)$')
        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_dict = ret_dict.setdefault('interfaces', {})
                interface = group['interface']
                intf_dict[interface] = {}
                intf_dict[interface]['max_secure_addr_cnt'] = int(group['max_secure_addr_cnt'])
                intf_dict[interface]['current_addr_cnt'] = int(group['current_addr_cnt'])
                intf_dict[interface]['security_violation_cnt'] = int(group['security_violation_cnt'])
                intf_dict[interface]['security_action'] = group['security_action']
                continue
            # Total Addresses in System (excluding one mac per port)     : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['total_addr_in_system'] = int(group['total_addr_in_system'])
                continue
            # Max Addresses limit in System (excluding one mac per port) : 4096
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['max_addr_limit_in_system'] = int(group['max_addr_limit_in_system'])
                continue
        return ret_dict
# ==================================================================================
# Parser for 'show port-security interface {interface} '
# ==================================================================================
class ShowPortSecurityInterfaceSchema(MetaParser):
    """Schema for 'show port-security  interface {interface} '
    """
    schema = {
        'port_security': str,
        'port_status': str,
        'violation_mode': str,
        'aging_time': str,
        'aging_type': str,
        'secure_static_addr_aging': str,
        'max_mac_addr': int,
        'total_mac_addr': int,
        'cfg_mac_addr': int,
        'sticky_mac_addr': int,
        'last_src_addr': str,
        'last_src_addr_vlan': int,
        'sec_violation_cnt': int,
    }


class ShowPortSecurityInterface(ShowPortSecurityInterfaceSchema):
    """Parser for 'show port-security interface {interface}'
    """
    cli_command = 'show port-security interface {interface}'

    def cli(self, interface=None, output=None):

        if not output:
            # get output from device
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output
        ''' 
        ###Actual Output
        Device#show port-security interface tenGigabitEthernet4/0/4
        Port Security              : Enabled
        Port Status                : Secure-up
        Violation Mode             : Shutdown
        Aging Time                 : 0 mins
        Aging Type                 : Absolute
        SecureStatic Address Aging : Disabled
        Maximum MAC Addresses      : 2
        Total MAC Addresses        : 1
        Configured MAC Addresses   : 0
        Sticky MAC Addresses       : 0
        Last Source Address:Vlan   : 0050.56be.3bd9:200
        Security Violation Count   : 0
        ###Parsed Output
        expected_output = {
            'port_security': 'Enabled',
            'port_status': 'Secure-up',
            'violation_mode': 'Shutdown',
            'aging_time': '0 mins',
            'aging_type': 'Absolute',
            'secure_static_addr_aging': 'Disabled',
            'max_mac_addr': 2,
            'total_mac_addr': 1,
            'cfg_mac_addr': 0,
            'sticky_mac_addr': 0,
            'last_src_addr': '0050.56be.3bd9',
            'last_src_addr_vlan': 200,
            'sec_violation_cnt': 0
            }'''
        # Port Security              : Enabled
        p1 = re.compile(r'^Port\sSecurity\s+\:\s(?P<port_security>\w+)$')
        # Port Status                : Secure-up
        p2 = re.compile(r'^Port\sStatus\s+\:\s(?P<port_status>[\w\-]+)$')
        # Violation Mode             : Shutdown
        p3 = re.compile(r'^Violation\sMode\s+\:\s(?P<violation_mode>\w+)$')
        # Aging Time                 : 0 mins
        p4 = re.compile(r'^Aging\sTime\s+\:\s(?P<aging_time>\w+\s\w+)$')
        # Aging Type                 : Absolute
        p5 = re.compile(r'^Aging\sType\s+\:\s(?P<aging_type>\w+)$')
        # SecureStatic Address Aging : Disabled
        p6 = re.compile(r'^SecureStatic\sAddress\sAging\s+\:\s(?P<secure_static_addr_aging>\w+)$')
        # Maximum MAC Addresses      : 2
        p7 = re.compile(r'^Maximum\sMAC\sAddresses\s+\:\s(?P<max_mac_addr>\d+)$')
        # Total MAC Addresses        : 1
        p8 = re.compile(r'^Total\sMAC\sAddresses\s+\:\s(?P<total_mac_addr>\d+)$')
        # Configured MAC Addresses   : 0
        p9 = re.compile(r'^Configured\sMAC\sAddresses\s+\:\s(?P<cfg_mac_addr>\d+)$')
        # Sticky MAC Addresses       : 0
        p10 = re.compile(r'^Sticky\sMAC\sAddresses\s+\:\s(?P<sticky_mac_addr>\d+)$')
        # Last Source Address:Vlan   : 0050.56be.3bd9:200
        p11 = re.compile(r'^Last\sSource\sAddress\:Vlan\s+\:\s'
                         r'(?P<last_src_addr>\w+\.\w+\.\w+)\:(?P<last_src_addr_vlan>\d+)$')
        # Security Violation Count   : 0
        p12 = re.compile(r'^Security\sViolation\sCount\s+\:\s(?P<sec_violation_cnt>\d+)$')

        # initial return dictionary
        intf_dict ={}
        for line in out.splitlines():
            line = line.strip()
            # Port Security              : Enabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_dict = {}
                intf_dict['port_security'] = group['port_security']
                continue
            # Port Status                : Secure-up
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict['port_status'] = group['port_status']
                continue
            # Violation Mode             : Shutdown
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf_dict['violation_mode'] = group['violation_mode']
                continue
            # Aging Time                 : 0 mins
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_dict['aging_time'] = group['aging_time']
                continue
            # Aging Type                 : Absolute
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_dict['aging_type'] = group['aging_type']
                continue
            # SecureStatic Address Aging : Disabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                intf_dict['secure_static_addr_aging'] = group['secure_static_addr_aging']
                continue
            # Maximum MAC Addresses      : 2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                intf_dict['max_mac_addr'] = int(group['max_mac_addr'])
                continue
            # Total MAC Addresses        : 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                intf_dict['total_mac_addr'] = int(group['total_mac_addr'])
                continue
            # Configured MAC Addresses   : 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                intf_dict['cfg_mac_addr'] = int(group['cfg_mac_addr'])
                continue
            # Sticky MAC Addresses       : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                intf_dict['sticky_mac_addr'] = int(group['sticky_mac_addr'])
                continue
            # Last Source Address:Vlan   : 0050.56be.3bd9:200
            m = p11.match(line)
            if m:
                group = m.groupdict()
                intf_dict['last_src_addr'] = group['last_src_addr']
                intf_dict['last_src_addr_vlan'] = int(group['last_src_addr_vlan'])
                continue
            # Security Violation Count   : 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                intf_dict['sec_violation_cnt'] = int(group['sec_violation_cnt'])
                continue

        return intf_dict
