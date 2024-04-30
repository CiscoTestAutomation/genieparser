"""show_platform_hardware_fed_switch_active_fwd_asic_resource_utilization.py
   supported commands:
     *  show platform hardware fed switch active fwd-asic resource utilization
     *  show platform hardware fed active fwd-asic resource utilization
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common

# =======================================================================
# Schema for 'show sdm prefer' for 9500 device
# =======================================================================
class ShowPlatformHardwareFedSwitchActiveFwdAsicResourceUtilizationSchema(MetaParser):
    """Schema for :
        'show platform hardware fed switch active fwd-asic resource utilization'
        'show platform hardware fed active fwd-asic resource utilization'
    """
    schema = {
            str:
                {
                int:
                    {
                    'resource': str,
                    'object_type': str,
                    'utilized': int,
                    'total': int,
                    }
                }
            }

# ==============================================
# Parser for 'show sdm prefer' for 9500 devices
# ==============================================
class ShowPlatformHardwareFedSwitchActiveFwdAsicResourceUtilization(ShowPlatformHardwareFedSwitchActiveFwdAsicResourceUtilizationSchema):
    """Parser for show platform hardware fed active fwd-asic resource utilization"""

    cli_command = ['show platform hardware fed {switch} active fwd-asic resource utilization','show platform hardware fed active fwd-asic resource utilization']

    def cli(self, output=None, switch=''):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        # initial regexp pattern for
        result_dict = {} #Final Dict
        count = 0 # Index number of sub_dict

        # Regex patern list

        # Resource              Slice         Utilized   Total
        # Resource              Slice Pair    Utilized   Total
        # Resource              Slice/IFG-id  Utilized   Total
        # Resource              Device        Utilized   Total
        p1 = re.compile(r'^(?P<resource>Resource)(?:\s*)(?P<resource_type>Slice\sPair|Slice\/IFG-id|Slice|Device)(?:\s*)(?P<utilized>Utilized)(?:\s*)(?P<total>Total)$')

        # MAC Termination EM table              s-0          172     8224
        # MAC Termination EM table              s-1          172     8224
        # MAC Termination EM table              s-2          176     8224
        # MAC Termination EM table              s-3          172     8224
        # MAC Termination EM table              s-4          172     8224
        # MAC Termination EM table              s-5          174     8224
        # Tunnel 0 Exact Match                  s-0          169     4128
        # Tunnel 0 Exact Match                  s-1          169     4128
        # Tunnel 0 Exact Match                  s-2          169     4128
        # Tunnel 0 Exact Match                  s-3          169     4128
        p2 = re.compile(r'^(?P<resource_1>((\w*\s\w*){1,10}\b)|(\w*.*\w\b))(?:\s*)(?P<slice_1>s-\d*)(?:\s*)(?P<utilized_1>\d*)(?:\s*)(?P<total_1>\d*)$')

        # Ingress Eth Narrow DB2 int_0 ACL IDs          p-1            0      127
        # Ingress Eth Narrow DB2 int_0 ACL IDs          p-2            0      127
        # Ingress IPv4 Security & QOS int_0 ACL IDs     p-0            1      127
        # Ingress IPv4 Security & QOS int_0 ACL IDs     p-1            1      127
        # Ingress IPv4 Security & QOS int_0 ACL IDs     p-2            1      127
        # Ingress IPv4 int_0 OGACL IDs                  p-0            0      127
        # Ingress IPv4 int_0 OGACL IDs                  p-1            0      127
        # Ingress IPv4 int_0 OGACL IDs                  p-2            0      127
        p3 = re.compile(r'^(?P<resource_2>((\w*\s\w*){1,10}\b)|(\w*.*\w\b))(?:\s*)(?P<slice_2>p-\d*)(?:\s*)(?P<utilized_2>\d*)(?:\s*)(?P<total_2>\d*)$')

        # Qos Meter actions                   i-5/0          1        4
        # Qos Meter actions                   i-5/1          1        4
        # Qos Meter profiles                  i-0/0          1       16
        # Qos Meter profiles                  i-0/1          1       16
        # Qos Meter profiles                  i-1/0          1       16
        p4 = re.compile(r'^(?P<resource_3>((\w*\s\w*){1,10}\b)|(\w*.*\w\b))(?:\s*)(?P<slice_3>i-\d*\/\d*)(?:\s*)(?P<utilized_3>\d*)(?:\s*)(?P<total_3>\d*)$')

        # AC Profiles                         d-0            2       15
        # Counter Bank                        d-0           92      108
        # IPv4 VRF DIP EM Table               d-0            6   622555
        # IPv6 VRF DIP EM Table               d-0           11   311285
        # LPM  Routes                         d-0            0      100
        # LPM IPv4 Routes                     d-0           51  2358465
        p5 = re.compile(r'^(?P<resource_4>((\w*\s\w*){1,8}\b)|(\w*.*\w\b))(?:\s*)(?P<slice_4>d-\d*)(?:\s*)(?P<utilized_4>\d*)(?:\s*)(?P<total_4>\d*)$')

        # loop to split lines of output
        for line in output.splitlines():
            line = line.strip()

            # Resource              Slice         Utilized   Total
            # Resource              Slice Pair    Utilized   Total
            # Resource              Slice/IFG-id  Utilized   Total
            # Resource              Device        Utilized   Total
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                table_type = groups['resource_type']
                if table_type == 'Slice':
                    result_dict.setdefault('slice',{})
                if table_type == 'Slice Pair':
                    result_dict.setdefault('slice_pair',{})
                if table_type == 'Slice/IFG-id':
                    result_dict.setdefault('slice_ifg_id',{})
                if table_type == 'Device':
                    result_dict.setdefault('device',{})
                continue
            
            # MAC Termination EM table              s-5          174     8224
            # Tunnel 0 Exact Match                  s-0          169     4128
            m = p2.match(line)
            if m:
                count += 1
                groups = m.groupdict()
                index_dict = result_dict.setdefault('slice',{}).setdefault(int(count), {}) # Create sub_dict inside slice dict with key of dict = count
                index_dict.update({                                                        # Update values of keys in sub_dict
                            'resource': str(groups['resource_1']),
                            'object_type': str(groups['slice_1']),
                            'utilized': int(groups['utilized_1']),
                            'total': int(groups['total_1']),
                        })
                continue
            
            # Ingress IPv4 Security & QOS int_0 ACL IDs     p-2            1      127
            # Ingress IPv4 int_0 OGACL IDs                  p-0            0      127
            m = p3.match(line)
            if m:
                count += 1
                groups = m.groupdict()
                index_dict = result_dict.setdefault('slice_pair',{}).setdefault(int(count), {}) # Create sub_dict inside slice dict with key of dict = count
                index_dict.update({                                                             # Update values of keys in sub_dict
                            'resource': str(groups['resource_2']),
                            'object_type': str(groups['slice_2']),
                            'utilized': int(groups['utilized_2']),
                            'total': int(groups['total_2']),
                        })
                continue
            
            # Qos Meter actions                   i-5/0          1        4
            # Qos Meter actions                   i-5/1          1        4
            # Qos Meter profiles                  i-0/0          1       16
            m = p4.match(line)
            if m:
                count += 1
                groups = m.groupdict()
                index_dict = result_dict.setdefault('slice_ifg_id',{}).setdefault(int(count), {}) # Create sub_dict inside slice dict with key of dict = count
                index_dict.update({                                                               # Update values of keys in sub_dict
                            'resource': str(groups['resource_3']),
                            'object_type': str(groups['slice_3']),
                            'utilized': int(groups['utilized_3']),
                            'total': int(groups['total_3']),
                        })
                continue

            # AC Profiles                         d-0            2       15
            # Counter Bank                        d-0           92      108
            # IPv4 VRF DIP EM Table               d-0            6   622555
            m = p5.match(line)
            if m:
                count += 1
                groups = m.groupdict()
                index_dict = result_dict.setdefault('device',{}).setdefault(int(count), {}) # Create sub_dict inside slice dict with key of dict = count
                index_dict.update({                                                         # Update values of keys in sub_dict
                            'resource': str(groups['resource_4']),
                            'object_type': str(groups['slice_4']),
                            'utilized': int(groups['utilized_4']),
                            'total': int(groups['total_4']),
                        })
                continue
        
        return result_dict
