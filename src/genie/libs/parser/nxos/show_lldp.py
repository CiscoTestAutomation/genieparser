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
    """parser for show lldp all"""
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
                                                          'dcbx'] == 'Y' else \
                    False

                continue

        return parsed_dict


# ==============================
# Schema for 'show lldp timers'
# ==============================
class ShowLldpTimersSchema(MetaParser):
    """Schema for show lldp timers"""
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

        '''
         LLDP Timers:
        
             Holdtime in seconds: 120
             Reinit-time in seconds: 2
             Transmit interval in seconds: 30
         '''
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
    """Schema for show lldp tlv-select"""
    schema = {'suppress_tlv_advertisement': {
        'port_description': bool,
        'system_name': bool,
        'system_description': bool,
        'system_capabilities': bool,
        'management_address': bool,
        'port_vlan': bool,
        'dcbxp': bool,
        # not sure about this one, what if there're more properties from output?
        # Any(): bool
    }
    }


class ShowLldpTlvSelect(ShowLldpTlvSelectSchema):
    """parser for show lldp tlv-select"""
    cli_command = 'show lldp tlv-select'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init return dictionary
        parsed_dict = {}
        mgmt_set = {'management_address_v4', 'management_address_v6'}

        #    management-address-v4
        #    management-address-v6
        #    port-description
        #    port-vlan
        #    power-management
        #    system-capabilities
        #    system-description
        #    system-name
        #    dcbxp
        for line in out.splitlines():
            line = line.strip().replace('-', '_')
            if not line:
                continue
            sub_dict = parsed_dict.setdefault('suppress_tlv_advertisement', {
                'port_description': True,
                'system_name': True,
                'system_description': True,
                'system_capabilities': True,
                'management_address': True,
                'port_vlan': True,
                'dcbxp': True
            })

            if line in sub_dict.keys():
                sub_dict[line] = False
            elif line in mgmt_set:
                sub_dict['management_address'] = False

        return parsed_dict


# # =================================
# # schema for 'show lldp neighbors detail'
# # =================================
# class ShowLldpNeighborsDetailSchema(MetaParser):
#     pass
#
#
# class ShowLldpNeighborsDetail(ShowLldpNeighborsDetailSchema):
#     pass


# =================================
# schema for 'show lldp traffic'
# =================================
class ShowLldpTrafficSchema(MetaParser):
    """Schema for show lldp traffic"""
    schema = {
        "frame_in": int,  # Total frames received: 209
        "frame_out": int,  # Total frames transmitted: 349
        "frame_error_in": int,  # Total frames received in error: 0
        "frame_discard": int,  # Total frames discarded: 0
        'tlv_unknown': int,  # Total unrecognized TLVs: 0
        'entries_aged_out': int  # Total entries aged: 0
    }


class ShowLldpTraffic(ShowLldpTrafficSchema):
    """parser ofr show lldp traffic"""
    cli_command = 'show lldp traffic'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init return dictionary
        parsed_dict = {}

        #     LLDP traffic statistics: 
        #
        #         Total frames transmitted: 349
        #         Total entries aged: 0
        #         Total frames received: 209
        #         Total frames received in error: 0
        #         Total frames discarded: 0
        #         Total unrecognized TLVs: 0
        p1 = re.compile(r'^Total +(?P<pattern>[\w\s]+): +(?P<value>\d+)$')
        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                traffic = m.groupdict()
                traffic_key = traffic['pattern']
                traffic_value = int(traffic['value'])
                if re.search(r'frames +transmitted', traffic_key):
                    parsed_dict['frame_out'] = traffic_value
                elif re.search(r'entries +aged', traffic_key):
                    parsed_dict['entries_aged_out'] = traffic_value
                elif re.search(r'frames +received$', traffic_key):
                    parsed_dict['frame_in'] = traffic_value
                elif re.search(r'frames +received +in +error', traffic_key):
                    parsed_dict['frame_error_in'] = traffic_value
                elif re.search(r'frames +discarded', traffic_key):
                    parsed_dict['frame_discard'] = traffic_value
                elif re.search(r'unrecognized +TLVs', traffic_key):
                    parsed_dict['tlv_unknown'] = traffic_value
                else:
                    continue
                continue
        return parsed_dict
