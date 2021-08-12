###########################################################################
# Parser For Show PRL ROUTE POLICY
###########################################################################

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowRplRoutePolicySchema(MetaParser):
    """Schema for show rpl route-policy"""
    schema = {
        Any():
            {
                Optional('description'): str,
                'statements':
                    {
                        Any():
                            {
                                'conditions':
                                    {
                                        Optional('match_med_eq'): int,
                                        Optional('match_origin_eq'): str,
                                        Optional('match_nexthop_in'): str,
                                        Optional('match_nexthop_in_v6'): str,
                                        Optional('match_local_pref_eq'): str,
                                        Optional('match_community_list'): str,
                                        Optional('match_ext_community_list'): list,
                                        Optional('match_ext_community_list_type'): str,
                                        Optional('match_as_path_list'): str,
                                        Optional('match_as_path_length'): int,
                                        Optional('match_as_path_length_oper'): str,
                                        Optional('match_level_eq'): str,
                                        Optional('match_area_eq'): str,
                                        Optional('match_prefix_list'): str,
                                        Optional('match_prefix_list_v6'): str,
                                        Optional('match_tag_list'): str
                                    },
                                'actions':
                                    {
                                        Optional('set_route_origin'): str,
                                        Optional('set_local_pref'): int,
                                        Optional('set_next_hop'): str,
                                        Optional('set_next_hop_v6'): str,
                                        Optional('set_next_hop_self'): bool,
                                        Optional('set_med'): int,
                                        Optional('set_as_path_prepend'): int,
                                        Optional('set_as_path_prepend_repeat_n'): int,
                                        Optional('set_community'): list,
                                        Optional('set_community_list'): str,
                                        Optional('set_community_no_export'): bool,
                                        Optional('set_community_no_advertise'): bool,
                                        Optional('set_community_additive'): bool,
                                        Optional('set_community_delete'): str,
                                        Optional('set_ext_community_rt'): list,
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
                                        Optional('actions'): str,
                                        Optional('set_spf_priority'): str,
                                    }
                            }
                    },
            },
    }


