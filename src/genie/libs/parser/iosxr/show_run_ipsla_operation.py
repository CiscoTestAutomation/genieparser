"""
show_run_ipsla_operation.py
IOSXR parsers for the following show commands:
    * show run ipsla operation
"""

# Python regex and rich module
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, ListOf

# ====================================
# Schema for 'show run ipsla operation'
# ====================================

class ShowRunIpslaOperationSchema(MetaParser):
    """Schema for show run ipsla operation"""

    schema = {
        'ipsla': {
          Optional('operations'): {
            Any(): {
              Optional('type'): {
                Any(): {
                  Optional('name'): str,
                  Optional('tag'): str,
                  Optional('vrf'): str,
                  Optional('src_addr'): str,
                  Optional('dest_addr'): str,
                  Optional('packet'): {
                    Optional('count'): int,
                    Optional('interval'): int
                  },
                  Optional('time_out'): int,
                  Optional('data_size_req'): int,
                  Optional('dest_port'): int,
                  Optional('frequency'): int,
                  Optional('verify-data'): bool
               }
              }
             }
            }
           }
          }


class ShowRunIpslaOperation(ShowRunIpslaOperationSchema):
    """Parser for show run ipsla operation on IOSXR"""

    cli_command = 'show run ipsla operation'

    def cli(self, output=None):
        
        if output is None:
            cmd = self.cli_command

            # Execute command on the device
            out = self.device.execute(cmd)
        else:
            out = output

        config_dict = {}

        # ipsla 
        p0 = re.compile(r'^(?P<ipsla>ipsla)$') 

        # operation 100
        p1 = re.compile(r'^oper\S+\s(?P<oper_id>\d+)$') 

        # type udp jitter
        p2 = re.compile(r'^type\s(?P<oper_type_name>\S+.*)$')

        # tag ABC
        p3 = re.compile(r'^tag.(?P<tag>\S+)$')
        
        # source address 1.1.1.1
        p4 = re.compile(r'^sour\w+\s\w+\s(?P<src_addr>\w+.*)$')
        
        # destination address 2.2.2.2
        p5 = re.compile(r'^dest\w+\saddress\s(?P<dest_addr>\w+.*)$')
        
        # destination port 15000
        p6 = re.compile(r'^dest\w+\sport\s(?P<dest_port>\d+)$')

        # packet count 1000
        p7 = re.compile(r'^pac\w+\scount\s(?P<pkt_cnt>\d+)$')

        # packet interval 20 
        p8 = re.compile(r'^pac\w+\sinterval\s(?P<pkt_int>\d+)$')

        # datasize request 500
        p9 = re.compile(r'^data\w+\sreq\w+\s(?P<data_size_req>\d+)$')

        # timeout 3000
        p10 = re.compile(r'^time\w+\s(?P<time_out>\d+)$')

        # frequency 60
        p11 = re.compile(r'^freq\w+\s(?P<freq>\d+)$')

        # vrf VRF-1
        p12 = re.compile(r'^vrf\s(?P<vrf>\S+)$')

        # verify-data
        p13 = re.compile(r'^(?P<verify_data>verify\-\w+)$')

        # breakpoint()

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # ipsla 
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ipsla = group['ipsla']
                ipsla_dict = config_dict.setdefault(ipsla, {}).setdefault('operations', {})
                continue

            # operation 100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                oper_id = int(group['oper_id'])

                oper_id_dict = {}
                
                ipsla_dict[oper_id] = oper_id_dict
                continue

            # type udp jitter
            m = p2.match(line)
            if m:
                group = m.groupdict()
                oper_type_name = group['oper_type_name']
                oper_type_dict = oper_id_dict.setdefault('type', {})
                
                type_dict = {}
                oper_type_dict[oper_type_name] = type_dict

                # type_dict = oper_type_dict
                continue

            # tag ABC
            m = p3.match(line)
            if m:
                type_dict['tag'] = m.groupdict()['tag']
                continue

            # source address 1.1.1.1
            m = p4.match(line)
            if m:
                type_dict['src_addr'] = m.groupdict()['src_addr']
                continue

            # destination address 2.2.2.2
            m = p5.match(line)
            if m:
                type_dict['dest_addr'] = m.groupdict()['dest_addr']
                continue

            # destination port 15000
            m = p6.match(line)
            if m:
                type_dict['dest_port'] = int(m.groupdict()['dest_port'])
                continue

            # packet count 1000
            m = p7.match(line)
            if m:
                packet_dict = {}
                packet_dict['count'] = int(m.groupdict()['pkt_cnt'])
                type_dict.setdefault('packet', packet_dict)
                continue

            # packet interval 20
            m = p8.match(line)
            if m:
                packet_dict['interval'] = int(m.groupdict()['pkt_int'])
                continue

            # # datasize request 500
            m = p9.match(line)
            if m:
                type_dict['data_size_req'] = int(m.groupdict()['data_size_req'])
                continue

            # timeout 3000
            m = p10.match(line)
            if m:
                type_dict['time_out'] = int(m.groupdict()['time_out'])
                continue

            # frequency 60
            m = p11.match(line)
            if m:
                type_dict['frequency'] = int(m.groupdict()['freq'])

            # vrf VRF-1
            m = p12.match(line)
            if m:
                type_dict['vrf'] = m.groupdict()['vrf']

            # verify-data
            m = p13.match(line)
            if m:
                group = m.groupdict()
                verify_data = group['verify_data']

                if 'verify-data' == verify_data:
                    type_dict['verify-data'] = True

        return config_dict