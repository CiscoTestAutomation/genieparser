''' show_vtemplate.py

IOSXE parsers for the following show commands:

    * 'show vtemplate'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use
from genie.libs.parser.utils.common import Common


class ShowVtemplateSchema(MetaParser):
    """Schema for 'show vtemplate' """

    schema = {
        'virtual_access_subinterface_creation': str, 
        'vt1': {
            'active_interface': int, 
            'active_sub_interface': int, 
            'sub_interface_capable': str, 
            'interface_type': str,
        }, 
        'usage_summary': {
            'current_serial_in_use': {
                'interface': int, 
                'sub_interface': int,
            }, 
            'current_serial_free': {
                'interface': int, 
                'sub_interface': int, 
            }, 
            'current_ether_in_use': {
                'interface': int, 
                'sub_interface': int,
            }, 
            'current_ether_free': {
                'interface': int, 
                'sub_interface': int,
            }, 
            'current_tunnel_in_use': {
                'interface': int, 
                'sub_interface': int,
            }, 
            'current_tunnel_free': {
                'interface': int, 
                'sub_interface': int,
            }, 
            'current_vpn_in_use': {
                'interface': int, 
                'sub_interface': int,
            }, 
            'current_vpn_free': {
                'interface': int, 
                'sub_interface': int,
            }, 
            'total': {
                'interface': int,
                'sub_interface': int,
            }, 
            'cumulative_created': {
                'interface': int,
                'sub_interface': int,
            }, 
            'cumulative_freed': {
                'interface': int, 
                'sub_interface': int,
            }, 
            'base_virtual_access_interfaces': int, 
            'total_create_or_clone_requests': int, 
            'cancelled_create_or_clone_requests': int, 
            'cumulative_create_request_waiting_for_sso_resources': int,
            'current_request_queue_size': int,
            'current_free_pending': int,
            'current_recycle_pending': int,
            'current_ordered_recycle_pending': int,
            'maximum_request_duration_in_milliseconds': int,
            'average_request_duration_in_milliseconds': int,
            'last_request_duration_in_milliseconds': int,
            'maximum_processing_duration_in_milliseconds': int, 
            'average_processing_duration_in_milliseconds': int, 
            'last_processing_duration_in_milliseconds': int
        }
    }


class ShowVtemplate(ShowVtemplateSchema):
    """
    Parser for 'show vtemplate'
    """

    cli_command = 'show vtemplate'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        # initial return dictionary
        ret_dict = {}

        # Virtual access subinterface creation is globally enabled
        p1 = re.compile(r'^(?P<var>[Vv]i\w+\s+\w+\s+\w+\s+\w+)\s+\w+\s+(?P<val>.+)$')

        # Vt1            0           11   Yes   Serial 
        p2 = re.compile(r'^(?P<var>[Vv]\w+)\s+(?P<val1>\d+)\s+(?P<val2>\d+)\s+(?P<val3>\w+)\s+(?P<val4>\w+)$')

        # Usage Summary
        p3 = re.compile(r'^(?P<var>[Uu]\w+\s+\w+)$')
                
        # Current Serial  in use                2             11
        # Current Ether   in use                0              0
        # Current Tunnel  in use                0              0 
        # Current VPN  in use                0              0
        p4 = re.compile(r'^(?P<var>\w+\s+\w+\s+\w+\s+\w+)\s+(?P<val1>\d+)\s+(?P<val2>\d+)$')

        # Current Serial  free                  0              1
        # Current Ether   free                  0              0
        # Current Tunnel  free                  0              0
        # Current VPN  free                  0              0
        p5 = re.compile(r'^(?P<var>[Cc]\w+\s+\w+\s+\w+)\s+(?P<val1>\d+)\s+(?P<val2>\d+)$')

        # Total                                 2             12
        p6 = re.compile(r'^(?P<var>[Tt]\w+)\s+(?P<val1>\d+)\s+(?P<val2>\d+)$')

        # Cumulative created                    5             69
        # Cumulative freed                      0             58
        p7 = re.compile(r'^(?P<var>[Cc]\w+\s+\w+)\s+(?P<val1>\d+)\s+(?P<val2>\d+)$')

        # Base virtual access interfaces: 2
        # Total create or clone requests: 43
        # Cancelled create or clone requests: 0
        # Cumulative create request waiting for sso resources: 0
        # Current request queue size: 0
        # Current free pending: 0
        # Current recycle pending: 0
        # Current ordered recycle pending: 0
        p8 = re.compile(r'^(?P<var>\w+.+)\s*:\s*(?P<val1>\d+)$')

        # Maximum request duration: 26 msec
        # Average request duration: 5 msec
        # Last request duration: 3 msec
        # Maximum processing duration: 9 msec
        # Average processing duration: 4 msec
        # Last processing duration: 3 msec
        p9 = re.compile(r'^(?P<var>\w+\s+\w+\s+[Dd]\w+)\s*:\s*(?P<val1>\d+)\s+\w+$')

        for lines in out.splitlines():
            line = lines.strip()

            # Virtual access subinterface creation is globally enabled
            m = p1.match(line)
            if m:
                var = m.groupdict()['var'].lower().replace(" ","_")
                ret_dict[var] = m.groupdict()['val'].lower().replace(" ","_")
                continue
            
            # Vt1            0           11   Yes   Serial
            m = p2.match(line)
            if m:
                var = m.groupdict()['var'].lower()
                ret_dict.setdefault(var,{})
                ret_dict[var]['active_interface'] = int(m.groupdict()['val1'])
                ret_dict[var]['active_sub_interface'] = int(m.groupdict()['val2'])
                ret_dict[var]['sub_interface_capable'] = m.groupdict()['val3'].lower()
                ret_dict[var]['interface_type'] = m.groupdict()['val4'].lower()
                continue
            
            # Usage Summary
            m = p3.match(line)
            if m:
                use_summ = m.groupdict()['var'].lower().replace(" ","_")
                ret_dict.setdefault(use_summ,{})
                # temp_dict = ret_dict.setdefault(use_summ,{})
                continue 
            
            # Current Serial  in use                2             11
            # Current Ether   in use                0              0
            # Current Tunnel  in use                0              0 
            # Current VPN  in use                0              0
            m = p4.match(line)
            if m:
                var = " ".join(m.groupdict()['var'].split()).lower().replace(" ","_")
                ret_dict[use_summ].setdefault(var,{})
                ret_dict[use_summ][var]['interface'] = int(m.groupdict()['val1'])
                ret_dict[use_summ][var]['sub_interface'] = int(m.groupdict()['val2'])
                continue

            # Current Serial  free                  0              1
            # Current Ether   free                  0              0
            # Current Tunnel  free                  0              0
            # Current VPN  free                  0              0    
            m = p5.match(line)
            if m:
                var = " ".join(m.groupdict()['var'].split()).lower().replace(" ","_")
                ret_dict[use_summ].setdefault(var,{})
                ret_dict[use_summ][var]['interface'] = int(m.groupdict()['val1'])
                ret_dict[use_summ][var]['sub_interface'] = int(m.groupdict()['val2'])
                continue
            
            # Total
            m = p6.match(line)
            if m:
                var = m.groupdict()['var'].lower().replace(" ","_")
                ret_dict[use_summ].setdefault(var,{})
                ret_dict[use_summ][var]['interface'] = int(m.groupdict()['val1'])
                ret_dict[use_summ][var]['sub_interface'] = int(m.groupdict()['val2'])
                continue
            
            # Base virtual access interfaces: 2
            # Total create or clone requests: 43
            # Cancelled create or clone requests: 0
            # Cumulative create request waiting for sso resources: 0
            # Current request queue size: 0
            # Current free pending: 0
            # Current recycle pending: 0
            # Current ordered recycle pending: 0
            m = p7.match(line)
            if m:
                var = m.groupdict()['var'].lower().replace(" ","_")
                ret_dict[use_summ].setdefault(var,{})
                ret_dict[use_summ][var]['interface'] = int(m.groupdict()['val1'])
                ret_dict[use_summ][var]['sub_interface'] = int(m.groupdict()['val2'])
                continue
            
            # Base virtual access interfaces: 2
            # Total create or clone requests: 43
            # Cancelled create or clone requests: 0
            # Cumulative create request waiting for sso resources: 0
            # Current request queue size: 0
            # Current free pending: 0
            # Current recycle pending: 0
            # Current ordered recycle pending: 0
            m = p8.match(line)
            if m:
                var = m.groupdict()['var'].lower().replace(" ","_")
                ret_dict[use_summ].setdefault(var,{})
                ret_dict[use_summ][var] = int(m.groupdict()['val1'])
                continue
            
            # Maximum request duration: 26 msec
            # Average request duration: 5 msec
            # Last request duration: 3 msec
            # Maximum processing duration: 9 msec
            # Average processing duration: 4 msec
            # Last processing duration: 3 msec
            m = p9.match(line)
            if m:
                var1 = m.groupdict()['var'].lower().replace(" ","_")
                var = var1 + '_in_milliseconds'
                ret_dict[use_summ].setdefault(var,{})
                ret_dict[use_summ][var] = int(m.groupdict()['val1'])
                continue
        
        return ret_dict
