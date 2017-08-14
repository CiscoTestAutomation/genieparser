import re
from metaparser import MetaParser   
from metaparser.util.schemaengine import Schema, Any, Optional 


class ShowRplRoutePolicySchema(MetaParser):

     # Schema for:
     # 'show rpl route-policy'
    schema = {
            Any():
               {Optional('description'): str,
                'statements':
                    {Any():
                        {'conditions':
                            {Optional('match_med_eq'): int,
                             Optional('match_origin_eq'): str,
                             Optional('match_nexthop_in'): str,
                             Optional('match_nexthop_in_v6'): str,
                             Optional('match_local_pref_eq'): str,
                             Optional('match_community_list'): str,
                             Optional('match_ext_community_list'): str,
                             Optional('match_ext_community_list_type'): str,
                             Optional('match_as_path_list'): str,
                             Optional('match_as_path_length'): int,
                             Optional('match_as_path_length_oper'): str,
                             Optional('match_level_eq'): str,
                             Optional('match_area_eq'): int,
                             Optional('match_prefix_list'): str,
                             Optional('match_prefix_list_v6'): str,
                             Optional('match_tag_list'): str
                             },
                         'actions':
                            {Optional('set_route_origin'): str,
                             Optional('set_local_pref'): int,
                             Optional('set_next_hop'): str,
                             Optional('set_next_hop_v6'): str,
                             Optional('set_next_hop_self'): bool,  
                             Optional('set_med'): str,
                             Optional('set_as_path_prepend'): int,
                             Optional('set_as_path_prepend_repeat_n'): int,
                             Optional('set_community'): str,
                             Optional('set_community_no_export'): bool,
                             Optional('set_community_no_advertise'): bool,
                             Optional('set_community_additive'): bool,
                             Optional('set_community_delete'): str,
                             Optional('set_ext_community_rt'): str,
                             Optional('set_ext_community_rt_additive'): bool,
                             Optional('set_ext_community_soo'): str,
                             Optional('set_ext_community_soo_additive'): bool,
                             Optional('set_ext_community_vpn'): str,
                             Optional('set_ext_community_delete'): str,
                             Optional('set_ext_community_delete_type'): str,
                             Optional('set_level'): str,
                             Optional('set_metric_type'): str,
                             Optional('set_metric'): str,
                             Optional('set_ospf_metric_type'): str,
                             Optional('set_ospf_metric'): str,
                             Optional('set_tag'): str,
                             Optional('set_weight'): str,
                             Optional('actions'): str
                            },
                        },
                    },
                },
            }


