'''
Author: Knox Hutchinson
Contact: https://dataknox.dev
https://twitter.com/data_knox
https://youtube.com/c/dataknox
'''
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ======================================================
# Schema for 'show mac address-table'
# ======================================================


class ShowMacAddressTableSchema(MetaParser):
    schema = {
        'macs': {
            Any(): {
                'vlan': str,
                'type': str,
                'port': str
                
            }
        }
    }


class ShowMacAddressTable(ShowMacAddressTableSchema):
    """Parser for show mac address-table on Dell PowerSwitch OS6 devices
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = 'show mac address-table'

    """
    Aging time is 300 Sec

    Vlan     Mac Address           Type        Port
    -------- --------------------- ----------- ---------------------
    1        F8B1.5683.8734        Management  Vl1
    20       0005.CDFA.3F30        Dynamic     Gi1/0/1
    20       0EFC.476B.D1E2        Dynamic     Gi1/0/1
    20       1865.90DF.E791        Dynamic     Gi1/0/1
    20       18C0.4D24.01DE        Dynamic     Gi1/0/1
    20       5897.BDAB.2E0A        Dynamic     Gi1/0/1
    20       5897.BDAB.2E56        Dynamic     Gi1/0/1
    20       6003.08BF.028C        Dynamic     Gi1/0/1
    20       AA43.2D3F.4223        Dynamic     Gi1/0/1
    20       C0D2.F389.D1E0        Dynamic     Gi1/0/1
    20       C61D.4667.C243        Dynamic     Gi1/0/1
    20       D003.4BEC.DF57        Dynamic     Gi1/0/1
    20       E007.1BFE.571A        Dynamic     Gi1/0/1
    20       E063.DA81.0C57        Dynamic     Gi1/0/1
    20       F8B1.5683.8734        Management  Vl20

    Total MAC Addresses in use: 15
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        mac_table_dict = {}

        result_dict = {}

        p0 = re.compile(r'^(?P<vlan>\d+)\s+(?P<bia>\w+\.\w+\.\w+)\s+(?P<type>(Management|Dynamic))\s+(?P<port>.+)')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'macs' not in mac_table_dict:
                    result_dict = mac_table_dict.setdefault('macs',{})
                vlan = m.groupdict()['vlan']
                bia = m.groupdict()['bia']
                type = m.groupdict()['type']
                port = m.groupdict()['port']
                result_dict[bia] = {}
                result_dict[bia]['vlan'] = vlan
                result_dict[bia]['type'] = type
                result_dict[bia]['port'] = port
                continue
        return mac_table_dict