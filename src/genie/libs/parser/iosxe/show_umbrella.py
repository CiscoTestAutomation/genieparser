''' 
IOSXE parsers for the following show commands:

    * 'show umbrella deviceid'
    * 'show umbrella config'
'''

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional

# ==============================================================
# Parser for 'show umbrella deviceid'
# ==============================================================
class ShowUmbrellaDeviceidSchema(MetaParser):
    """Schema for show umbrella deviceid"""
    schema = {
        'interfaces': {
            Any(): {
                Optional('tag'): str,
                Optional('status'): str,
                Optional('device_id'): str
            }
        }
    }

class ShowUmbrellaDeviceid(ShowUmbrellaDeviceidSchema):
    """Parser for show umbrella deviceid"""

    cli_command = 'show umbrella deviceid'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        
        # Te2/0/12                tag_9300         200 SUCCESS     010aa1c364862f56
        p1 = re.compile(r'^(?P<interface>[\w\/\.\-]+) '
               '+(?P<tag>[\w\_\-]+) +(?P<status>\w+\s+\w+) '
               '+(?P<device_id>[\w\-]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Te2/0/12                tag_9300         200 SUCCESS     010aa1c364862f56
            m = p1.match(line)

            if m:
                interface_id = m.groupdict()['interface']
                if interface_id == 'Interface':
                    continue
                ret_dict.setdefault('interfaces', {})[interface_id] = {}
                ret_dict['interfaces'][interface_id]['tag'] = m.groupdict()['tag']
                ret_dict['interfaces'][interface_id]['status'] = m.groupdict()['status']
                ret_dict['interfaces'][interface_id]['device_id'] = m.groupdict()['device_id']
                continue
        return ret_dict


# ==============================================================
# Parser for 'show umbrella config'
# ==============================================================
class ShowUmbrellaConfigSchema(MetaParser):
    """Schema for show umbrella config"""
    schema = {
        'umbrella_configuration': {
            'token_key': str,
            'api_key': str,
            'org_id': str,
            'local_domain_regex_parameter_map_name': str,
            'dns_crypt': str,
            'public_key': str,
            'udp_timeout': int,
            'resolver_address': list,
            'umbrella_interface_config': {
                'umbrella out': {
                    'number_of_interfaces': int,
                    Optional('indexes'): {
                        1: {
                            'interface': str,
                            'mode': str,
                            'vrf': str,
                            'vrf_id': int
                        }
                    }
                },
                'umbrella in': {
                    'number_of_interfaces': int,
                    Optional('indexes'): {
                        1: {
                            'interface': str,
                            'mode': str,
                            'dca': str,
                            'tag': str,
                            'device_id': str,
                            'vrf': str,
                            'vrf_id': int
                        }
                    }
                }
            },
            'parameter_maps': {
                1: {
                    'type': str
                }
            }
        }
    }

class ShowUmbrellaConfig(ShowUmbrellaConfigSchema):
    """Parser for show umbrella config"""

    cli_command = 'show umbrella config'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
 
        #Umbrella Configuration
        p0 =  re.compile(r'^Umbrella\s+Configuration$')

        #Token: FC4C18E820D29D6CFC9B5224D5EAE8020026E638
        p1 = re.compile(r'^Token:\s+(?P<TokenKey>\w+)$')

        #API-KEY: NONE
        p2 = re.compile(r'^API-KEY:\s+(?P<ApiKey>\w+)$')

        #OrganizationID: 2549304
        p3 = re.compile(r'^OrganizationID:\s+(?P<OrgId>\w+)$')

        #Local Domain Regex parameter-map name: NONE
        p4 = re.compile(r'^Local\s+Domain\s+Regex\s+parameter-map\s+name:\s+(?P<LocalBypass>[\w\-]+)$')

        #DNSCrypt: Not enabled           
        p5 = re.compile(r'^DNSCrypt:\s+(?P<DnsyCrypt>Not enabled|Enabled)$')   

        #Public-key: NONE           
        p6 = re.compile(r'^Public-key:\s+(?P<PublicKey>[\w:]+)$')  

        #UDP Timeout: 5 seconds              
        p7 = re.compile(r'^UDP\s+Timeout:\s+(?P<UdpTimeout>\d+) +seconds$') 

        #   Number of interfaces with "umbrella out" config: 1
        p8 = re.compile(r'^Number\s+of\s+interfaces\s+with\s+"umbrella\s+out"\s+config:\s+(?P<OutCount>\d+)$') 

        #    1. TenGigabitEthernet2/0/1 
        p9 = re.compile(r'^(?P<Index>[0-9]+).\s+(?P<OutInt>[\w\/\.\-]+\d)$') 

        #Number of interfaces with "umbrella in" config: 1
        p10 = re.compile(r'^Number\s+of\s+interfaces\s+with\s+"umbrella\s+in"\s+config:\s+(?P<InCount>\d+)$')

        #    1. TenGigabitEthernet2/0/12
        p11 =  re.compile(r'^(?P<Index>[0-9]+).\s+(?P<InInt>[\w\/\.\-]+)$') 

        #     Tag        : tag_9300 
        p12 = re.compile(r'^Tag\s+:\s+(?P<Tag>[\w\-]+)$')

        #     Device-id  : 010aa1c364862f56
        p13 = re.compile(r'^Device-id\s+:\s+(?P<DeviceId>[\w\s]+)$')

        #       Mode     :  OUT
        #       Mode     :  IN
        p14 = re.compile(r'^Mode\s+:\s+(?P<mode>IN|OUT)$')

        #       VRF      : global(Id: 0)
        p15 = re.compile(r'^VRF\s+:\s+(?P<vrf>\w+)\(Id:\s+(?P<vrf_id>\d+)\)$')

        #   DCA        : Disabled
        p16 = re.compile(r'^DCA\s+:\s+(?P<dca>\w+)$')

        #   Resolver address:
        p17 = re.compile(r'^Resolver\s+address:$')

        #   1. 208.67.220.220
        #   2. 208.67.222.222
        #   3. 2620:119:53::53
        #   4. 2620:119:35::35
        p18 = re.compile(r'^(?P<ip_index>\d+).\s+(?P<resolver_ip>[\d\.|\w\:]+)$')

        # Configured Umbrella Parameter-maps:
        p19 = re.compile(r'^Configured\s+Umbrella\s+Parameter-maps:$')

        # 1. global
        p20 = re.compile(r'^(?P<Index>[0-9]+).\s+(?P<patameter_maps_type>\w+)$')

        ret_dict = {}
        flag = 0
        in_int_count = 0
        out_int_count = 0
        resolver_ip_count = 0

        for line in out.splitlines():
            line = line.strip()
            
            # Umbrella Configuration
            m = p0.match(line)
            if m:
                ret_dict['umbrella_configuration'] = {}

            #Token: FC4C18E820D29D6CFC9B5224D5EAE8020026E638 
            #Token: NONE
            m = p1.match(line)  
            if m:
                ret_dict['umbrella_configuration']['token_key'] = m.groupdict()['TokenKey']
                continue

            #API-KEY: NONE 
            #API-KEY: FC4C18E820D29D6CFC9B5224D5EAE8020026E638
            m = p2.match(line)
            if m:
                ret_dict['umbrella_configuration']['api_key'] = m.groupdict()['ApiKey']
                continue
            
            #OrganizationID: 2549304
            m = p3.match(line)
            if m:
                ret_dict['umbrella_configuration']['org_id'] = m.groupdict()['OrgId'] 
                continue

            #Local Domain Regex parameter-map name: NONE
            m = p4.match(line)
            if m:
                ret_dict['umbrella_configuration']['local_domain_regex_parameter_map_name'] = m.groupdict()['LocalBypass']  
                continue

            #DNSCrypt: Not enabled                  
            m = p5.match(line)
            if m: 
                ret_dict['umbrella_configuration']['dns_crypt'] = m.groupdict()['DnsyCrypt']
                continue

            #Public-key: NONE
            m = p6.match(line)
            if m:
                ret_dict['umbrella_configuration']['public_key'] = m.groupdict()['PublicKey'] 
                continue

            #UDP Timeout: 5 seconds
            m = p7.match(line)
            if m: 
                ret_dict['umbrella_configuration']['udp_timeout'] = int(m.groupdict()['UdpTimeout'])
                continue 
            
            # Resolver address:
            m = p17.match(line)
            if m:
                resolver_ip_count = 1
                resolver_address_list = []
                continue
            
            if resolver_ip_count:
                m = p18.match(line) 

                if int(m.groupdict()['ip_index']):
                    resolver_address_list.append(m.groupdict()['resolver_ip'])
                    if int(m.groupdict()['ip_index']) == 4:
                        ret_dict['umbrella_configuration']['resolver_address'] = resolver_address_list
                        resolver_ip_count = 0
                    continue

            #Number of interfaces with "umbrella out" config: 1
            m = p8.match(line)
            if m:
                ret_dict['umbrella_configuration'].setdefault('umbrella_interface_config', {})['umbrella out'] = {}
                ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella out']['number_of_interfaces'] = int(m.groupdict()['OutCount'])
                if int(m.groupdict()['OutCount']) != 0:
                    out_int_count = 1
                
                continue
            
            #1. TenGigabitEthernet2/0/1
            if  out_int_count:
                m = p9.match(line)
                if m:
                    index = int(m.groupdict()['Index'])
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella out'].setdefault('indexes', {})[int(m.groupdict()['Index'])] = {}
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella out']['indexes'][int(m.groupdict()['Index'])]['interface'] = m.groupdict()['OutInt']
                    out_int_count += 1
                    continue

                #   Mode     :  OUT   
                m = p14.match(line)
                if m:
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella out']['indexes'][index]['mode'] = m.groupdict()['mode'] 
                    out_int_count += 1
                    continue
                
                #   VRF      : global(Id: 0)   
                m = p15.match(line)
                if m:
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella out']['indexes'][index]['vrf'] = m.groupdict()['vrf']
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella out']['indexes'][index]['vrf_id'] = int(m.groupdict()['vrf_id'])
                    out_int_count += 1
                    continue

            if out_int_count == 4:
                out_int_count = 0
 
            #Number of interfaces with "umbrella in" config: 1
            m = p10.match(line)
            if m:
                ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in'] = {}
                ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in']['number_of_interfaces'] = int(m.groupdict()['InCount'])
                if int(m.group('InCount')) != 0:
                    in_int_count = 1
                
                continue
             
            #1. TenGigabitEthernet2/0/12
            if  in_int_count:
                m = p11.match(line)
                if m:
                    index = int(m.groupdict()['Index'])
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in'].setdefault('indexes', {})[int(m.groupdict()['Index'])] = {}
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in']['indexes'][int(m.groupdict()['Index'])]['interface'] = m.groupdict()['InInt']
                    in_int_count += 1 
                    continue
            
                #   Mode       : IN  
                m = p14.match(line)
                if m:
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in']['indexes'][index]['mode'] = m.groupdict()['mode'] 
                    in_int_count += 1 
                    continue

                #   VRF        : global(Id: 0)   
                m = p15.match(line)
                if m:
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in']['indexes'][index]['vrf'] = m.groupdict()['vrf']
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in']['indexes'][index]['vrf_id'] = int(m.groupdict()['vrf_id'])
                    in_int_count += 1   
                    continue        

                # Tag        : tag_9300
                m = p12.match(line)
                if m:
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in']['indexes'][index]['tag'] = m.groupdict()['Tag']
                    in_int_count += 1
                    continue

                # Device-id  : 010aa1c364862f56
                m = p13.match(line)
                if m:
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in']['indexes'][index]['device_id'] = m.groupdict()['DeviceId'] 
                    in_int_count += 1  
                    continue
            
                #   DCA        : Disabled
                m = p16.match(line)
                if m:
                    ret_dict['umbrella_configuration']['umbrella_interface_config']['umbrella in']['indexes'][index]['dca'] = m.groupdict()['dca'] 
                    in_int_count += 1  
                    continue

            if in_int_count == 7:
                in_int_count = 0               
                
            # Configured Umbrella Parameter-maps:
            m = p19.match(line)
            if m:
                ret_dict['umbrella_configuration']['parameter_maps'] = {}
                continue

            # 1. global
            m = p20.match(line)
            if m:
                ret_dict['umbrella_configuration']['parameter_maps'].setdefault(int(m.groupdict()['Index']), {})['type'] = m.groupdict()['patameter_maps_type']

        return ret_dict