class ShowRplRoutePolicy(ShowRplRoutePolicySchema):

    def cli(self):
        out = self.device.execute('show rpl route-policy')

        rpl_route_policy_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # route-policy test
            p1 = re.compile(r'^\s*route-policy *(?P<name>[\w\W\s]+)$')
            m = p1.match(line)
            if m:
                name = str(m.groupdict()['name'])
                statements = 10

                if name not in rpl_route_policy_dict:
                    rpl_route_policy_dict[name] = {}

                if 'statements' not in rpl_route_policy_dict[name]:
                    rpl_route_policy_dict[name]['statements'] = {}
                if statements not in rpl_route_policy_dict[name]['statements']:
                    rpl_route_policy_dict[name]['statements'][statements] = {}
                if 'actions' not in rpl_route_policy_dict[name]:
                    rpl_route_policy_dict[name]['statements'][statements]['actions'] = {}
                if 'conditions' not in rpl_route_policy_dict[name]:
                    rpl_route_policy_dict[name]['statements'][statements]['conditions'] = {}
                    continue

            if line.startswith('elseif') or line.startswith('else'):
                statements = statements + 10

                if statements not in rpl_route_policy_dict[name]['statements']:
                    rpl_route_policy_dict[name]['statements'][statements] = {}
                if 'actions' not in rpl_route_policy_dict[name]:
                    rpl_route_policy_dict[name]['statements'][statements]['actions'] = {}
                if 'conditions' not in rpl_route_policy_dict[name]:
                    rpl_route_policy_dict[name]['statements'][statements]['conditions'] = {}

            # 36 / #test
            p1_1 = re.compile(r'^\s*# *(?P<description>[\w\W]+)$')
            m = p1_1.match(line)
            if m:
                description = str(m.groupdict()['description'])

                rpl_route_policy_dict[name]['description'] = description
                continue

            #36
            p1_2 = re.compile(r'^\s*# *(?P<statements>[0-9]+)$')
            m = p1_2.match(line)
            if m:
                statements = m.groupdict()['statements']

                if 'statements' not in rpl_route_policy_dict[name]:
                    rpl_route_policy_dict[name]['statements'] = {}
                if statements not in rpl_route_policy_dict[name]['statements']:
                    rpl_route_policy_dict[name]['statements'][statements] = {}
                    continue

            # set med 113
            p2 = re.compile(r'^\s*set *med *(?P<set_med>[0-9]+)$')
            m = p2.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_med'] = set_med = str(m.groupdict()['set_med'])
                continue

            # set origin egp
            p3 = re.compile(r'^\s*set *origin *(?P<set_route_origin>[a-z]+)$')
            m = p3.match(line)
            if m:                
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_route_origin'] = str(m.groupdict()['set_route_origin'])
                continue

            # set local-preference 100
            p4 = re.compile(r'^\s*set *local-preference *(?P<set_local_pref>[0-9]+)$')
            m = p4.match(line)
            if m:                
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_local_pref'] = int(m.groupdict()['set_local_pref'])
                continue

            # set next-hop 1.1.1.1
            # set next-hop self
            p5 =  re.compile(r'^\s*set *next-hop( *(?P<set_next_hop>[0-9\.]+)'
                              '| *(?P<set_next_hop_self>(self)))$')
            m = p5.match(line)
            if m:
                set_next_hop_self = m.groupdict()['set_next_hop_self']

                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_next_hop'] = str(m.groupdict()['set_next_hop'])
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_next_hop_self'] = True
                continue

            # prepend as-path 100 10
            p6 = re.compile(r'\s*prepend *as-path *(?P<set_as_path_prepend>[0-9]+)'
                             ' *(?P<set_as_path_prepend_repeat_n>[0-9]+)$')
            m = p6.match(line)
            if m:
                set_as_path_prepend = int(m.groupdict()['set_as_path_prepend'])
                set_as_path_prepend_repeat_n = int(m.groupdict()['set_as_path_prepend_repeat_n'])

                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_as_path_prepend'] = set_as_path_prepend
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_as_path_prepend_repeat_n'] = set_as_path_prepend_repeat_n
                continue

            # set community test
            # set community test additive
            p7 = re.compile(r'^\s*set *community *(?P<set_community>\S+)'
                             '(?: *(?P<set_community_additive>(additive)))?$')
            m = p7.match(line)
            if m:
                set_community = str(m.groupdict()['set_community'])
                set_community = set_community.replace("(","")
                set_community = set_community.replace(")","")
                set_community_additive = m.groupdict()['set_community_additive']

                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_community'] = set_community
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_community_additive'] = True
                continue

            # set community (100:100, no-export, no-advertise) additive
            # set community (100:100, no-export, 200:200) additive
            p8 = re.compile(r'^\s*set *community *\((?P<set_community>[0-9\:]+),'
                             '(?: *(?P<set_community_no_export>(no-export)),)?'
                             '(?: *(?P<set_community_no_advertise>(no-advertise)'
                             '))?\)(?: *(?P<set_community_additive>(additive)))?$')
            m = p8.match(line)
            if m:
                set_community_no_export = m.groupdict()['set_community_no_export']
                set_community_no_advertise = m.groupdict()['set_community_no_advertise']
                set_community_additive = m.groupdict()['set_community_additive']

                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_community'] = str(m.groupdict()['set_community'])
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_community_no_export'] = True
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_community_no_advertise'] = True
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_community_additive'] = True
                continue

            # delete community in test
            p9 = re.compile(r'^\s*delete *community *in'
                             ' *(?P<set_community_delete>[a-zA-Z]+)$')
            m = p9.match(line)
            if m:
            
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_community_delete'] = str(m.groupdict()['set_community_delete'])
                continue

            # set extcommunity rt (100:100, 200:200) additive            
            # set extcommunity rt (300:1, 300:2) additive
            p10 = re.compile(r'^\s*set *extcommunity *rt'
                              ' *\((?P<set_ext_community_rt>[0-9\:\,\s]+)\)(?:'
                              ' *(?P<set_ext_community_rt_additive>(additive)))?$')
            m = p10.match(line)
            if m:
                set_ext_community_rt_additive = m.groupdict()['set_ext_community_rt_additive']

                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_ext_community_rt'] = str(m.groupdict()['set_ext_community_rt'])
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_ext_community_rt_additive'] = True
                continue

            # set extcommunity soo (100:100) additive
            p11 = re.compile(r'^\s*set extcommunity *soo'
                              ' *\((?P<set_ext_community_soo>[0-9\:]+)\)(?:'
                              ' *(?P<set_ext_community_soo_additive>(additive)))?$')
            m = p11.match(line)
            if m:
                set_ext_community_soo_additive = m.groupdict()['set_ext_community_soo_additive']

                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_ext_community_soo'] = str(m.groupdict()['set_ext_community_soo'])
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_ext_community_soo_additive'] = True
                continue

            # delete extcommunity rt in test
            p12 = re.compile(r'^\s*delete *extcommunity *rt *in'
                              ' *(?P<set_ext_community_delete>[a-z]+)$')
            m = p12.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_ext_community_delete'] = str(m.groupdict()['set_ext_community_delete'])
                continue
            
            # set level level-1
            # set level level-2
            # set level level-1-2
            p13 = re.compile(r'^\s*set *level *(?P<set_level>[a-z0-9\-]+)$')
            m = p13.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_level'] = str(m.groupdict()['set_level'])
                continue

            # set metric-type internal
            # set metric-type external
            p14 = re.compile(r'^\s*set *metric-type *(?P<set_metric_type>[a-z0-9\-]+)$')
            m = p14.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_metric_type'] = str(m.groupdict()['set_metric_type'])
                continue

            # set isis-metric 100
            p15 = re.compile(r'^\s*set *isis-metric *(?P<set_metric>[0-9]+)$')
            m = p15.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_metric'] = str(m.groupdict()['set_metric'])
                continue

            # set ospf-metric 100
            p16 = re.compile(r'^\s*set *ospf-metric *(?P<set_ospf_metric>[0-9]+)$')
            m = p16.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_ospf_metric'] = str(m.groupdict()['set_ospf_metric'])
                continue

            # set tag 111
            p17 = re.compile(r'^\s*set(?: *tag *(?P<set_tag>[0-9\s]+))?(?:'
                              ' *weight *(?P<set_weight>[0-9\s]+))?$')
            m = p17.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_tag'] = str(m.groupdict()['set_tag'])
                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['set_weight'] = str(m.groupdict()['set_weight'])
                continue

            #if destination in prefix-set1 and community matches-any cs1 then
            p18 = re.compile(r'^\s*if *destination *in'
                              ' *(?P<match_prefix_list>[\w\W\S]+) *and *community'
                              ' *matches-any *(?P<match_community_list>[\w\W]+)'
                              ' *then$')
            m = p18.match(line)
            if m:
                match_prefix_list = str(m.groupdict()['match_prefix_list'])
                match_community_list = str(m.groupdict()['match_community_list'])

                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_prefix_list'] = match_prefix_list
                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_community_list'] = match_community_list
                continue

            # if origin is egp and med eq 100 then
            p19 = re.compile(r'^\s*(if|elseif|else)(?: *origin *is'
                              ' *(?P<match_origin_eq>[a-z]+))?( *and)?(?: *med'
                              ' *eq *(?P<match_med_eq>[0-9]+))? *then$')
            m = p19.match(line)
            if m:

                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_origin_eq'] = str(m.groupdict()['match_origin_eq'])
                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_med_eq'] = int(m.groupdict()['match_med_eq'])
                continue

            # elseif next-hop in prefix-set1 and next-hop in test6 then
            p20 = re.compile(r'^\s*(elseif|if|else) *next-hop *in'
                              ' *(?P<match_prefix_list>[\w\W\S]+) *and *next-hop'
                              ' *in *(?P<match_nexthop_in>[\w\W]+) *then$')
            m = p20.match(line)
            if m:

                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_prefix_list'] = str(m.groupdict()['match_prefix_list'])
                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_nexthop_in'] = m.groupdict()['match_nexthop_in']
                continue

            # elseif local-preference eq 130 and community matches-any test then
            p21 = re.compile(r'^\s*(elseif|if|else) *local-preference *eq'
                              ' *(?P<match_local_pref_eq>[0-9]+)( *and)?'
                              '(?: *community *matches-any'
                              ' *(?P<match_community_list>[\w\W]+))? *then$')
            m = p21.match(line)
            if m:

                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_local_pref_eq'] = str(m.groupdict()['match_local_pref_eq'])
                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_community_list'] = str(m.groupdict()['match_community_list'])
                continue

            # if extcommunity rt matches-any test then
            p22 = re.compile(r'^\s*if *extcommunity'
                              ' *(?P<match_ext_community_list_type>[a-z]+)'
                              ' *matches-any'
                              ' *(?P<match_ext_community_list>[/w/W\s]+) *then$')
            m = p22.match(line)
            if m:
                match_ext_community_list_type = m.groupdict()['match_ext_community_list_type']
                match_ext_community_list = m.groupdict()['match_ext_community_list']

                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_ext_community_list_type'] = match_ext_community_list_type
                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_ext_community_list'] = match_ext_community_list
                continue

            # elseif ospf-area is 1.1.1.1 and route-type is level-1 and route-type is level-2 then
            p23 = re.compile(r'^\s*(elif|if) *ospf-area *is'
                              ' *(?P<match_area_eq>[0-9\.]+) *and *route-type *is'
                              ' *(?P<match_level_eq>[a-z0-9\-\s]+)'
                              ' *then$')
            m = p23.match(line)
            if m:
                match_area_eq = m.groupdict()['match_area_eq']
                match_level_eq = m.groupdict()['match_level_eq']
                match_level_eq = match_level_eq.replace("and route-type is",",")
                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_ext_community_list_type'] = match_ext_community_list_type
                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_ext_community_list'] = match_ext_community_list
                continue

            #elseif as-path length ge 7 then
            p24 = re.compile(r'^\s*(elif|if) *as-path *length'
                              ' *(?P<match_as_path_length_oper>[a-z]+)'
                              ' *(?P<match_as_path_length>[0-9]+) *then$')
            m = p24.match(line)
            if m:
                match_as_path_length_oper = m.groupdict()['match_as_path_length_oper']
                match_as_path_length = m.groupdict()['match_as_path_length']

                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_as_path_length_oper'] = match_as_path_length_oper
                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_as_path_length'] = match_as_path_length
                continue

            #if as-path in test then
            p25 = re.compile(r'^\s*(elif|if) *as-path *in *(?P<match_as_path_list>[\w\W]+) *then$')
            m = p25.match(line)
            if m:
                match_as_path_list = m.groupdict()['match_as_path_list']

                rpl_route_policy_dict[name]['statements'][statements]['conditions']\
                ['match_as_path_list'] = match_as_path_list
                continue

            #pass|done|drop
            p26 = re.compile(r'^\s*(?P<actions>(pass|done|drop))$')
            m = p26.match(line)
            if m:
                actions = m.groupdict()['actions']

                rpl_route_policy_dict[name]['statements'][statements]['actions']\
                ['actions'] = actions
                continue

        return rpl_route_policy_dict
