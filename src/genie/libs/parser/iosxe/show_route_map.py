''' show_route_map.py

IOSXE parsers for the following show commands:

    * 'show route-map all'
    * 'show route-map {name}'
    
'''

#Python
import re

#MetaParser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowRouteMapAllSchema(MetaParser):
    """
    Schema for 
    * show route-map all
    * show route-map {name}
    """
    schema = {
        Any(): {
            Optional('description'): str,
            'statements': {
                Any(): {
                    'conditions': {
                        Optional('match_med_eq'): int,
                        Optional('match_local_pref_eq'): int,
                        Optional('match_nexthop_in'): list,
                        Optional('match_nexthop_in_v6'): list,
                        Optional('match_level_eq'): str,
                        Optional('match_route_type'): str,
                        Optional('match_community_list'): str,
                        Optional('match_ext_community_list'): str,
                        Optional('match_as_path_list'): str,
                        Optional('match_interface'): str,
                        Optional('match_prefix_list'): str,
                        Optional('match_access_list'): str,
                        Optional('match_as_number_list'): str,
                        Optional('match_prefix_list_v6'): str,
                        Optional('match_tag_list'): str,
                    },
                    'actions': {
                        Optional('set_route_origin'): str,
                        Optional('set_distance'): int,
                        Optional('set_local_pref'): int,
                        Optional('set_next_hop'): list,
                        Optional('set_next_hop_v6'): list,
                        Optional('set_next_hop_self'): bool,
                        Optional('set_as_path_prepend'): str,
                        Optional('set_as_path_group'): list,
                        Optional('set_as_path_prepend_repeat_n'): int,
                        Optional('set_community'): str,
                        Optional('set_community_additive'): bool,
                        Optional('set_community_no_advertise'): bool,
                        Optional('set_community_no_export'): bool,
                        Optional('set_community_delete'): str,
                        Optional('set_ext_community_rt'): list,
                        Optional('set_ext_community_soo'): str,
                        Optional('set_ext_community_vpn'): str,
                        Optional('set_ext_community_rt_additive'): bool,
                        Optional('set_ext_community_delete'): str,
                        Optional('set_level'): str,
                        Optional('set_weight'): int,
                        Optional('set_metric'): int,
                        Optional('set_ospf_metric_type'): str,
                        Optional('set_metric_type'): str,
                        'route_disposition': str,
                        Optional('set_tag'): str
                    },
                    Optional('policy_routing_matches'): {
                        'packets': int,
                        'bytes': int,
                    }
                },
            },
        },
    }


