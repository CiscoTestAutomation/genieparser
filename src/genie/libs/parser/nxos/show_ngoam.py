"""show_ngoam.py

NXOS parsers for the following show commands:
    * show ngoam loop-detection status 
    * show ngoam loop-detection summary

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
from genie.libs.parser.utils.common import Common

# ====================================================================
# Schema for 'show ngoam loop-detection status '
# ====================================================================
class ShowNgoamLoopDetectionStatusSchema(MetaParser):

    """Schema for show ngoam loop-detection status"""
    schema = {
        Optional("error"): str,
        Optional("vlans"): {
            Any(): {
                Any(): {
                    "state": str,
                    "loop_count": int,
                    "created_time": str,
                    "last_cleared": str,
                }
            }
        }
    }
# ====================================================================
# Parser for 'show ngoam loop-detection status '
# ====================================================================    
class ShowNgoamLoopDetectionStatus(ShowNgoamLoopDetectionStatusSchema):

    """Parser for 'show ngoam loop-detection status '"""

    cli_command = 'show ngoam loop-detection status'

    def cli(self, output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return_dict = {}
        #========================================================================================
        # Message that appears when no loop-detection is enabled
        # node01# show ngoam loop-detection summary 
        # ERROR: Loop detection is not enabled
        #========================================================================================
        p0 = re.compile("ERROR: Loop detection is not enabled")

        #========================================================================================
        #101        Eth1/11    RECOVERING   17            Mon Jun 10 02:56:55 2024  Mon Jun 10 02:44:05 2024
        #========================================================================================

        p1 = re.compile("^(?P<vlan_id>\d+)\s+(?P<intf_name>Eth\d+\/\d+(\/d+)?)\s+(?P<state>\S+)\s+(?P<count>\d+)\s+(?P<date>[A-Za-z]{3}\s+[A-Za-z]{3}\s+[0-9]{1,2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}\s+[0-9]{4})\s+(?P<last_cleared>(\S+)|([A-Za-z]{3}\s+[A-Za-z]{3}\s+[0-9]{1,2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}\s+[0-9]{4}))$")


        for line in out.splitlines():

            # ERROR: Loop detection is not enabled
            m = p0.match(line)
            if m:
                return_dict.setdefault('error', {})
                return_dict['error'] = "Loop detection is not enabled"

            #101        Eth1/11    RECOVERING   17            Mon Jun 10 02:56:55 2024  Mon Jun 10 02:44:05 2024
            m = p1.match(line)
            if m: 
                if 'vlans' not in return_dict:
                    return_dict['vlans'] = {}
                match_dict = m.groupdict()
                interface = match_dict['intf_name']
                intf_name = Common.convert_intf_name(intf=interface)
                vlan_id = match_dict['vlan_id']

                data = {intf_name: {
                        'state': match_dict['state'],
                        'loop_count': int(match_dict['count']),
                        'created_time': match_dict['date'],
                        'last_cleared': match_dict['last_cleared']}}
                if vlan_id in return_dict['vlans']:
                    return_dict['vlans'][vlan_id].update(data)
                else:
                    return_dict['vlans'].update({vlan_id: data})

        return return_dict
    
# ====================================================================
# Schema for 'show ngoam loop-detection summary '
# ====================================================================
class ShowNgoamLoopDetectionSummarySchema(MetaParser):    
    """Schema for show ngoam loop-detection summary"""

    schema = {
        "summary": {
            Optional("sld_state"): bool,
            Optional("probe_interval"): int,
            Optional("recovery_interval"): int,
            Optional("vlan_count"): int,
            Optional("port_count"): int,
            Optional("loop_count"): int,
            Optional("ports_blocked_count"): int,
            Optional("vlan_disabled_count"): int,
            Optional("port_disabled_count"): int,
            Optional("sent_probes_count"): int,
            Optional("received_probes_count"): int,
            Optional("next_probe_window_start_date"): str,
            Optional("next_recovery_window_start_date"): str,
            Optional("next_probe_wait_sec"): int,
            Optional("next_recovery_wait_sec"): int,
        }
    }

# ====================================================================
# Parser for 'show ngoam loop-detection summary '
# ====================================================================
class ShowNgoamLoopDetectionSummary(ShowNgoamLoopDetectionSummarySchema):
    """Parser for 'show ngoam loop-detection summary '"""

    cli_command = 'show ngoam loop-detection summary'

    def cli(self, output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return_dict = {}

        # Message that appears when no loop-detection is enabled
        # node01# show ngoam loop-detection summary 
        # ERROR: Loop detection is not enabled
        p0 = re.compile("ERROR: Loop detection is not enabled")

        # Loop detection:enabled
        p1 = re.compile("Loop detection:(?P<sld_state>\S+)")
        
        # Periodic probe interval: 60
        p2 = re.compile("Periodic probe interval: (?P<probe_interval>\d+)")

        # Port recovery interval: 300
        p3 = re.compile("Port recovery interval: (?P<recovery_interval>\d+)")

        # Number of vlans: 0
        p4 = re.compile("Number of vlans: (?P<vlan_count>\d+)")

        # Number of ports: 0
        p5 = re.compile("Number of ports: (?P<port_count>\d+)")

        # Number of loops: 0
        p6 = re.compile("Number of loops: (?P<loop_count>\d+)")

        # Number of ports blocked: 0
        p7 = re.compile("Number of ports blocked: (?P<ports_blocked_count>\d+)")

        # Number of vlans disabled: 0
        p8 = re.compile("Number of vlans disabled: (?P<vlan_disabled_count>\d+)")

        # Number of ports disabled: 0
        p9 = re.compile("Number of ports disabled: (?P<port_disabled_count>\d+)")

        # Total number of probes sent: 187864
        p10 = re.compile("Total number of probes sent: (?P<sent_probes_count>\d+)")

        # Total number of probes received: 908
        p11 = re.compile("Total number of probes received: (?P<received_probes_count>\d+)")
        # Next probe window start: Mon Jun 10 21:35:02 2024 (27 seconds)
        p12 = re.compile(".*?probe.*?(?P<date>[A-Za-z]{3}\s+[A-Za-z]{3}\s+[0-9]{1,2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}\s+[0-9]{4})\s+(\((?P<probe_wait>\d+))\s+seconds\)")

        # Next recovery window start: Mon Jun 10 21:35:52 2024 (77 seconds) 
        p13 = re.compile(".*?recovery.*?(?P<date>[A-Za-z]{3}\s+[A-Za-z]{3}\s+[0-9]{1,2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}\s+[0-9]{4})\s+(\((?P<recovery_wait>\d+)\s+seconds\))")

        for line in out.splitlines():

            # ERROR: Loop detection is not enabled
            m = p0.match(line)
            if m:
                return_dict.setdefault('summary', {})['sld_state'] = False

            # Loop detection:enabled
            m = p1.match(line)
            if m:
                sld_state = m.groupdict()['sld_state']
                if sld_state == 'enabled':
                    return_dict.setdefault('summary', {})['sld_state'] = True

            # Periodic probe interval: 60
            m = p2.match(line)
            if m:
                return_dict['summary']['probe_interval'] = int(m.groupdict()['probe_interval'])
                
            # Port recovery interval: 300
            m = p3.match(line)
            if m:
                return_dict['summary']['recovery_interval'] = int(m.groupdict()['recovery_interval'])

            # Number of vlans: 0
            m = p4.match(line)
            if m:
                return_dict['summary']['vlan_count'] = int(m.groupdict()['vlan_count'])
                
            # Number of ports: 0
            m = p5.match(line)
            if m:
                return_dict['summary']['port_count'] = int(m.groupdict()['port_count'])
            
            # Number of loops: 0
            m = p6.match(line)
            if m:
                return_dict['summary']['loop_count'] = int(m.groupdict()['loop_count'])
            
            # Number of ports blocked: 0
            m = p7.match(line)
            if m:
                return_dict['summary']['ports_blocked_count'] = int(m.groupdict()['ports_blocked_count'])

            # Number of vlans disabled: 0
            m = p8.match(line)
            if m:
                return_dict['summary']['vlan_disabled_count'] = int(m.groupdict()['vlan_disabled_count'])
                
            # Number of ports disabled: 0
            m = p9.match(line)
            if m:
                return_dict['summary']['port_disabled_count'] = int(m.groupdict()['port_disabled_count'])
                
            # Total number of probes sent: 187864
            m = p10.match(line)
            if m:
                return_dict['summary']['sent_probes_count'] = int(m.groupdict()['sent_probes_count'])
                
            # Total number of probes received: 908
            m = p11.match(line)
            if m:
                return_dict['summary']['received_probes_count'] = int(m.groupdict()['received_probes_count'])

            # Next probe window start: Mon Jun 10 21:35:02 2024 (27 seconds)
            m = p12.match(line)
            if m:
                next_probe_date = m.groupdict()['date']
                return_dict['summary']['next_probe_window_start_date'] = next_probe_date
                return_dict['summary']['next_probe_wait_sec'] = int(m.groupdict()['probe_wait'])

            # Next recovery window start: Mon Jun 10 21:35:52 2024 (77 seconds) 
            m = p13.match(line)
            if m:
                next_recovery_date = m.groupdict()['date']
                return_dict['summary']['next_recovery_window_start_date'] = next_recovery_date
                return_dict['summary']['next_recovery_wait_sec'] = int(m.groupdict()['recovery_wait'])

        return return_dict
