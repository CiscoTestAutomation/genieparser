"""show_igmp.py
NXOS revision parser for the following show commands:
    * show ip igmp snooping
    * show ip igmp snooping vlan {vlan}
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ==============================================
#  Schema for show ip igmp snooping
# ==============================================
class ShowIpIgmpSnoopingSchema(MetaParser):
    """Schema for show ip igmp snooping"""

    schema = {
        Optional('global_configuration'): {
            Optional('enabled'): str,
            Optional('v1v2_report_suppression'): str,
            Optional('v3_report_suppression'): str,
            Optional('link_local_groups_suppression'): str,
            Optional('vpc_multicast_optimization'): str,
        },
        'vlans': {
            Any(): { # configuration_vlan_id
                Optional('ip_igmp_snooping'): str,
                Optional('lookup_mode'): str,
                Optional('v1v2_report_suppression'): str,
                Optional('v3_report_suppression'): str,
                Optional('link_local_groups_suppression'): str,
                Optional('igmp_querier'): {
                    Optional('address'): str,
                    Optional('version'): int,
                    Optional('interval'): int,
                    Optional('last_member_query_interval'): int,
                    Optional('robustness'): int,
                },
                Optional('switch_querier'): {
                        Optional('ip_address'): str,
                        Optional('state'):str,
                        Optional('type'): str,
                },  
                Optional('igmp_explicit_tracking'): str,
                Optional('v2_fast_leave'): str,
                Optional('router_ports_count'): int,
                Optional('groups_count'): int,
                Optional('vlan_vpc_function'): str,
                Optional('active_ports'): list,
                Optional('report_flooding'): str,
                Optional('report_flooding_interfaces'): str,
                Optional('group_address_for_proxy_leaves'): str,

            },
        },
    }

# ==============================================
#  Parser for show ip igmp snooping
# ==============================================
class ShowIpIgmpSnooping(ShowIpIgmpSnoopingSchema):
    """Parser for show ip igmp snooping"""

    cli_command = ['show ip igmp snooping vlan {vlan}', 'show ip igmp snooping']
    exclude = [
        'igmp_explicit_tracking']

    def cli(self, vlan='', output=None):
        if output is None:
            if vlan:
                output = self.device.execute(self.cli_command[0].format(vlan=vlan))
            else:
                output = self.device.execute(self.cli_command[1])

        # initial variables
        ret_dict = {}

        # Global IGMP Snooping Information:
        #  IGMP Snooping enabled
        p1 = re.compile(r'^\s*IGMP +Snooping +(?P<enabled>\w+)$')

        #  IGMPv1/v2 Report Suppression enabled
        #  IGMPv1/v2 Report Suppression enabled
        p2 = re.compile(r'^\s*IGMPv1\/v2 +Report +Suppression +(?P<v1v2_report_suppression_enabled>\w+)$')

        #  IGMPv3 Report Suppression disabled
        p3 = re.compile(r'^\s*IGMPv3 +Report +Suppression +(?P<v3_report_suppression_enabled>\w+)$')

        #  Link Local Groups Suppression enabled
        p4 = re.compile(r'^\s*Link +Local +Groups +Suppression +(?P<link_local_group_suppression_enabled>\w+)$')

        #  VPC Multicast optimization disabled
        p5 = re.compile(r'^\s*VPC +Multicast +optimization +(?P<vpc_multicast_optimization_enabled>\w+)$')

        # IGMP Snooping information for vlan 1
        p6 = re.compile(r'^\s*IGMP +Snooping +information +for +vlan +(?P<vlan_id>\d+)$')

        #  IGMP snooping enabled
        p7 = re.compile(r'^\s*IGMP +snooping +(?P<ip_igmp_snooping>\w+)$')

        #  Lookup mode: IP
        p8 = re.compile(r'^\s*Lookup +mode: +(?P<lookup_mode>\w+)$')

        #  IGMP querier none
        #  IGMP querier present, address: 10.51.1.1, version: 2, i/f Vlan100
        p9 = re.compile(r'^\s*IGMP +querier +(?P<igmp_querier>\S+)'
            r'(, +address: +(?P<address>\S+))?'
            r'(, +version: +(?P<version>\d))?'
            r'(, +i\/f +(?P<vlan>\w+))?$')
        
        # Querier interval: 125 secs
        p9_1 = re.compile(r'^\s*Querier +interval: +(?P<querier_interval>\d+) +secs$')

        # Querier last member query interval: 1 secs
        p9_2 = re.compile(r'^\s*Querier +last +member +query +interval: +(?P<querier_last_member_query_interval>\d+) +secs$')

        # Querier robustness: 2
        p9_3 = re.compile(r'^\s*Querier +robustness: +(?P<querier_robustness>\d+)$')

        # Switch-querier disabled
        # Switch-querier enabled, address XXX.XXX.XXX.XXX, currently running
        # Switch-querier enabled, address 1.2.3.200, currently not running
        # Switch-querier enabled, address 1.2.3.200, currently running
        p10 = re.compile(r'^\s*Switch\-querier +(?P<type>\S+)(, +address +(?P<ip_address>(\S+)), +currently +(?P<state>[\s\w]+))?$')

        #  IGMP Explicit tracking enabled
        p11 = re.compile(r'^\s*IGMP +Explicit +tracking +(?P<igmp_explicit_tracking>\w+)$')

        #  IGMPv2 Fast leave disabled
        p12 = re.compile(r'^\s*IGMPv2 +Fast +leave +(?P<v2_fast_leave>\w+)$')

        #  Number of router-ports: 1
        p13 = re.compile(r'^\s*Number +of +router\-ports: +(?P<router_ports_count>\d+)$')

        #  Number of groups: 0
        p14 = re.compile(r'^\s*Number +of +groups: +(?P<groups_count>\d+)$')

        #  VLAN vPC function enabled
        p14_1 = re.compile(r'^\s*VLAN +vPC +function +(?P<vlan_vpc_function>\w+)$')

        #  Active ports:
        #    Po20        Po30
        p15_1 = re.compile(r'^(?P<space>\s{4})(?P<active_ports>[\w\s]+)$')

        #  Report Flooding: Disabled
        p16 = re.compile(r'^\s*Report +Flooding: +(?P<report_flooding>\w+)$')

        #  Interfaces for Report Flooding: n/a
        p17 = re.compile(r'^\s*Interfaces +for +Report +Flooding: +(?P<report_flooding_interfaces>\S+)$')

        #  Use Group Address for Proxy Leaves: no
        p18 = re.compile(r'^\s*Use +Group +Address +for +Proxy +Leaves: +(?P<group_address_for_proxy_leaves>\S+)$')

        for line in output.splitlines():
            line = line.rstrip()

            # Global IGMP Snooping Information:
            #  IGMP Snooping enabled
            m = p1.match(line)
            if m:
                ret_dict.setdefault('global_configuration', {})
                ret_dict['global_configuration']['enabled'] = m.groupdict()['enabled']
                continue

            #  IGMPv1/v2 Report Suppression enabled
            #  IGMPv1/v2 Report Suppression enabled
            m = p2.match(line)
            if m:
                v1v2_report_suppression = m.groupdict()['v1v2_report_suppression_enabled']
                if v1v2_report_suppression:
                    ret_dict.setdefault('global_configuration', {})['v1v2_report_suppression'] = v1v2_report_suppression
                continue

            #  IGMPv3 Report Suppression disabled
            m = p3.match(line)
            if m:
                v3_report_suppression = m.groupdict()['v3_report_suppression_enabled']
                if v3_report_suppression:
                    ret_dict.setdefault('global_configuration', {})['v3_report_suppression'] = v3_report_suppression
                continue

            #  Link Local Groups Suppression enabled
            m = p4.match(line)
            if m:
                link_local_group_suppression_enabled = m.groupdict()['link_local_group_suppression_enabled']
                if link_local_group_suppression_enabled:
                    ret_dict.setdefault('global_configuration', {})['link_local_groups_suppression'] = link_local_group_suppression_enabled
                continue

            #  VPC Multicast optimization disabled
            m = p5.match(line)
            if m:
                ret_dict.setdefault('global_configuration', {})
                ret_dict['global_configuration']['vpc_multicast_optimization'] = m.groupdict()['vpc_multicast_optimization_enabled']
                continue

            # IGMP Snooping information for vlan 1
            m = p6.match(line)
            if m:
                configuration_vlan_id = m.groupdict()['vlan_id']
                vlans_dict = ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                if v1v2_report_suppression:
                    vlans_dict['v1v2_report_suppression'] = v1v2_report_suppression 
                if link_local_group_suppression_enabled:
                    vlans_dict['link_local_groups_suppression'] = link_local_group_suppression_enabled
                if v3_report_suppression:
                    vlans_dict['v3_report_suppression'] = v3_report_suppression
                continue

            #  IGMP snooping enabled
            m = p7.match(line)
            if m:
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['ip_igmp_snooping'] = m.groupdict()['ip_igmp_snooping']
                continue

            #  Lookup mode: IP
            m = p8.match(line)
            if m:
                ret_dict['vlans'][configuration_vlan_id]['lookup_mode'] = m.groupdict()['lookup_mode'].lower()
                continue

            #  IGMP querier none
            #  IGMP querier present, address: 10.51.1.1, version: 2, i/f Vlan100
            m = p9.match(line)
            if m:
                group = m.groupdict()
                igmp_querier = group['igmp_querier']
                if 'none' not in igmp_querier.lower():
                    vlan_querier = ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {}).setdefault('igmp_querier', {})
                    
                    if group['address']:
                        vlan_querier['address'] = group['address']
                    if group['version']:
                        vlan_querier['version'] = int(group['version'])

                continue

            # Querier interval: 125 secs
            m = p9_1.match(line)
            if m:
                querier_interval = m.groupdict()['querier_interval']
                
                if igmp_querier and 'none' not in igmp_querier.lower():
                    vlan_igmp_querier = ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {}).setdefault('igmp_querier', {})
                    vlan_igmp_querier['interval'] = int(querier_interval)
                continue

            # Querier last member query interval: 1 secs
            m = p9_2.match(line)
            if m:
                querier_last_member_query_interval = m.groupdict()['querier_last_member_query_interval']
                
                if igmp_querier and 'none' not in igmp_querier.lower():
                    vlan_igmp_querier = ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {}).setdefault('igmp_querier', {})
                    vlan_igmp_querier['last_member_query_interval'] = int(querier_last_member_query_interval)
                continue

            # Querier robustness: 2
            m = p9_3.match(line)
            if m:
                querier_robustness = m.groupdict()['querier_robustness']
                
                if igmp_querier and 'none' not in igmp_querier.lower():
                    vlan_igmp_querier = ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {}).setdefault('igmp_querier', {})
                    vlan_igmp_querier['robustness'] = int(querier_robustness)
                continue

            # Switch-querier disabled
            # Switch-querier enabled, address XXX.XXX.XXX.XXX, currently running
            # Switch-querier enabled, address 1.2.3.200, currently not running
            # Switch-querier enabled, address 1.2.3.200, currently running
            p10 = re.compile(r'^\s*Switch\-querier +(?P<type>\S+)(, +address +(?P<ip_address>(\S+)), +currently +(?P<state>[\s\w]+))?$')
            m = p10.match(line)
            if m:
                switch_querier = {}
                group = m.groupdict()
                switch_querier['type'] = group.get('type')
                ip_address = group.get('ip_address')
                state = group.get('state')
                if ip_address:
                    switch_querier['ip_address'] = ip_address
                if state:
                    switch_querier['state'] = state

                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})['switch_querier'] = switch_querier
                continue

            #  IGMP Explicit tracking enabled
            m = p11.match(line)
            if m:
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['igmp_explicit_tracking'] = m.groupdict()['igmp_explicit_tracking']
                continue

            #  IGMPv2 Fast leave disabled
            m = p12.match(line)
            if m:
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['v2_fast_leave'] = m.groupdict()['v2_fast_leave']
                continue

            #  Number of router-ports: 1
            m = p13.match(line)
            if m:
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['router_ports_count'] = int(m.groupdict()['router_ports_count'])
                continue

            #  Number of groups: 0
            m = p14.match(line)
            if m:
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['groups_count'] = int(m.groupdict()['groups_count'])
                continue

            #  VLAN vPC function enabled
            m = p14_1.match(line)
            if m:
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['vlan_vpc_function'] = m.groupdict()['vlan_vpc_function']
                continue

            #  Active ports:
            #    Po20        Po30
            m = p15_1.match(line)
            if m:
                active_ports = m.groupdict()['active_ports'].split()
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['active_ports'] = active_ports
                continue

            #  Report Flooding: Disabled
            m = p16.match(line)
            if m:
                report_flooding = m.groupdict()['report_flooding'].lower()
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['report_flooding'] = report_flooding
                continue

            #  Interfaces for Report Flooding: n/a
            m = p17.match(line)
            if m:
                report_flooding_interfaces = m.groupdict()['report_flooding_interfaces']
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['report_flooding_interfaces'] = report_flooding_interfaces
                continue

            #  Use Group Address for Proxy Leaves: no
            m = p18.match(line)
            if m:
                group_address_for_proxy_leaves = m.groupdict()['group_address_for_proxy_leaves']
                ret_dict.setdefault('vlans', {}).setdefault(configuration_vlan_id, {})
                ret_dict['vlans'][configuration_vlan_id]['group_address_for_proxy_leaves'] = group_address_for_proxy_leaves
                continue

        return ret_dict