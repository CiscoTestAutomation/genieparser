"""show_ip_vrf.py
   supported commands:
     *  show ip vrf
     *  show ip vrf <vrf>
     *  show ip vrf detail
     *  show ip vrf detial <vrf>
"""
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
from genie.libs.parser.utils.common import Common
from genie.libs.parser.iosxe.show_vrf import ShowVrfDetailSchema, ShowVrfDetail

class ShowIpVrfSchema(MetaParser):
    """Schema for 
        * 'show ip vrf'
        * 'show ip vrf <vrf>'"""

    schema = {'vrf':
                {Any():
                    {Optional('route_distinguisher'): str,
                     'interfaces': list,
                    }
                },
            }


class ShowIpVrf(ShowIpVrfSchema):
    """Parser for: 
        * 'show ip vrf'
        * 'show ip vrf <vrf>'"""

    cli_command = ['show ip vrf', 'show ip vrf {vrf}']
    def cli(self, vrf='', output=None):

        cmd = ""
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #   Name                             Default RD            Interfaces
        #   Mgmt-intf                        <not set>             Gi1
        #   VRF1                             65000:1               Tu1
        #                                                          Lo300
        #                                                          Gi2.390
        p1 = re.compile(r'^(?P<vrf>[\S]+)\s+'
            '(?P<rd>([\d\:]+|(<not set>)))\s+'
            '(?P<interfaces>[\w\/\.\-]+)$')
        p2 = re.compile(r'(?P<interfaces>[\w\/\.\-]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                vrf_dict = ret_dict.setdefault('vrf',{}).setdefault(str(groups['vrf']),{})
                if 'not' not in groups['rd']:
                    vrf_dict['route_distinguisher'] = str(groups['rd'])
                vrf_dict['interfaces'] = [Common.convert_intf_name(groups['interfaces'])]
                continue

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                if 'interfaces' in vrf_dict:
                    vrf_dict.get('interfaces').append(Common.convert_intf_name(groups['interfaces']))

        return ret_dict


class ShowIpVrfDetail(ShowVrfDetail, ShowVrfDetailSchema):
    """Parser for 
        * 'show ip vrf detail'
        * 'show ip vrf detail <vrf>'"""
    cli_command = ['show ip vrf detail' , 'show ip vrf detail {vrf}']

    def cli(self, vrf='', output=None, flag_showipvrfdetail=True):
        return super().cli(vrf, output, flag_showipvrfdetail)
