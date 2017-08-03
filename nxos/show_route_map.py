import re   
from metaparser import MetaParser   
from metaparser.util.schemaengine import Schema, Any, Optional 

class ShowRouteMapSchema(MetaParser):

    ''' Schema for:
        # 'show route-map'
    '''

    schema = {
        Any():
            {'statements':
                {Any():
                    {'conditions':
                        {'match_med_eq': int,
                         'match_nexthop_in': str,
                         'match_nexthop_in_v6': str,
                         'match_route_type': str,
                         'match_community_list': str,
                         'match_ext_community_list': str,
                         'match_as_path_list': str,
                         'match_interface': str,
                         'match_prefix_list': str,
                         'match_prefix_list_v6': str,
                         'match_tag_list': int,
                         },
                     'actions':
                        {'set_route_origin': str, 
                         'set_local_pref': int, 
                         'set_next_hop': str, 
                         'set_next_hop_v6': str, 
                         'set_med': int, 
                         'set_as_path_prepend': str,
                         'set_as_path_group': list, 
                         'set_as_path_prepend_repeat_n': int,
                         'set_community': str,
                         'set_community_additive': bool,
                         'set_community_no_advertise': bool,
                         'set_community_no_export': bool,
                         'set_community_delete': str,
                         'set_ext_community_rt': str,
                         'set_ext_community_delete': str,
                         'set_level': str,
                         'set_metric_type': str,
                         'route_disposition': str,
                         'set_tag': int
                        },
                    },
                },
            },
        }
    
