"""show_spanning_tree.py
    supported commands:
        *  show spanning tree summary totals
"""
import re
import logging

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional, Any

# import parser utils
from genie.libs.parser.utils.common import Common

# ===============================================================
# Schema for 'show spanning-tree summary totals' for 9500 device
# ===============================================================
class ShowSpanningTreeSummaryTotalsSchema(MetaParser):
    """
        Schema for show spanning-tree summary totals
    """
    schema = {
        'mode': str,
        'root_bridge': str,
        'extended_system_id': str,
        'portfast': str,
        'portfast_edge_bpdu_guard': str,
        'portfast_edge_bpdu_filter': str,
        'loopguard': str,
        'pvst_simulation': str,
        'bridge_assurance': str,
        'etherchannel_misconfig_guard': str,
        'uplinkfast': str,
        'backbonefast': str,
        'pathcost_method': str,
        'spanning_tree_name': {
            Any(): { 
                'blocking': int,
                'listening': int,
                'learning': int,
                'forwarding': int,
                'stp_active': int
            }
        }
    }

# ===============================================================
# Parser for 'show spanning-tree summary totals' for 9500 device
# ===============================================================
class ShowSpanningTreeSummaryTotals(ShowSpanningTreeSummaryTotalsSchema):
    """
        Parser for show spanning-tree summary totals
    """

    cli_command = 'show spanning-tree summary totals'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Switch is in rapid-pvst mode
        p1 = re.compile(r'^Switch is in (?P<mode>\S+) mode$')

        # Root bridge for: none
        p2 = re.compile(r'^Root bridge for:\s+(?P<root_bridge>.+)$')

        # Extended system ID                      is enabled
        p3 = re.compile(r'^Extended system ID\s+is\s+(?P<extended_system_id>\S+)$')

        # Portfast Default                        is disabled
        p4 = re.compile(r'^Portfast Default\s+is\s+(?P<portfast>\S+)$')

        # Portfast Edge BPDU Guard Default        is disabled
        p5 = re.compile(r'^Portfast Edge BPDU Guard Default\s+is\s+(?P<portfast_edge_bpdu_guard>\S+)$')

        # Portfast Edge BPDU Filter Default       is disabled
        p6 = re.compile(r'^^Portfast Edge BPDU Filter Default\s+is\s+(?P<portfast_edge_bpdu_filter>\S+)$')

        # Loopguard Default                       is disabled
        p7 = re.compile(r'^Loopguard Default\s+is\s+(?P<loopguard>\S+)$')

        # PVST Simulation Default                 is enabled but inactive in rapid-pvst mode
        p8 = re.compile(r'^PVST Simulation Default\s+is\s+(?P<pvst_simulation>\S+ but inactive in rapid-pvst mode)$')

        # Bridge Assurance                        is enabled
        p9 = re.compile(r'^Bridge Assurance\s+is\s+(?P<bridge_assurance>\S+)$')

        # EtherChannel misconfig guard            is enabled
        p10 = re.compile(r'^EtherChannel misconfig guard\s+is\s+(?P<etherchannel_misconfig_guard>\S+)$')

        # UplinkFast                              is disabled
        p11 = re.compile(r'^UplinkFast\s+is\s+(?P<uplinkfast>\S+)$')

        # BackboneFast                            is disabled
        p12 = re.compile(r'^BackboneFast\s+is\s+(?P<backbonefast>\S+)$')

        # Configured Pathcost method used is long
        p13 = re.compile(r'^Configured Pathcost method used is (?P<pathcost_method>\S+)$')

        # Name                   Blocking Listening Learning Forwarding STP Active
        p14 = re.compile(r'^Name\s+Blocking Listening Learning Forwarding STP Active$')

        # 300 vlans                  300         0        0        600        900
        p15 = re.compile(r'^(?P<spanning_tree_name>[\s\S]+)\s+(?P<blocking>\d+)\s+(?P<listening>\d+)\s+'
            r'(?P<learning>\d+)\s+(?P<forwarding>\d+)\s+(?P<stp_active>\d+)$')
        
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Switch is in rapid-pvst mode
            m = p1.match(line)
            if m:
                ret_dict['mode'] = m.groupdict()['mode']
                continue

            # Root bridge for: none
            m = p2.match(line)
            if m:
                ret_dict['root_bridge'] = m.groupdict()['root_bridge']
                continue

            # Extended system ID                      is enabled
            m = p3.match(line)
            if m:
                ret_dict['extended_system_id'] = m.groupdict()['extended_system_id']
                continue

            # Portfast Default                        is disabled
            m = p4.match(line)
            if m:
                ret_dict['portfast'] = m.groupdict()['portfast']
                continue

            # Portfast Edge BPDU Guard Default        is disabled
            m = p5.match(line)
            if m:
                ret_dict['portfast_edge_bpdu_guard'] = m.groupdict()['portfast_edge_bpdu_guard']
                continue
            
            # Portfast Edge BPDU Filter Default       is disabled
            m = p6.match(line)
            if m:
                ret_dict['portfast_edge_bpdu_filter'] = m.groupdict()['portfast_edge_bpdu_filter']
                continue

            # Loopguard Default                       is disabled
            m = p7.match(line)
            if m:
                ret_dict['loopguard'] = m.groupdict()['loopguard']
                continue
                
            # PVST Simulation Default                 is enabled but inactive in rapid-pvst mode
            m = p8.match(line)
            if m:
                ret_dict['pvst_simulation'] = m.groupdict()['pvst_simulation']
                continue

            # Bridge Assurance                        is enabled
            m = p9.match(line)
            if m:
                ret_dict['bridge_assurance'] = m.groupdict()['bridge_assurance']
                continue
               
            # EtherChannel misconfig guard            is enabled
            m = p10.match(line)
            if m:
                ret_dict['etherchannel_misconfig_guard'] = m.groupdict()['etherchannel_misconfig_guard']
                continue
            
            # UplinkFast                              is disabled
            m = p11.match(line)
            if m:
                ret_dict['uplinkfast'] = m.groupdict()['uplinkfast']
                continue

            # BackboneFast                            is disabled
            m = p12.match(line)
            if m:
                ret_dict['backbonefast'] = m.groupdict()['backbonefast']
                continue

            m = p13.match(line)
            if m:
                ret_dict['pathcost_method'] = m.groupdict()['pathcost_method']
                continue

            # Name                   Blocking Listening Learning Forwarding STP Active
            m = p14.match(line)
            if m:
                spanning_tree_name_dict = ret_dict.setdefault('spanning_tree_name', {})
                continue

            # 300 vlans                  300         0        0        600        900
            m = p15.match(line)
            if m:
                group_dict = m.groupdict()
                span_dict = spanning_tree_name_dict.setdefault(group_dict['spanning_tree_name'].strip(), {})
                span_dict['blocking'] = int(group_dict['blocking'])
                span_dict['listening'] = int(group_dict['listening'])
                span_dict['learning'] = int(group_dict['learning'])
                span_dict['forwarding'] = int(group_dict['forwarding'])
                span_dict['stp_active'] = int(group_dict['stp_active'])
                continue
        
        return ret_dict
