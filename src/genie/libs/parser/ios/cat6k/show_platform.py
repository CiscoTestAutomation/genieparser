''' cat6k implementation of show_platform.py
'''
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowModuleSchema(MetaParser):
    ''' Schema for commands:
        * show module
    '''
    schema = {
        'mod': {
            Any(): {
                'port': int,
                'card_type': str,
                'model': str,
                'serial_number': str,
                'mac_address_from': str,
                'mac_address_to': str,
                'hw_ver': str,
                Optional('fw_ver'): str,
                Optional('sw_ver'): str,
                'status': str,
                Optional('sub_mod'): {
                    Any(): {
                        'hw_ver': str,
                        'status': str,
                        'serial_number': str,
                        'model': str,

                    }
                }
            }
        }   
    }


class ShowModule(ShowModuleSchema):
    ''' Parser for commands: 
        * show module 
    '''

    cli_command = 'show module'
    
    def cli(self, output=None):
        
        if output is None:
            output = self.device.execute('show module')

        parsed_output = {}

        # 1    2  Catalyst 6000 supervisor 2 (Active)    WS-X6K-S2U-MSFC2   SAD0628035C
        # 5    0  Switching Fabric Module-136 (Active)   WS-X6500-SFM2      SAD061701YC
        r1 = re.compile(r'(?P<mod>\d)\s+(?P<ports>\d+)\s+(?P<card_type>.+\(.+\))'
                         '\s+(?P<model>\S+)\s+(?P<serial_number>\S+)')

        
        # 2    0  Supervisor-Other                       unknown            unknown
        # 6    1  1 port 10-Gigabit Ethernet Module      WS-X6502-10GE      SAD062003CM
        # 3   16  Pure SFM-mode 16 port 1000mb GBIC      WS-X6816-GBIC      SAL061218K3
        r2 = re.compile(r'(?P<mod>\d)\s+(?P<ports>\d+)\s+(?P<card_type>.+)\s{2,}'
                         '(?P<model>\S+)\s+(?P<serial_number>\S+)')

        # 1  0001.6416.0342 to 0001.6416.0343   3.9   6.1(3)       7.5(0.6)HUB9 Ok 
        # 3  0005.7485.9518 to 0005.7485.9527   1.3   12.1(5r)E1   12.1(13)E3,  Ok
        # 1  0001.6416.0342 to 0001.6416.0343   3.9   6.1(3)       7.5(0.6)HUB9 Ok    
        r3 = re.compile(r'(?P<mod>\d+)\s+(?P<mac_from>\S+)\s+to\s+(?P<mac_to>\S+)'
                         '\s+(?P<hw>\S+)\s+(?P<fw>\S+)\s+(?P<sw>[\d\.\(\)\w]+)\,'
                         '*\s+(?P<status>\S+)')

        # 1 Policy Feature Card 2       WS-F6K-PFC2     SAD062802AV      3.2    Ok     
        # 1 Cat6k MSFC 2 daughterboard  WS-F6K-MSFC2    SAD062803TX      2.5    Ok   
        # 6 Distributed Forwarding Card WS-F6K-DFC      SAL06261R0A      2.3    Ok     
        # 6 10GBASE-LR Serial 1310nm lo WS-G6488        SAD062201BN      1.1    Ok
        r4 = re.compile(r'(?P<mod>\d+)\s+(?P<sub_mod>.+)\s+(?P<model>\S+)\s+'
                         '(?P<serial>\S+)\s+(?P<hw>\S+)\s+(?P<status>\S+)')

        for line in output.splitlines():
            line = line.strip()

            # 1    2  Catalyst 6000 supervisor 2 (Active)    WS-X6K-S2U-MSFC2   SAD0628035C
            # 5    0  Switching Fabric Module-136 (Active)   WS-X6500-SFM2      SAD061701YC
            result = r1.match(line)
            if result:
                group = result.groupdict()

                mod = int(group['mod'])
                ports = int(group['ports'])
                card_type = group['card_type']
                model = group['model']
                serial_number = group['serial_number']

                module_dict = parsed_output\
                    .setdefault('mod', {})\
                    .setdefault(mod, {})

                module_dict['port'] = ports
                module_dict['card_type'] = card_type
                module_dict['model'] = model
                module_dict['serial_number'] = serial_number

                continue


            # 2    0  Supervisor-Other                       unknown            unknown
            # 6    1  1 port 10-Gigabit Ethernet Module      WS-X6502-10GE      SAD062003CM
            # 3   16  Pure SFM-mode 16 port 1000mb GBIC      WS-X6816-GBIC      SAL061218K3
            result = r2.match(line)
            if result:
                group = result.groupdict()
                mod = int(group['mod'])
                ports = int(group['ports'])
                card_type = group['card_type']
                model = group['model']
                serial_number = group['serial_number']

                module_dict = parsed_output\
                    .setdefault('mod', {})\
                    .setdefault(mod, {})

                module_dict['port'] = ports
                module_dict['card_type'] = card_type
                module_dict['model'] = model
                module_dict['serial_number'] = serial_number

                continue

            # 1  0001.6416.0342 to 0001.6416.0343   3.9   6.1(3)       7.5(0.6)HUB9 Ok 
            # 3  0005.7485.9518 to 0005.7485.9527   1.3   12.1(5r)E1   12.1(13)E3,  Ok
            # 1  0001.6416.0342 to 0001.6416.0343   3.9   6.1(3)       7.5(0.6)HUB9 Ok   
            result = r3.match(line)
            if result:
                group = result.groupdict()

                mod = int(group['mod'])
                mac_from = group['mac_from']
                mac_to = group['mac_to']
                hw = group['hw']
                fw = group['fw']
                sw = group['sw']
                status = group['status']

                module_dict = parsed_output\
                    .setdefault('mod', {})\
                    .setdefault(mod, {})

                module_dict['mac_address_from'] = mac_from
                module_dict['mac_address_to'] = mac_to
                module_dict['hw_ver'] = hw
                module_dict['fw_ver'] = fw
                module_dict['sw_ver'] = sw
                module_dict['status'] = status

                continue

            # 1 Policy Feature Card 2       WS-F6K-PFC2     SAD062802AV      3.2    Ok        
            # 1 Cat6k MSFC 2 daughterboard  WS-F6K-MSFC2    SAD062803TX      2.5    Ok   
            # 6 Distributed Forwarding Card WS-F6K-DFC      SAL06261R0A      2.3    Ok     
            # 6 10GBASE-LR Serial 1310nm lo WS-G6488        SAD062201BN      1.1    Ok
            result = r4.match(line)
            if result:
                group = result.groupdict()
                mod = int(group['mod'])
                sub_mod = group['sub_mod']
                model = group['model']
                serial = group['serial']
                hw = group['hw']
                status = group['status']

                submodule_dict = parsed_output\
                    .setdefault('mod', {})\
                    .setdefault(mod, {})\
                    .setdefault('sub_mod', {})\
                    .setdefault(model, {})


                submodule_dict['hw_ver'] = hw
                submodule_dict['status'] = status
                submodule_dict['serial_number'] = serial
                submodule_dict['model'] = model

                continue

        return parsed_output