class ShowRouteMap(ShowRouteMapSchema):

    def cli(self):
        out = self.device.execute('show route-map')

        route_map_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # route-map test, permit, sequence 10 
            p1 =  re.compile(r'^\s*route-map *(?P<name>[a-zA-Z]+),'
                              ' *(?P<route_disposition>[a-z]+), *sequence'
                              ' *(?P<statements>[0-9]+)$')
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

                    set_as_path_group = []
                    continue

            # as-path (as-path filter): aspathlist1 
            p2 = re.compile(r'^\s*as-path *\(as-path *filter\):'
                             ' *(?P<match_as_path_list>[a-z0-9]+)$')
            m = p2.match(line)
            if m:
                match_as_path_list = str(m.groupdict()['match_as_path_list'])
                if 'conditions' not in route_map_dict[name]['statements'][statements]:
                    route_map_dict[name]['statements'][statements]['conditions'] = {}

                route_map_dict[name]['statements'][statements]['conditions']['match_as_path_list'] = match_as_path_list
                continue

            # ip address prefix-lists: test-test 
            p3 = re.compile(r'^\s*ip *address *prefix-lists:'
                             ' *(?P<match_prefix_list>[a-z\-]+)$')
            m = p3.match(line)
            if m:
                match_prefix_list = str(m.groupdict()['match_prefix_list'])

                route_map_dict[name]['statements'][statements]['conditions']['match_prefix_list'] = match_prefix_list
                continue

            #ip next-hop prefix-lists: test
            p4 =  re.compile(r'^\s*ip *next-hop *prefix-lists: *(?P<match_nexthop_in>[a-z]+)$')
            m = p4.match(line)
            if m:
                match_nexthop_in = str(m.groupdict()['match_nexthop_in'])

                route_map_dict[name]['statements'][statements]['conditions']['match_nexthop_in'] = match_nexthop_in
                continue

            # ipv6 address prefix-lists: test-test
            p5 = re.compile(r'^\s*ipv6 *address *prefix-lists: *(?P<match_prefix_list_v6>[a-z\-]+)$')
            m = p5.match(line)
            if m:
                match_prefix_list_v6 = str(m.groupdict()['match_prefix_list_v6'])

                route_map_dict[name]['statements'][statements]['conditions']['match_prefix_list_v6'] = match_prefix_list_v6
                continue

            # ipv6 next-hop prefix-lists: test2
            p6 = re.compile(r'^\s*ipv6 *next-hop *prefix-lists: *(?P<match_nexthop_in_v6>[a-z0-9]+)$')
            m = p6.match(line)
            if m:
                match_nexthop_in_v6 = str(m.groupdict()['match_nexthop_in_v6'])

                route_map_dict[name]['statements'][statements]['conditions']['match_nexthop_in_v6'] = match_nexthop_in_v6
                continue

            #interface: Ethernet2/2 
            p7 = re.compile(r'^\s*interface: *(?P<match_interface>[a-zA-Z0-9\/]+)$')
            m = p7.match(line)
            if m:
                match_interface = str(m.groupdict()['match_interface']) 

                route_map_dict[name]['statements'][statements]['conditions']['match_interface'] = match_interface
                continue

            #metric: 20 
            p8 = re.compile(r'^\s*metric: *(?P<match_med_eq>[0-9]+)$')
            m = p8.match(line)
            if m:
                match_med_eq = int(m.groupdict()['match_med_eq'])

                route_map_dict[name]['statements'][statements]['conditions']['match_med_eq'] = match_med_eq
                continue

            #tag: 23 
            p9 = re.compile(r'^\s*tag: *(?P<match_tag_list>[0-9]+)$')
            m = p9.match(line)
            if m:
                match_tag_list = int(m.groupdict()['match_tag_list'])

                route_map_dict[name]['statements'][statements]['conditions']['match_tag_list'] = match_tag_list
                continue

            #community  (community-list filter): test3 
            p10 = re.compile(r'^\s*community *\(community-list *filter\): *(?P<match_community_list>[a-z0-9]+)$')
            m = p10.match(line)
            if m:
                match_community_list = str(m.groupdict()['match_community_list'])

                route_map_dict[name]['statements'][statements]['conditions']['match_community_list'] = match_community_list
                continue

            #route-type: level-1 level-2
            p11 = re.compile(r'^\s*route-type: *(?P<match_route_type>[a-z0-9\-\s]+)$')
            m = p11.match(line)
            if m:
                match_route_type = str(m.groupdict()['match_route_type'])

                route_map_dict[name]['statements'][statements]['conditions']['match_route_type'] = match_route_type
                continue

            # extcommunity  (extcommunity-list filter): testing
            p11_1 = re.compile(r'^\s*extcommunity *\(extcommunity-list *filter\): *(?P<match_ext_community_list>[a-zA-Z]+)$')
            m = p11_1.match(line)
            if m:
                match_ext_community_list = str(m.groupdict()['match_ext_community_list'])

                route_map_dict[name]['statements'][statements]['conditions']['match_ext_community_list'] = match_ext_community_list
                continue

            # ip next-hop 4.4.4.4 
            p12 = re.compile(r'^\s*ip *next-hop *(?P<set_next_hop>[0-9\.]+)$')
            m = p12.match(line)
            if m:
                set_next_hop = str(m.groupdict()['set_next_hop'])
                
                if 'actions' not in route_map_dict[name]['statements'][statements]:
                    route_map_dict[name]['statements'][statements]['actions'] = {}

                route_map_dict[name]['statements'][statements]['actions']['set_next_hop'] = set_next_hop
                continue

            # ipv6 next-hop 2001:db8:1::1 
            p13 = re.compile(r'^\s*ipv6 *next-hop *(?P<set_next_hop_v6>[a-z0-9\:]+)$')
            m = p13.match(line)
            if m:
                set_next_hop_v6 = str(m.groupdict()['set_next_hop_v6'])

                route_map_dict[name]['statements'][statements]['actions']['set_next_hop_v6'] = set_next_hop_v6
                continue

            #tag 30
            p14 = re.compile(r'^\s*tag *(?P<set_tag>[0-9]+)$')
            m = p14.match(line)
            if m:
                set_tag = int(m.groupdict()['set_tag'])

                route_map_dict[name]['statements'][statements]['actions']['set_tag'] = set_tag
                continue

            #metric 20 
            p15 = re.compile(r'^\s*metric *(?P<set_med>[0-9]+)$')
            m = p15.match(line)
            if m:
                set_med = int(m.groupdict()['set_med'])

                route_map_dict[name]['statements'][statements]['actions']['set_med'] = set_med
                continue

            #metric-type external 
            p16 = re.compile(r'^\s*metric-type *(?P<set_metric_type>[0-9a-z]+)$')
            m = p16.match(line)
            if m:
                set_metric_type = str(m.groupdict()['set_metric_type'])

                route_map_dict[name]['statements'][statements]['actions']['set_metric_type'] = set_metric_type
                continue

            #level level-1 
            p17 = re.compile(r'^\s*level *(?P<set_level>[a-z0-9\-]+)$')
            m = p17.match(line)
            if m:
                set_level = str(m.groupdict()['set_level'])

                route_map_dict[name]['statements'][statements]['actions']['set_level'] = set_level
                continue

            #local-preference 20
            p18 = re.compile(r'^\s*local-preference *(?P<set_local_pref>[0-9]+)$')
            m = p18.match(line)
            if m:
                set_local_pref = int(m.groupdict()['set_local_pref'])

                route_map_dict[name]['statements'][statements]['actions']['set_local_pref'] = set_local_pref
                continue

            #origin igp
            p19 = re.compile(r'^\s*origin *(?P<set_route_origin>[a-z]+)$')
            m = p19.match(line)
            if m:
                set_route_origin = str(m.groupdict()['set_route_origin'])

                route_map_dict[name]['statements'][statements]['actions']['set_route_origin'] = set_route_origin
                continue

            # comm-list test delete
            p20 = re.compile(r'^\s*comm-list *(?P<set_community_delete>[a-z]+) *delete$')
            m = p20.match(line)
            if m:
                set_community_delete = str(m.groupdict()['set_community_delete'])

                route_map_dict[name]['statements'][statements]['actions']['set_community_delete'] = set_community_delete
                continue

            #community 100:1 no-export no-advertise additive 
            p20_1 = re.compile(r'^\s*community *(?P<set_community>[0-9\:]+)(?: *(?P<set_community_no_export>(no-export)))?(?: *(?P<set_community_no_advertise>(no-advertise)))?(?: *(?P<set_community_additive>(additive)))?$')
            m = p20_1.match(line)
            if m:
                set_community = str(m.groupdict()['set_community'])
                set_community_no_export = m.groupdict()['set_community_no_export']
                set_community_no_advertise = m.groupdict()['set_community_no_advertise']
                set_community_additive = m.groupdict()['set_community_additive']

                route_map_dict[name]['statements'][statements]['actions']['set_community'] = set_community
                route_map_dict[name]['statements'][statements]['actions']['set_community_no_export'] = True
                route_map_dict[name]['statements'][statements]['actions']['set_community_no_advertise'] = True
                route_map_dict[name]['statements'][statements]['actions']['set_community_additive'] = True
                continue

            #as-path prepend 10 10 10 
            p21 = re.compile(r'^\s*as-path *prepend *(?P<set_as_path_prepend>[0-9\s]+)$')
            m = p21.match(line)
            if m:
                set_as_path_prepend = str(m.groupdict()['set_as_path_prepend'])

                set_as_path_prepend = [str(i) for i in set_as_path_prepend.split()]

                for path in set_as_path_prepend:
                    set_as_path_group.append(path)

                set_as_path_prepend = set_as_path_group[0]
                set_as_path_prepend_repeat_n = len(set_as_path_group)

                route_map_dict[name]['statements'][statements]['actions']['set_as_path_prepend'] = set_as_path_prepend
                route_map_dict[name]['statements'][statements]['actions']['set_as_path_prepend_repeat_n'] = set_as_path_prepend_repeat_n
                route_map_dict[name]['statements'][statements]['actions']['set_as_path_group'] = set_as_path_group
                continue

            #extcomm-list cisco delete
            p22 = re.compile(r'^\s*extcomm-list *(?P<set_ext_community_delete>[a-z]+) *delete$')
            m = p22.match(line)
            if m:
                set_ext_community_delete = str(m.groupdict()['set_ext_community_delete'])

                route_map_dict[name]['statements'][statements]['actions']['set_ext_community_delete'] = set_ext_community_delete
                continue

            # extcommunity RT:100:10 additive 
            p23 = re.compile(r'^\s*extcommunity *RT:(?P<set_ext_community_rt>[0-9\:]+) *additive$')
            m = p23.match(line)
            if m:
                set_ext_community_rt = str(m.groupdict()['set_ext_community_rt'])

                route_map_dict[name]['statements'][statements]['actions']['set_ext_community_rt'] = set_ext_community_rt
                route_map_dict[name]['statements'][statements]['actions']['route_disposition'] = route_disposition
                continue

        return route_map_dict






