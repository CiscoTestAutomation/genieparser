'''show_platform.py

IOSXE c9606r parser for the following show command:
   * show platform hardware fed active fwd-asic resource tcam utilization
   
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any



class ShowPlatformHardwareFedActiveTcamUtilizationSchema(MetaParser):
    """Schema for show platform hardware fed active fwd-asic resource tcam utilization """
    schema = {
        'asic': {
            Any(): {
                'table': {
                    Any(): {
                        'subtype': {
                            Any(): {
                                'dir': {
                                    Any(): {
                                        'max': int,
                                        'used': int,
                                        'used_percent': str,
                                        'v4': int,
                                        'v6': int,
                                        'mpls': int,
                                        'other': int,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
class ShowPlatformHardwareFedActiveTcamUtilization(ShowPlatformHardwareFedActiveTcamUtilizationSchema):
    """Parser for show platform hardware fed active fwd-asic resource tcam utilization """

    cli_command = 'show platform hardware fed active fwd-asic resource tcam utilization'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # CAM Utilization for ASIC  [0]
        p1 = re.compile(r'^CAM +Utilization +for +ASIC  +\[+(?P<asic>(\d+))\]$')

        #CTS Cell Matrix/VPN
        #Label                  EM           O       16384        0    0.00%        0        0        0        0
        #CTS Cell Matrix/VPN
        #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
        # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
        # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
        p2 = re.compile(r'^(?P<table>.+?) +(?P<subtype>\S+) +(?P<dir>\S+) +(?P<max>\d+) +(?P<used>\d+) +(?P<used_percent>\S+\%) +(?P<v4>\d+) +(?P<v6>\d+) +(?P<mpls>\d+) +(?P<other>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # CAM Utilization for ASIC  [0]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                asic = group['asic']
                asic_dict = ret_dict.setdefault('asic', {}).setdefault(asic, {})
                continue

            #CTS Cell Matrix/VPN
            #Label                  EM           O       16384        0    0.00%        0        0        0        0
            #CTS Cell Matrix/VPN
            #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
            # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
            # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
            m = p2.match(line)
            if m:
                group = m.groupdict()
                table_ = group.pop('table').lower().replace(' ','_')
                if table_ == 'label':
                    table_ = 'cts_cell_matrix_vpn_label'
                subtype_ = group.pop('subtype').lower().replace('/','_')
                dir_ = group.pop('dir').lower()
                dir_dict = asic_dict.setdefault('table', {}). \
                            setdefault(table_, {}). \
                            setdefault('subtype', {}). \
                            setdefault(subtype_, {}). \
                            setdefault('dir', {}). \
                            setdefault(dir_, {})
                dir_dict.update({k: v if k=='used_percent' else int(v) for k, v in group.items()})
                continue
                      
        return ret_dict