"""  show_ldp.py
   supported commands:
        *  show mpls ldp neighbor
        *  show mpls ldp neighbor vrf <vrf>
        *  show mpls ldp neighbor detail
        *  show mpls ldp bindings
        *  show mpls ldp bindings all
        *  show mpls ldp bindings all detail
        *  show mpls ldp capabilities
        *  show mpls ldp capabilities all
        *  show mpls ldp discovery
        *  show mpls ldp discovery detail
        *  show mpls ldp discovery all
        *  show mpls ldp discovery all detail
        *  show mpls ldp discovery vrf <vrf>
        *  show mpls ldp discovery vrf <vrf> detail
        *  show mpls ldp igp sync
        *  show mpls ldp igp sync all
        *  show mpls ldp igp sync interface <interface>
        *  show mpls ldp igp sync vrf <vrf>
        *  show mpls ldp statistics
       	*  show mpls ldp parameters
"""
import re

from genie.metaparser import MetaParser

class ShowMplsLdpParametersSchema(MetaParser):
    """Schema for show mpls ldp Parameters"""

    schema = {
        'ldp_featureset_manager': {
            'ldp': {
                'features': list,
                'backoff': {
                    'initial': int,
                    'maximum': int,
                },
                'state_initialized': bool,
                'loop_detection': str,
                'nsr_enabled': bool,
                'version': int,
                'holdtime': int,
                'keepalive_interval': int,
                'discovery_targeted_hello': {
                    'holdtime': int,
                    'interval': int,
                },
                'discovery_hello': {
                    'holdtime': int,
                    'interval': int,
                },
                'downstream': {
                    'maxhop_count': int,
                }
            },
        }
    }

class ShowMplsLdpParameters(ShowMplsLdpParametersSchema):
    """Parser for show mpls ldp parameters"""

    cli_command = 'show mpls ldp parameters'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        ldp_feature_flag = False
        ldp_feature_list = []

        # LDP Feature Set Manager: State Initialized
        p1 = re.compile(r'^LDP +Feature +Set +Manager: +(S|s)tate +(?P<state_initialized>\w+)$')
        #   LDP features:
        p2 = re.compile(r'^LDP +features:$')
        #  Auto-Configuration
        p2_1 = re.compile(r'^(?P<ldp_features>[\w\-]+)?$')
        # Protocol version: 1
        p3 = re.compile(r'^Protocol version: +(?P<version>\d+)$')
        # Session hold time: 180 sec; keep alive interval: 60 sec
        p4 = re.compile(r'^Session +hold +time: +(?P<session_holdtime>\d+) +sec;'
                        ' +keep +alive +interval: +(?P<keepalive_interval>\d+) +sec$')

        # Discovery hello: holdtime: 15 sec; interval: 5 sec
        p5 = re.compile(r'^Discovery +hello: +holdtime: +(?P<holdtime>\d+) +sec; +interval: +(?P<interval>\d+) +sec$')

        # Discovery targeted hello: holdtime: 90 sec; interval: 10 sec
        p6 = re.compile(r'^Discovery +targeted +hello: +holdtime: +(?P<targeted_holdtime>\d+) +sec; +interval:'
                        ' +(?P<targeted_interval>\d+) +sec$')

        # Downstream on Demand max hop count: 255
        p7 = re.compile(r'^Downstream +on +Demand +max +hop +count: +(?P<maxhop_count>\d+)$')
        # LDP for targeted sessions
        p8 = re.compile(r'^LDP +for +targeted +sessions$')
        # LDP initial/maximum backoff: 15/120 sec
        p9 = re.compile(r'^LDP +initial\/maximum +backoff: +(?P<initial>\w+)/+(?P<maximum>\w+) sec$')
        # LDP loop detection: off
        p10 = re.compile(r'^LDP +loop +detection: +(?P<loop_detection>\w+)$')
        # LDP NSR: Disabled
        p11 = re.compile(r'^LDP +NSR: +(?P<nsr>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            # LDP Feature Set Manager: State Initialized
            m = p1.match(line)
            if m:
                ldp_dict = result_dict.setdefault('ldp_featureset_manager', {}).setdefault('ldp', {})
                ldp_dict.update({'state_initialized': True})
                continue

            #  LDP features:
            m = p2.match(line)
            if m:
                ldp_feature_flag = True
                continue

            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                if ldp_feature_flag:
                    ldp_feature_list.append(group['ldp_features'])
                    ldp_dict.update({'features': ldp_feature_list})
                continue

            # Protocol version: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'version': int(group['version'])})
                continue

            # Session hold time: 180 sec; keep alive interval: 60 sec
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'holdtime': int(group['session_holdtime'])})
                ldp_dict.update({'keepalive_interval': int(group['keepalive_interval'])})
                continue

            # Discovery hello: holdtime: 15 sec; interval: 5 sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                discovery_hello = ldp_dict.setdefault('discovery_hello', {})
                discovery_hello.update({'holdtime': int(group['holdtime'])})
                discovery_hello.update({'interval': int(group['interval'])})
                continue

            # Discovery targeted hello: holdtime: 90 sec; interval: 10 sec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                discovery_targeted_hello = ldp_dict.setdefault('discovery_targeted_hello', {})
                discovery_targeted_hello.update({'holdtime': int(group['targeted_holdtime'])})
                discovery_targeted_hello.update({'interval': int(group['targeted_interval'])})
                continue

            # Downstream on Demand max hop count: 255
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.setdefault('downstream', {}).update({'maxhop_count': int(group['maxhop_count'])})
                continue

            # LDP initial/maximum backoff: 15/120 sec
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                backoff_dict = ldp_dict.setdefault('backoff', {})
                backoff_dict.update({'initial': int(group['initial'])})
                backoff_dict.update({'maximum': int(group['maximum'])})
                continue

            # LDP loop detection: off
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'loop_detection': group['loop_detection']})
                continue

            # LDP NSR: Disabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'nsr_enabled': False if group['nsr'].lower() == 'disabled' else True})
                continue

        return result_dict
