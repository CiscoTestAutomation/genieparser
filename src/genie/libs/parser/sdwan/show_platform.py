# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =======================================================================
# Parser for 'show platform hardware qfp active feature appqoe stats all'
# =======================================================================


class ShowPlatformHardwareQfpActiveFeatureAppqoeSchema(MetaParser):
    schema = {
        'feature': {
            Any(): {
                'global': {
                    'ip_non_tcp_pkts': int,
                    'not_enabled': int,
                    'cft_handle_pkt': int,
                    'sdvt_divert_req_fail': int,
                    'syn_policer_rate': int,
                    'sdvt_global_stats': {
                        'appnav_registration': int,
                        'within_sdvt_syn_policer_limit': int
                    }
                },
                'sn_index': {
                    Any(): {
                        'sdvt_count_stats': {
                            Optional('decaps'): int,
                            Optional('encaps'): int,
                            Optional('packets_unmarked_in_ingress'): int,
                            Optional('expired_connections'): int,
                            Optional('idle_timed_out_persistent_connections'): int,
                            Optional('decap_messages'): {
                                'processed_control_messages': int,
                                'delete_requests_recieved': int,
                                'deleted_protocol_decision': int
                            }
                        },
                        'sdvt_packet_stats': {
                            Optional('divert'): {
                                'packets': int,
                                'bytes': int
                            },
                            Optional('reinject'): {
                                'packets': int,
                                'bytes': int
                            }
                        },
                        'sdvt_drop_cause_stats': dict, # This is here because not enough info in output shared
                        'sdvt_errors_stats': dict, # This is here because not enough info in output shared
                    }
                }
            }
        }
    }

class ShowPlatformHardwareQfpActiveFeatureAppqoe(ShowPlatformHardwareQfpActiveFeatureAppqoeSchema):

    cli_command = ['show platform hardware qfp active feature appqoe stats all']

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command[0])

        # APPQOE Feature Statistics:
        p1 = re.compile(r'^(?P<feature>\w+) +Feature +Statistics:$')

        # Global:
        p2 = re.compile(r'^Global:$')

        # SDVT Global stats:
        p3 = re.compile(r'^SDVT +Global +stats:$')

        # SN Index [0 (Green)]
        # SN Index [Default]
        p4 = re.compile(r'^SN +Index +\[(?P<index>[\s\S]+)\]$')

        # SDVT Count stats:
        # SDVT Packet stats:
        # SDVT Drop Cause stats:
        # SDVT Errors stats:
        p5 = re.compile(r'^(?P<sdvt_stats_type>SDVT +[\s\S]+ +stats):$')

        # decaps: Processed control messages from SN: 14200
        # decaps: delete requests received total: 14200
        # decaps: delete - protocol decision: 14200
        p6 = re.compile(r'^decaps: +(?P<decap_type>[\s\S]+): +(?P<value>\d+)$')

        # Divert packets/bytes: 743013/43313261
        # Reinject packets/bytes: 679010/503129551
        p7 = re.compile(r'^(?P<type>Divert|Reinject) +packets\/bytes: +(?P<packets>\d+)\/(?P<bytes>\d+)$')

        # ip-non-tcp-pkts: 0
        # not-enabled: 0
        # cft_handle_pkt:  0
        # sdvt_divert_req_fail:  0
        # syn_policer_rate: 800
        p8 = re.compile(r'^(?P<key>[\s\S]+): +(?P<value>\d+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # APPQOE Feature Statistics:
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                feature_name = groups['feature'].lower()

                # ret_dict = {
                #     'feature': {
                #         'appqoe': {
                #
                #         }
                #     }
                # }
                feature_dict = ret_dict.setdefault('feature', {}).setdefault(feature_name, {})

                last_dict_ptr = feature_dict
                continue

            # Global:
            m = p2.match(line)
            if m:
                global_dict = feature_dict.setdefault('global', {})

                last_dict_ptr = global_dict
                continue

            # SDVT Global stats:
            m = p3.match(line)
            if m:
                sdvt_global_dict = global_dict.setdefault('sdvt_global_stats', {})

                last_dict_ptr = sdvt_global_dict
                continue

            # SN Index [0 (Green)]
            # SN Index [Default]
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                index_dict = feature_dict.setdefault('sn_index', {}).setdefault(groups['index'], {})

                last_dict_ptr = index_dict
                continue

            # SDVT Count stats
            # SDVT Packet stats
            # SDVT Drop Cause stats
            # SDVT Errors stats
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                sdvt_stats_type = groups['sdvt_stats_type'].replace(' ', '_').lower()
                sdvt_stats_type_dict = index_dict.setdefault(sdvt_stats_type, {})

                last_dict_ptr = sdvt_stats_type_dict
                continue

            # decaps: Processed control messages from SN: 14200
            # decaps: delete requests received total: 14200
            # decaps: delete - protocol decision: 14200
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                decap_messages_dict = sdvt_stats_type_dict.setdefault('decap_messages', {})

                if 'control messages' in groups['decap_type']:
                    decap_messages_dict.update({'processed_control_messages': int(groups['value'])})

                elif 'delete requests' in groups['decap_type']:
                    decap_messages_dict.update({'delete_requests_recieved': int(groups['value'])})

                elif 'protocol decision' in groups['decap_type']:
                    decap_messages_dict.update({'deleted_protocol_decision': int(groups['value'])})

                last_dict_ptr = decap_messages_dict
                continue

            # Divert packets/bytes: 743013/43313261
            # Reinject packets/bytes: 679010/503129551
            m = p7.match(line)
            if m:
                groups = m.groupdict()

                if 'Divert' in groups['type']:
                    divert_reinject_dict = sdvt_stats_type_dict.setdefault('divert', {})
                elif 'Reinject' in groups['type']:
                    divert_reinject_dict = sdvt_stats_type_dict.setdefault('reinject', {})

                divert_reinject_dict.update({
                    'packets': int(groups['packets']),
                    'bytes': int(groups['bytes'])
                })

                last_dict_ptr = divert_reinject_dict
                continue

            # ip-non-tcp-pkts: 0
            # not-enabled: 0
            # cft_handle_pkt:  0
            # sdvt_divert_req_fail:  0
            # syn_policer_rate: 800
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').replace(' ', '_').lower()
                last_dict_ptr.update({key: int(groups['value'])})

        return ret_dict