class ShowRouteMapAll(ShowRouteMapAllSchema):
    """
    Parser for 
    * show route-map all
    * show route-map {name}
    """
    cli_command = ['show route-map all',
                   'show route-map {name}']

    def cli(self, name="", output=None):
        if output is None:
            if name:
                cmd = self.cli_command[1].format(name=name) 
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        route_map_dict = {}
        clause_type = ''

        # route-map test, permit, sequence 10
        p1 =  re.compile(r'^\s*route-map *(?P<name>\S+)\,'
                         r' *(?P<route_disposition>[\w\W]+)\, *sequence'
                         r' *(?P<statements>[0-9]+)$')

        # Match clauses:
        # Set clauses:
        p1_2 = re.compile(r'^\s*(?P<clause_type>[a-zA-Z]+) +clauses:$')

        # description <description>
        p1_1 = re.compile(r'^\s*description +(?P<description>.+)$')

        # as-path (as-path filter): aspathlist1
        p2 = re.compile(r'^\s*as-path *\(as-path *filter\):'
                        r' *(?P<match_as_path_list>[a-z0-9]+)$')

        # as-number (as-path-list filter): List1, List2
        p2_1 = re.compile(r'^\s*as-number *\(as-path-list *filter\)\:'
                          r' *(?P<match_as_number_list>[\w\W\,\s]+)$')

        # ip address prefix-lists: test-test
        p3 = re.compile(r'^\s*ip *address *prefix-lists:'
                        r' *(?P<match_prefix_list>.+)$')
        
        #ip address (access-lists): pbr-acl
        p3_1 = re.compile(r'^\s*ip\saddress\s\(access\-lists\)\:\s(?P<match_access_list>.+)')
       
        #ip next-hop prefix-lists: test
        #ip next-hop (access-lists): 1
        p4 =  re.compile(r'^\s*ip *next-hop *(?P<match_type>[a-zA-Z0-9\S\(\)]+):'
                         r' *(?P<match_nexthop_in>.+)$')
        
        # ipv6 address prefix-list test-test
        p5 = re.compile(r'^\s*ipv6 *address *prefix-list(?:s\:)?'
                        r' *(?P<match_prefix_list_v6>.+)$')

        # ipv6 next-hop prefix-list test2
        p6 = re.compile(r'^\s*ipv6 *next-hop *prefix-list(?:s\:)?'
                        r' *(?P<match_nexthop_in_v6>.+)$')

        #interface GigabitEthernet1
        p7 = re.compile(r'^\s*interface *(?P<match_interface>[a-zA-Z0-9\/\s]+)$')

        #metric 100
        p8 = re.compile(r'^\s*metric *(?P<match_med_eq>[0-9\-]+)$')

        #community  (community-list filter): test3
        p10 = re.compile(r'^\s*community *\(community-list *filter\):'
                         r' *(?P<match_community_list>.+)$')

        #route-type: level-1 level-2
        p11 = re.compile(r'^\s*route-type *(?P<match_level_eq>[a-z0-9\-\s]+)$')

        # extcommunity  (extcommunity-list filter): testing
        p11_1 = re.compile(r'^\s*extcommunity *\(extcommunity-list *filter\):'
                           r' *(?P<match_ext_community_list>.+)$')

        # ip next-hop 10.64.4.4
        # ip next-hop 10.4.1.1 10.16.2.2
        p12 = re.compile(r'^\s*ip *next-hop *(?P<set_next_hop>[0-9\.\s]+)$')

        # ip next-hop self
        p12_1 = re.compile(r'^\s*ip *next-hop self$')

        #ip default next-hop 100.0.0.2                                          
        p12_2 = re.compile(r'^\s*ip\s(?P<match_type>\S+)\snext\-hop\s(?P<set_next_hop>.+)$')
      
        # ipv6 next-hop 2001:db8:1::1
        # ipv6 next-hop 2001:DB8:1::1 2001:DB8:2::1
        p13 = re.compile(r'^\s*ipv6 *next-hop *(?P<set_next_hop_v6>[a-zA-Z0-9\:\s]+)$')

        #tag 30
        p14 = re.compile(r'^\s*tag *(?P<set_tag>[0-9]+)$')

        # weight 50
        p14_1 = re.compile(r'^\s*weight *(?P<set_weight>[0-9]+)$')

        #metric 20
        p15 = re.compile(r'^\s*metric *(?P<set_med>[0-9]+)$')

        #distance: 10
        p15_1 = re.compile(r'^\s*distance: *(?P<set_distance>[0-9]+)$')

        # metric-type external ---- > set_metric_type
        # metric-type type-1   ---- > set_ospf_metric_type
        p16 = re.compile(r'^\s*metric-type *(?P<set_ospf_metric_type>[0-9a-z\-]+)$')

        #level level-1
        p17 = re.compile(r'^\s*level *(?P<set_level>[a-z0-9\-]+)$')

        #local-preference 111
        p18 = re.compile(r'^\s*local-preference *(?P<match_local_pref_eq>[0-9]+)$')

        #origin igp
        p19 = re.compile(r'^\s*origin *(?P<set_route_origin>[a-z]+)$')

        # comm-list test delete
        p20 = re.compile(r'^\s*comm-list *(?P<set_community_delete>[a-z]+)'
                         r' *delete$')

        #community 100:1 no-export no-advertise additive
        p20_1 = re.compile(r'^\s*community *(?P<set_community>[0-9\:]+)(?:'
                           r' *(?P<set_community_no_export>(no-export)))?(?:'
                           r' *(?P<set_community_no_advertise>(no-advertise)))?(?:'
                           r' *(?P<set_community_additive>(additive)))?$')

        #as-path prepend 10 10 10
        p21 = re.compile(r'^\s*as-path *prepend'
                         r' *(?P<set_as_path_prepend>[0-9\s]+)$')

        #extcomm-list cisco delete
        p22 = re.compile(r'^\s*extcomm-list'
                         r' *(?P<set_ext_community_delete>[a-z]+) *delete$')

        # extended community RT:100:10 RT:100:100 RT:200:200 additive
        p23 = re.compile(r'^\s*extended community'
                         r'(?P<set_ext_community_rt>( RT\:[0-9]+\:[0-9]+)*)(\s)?'
                         r'((?P<set_ext_community_rt_additive>(additive))?)')

        # extended community VD:100:100
        p24 = re.compile(r'^\s*extended *community'
                         r' *VD:(?P<set_ext_community_vpn>[0-9\:]+)$')

        # extended community SoO:100:10
        p25 = re.compile(r'^\s*extended *community'
                         r' *SoO:(?P<set_ext_community_soo>[0-9\:]+)$')

        # Policy routing matches: 0 packets, 0 bytes
        p26 = re.compile(r'^\s*Policy\s+routing\s+matches:\s+(?P<packets>\d+)\spackets,\s+(?P<bytes>\d+)\s+bytes')

        for line in output.splitlines():
            line = line.rstrip()

            # route-map test, permit, sequence 10
            m = p1.match(line)
            if m:
                name = str(m.groupdict()['name'])
                route_disposition = str(m.groupdict()['route_disposition'])
                statements = str(m.groupdict()['statements'])

                if name not in route_map_dict:
                    route_map_dict[name] = {}
                if 'statements' not in route_map_dict[name]:
                    route_map_dict[name]['statements'] = {}
                if statements not in route_map_dict[name]['statements']:
                    route_map_dict[name]['statements'][statements] = {}
                if 'actions' not in route_map_dict[name]['statements'][statements]:
                    route_map_dict[name]['statements'][statements]['actions'] = {}
                if 'conditions' not in route_map_dict[name]['statements'][statements]:
                    route_map_dict[name]['statements'][statements]['conditions'] = {}
                    set_as_path_group = []

                route_map_dict[name]['statements'][statements]['actions']\
                ['set_next_hop_self'] = False
                continue

            # description <description>
            m = p1_1.match(line)
            if m:
                description = str(m.groupdict()['description'])
                route_map_dict[name]['description'] = description

            # Match clauses:
            # Set clauses:
            m = p1_2.match(line)
            if m:
                clause_type = str(m.groupdict()['clause_type'])
                route_map_dict[name]['statements'][statements]['actions']\
                ['route_disposition'] = route_disposition
                continue

            # as-path (as-path filter): aspathlist1
            m = p2.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_as_path_list'] = str(m.groupdict()['match_as_path_list'])
                continue

            # as-number (as-path-list filter): List1, List2
            m = p2_1.match(line)
            if m:
                match_as_number_list = m.groupdict()['match_as_number_list']
                match_as_number_list = match_as_number_list.replace(" ","")
                match_as_number_list = match_as_number_list.lower()

                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_as_number_list'] = match_as_number_list
                continue

            # ip address prefix-lists: test-test
            m = p3.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_prefix_list'] = str(m.groupdict()['match_prefix_list'])
                continue
            
            # ip address (access-lists): pbr-acl
            m = p3_1.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_access_list'] = m.groupdict()['match_access_list']
                continue
            
            #ip next-hop prefix-lists: test
            #ip next-hop (access-lists): 1
            m = p4.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_nexthop_in'] = m.groupdict()['match_nexthop_in'].split()
                continue
            
            # ipv6 address prefix-list test-test
            m = p5.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_prefix_list_v6'] = str(m.groupdict()['match_prefix_list_v6'])
                continue

            # ipv6 next-hop prefix-list test2
            m = p6.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_nexthop_in_v6'] = m.groupdict()['match_nexthop_in_v6'].split()
                continue

            #interface GigabitEthernet1
            m = p7.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_interface'] = str(m.groupdict()['match_interface'])
                continue

            #metric 100
            m = p8.match(line)
            if m:
                if clause_type == 'Match':
                    route_map_dict[name]['statements'][statements]['conditions']\
                    ['match_med_eq'] = int(m.groupdict()['match_med_eq'])
                else:
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_metric'] = int(m.groupdict()['match_med_eq'])
                continue

            #community  (community-list filter): test3
            m = p10.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_community_list'] = str(m.groupdict()['match_community_list'])
                continue

            #route-type: level-1 level-2
            m = p11.match(line)
            if m:
                if m.groupdict()['match_level_eq'] == 'level-1 level-2':
                    route_map_dict[name]['statements'][statements]['conditions']\
                    ['match_level_eq'] = 'level-1-2'
                else:
                    route_map_dict[name]['statements'][statements]['conditions']\
                    ['match_level_eq'] = str(m.groupdict()['match_level_eq'])
                continue

            # extcommunity  (extcommunity-list filter): testing
            m = p11_1.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['conditions']\
                ['match_ext_community_list'] = str(m.groupdict()['match_ext_community_list'])
                continue

            # ip next-hop 10.64.4.4
            # ip next-hop 10.4.1.1 10.16.2.2
            m = p12.match(line)
            if m:
                if clause_type == 'Match':
                    route_map_dict[name]['statements'][statements]['conditions']\
                    ['match_nexthop_in'] = m.groupdict()['set_next_hop'].split()
                else:
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_next_hop'] = m.groupdict()['set_next_hop'].split()
                continue

            # ip next-hop self
            m = p12_1.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_next_hop_self'] = True
                continue

            #ip default next-hop 100.0.0.2                                      
            m = p12_2.match(line)                                                
            if m:                                                               
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_next_hop'] = m.groupdict()['set_next_hop'].split()
                continue 

            # ipv6 next-hop 2001:db8:1::1
            # ipv6 next-hop 2001:DB8:1::1 2001:DB8:2::1
            m = p13.match(line)
            if m:
                if clause_type == 'Match':
                    route_map_dict[name]['statements'][statements]['conditions']\
                    ['match_nexthop_in_v6'] = m.groupdict()['set_next_hop_v6'].split()
                else:
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_next_hop_v6'] = m.groupdict()['set_next_hop_v6'].split()
                continue

            #tag 30
            m = p14.match(line)
            if m:
                if clause_type == 'Match':
                    route_map_dict[name]['statements'][statements]['conditions']\
                    ['match_tag_list'] = str(m.groupdict()['set_tag'])
                else:
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_tag'] = str(m.groupdict()['set_tag'])
                continue

            # weight 50
            m = p14_1.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_weight'] = int(m.groupdict()['set_weight'])
                continue

            #metric 20
            m = p15.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_med'] = int(m.groupdict()['set_med'])
                continue

            #distance: 10
            m = p15_1.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_distance'] = int(m.groupdict()['set_distance'])
                continue

            # metric-type external ---- > set_metric_type
            # metric-type type-1   ---- > set_ospf_metric_type
            m = p16.match(line)
            if m:
                if m.groupdict()['set_ospf_metric_type'] == 'interanl' or\
                    m.groupdict()['set_ospf_metric_type'] == 'external':
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_metric_type'] = str(m.groupdict()['set_ospf_metric_type'])
                else:
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_ospf_metric_type'] = str(m.groupdict()['set_ospf_metric_type'])
                continue

            #level level-1
            m = p17.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_level'] = str(m.groupdict()['set_level'])
                continue

            #local-preference 111
            m = p18.match(line)
            if m:
                if clause_type == 'Match':
                    route_map_dict[name]['statements'][statements]['conditions']\
                    ['match_local_pref_eq'] = int(m.groupdict()['match_local_pref_eq'])
                else:
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_local_pref'] = int(m.groupdict()['match_local_pref_eq'])
                continue

            #origin igp
            m = p19.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_route_origin'] = str(m.groupdict()['set_route_origin'])
                continue

            # comm-list test delete
            m = p20.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_community_delete'] = str(m.groupdict()['set_community_delete'])
                continue

            #community 100:1 no-export no-advertise additive
            m = p20_1.match(line)
            if m:
                set_community = str(m.groupdict()['set_community'])
                set_community_no_export = m.groupdict()['set_community_no_export']
                set_community_no_advertise = m.groupdict()['set_community_no_advertise']
                set_community_additive = m.groupdict()['set_community_additive']

                route_map_dict[name]['statements'][statements]['actions']\
                ['set_community'] = set_community
                if set_community_no_export:
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_community_no_export'] = True
                if set_community_no_advertise:
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_community_no_advertise'] = True
                if set_community_additive:
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_community_additive'] = True
                continue

            #as-path prepend 10 10 10
            m = p21.match(line)
            if m:
                set_as_path_prepend = str(m.groupdict()['set_as_path_prepend'])

                set_as_path_prepend = [str(i) for i in set_as_path_prepend.split()]

                for path in set_as_path_prepend:
                    set_as_path_group.append(path)

                set_as_path_prepend = set_as_path_group[0]
                set_as_path_prepend_repeat_n = len(set_as_path_group)

                route_map_dict[name]['statements'][statements]['actions']\
                ['set_as_path_prepend'] = set_as_path_prepend
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_as_path_prepend_repeat_n'] = set_as_path_prepend_repeat_n
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_as_path_group'] = set_as_path_group
                continue

            #extcomm-list cisco delete
            m = p22.match(line)
            if m:
                route_map_dict[name]['statements'][statements]['actions']\
                ['set_ext_community_delete'] = str(m.groupdict()\
                ['set_ext_community_delete'])
                continue

            # extended community RT:100:10 RT:100:100 RT:200:200 additive
            m = p23.match(line)
            if m:
                if m.groupdict()['set_ext_community_rt']:
                    set_ext_community_rt = \
                        m.groupdict()['set_ext_community_rt'].\
                            replace('RT:','').strip().split()
                    if m.groupdict()['set_ext_community_rt_additive']:
                        set_ext_community_rt_additive = m.groupdict()\
                        ['set_ext_community_rt_additive']
                        route_map_dict[name]['statements'][statements]['actions']\
                        ['set_ext_community_rt_additive'] = True

                    route_map_dict[name]['statements'][statements]['actions']\
                    ['set_ext_community_rt'] = set_ext_community_rt
                    route_map_dict[name]['statements'][statements]['actions']\
                    ['route_disposition'] = route_disposition
                    continue
                else:
                    # extended community VD:100:100
                    m = p24.match(line)
                    if m:
                        set_ext_community_vpn = str(m.groupdict()['set_ext_community_vpn'])
                        route_map_dict[name]['statements'][statements]['actions']\
                        ['set_ext_community_vpn'] = set_ext_community_vpn
                        continue

                    # extended community SoO:100:10
                    m = p25.match(line)
                    if m:
                        set_ext_community_soo = str(m.groupdict()['set_ext_community_soo'])
                        route_map_dict[name]['statements'][statements]['actions']\
                        ['set_ext_community_soo'] = set_ext_community_soo
                        continue

            # Policy routing matches: 0 packets, 0 bytes
            m = p26.match(line)
            if m:
                for k, v in m.groupdict().items():
                    route_map_dict[name]['statements'][statements].setdefault('policy_routing_matches', {}).setdefault(k, int(v))
                    continue

        return route_map_dict
