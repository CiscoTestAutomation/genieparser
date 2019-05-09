"""show_lldp.py
    supported commands:
        *show lldp all
        *show lldp timers
        *show lldp tlv-select 
        *show lldp neighbors detail
        *show lldp traffic 
"""
import re

# metaparsers
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional


# ==============================
# Schema for 'show lldp all'
# ==============================
class ShowLldpAllSchema(MetaParser):
    """schema for show lldp all"""
    schema = {
        'interfaces':
            {Any():
                 {'enabled': bool,
                  'tx': bool,
                  'rx': bool,
                  'dcbx': bool
                  },
             },
    }


class ShowLldpAll(ShowLldpAllSchema):
    '''parser for "show lldp all"'''
    cli_command = 'show lldp all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init dictionary
        parsed_dict = {}

        # Interface Information: Eth1/64 Enable (tx/rx/dcbx): Y/Y/Y
        # Interface Information: mgmt0 Enable (tx/rx/dcbx): Y/Y/N  
        p1 = re.compile(
            r'^Interface Information: +(?P<interface>[\w/,]+) +('
            r'?P<enabled>[a-zA-Z]+) +\(tx/rx/dcbx\): +(?P<tx>[YN])/('
            r'?P<rx>[YN])/(?P<dcbx>[YN])$')

        for line in out.splitlines():
            line = line.strip()

            # Interface Information: Eth1/64 Enable (tx/rx/dcbx): Y/Y/Y
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                sub_dict = parsed_dict.setdefault('interfaces', {})
                sub_dict.setdefault(interface, {})
                sub_dict[interface]['enabled'] = True if group[
                                                             'enabled'] == \
                                                         'Enable' else False
                sub_dict[interface]['tx'] = True if group[
                                                        'tx'] == 'Y' else False
                sub_dict[interface]['rx'] = True if group[
                                                        'rx'] == 'Y' else False
                sub_dict[interface]['dcbx'] = True if group[
                                                          'dcbx'] == 'Y' else\
                    False

                continue

        return parsed_dict


# ==============================
# Schema for 'show lldp timers'
# ==============================
class ShowLldpTimersSchema(MetaParser):
    '''Schema for 'show lldp timers''''
    schema = {
        'hold_timer': int,
        'reinit_timer': int,
        'hello_timer': int
    }


class ShowLldpTimers(ShowLldpTimersSchema):
    """parser for show lldp timers"""
    cli_command = 'show lldp timers'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init return dictionary
        parsed_dict = {}

        # LLDP Timers:
        #
        #     Holdtime in seconds: 120
        #     Reinit-time in seconds: 2
        #     Transmit interval in seconds: 30
        p1 = re.compile(r'^(?P<timer>[\w -]+) +in +seconds: +(?P<seconds>\d+)$')
        for line in out.splitlines():
            line = line.strip()

            # Holdtime in seconds: 120
            m = p1.match(line)
            if m:
                timer = m.groupdict()
                timer_name = timer['timer']
                seconds = int(timer['seconds'])
                if timer_name == 'Holdtime':
                    parsed_dict['hold_timer'] = seconds
                elif timer_name == 'Reinit-time':
                    parsed_dict['reinit_timer'] = seconds
                else:
                    parsed_dict['hello_timer'] = seconds
                continue

        return parsed_dict


# =================================
# schema for 'show lldp tlv-select'
# =================================

class ShowLldpTlvSelectSchema(MetaParser):
    '''Schema for 'show lldp tlv-select''''
    schema={

    }
    pass
class ShowLldpTlvSelect(ShowLldpTlvSelectSchema)
    cli_command = 'show lldp tlv-select'

#    management-address-v4
#    management-address-v6
#    port-description
#    port-vlan
#    power-management
#    system-capabilities
#    system-description
#    system-name
#    dcbxp
    pass


# =================================
# schema for 'show lldp neighbors detail'
# =================================
class ShowLldpNeighborsDetailSchema(MetaParser):
    pass

class ShowLldpNeighborsDetail(ShowLldpNeighborsDetailSchema):
    pass

# =================================
# schema for 'show lldp traffic'
# =================================
class ShowLldpTrafficSchema(MetaParser):
    pass

class ShowLldpTraffic(ShowLldpTrafficSchema):
    pass