class ShowRplRoutePolicy(ShowRplRoutePolicySchema):
    """Parser for show rpl route-policy"""

    cli_command = 'show rpl route-policy'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        rpl_route_policy_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # route-policy test

            p1 = re.compile(r'^\s*route-policy +(?P<name>[\w\W\s]+)$')
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

            # test
            p1_1 = re.compile(r'^\s*# *(?P<description>[a-zA-Z\W]+)$')
            m = p1_1.match(line)
            if m:
                description = str(m.groupdict()['description'])

                rpl_route_policy_dict[name]['description'] = description
                continue

            # 36
            p1_2 = re.compile(r'^\s*# *(?P<statements>[0-9]+)$')
            m = p1_2.match(line)
            if m:

                if statements in rpl_route_policy_dict[name]['statements']:
                    del rpl_route_policy_dict[name]['statements'][statements]

                statements = int(m.groupdict()['statements'])
                if 'statements' not in rpl_route_policy_dict[name]:
                    rpl_route_policy_dict[name]['statements'] = {}
                if statements not in rpl_route_policy_dict[name]['statements']:
                    rpl_route_policy_dict[name]['statements'][statements] = {}
                if 'actions' not in rpl_route_policy_dict[name]:
                    rpl_route_policy_dict[name]['statements'][statements]['actions'] = {}
                if 'conditions' not in rpl_route_policy_dict[name]:
                    rpl_route_policy_dict[name]['statements'][statements]['conditions'] = {}
                continue

            # set med 113
            p2 = re.compile(r'^\s*set +med +(?P<set_med>[0-9]+)$')
            m = p2.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_med'] = int(m.groupdict()['set_med'])
                continue

            # set origin egp
            p3 = re.compile(r'^\s*set +origin +(?P<set_route_origin>[a-z]+)$')
            m = p3.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_route_origin'] = str(m.groupdict()['set_route_origin'])
                continue

            # set local-preference 100
            p4 = re.compile(r'^\s*set +local-preference +(?P<set_local_pref>[0-9]+)$')
            m = p4.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_local_pref'] = int(m.groupdict()['set_local_pref'])
                continue

            # set next-hop 10.4.1.1
            p5 = re.compile(r'^\s*set +next-hop +(?P<set_next_hop>[0-9\.]+)$')
            m = p5.match(line)
            if m:
                set_next_hop = m.groupdict()['set_next_hop']
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_next_hop'] = str(m.groupdict()['set_next_hop'])
                continue

            # set next-hop self
            p5_1 = re.compile(r'^\s*(?P<set_next_hop_self>(self))$')
            m = p5_1.match(line)
            if m:
                set_next_hop_self = m.groupdict()['set_next_hop_self']
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_next_hop_self'] = True
                continue

            # prepend as-path 100 10
            p6 = re.compile(r'\s*prepend +as-path +(?P<set_as_path_prepend>[0-9]+)'
                            ' *(?P<set_as_path_prepend_repeat_n>[0-9]+)$')
            m = p6.match(line)
            if m:
                set_as_path_prepend = int(m.groupdict()['set_as_path_prepend'])
                set_as_path_prepend_repeat_n = int(m.groupdict()['set_as_path_prepend_repeat_n'])

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_as_path_prepend'] = set_as_path_prepend
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_as_path_prepend_repeat_n'] = set_as_path_prepend_repeat_n
                continue

            # set community test
            p7 = re.compile(r'^\s*set +community +(?P<set_community_list>\S+)$')
            m = p7.match(line)
            if m:
                set_community_list = m.groupdict()['set_community_list']
                set_community_list = set_community_list.replace("(", "")
                set_community_list = set_community_list.replace(")", "")

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_list'] = set_community_list
                continue

            # set community test additive
            p7_1 = re.compile(r'^\s*set +community +(?P<set_community_list>\S+)'
                              ' *(?P<set_community_additive>(additive))$')
            m = p7_1.match(line)
            if m:
                set_community_list = m.groupdict()['set_community_list']
                set_community_list = set_community_list.replace("(", "")
                set_community_list = set_community_list.replace(")", "")
                set_community_additive = m.groupdict()['set_community_additive']

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_list'] = set_community_list
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_additive'] = True
                continue

            # set community (100:100, no-export, no-advertise) additive
            p8 = re.compile(r'^\s*set +community +\((?P<set_community>[0-9\:\s\,]+),'
                            ' *(?P<set_community_no_export>(no-export)),'
                            ' *(?P<set_community_no_advertise>(no-advertise))\)'
                            ' *(?P<set_community_additive>(additive))$')
            m = p8.match(line)
            if m:
                set_community_no_export = m.groupdict()['set_community_no_export']
                set_community_no_advertise = m.groupdict()['set_community_no_advertise']
                set_community_additive = m.groupdict()['set_community_additive']
                set_community = m.groupdict()['set_community']

                set_community = set_community.split(", ")

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community'] = set_community
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_no_export'] = True
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_no_advertise'] = True
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_additive'] = True
                continue

            #  set community (111:1, 222:1, no-advertise) additive
            p8_1 = re.compile(r'^\s*set +community +\((?P<set_community>[0-9\:\s\,]+),'
                              ' *(?P<set_community_no_advertise>(no-advertise))\)'
                              '(?: *(?P<set_community_additive>(additive)))?$')
            m = p8_1.match(line)
            if m:
                set_community_no_advertise = m.groupdict()['set_community_no_advertise']
                set_community_additive = m.groupdict()['set_community_additive']
                set_community = m.groupdict()['set_community']

                set_community = set_community.split(", ")

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community'] = set_community
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_no_advertise'] = True
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_additive'] = True
                continue

            # set community (100:100, no-export) additive
            p8_2 = re.compile(r'^\s*set +community +\((?P<set_community>[0-9\:\s\,]+),'
                              ' *(?P<set_community_no_export>(no-export))\)'
                              '(?: *(?P<set_community_additive>(additive)))?$')
            m = p8_2.match(line)
            if m:
                set_community_no_export = m.groupdict()['set_community_no_export']
                set_community_additive = m.groupdict()['set_community_additive']
                set_community = m.groupdict()['set_community']

                set_community = set_community.split(", ")

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community'] = set_community
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_no_export'] = True
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_additive'] = True
                continue

            # set community (100:1, 200:1, 300:1, no-export, no-advertise)
            p8_3 = re.compile(r'^\s*set +community +\((?P<set_community>[0-9\:\s\,]+),'
                              ' *(?P<set_community_no_export>(no-export)),'
                              ' *(?P<set_community_no_advertise>(no-advertise))\)$')
            m = p8_3.match(line)
            if m:
                set_community_no_export = m.groupdict()['set_community_no_export']
                set_community_no_advertise = m.groupdict()['set_community_no_advertise']
                set_community = m.groupdict()['set_community']

                set_community = set_community.split(", ")

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community'] = set_community
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_no_export'] = True
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_no_advertise'] = True
                continue

            # set community (100:100, no-export, no-advertise) additive
            p8_4 = re.compile(r'^\s*set +community +\((?:(?P<set_community>[0-9\:\s\,]+),)?'
                              '(?: *(?P<set_community_no_export>(no-export)),)?'
                              '(?: *(?P<set_community_no_advertise>(no-advertise)))?\)'
                              '(?: *(?P<set_community_additive>(additive)))?$')
            m = p8_4.match(line)
            if m:
                set_community_no_export = m.groupdict()['set_community_no_export']
                set_community_no_advertise = m.groupdict()['set_community_no_advertise']
                set_community_additive = m.groupdict()['set_community_additive']
                set_community = m.groupdict()['set_community']

                set_community = set_community.split(", ")

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community'] = set_community
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_no_export'] = True
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_no_advertise'] = True
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_additive'] = True
                continue

            # delete community in test
            p9 = re.compile(r'^\s*delete +community *in'
                            ' *(?P<set_community_delete>[a-zA-Z]+)$')
            m = p9.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_community_delete'] = str(m.groupdict()['set_community_delete'])
                continue

            # set extcommunity rt (100:100, 200:200) additive
            # set extcommunity rt (300:1, 300:2) additive
            p10 = re.compile(r'^\s*set +extcommunity +rt'
                             ' *\((?P<set_ext_community_rt>[0-9\:\,\s]+)\)(?:'
                             ' *(?P<set_ext_community_rt_additive>(additive)))?$')
            m = p10.match(line)
            if m:
                set_ext_community_rt_additive = m.groupdict()['set_ext_community_rt_additive']
                set_ext_community_rt = m.groupdict()['set_ext_community_rt']

                set_ext_community_rt = set_ext_community_rt.split(", ")

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_ext_community_rt'] = set_ext_community_rt
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_ext_community_rt_additive'] = True
                continue

            # set extcommunity soo (100:100) additive
            p11 = re.compile(r'^\s*set extcommunity +soo'
                             ' +\((?P<set_ext_community_soo>[0-9\:]+)\)(?:'
                             ' *(?P<set_ext_community_soo_additive>(additive)))?$')
            m = p11.match(line)
            if m:
                set_ext_community_soo_additive = m.groupdict()['set_ext_community_soo_additive']

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_ext_community_soo'] = str(m.groupdict()['set_ext_community_soo'])
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_ext_community_soo_additive'] = True
                continue

            # delete extcommunity rt in test
            p12 = re.compile(r'^\s*delete +extcommunity +rt *in'
                             ' +(?P<set_ext_community_delete>[a-z]+)$')
            m = p12.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_ext_community_delete'] = str(m.groupdict()['set_ext_community_delete'])
                continue

            # set level level-1
            # set level level-2
            # set level level-1-2
            p13 = re.compile(r'^\s*set +level +(?P<set_level>[a-z0-9\-]+)$')
            m = p13.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_level'] = str(m.groupdict()['set_level'])
                continue

            # set metric-type internal
            # set metric-type external
            p14 = re.compile(r'^\s*set +metric-type +(?P<set_metric_type>[a-z0-9\-]+)$')
            m = p14.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_metric_type'] = str(m.groupdict()['set_metric_type'])
                continue

            # set isis-metric 100
            p15 = re.compile(r'^\s*set +isis-metric +(?P<set_metric>[0-9]+)$')
            m = p15.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_metric'] = str(m.groupdict()['set_metric'])
                continue

            # set ospf-metric 100
            p16 = re.compile(r'^\s*set +ospf-metric +(?P<set_ospf_metric>[0-9]+)$')
            m = p16.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_ospf_metric'] = str(m.groupdict()['set_ospf_metric'])
                continue

            # set weight 111
            p16_1 = re.compile(r'^\s*set +weight +(?P<set_weight>[0-9\s]+)$')
            m = p16_1.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_weight'] = str(m.groupdict()['set_weight'])
                continue

            # set tag 111
            p17 = re.compile(r'^\s*set +tag +(?P<set_tag>[0-9\s]+)$')
            m = p17.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_tag'] = str(m.groupdict()['set_tag'])
                continue

            # set spf-priority medium
            p20 = re.compile(r'^\s*set +spf-priority +(?P<spf_priority>[a-z]+)$')
            m = p20.match(line)
            if m:
                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['set_spf_priority'] = str(m.groupdict()['spf_priority'])
                continue

            # pass|done|drop
            p18 = re.compile(r'^\s*(?P<actions>(pass|done|drop))$')
            m = p18.match(line)
            if m:
                actions = m.groupdict()['actions']

                rpl_route_policy_dict[name]['statements'][statements]['actions'] \
                    ['actions'] = actions
                continue

            # if med eq 100 and local-preference eq 100 and ospf-area is 0 then
            # m.groupdict()[cond] == None - set to none if there is no parsed condition
            p19 = re.compile(r'^\s*(if|elseif|else) *(?P<condition1>\S+ \S+ \S+)'
                             '( *and)?(?: *(?P<condition2>\S+ \S+ \S+))?( *and)?'
                             '(?: *(?P<condition3>\S+ \S+ \S+))?( *and)?(?:'
                             ' *(?P<condition4>\S+ \S+ \S+))?( *and)?(?:'
                             ' *(?P<condition5>\S+ \S+ \S+))? *then$')
            m = p19.match(line)
            if m:
                for cond in m.groupdict().keys():
                    if cond == None or m.groupdict()[cond] == None:
                        continue
                    if 'origin is' in m.groupdict()[cond]:
                        v = re.match('origin is (?P<match_origin_eq>[a-z]+)', m.groupdict()[cond])
                        match_origin_eq = v.groupdict()['match_origin_eq']
                        rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                            ['match_origin_eq'] = match_origin_eq

                    if 'med eq' in m.groupdict()[cond]:
                        v = re.match('med eq (?P<match_med_eq>[0-9]+)', m.groupdict()[cond])
                        match_med_eq = v.groupdict()['match_med_eq']
                        rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                            ['match_med_eq'] = int(v.groupdict()['match_med_eq'])

                    if 'local-preference eq' in m.groupdict()[cond]:
                        v = re.match('local-preference eq (?P<match_local_pref_eq>[0-9]+)', m.groupdict()[cond])
                        match_local_pref_eq = v.groupdict()['match_local_pref_eq']
                        rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                            ['match_local_pref_eq'] = match_local_pref_eq

                    if 'ospf-area is' in m.groupdict()[cond]:
                        v = re.match('ospf-area is (?P<match_area_eq>(\d+\.\d+\.\d+\.\d+|[0-9]+))', m.groupdict()[cond])
                        match_area_eq = v.groupdict()['match_area_eq']
                        rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                            ['match_area_eq'] = match_area_eq

                    if 'next-hop in' in m.groupdict()[cond]:
                        v = re.match('next-hop in (?P<match_nexthop_in>[0-9a-zA-Z-]+)', m.groupdict()[cond])
                        match_nexthop_in = v.groupdict()['match_nexthop_in']
                        rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                            ['match_nexthop_in'] = match_nexthop_in

                    # if (community matches-any CMT-TP or community matches-any CMT-OLDTP or community matches-any
                    # CMT-SBTP or community matches-any CMT-FP) then
                    if 'community matches-any' in m.groupdict()[cond]:
                        match_ext_community_list = re.findall(
                            'community matches-any (?P<match_ext_community_list>[0-9a-zA-Z\-]+)', line)
                        if len(match_ext_community_list) > 0:
                            rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                                ['match_ext_community_list'] = match_ext_community_list

                    if 'as-path in' in m.groupdict()[cond]:
                        v = re.match('as-path in (?P<match_as_path_list>[0-9a-zA-Z-]+)', m.groupdict()[cond])
                        match_as_path_list = v.groupdict()['match_as_path_list']
                        rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                            ['match_as_path_list'] = match_as_path_list

                    if 'as-path length' in m.groupdict()[cond]:
                        v = re.match('as-path length (?P<match_as_path_length_oper>[\w\W]+)', m.groupdict()[cond])
                        match_as_path_length_oper = v.groupdict()['match_as_path_length_oper']
                        rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                            ['match_as_path_length_oper'] = match_as_path_length_oper

                    if 'route-type is' in m.groupdict()[cond]:
                        v = re.match('route-type is (?P<match_level_eq>[\w\W]+)', m.groupdict()[cond])
                        match_level_eq = v.groupdict()['match_level_eq']
                        rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                            ['match_level_eq'] = match_level_eq

                    # if (destination in PE-LOOPBACKS) then
                    # elseif destination in (0.0.0.0/0 eq 32) then
                    if 'destination in' in m.groupdict()[cond]:
                        match = re.search('destination in (?P<match_prefix_list>[0-9a-zA-Z-_]+)', m.groupdict()[cond])
                        if match:
                            match_prefix_list = match.group(1)
                        else:
                            match_2 = re.search(r'destination in (?P<match_prefix_list>\((.*?)\))', line)
                            match_prefix_list = match_2.group(1)

                        rpl_route_policy_dict[name]['statements'][statements]['conditions'] \
                            ['match_prefix_list'] = match_prefix_list
                    continue

        return rpl_route_policy_dict
