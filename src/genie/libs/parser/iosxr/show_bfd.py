""" show_bfd.py
    supports commands:
        * show bfd session
"""

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =============================================
# Parser for 'show bfd session'
# =============================================


class ShowBfdSessionSchema(MetaParser):
    schema = {
        'interface': {
            Any(): {
                'dest_ip_address': {
                    Any(): {
                        'echo': str,
                        Optional('echo_multiplier'): str,
                        'async': str,
                        Optional('async_multiplier'): str,
                        'state': str,
                        'hardware': str,
                        'npu': str,
                        Optional('dampening'): str,
                    }
                }
            }
        }
    }


class ShowBfdSession(ShowBfdSessionSchema):
    """ Parser for show bfd session"""

    cli_command = 'show bfd session'

    def cli(self, output=None):
        """parsing mechanism: cli
        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        #Gi0/0/0/36.52       10.129.196.34   450ms(150ms*3)   6s(2s*3)         UP
        p1 = re.compile(
            r'^(?P<intf>\S+) +(?P<dest>\d+\.\d+\.\d+\.\d+) +(?P<echo>\d+\w+)(?P<echo_multiplier>\(\d+\w+\*\d\)) +(?P<async>\d+\w+)(?P<async_multiplier>\(\d+\w+\*\d\)) +(?P<state>\S+)')
        #Gi0/0/0/26.110      10.0.221.98     0s               0s               DOWN DAMP
        p2 = re.compile(
            r'^(?P<intf>\S+) +(?P<dest>\d+\.\d+\.\d+\.\d+) +(?P<echo>\d+\w+) +(?P<async>\d+\w+) +(?P<state>\S+) ?(?P<damp>\S+)?')
        #BE300               172.16.253.53   n/a              n/a              UP
        p3 = re.compile(
            r'^(?P<intf>\S+) +(?P<dest>\d+\.\d+\.\d+\.\d+) +(?P<echo>\w+\/\w+) +(?P<async>\w+\/\w+) +(?P<state>\S+) ?(?P<damp>\S+)?')
        #                                                             No    n/a
        p4 = re.compile(
            r'(?P<hw>[No|Yes]+) +(?P<npu>\S+)')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            #Gi0/0/0/36.52       10.129.196.34   450ms(150ms*3)   6s(2s*3)         UP
            m = p1.match(line)

            if m:
                group = m.groupdict()
                interface = group['intf']
                destaddress = group['dest']
                bfd_dict = result_dict.setdefault('interface',{}).setdefault(interface,{}).setdefault('dest_ip_address',{}).setdefault(destaddress,{})
                bfd_dict.update({'echo': group['echo']})
                bfd_dict.update({'echo_multiplier': group['echo_multiplier']})
                bfd_dict.update({'async': group['async']})
                bfd_dict.update({'async_multiplier': group['async_multiplier']})
                bfd_dict.update({'state': group['state']})

            #Gi0/0/0/26.110      10.0.221.98     0s               0s               DOWN DAMP
            m = p2.match(line)

            if m:
                group = m.groupdict()
                interface = group['intf']
                destaddress = group['dest']
                bfd_dict = result_dict.setdefault('interface',{}).setdefault(interface,{}).setdefault('dest_ip_address',{}).setdefault(destaddress,{})
                bfd_dict.update({'echo': group['echo']})
                bfd_dict.update({'async': group['async']})
                bfd_dict.update({'state': group['state']})
                if group['damp']:
                    bfd_dict.update({'dampening': group['damp']})

            #BE300               172.16.253.53   n/a              n/a              UP
            m = p3.match(line)

            if m:
                group = m.groupdict()
                interface = group['intf']
                destaddress = group['dest']
                bfd_dict = result_dict.setdefault('interface',{}).setdefault(interface,{}).setdefault('dest_ip_address',{}).setdefault(destaddress,{})
                bfd_dict.update({'echo': group['echo']})
                bfd_dict.update({'async': group['async']})
                bfd_dict.update({'state': group['state']})
                if group['damp']:
                    bfd_dict.update({'dampening': group['damp']})

            #                                                             No    n/a
            m = p4.match(line)

            if m:
                group = m.groupdict()
                bfd_dict.update({'hardware': group['hw']})
                bfd_dict.update({'npu': group['npu']})
                continue

        return result_dict
