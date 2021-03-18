''' show_smnp.py

JUNOS parsers for the following commands:
    * show snmp mib walk system
    * show configuration snmp
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema, ListOf)


    # Sub Schema snmp-object
class ShowSnmpMibWalkSystemSchema(MetaParser):
    """ Schema for:
            * show snmp mib walk system
    """

    schema = {
        "snmp-object-information": {
            "snmp-object": ListOf({
                    "name": str,
                    "object-value": str,
                    Optional("object-value-type"): str,
                    Optional("oid"): str
                }
            ),
        }
    }


class ShowSnmpMibWalkSystem(ShowSnmpMibWalkSystemSchema):
    """ Parser for:
            * show snmp mib walk system
    """
    cli_command = 'show snmp mib walk system'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # sysContact.0  = KHK
        p1 = re.compile(r'^(?P<name>\S+) += +(?P<object_value>.+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()

                snmp_object_list = ret_dict.setdefault("snmp-object-information", {})\
                    .setdefault("snmp-object",[])

                entry = {}
                entry['name'] = group['name']
                entry['object-value'] = group["object_value"]

                snmp_object_list.append(entry)

        return ret_dict

class ShowSnmpConfigurationSchema(MetaParser):
    """ Schema for:
            * show configuration snmp
    """
    '''
    schema = {
        "configuration": {
            "snmp": {
                Optional("location"): str,
                Optional(("contact"): str,
                Optional("community"): [
                    {
                        "community-name": str,
                        Optional("authorization"): str,
                        Optional("clients"): [
                            {
                                "name": str,
                                Optional("restrict"): bool
                            },
                        ]
                    },
                ],
                Optional("trap-options"): {
                    "source-address": str
                },
                Optional("trap-group"): {
                    "trap-group-name": str,
                    Optional("version"): str,
                    Optional("categories"): [
                        {
                            "name": str,
                        },
                    ],
                    Optional("targets"): [
                        {
                            "name": str
                        },
                    ]
                }
            }
        },
    }
    '''

    schema = {
        "configuration": {
            "snmp": {
                Optional("location"): str,
                Optional("contact"): str,
                Optional("community"): ListOf({
                    "name": str,
                    Optional("authorization"): str,
                    Optional("clients"): ListOf({
                        "name": str,
                        Optional("restrict"): bool
                    }),
                }),
                Optional("trap-options"): {
                    "source-address": str
                },
                Optional("trap-group"): {
                    "name": str,
                    Optional("version"): str,
                    Optional("categories"): ListOf({
                        "name": str,
                    }),
                    Optional("targets"): ListOf({
                        "name": str,
                    }),
                }
            }
        }
    }


class ShowSnmpConfiguration(ShowSnmpConfigurationSchema):
    """ Parser for:
            * show configuration snmp
    """
    cli_command = 'show configuration snmp'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # location TH-HK2/floor_1B-002/rack_KHK1104;
        p1 = re.compile(r'^location +(?P<location>.+);+$')

        # contact KHK;
        p2 = re.compile(r'^contact +(?P<contact>.+);+$')

        # community safaripub {
        #     authorization read-only;
        #     clients {
        #         10.169.5.0/25;
        #         0.0.0.0/0 restrict;
        #         2001:db8:d38a:cf16::/64;
        #         2001:db8:d38a:d3e9::/64;
        #     }
        # }
        p3 = re.compile(r'^(community +(?P<name>.+) +\{)$')
        p4 = re.compile(r'^(authorization +(?P<authorization>.+);)$')
        p5 = re.compile(r'^(?P<client>((\d+\.[\d\.]+\/[\d]+)|(\w+\:[\w\:]+\/[\d]+)|(0x\d+))([\s\S])*);$')

        # trap-options {
        #     source-address lo0;
        # }
        p6 = re.compile(r'^source-address +(?P<source_address>.+);$')

        # trap-group safaripub {
        #     version v1;
        #     categories {
        #         chassis;
        #         link;
        #         routing;
        #     }
        #     targets {
        #         10.64.99.32;
        #         10.169.249.67;
        #     }
        # }
        p7 = re.compile(r'^trap-group +(?P<name>.+) +\{$')
        p8 = re.compile(r'^version +(?P<version>.+);$')
        p9 = re.compile(r'^categories +\{(?P<categories>.+);$')
        p10 = re.compile(r'^(?P<target>((\d+\.[\d\.]+)|(\w+\:[\w\:]+)|(0x\d+)));$')

        ret_dict = {}
        inner_block_text = ''
        category_block_started = False

        for line in out.splitlines():
            line = line.strip()

            # location TH-HK2/floor_1B-002/rack_KHK1104;
            m = p1.match(line)
            if m:
                group = m.groupdict()
                snmp_dict = ret_dict.setdefault("configuration", {})\
                    .setdefault("snmp", {})
                snmp_dict['location'] = group['location']
                continue

            # contact KHK;
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if "configuration" not in ret_dict:
                    snmp_dict = ret_dict.setdefault("configuration", {}) \
                        .setdefault("snmp", {})
                snmp_dict['contact'] = group['contact']
                continue

            # community safaripub {
            #     authorization read-only;
            #     clients {
            #         10.169.5.0/25;
            #         0.0.0.0/0 restrict;
            #         2001:db8:d38a:cf16::/64;
            #         2001:db8:d38a:d3e9::/64;
            #     }
            # }
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if "configuration" not in ret_dict:
                    snmp_dict = ret_dict.setdefault("configuration", {}) \
                        .setdefault("snmp", {})
                if not snmp_dict.get('community', []):
                    community_list = snmp_dict.setdefault('community', [])
                community_list.append({})
                community_list[-1]['name'] = group['name']

            m = p4.match(line)
            if m:
                group = m.groupdict()
                community_list[-1]['authorization'] = group['authorization']

            if 'client' in line:
                community_list[-1]['clients'] = []
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                client = group['client']
                if '/' in client:
                    client = client.split()
                    if client:
                        client_dict = {}
                        client_dict['name'] = client[0]
                        if len(client) > 1 and 'restrict' in client:
                            client_dict['restrict'] = True
                        community_list[-1]['clients'].append(client_dict)
                continue

            # trap-options {
            #     source-address lo0;
            # }
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if "configuration" not in ret_dict:
                    snmp_dict = ret_dict.setdefault("configuration", {}) \
                        .setdefault("snmp", {})
                trap_options = snmp_dict.setdefault('trap-options', {})
                trap_options['source-address'] = group['source_address']
                continue


            # trap-group safaripub {
            #     version v1;
            #     categories {
            #         chassis;
            #         link;
            #         routing;
            #     }
            #     targets {
            #         10.64.99.32;
            #         10.169.249.67;
            #     }
            # }
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if "configuration" not in ret_dict:
                    snmp_dict = ret_dict.setdefault("configuration", {}) \
                        .setdefault("snmp", {})
                trap_group = snmp_dict.setdefault('trap-group', {})
                trap_group['name'] = group['name']
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                trap_group['version'] = group['version']
                continue

            if 'categories' in line:
                category_block_started = True

            if category_block_started:
                if not '}' in line:
                    inner_block_text += line
                    continue

            if inner_block_text and category_block_started:
                category_block_started = False
                m = p9.match(inner_block_text)
                if m:
                    group = m.groupdict()
                    categories = trap_group.setdefault('categories', [])
                    for category in group['categories'].split(';'):
                        categories.append({'name': category})
                inner_block_text = ''
                continue

            if 'targets' in line:
                targets = trap_group.setdefault('targets', [])

            m = p10.match(line)
            if m:
                group = m.groupdict()
                targets.append({'name': group['target']})
                continue

        return ret_dict


class ShowSnmpStatisticsSchema(MetaParser):
    """ Schema for:
            * show snmp statistics
    """
    '''
    schema = {
        "snmp-statistics": {
            "snmp-input-statistics": {
                "packets": str,
                "bad-versions": str,
                "bad-community-names": str,
                "bad-community-uses": str,
                "asn-parse-errors": str,
                "too-bigs": str,
                "no-such-names": str,
                "bad-values": str,
                "read-onlys": str,
                "general-errors": str,
                "total-request-varbinds": str,
                "total-set-varbinds": str,
                "get-requests": str,
                "get-nexts": str,
                "set-requests": str,
                "get-responses": str,
                "traps": str,
                "silent-drops": str,
                "proxy-drops": str,
                "commit-pending-drops": str,
                "throttle-drops": str,
                "duplicate-request-drops": str
            },
            "snmp-v3-input-statistics": {
                "unknown-secmodels": str,
                "invalid-msgs": str,
                "unknown-pduhandlers": str,
                "unavail-contexts": str,
                "unknown-contexts": str,
                "unsupported-seclevels": str,
                "not-in-timewindows": str,
                "unknown-usernames": str,
                "unknown-eids": str,
                "wrong-digests": str,
                "decrypt-errors": str
            },
            "snmp-output-statistics": {
                "packets": str,
                "too-bigs": str,
                "no-such-names": str,
                "bad-values": str,
                "general-errors": str,
                "get-requests": str,
                "get-nexts": str,
                "set-requests": str,
                "get-responses": str,
                "traps": str
            },
            Optional("snmp-performance-statistics"): {
                "average-response-time": str,
                "one-minute-request-throughput": str,
                "five-minute-request-throughput": str,
                "fifteen-minute-request-throughput": str,
                "one-minute-response-throughput": str,
                "five-minute-response-throughput": str,
                "fifteen-minute-response-throughput": str
            }
        }
    }
    '''
    # Sub Schema snmp community
    def validate_community_list(value):

        if not isinstance(value, list):
            raise SchemaError('snmp community is not a list')
        snmp_community_schema = Schema({
                    "name": str,
                    "authorization": str,
                    "clients": ListOf({
                        "name": str,
                        Optional("restrict"): bool
                    }),
                })
        # Validate each dictionary in list
        for item in value:
            snmp_community_schema.validate(item)
        return value

    # Sub Schema snmp categories or targets
    def validate_categories_or_targets_list(value):
        if not isinstance(value, list):
            raise SchemaError('snmp categories is not a list')

        snmp_categories_or_targets_schema = Schema({
            "name": str,
        })
        # Validate each dictionary in list
        for item in value:
            snmp_categories_or_targets_schema.validate(item)
        return value

    schema = {
        "snmp-statistics": {
            "snmp-input-statistics": {
                "packets": str,
                "bad-versions": str,
                "bad-community-names": str,
                "bad-community-uses": str,
                "asn-parse-errors": str,
                "too-bigs": str,
                "no-such-names": str,
                "bad-values": str,
                "read-onlys": str,
                "general-errors": str,
                "total-request-varbinds": str,
                "total-set-varbinds": str,
                "get-requests": str,
                "get-nexts": str,
                "set-requests": str,
                "get-responses": str,
                "traps": str,
                "silent-drops": str,
                "proxy-drops": str,
                "commit-pending-drops": str,
                "throttle-drops": str,
                "duplicate-request-drops": str
            },
            "snmp-v3-input-statistics": {
                "unknown-secmodels": str,
                "invalid-msgs": str,
                "unknown-pduhandlers": str,
                "unavail-contexts": str,
                "unknown-contexts": str,
                "unsupported-seclevels": str,
                "not-in-timewindows": str,
                "unknown-usernames": str,
                "unknown-eids": str,
                "wrong-digests": str,
                "decrypt-errors": str
            },
            "snmp-output-statistics": {
                "packets": str,
                "too-bigs": str,
                "no-such-names": str,
                "bad-values": str,
                "general-errors": str,
                "get-requests": str,
                "get-nexts": str,
                "set-requests": str,
                "get-responses": str,
                "traps": str
            },
            Optional("snmp-performance-statistics"): {
                "average-response-time": str,
                "one-minute-request-throughput": str,
                "five-minute-request-throughput": str,
                "fifteen-minute-request-throughput": str,
                "one-minute-response-throughput": str,
                "five-minute-response-throughput": str,
                "fifteen-minute-response-throughput": str
            }
        }
    }


class ShowSnmpStatistics(ShowSnmpStatisticsSchema):
    """ Parser for:
            * show snmp statistics
    """
    cli_command = 'show snmp statistics'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # SNMP statistics:
        p1 = re.compile(r'^SNMP +statistics:$')

        # Input:
        p2 = re.compile(r'^Input:$')

        # Packets: 8, Bad versions: 0, Bad community names: 0,
        # Bad community uses: 0, ASN parse errors: 0,
        # Too bigs: 0, No such names: 0, Bad values: 0,
        # Read onlys: 0, General errors: 0,
        # Total request varbinds: 8, Total set varbinds: 0,
        # Get requests: 0, Get nexts: 8, Set requests: 0,
        # Get responses: 0, Traps: 0,
        # Silent drops: 0, Proxy drops: 0, Commit pending drops: 0,
        # Throttle drops: 0, Duplicate request drops: 0
        p3 = re.compile(
            r'^(Packets: (?P<packets>\S+))|(Bad versions: (?P<bad_versions>\S+))|(Bad community names: (?P<bad_community_names>\S+))'
            r'|(Bad community uses: (?P<bad_community_uses>\S+))|(ASN parse errors: (?P<asn_parse_errors>\S+))'
            r'|(Too bigs: (?P<too_bigs>\S+))|(No such names: (?P<no_such_names>\S+))|(Bad values: (?P<bad_values>\S+))'
            r'|(Read onlys: (?P<read_onlys>\S+))|(General errors: (?P<general_errors>\S+))'
            r'|(Total request varbinds: (?P<total_request_varbinds>\S+))|(Total set varbinds: (?P<total_set_varbinds>\S+))'
            r'|(Get requests: (?P<get_requests>\S+))|(Get nexts: (?P<get_nexts>\S+))|(Set requests: (?P<set_requests>\S+))'
            r'|(Get responses: (?P<get_responses>\S+))|(Traps: (?P<traps>\S+))'
            r'|(Silent drops: (?P<silent_drops>\S+))|(Proxy drops: (?P<proxy_drops>\S+))|(Commit pending drops: (?P<commit_pending_drops>\S+))'
            r'|(Throttle drops: (?P<throttle_drops>\S+))|(Duplicate request drops: (?P<duplicate_request_drops>\S+))$')

        # V3 Input:
        p4 = re.compile(r'^V3 Input:$')

        # Unknown security models: 0, Invalid messages: 0
        # Unknown pdu handlers: 0, Unavailable contexts: 0
        # Unknown contexts: 0, Unsupported security levels: 0
        # Not in time windows: 0, Unknown user names: 0
        # Unknown engine ids: 0, Wrong digests: 0, Decryption errors: 0
        p5 = re.compile(
            r'^(Unknown security models: (?P<unknown_secmodels>\S+))|(Invalid messages: (?P<invalid_msgs>\S+))'
            r'|(Unknown pdu handlers: (?P<unknown_pduhandlers>\S+))|(Unavailable contexts: (?P<unavail_contexts>\S+))'
            r'|(Unknown contexts: (?P<unknown_contexts>\S+))|(Unsupported security levels: (?P<unsupported_seclevels>\S+))'
            r'|(Not in time windows: (?P<not_in_timewindows>\S+))|(Unknown user names: (?P<unknown_usernames>\S+))'
            r'|(Unknown engine ids: (?P<unknown_eids>\S+))|(Wrong digests: (?P<wrong_digests>\S+))|(Decryption errors: (?P<decrypt_errors>\S+))$')

        # Output:
        p6 = re.compile(r'^Output:$')

        # Packets: 8, Too bigs: 0, No such names: 0,
        # Bad values: 0, General errors: 0,
        #   Get requests: 0, Get nexts: 0, Set requests: 0,
        # Get responses: 8, Traps: 0
        p7 = re.compile(
            r'^(Packets: (?P<packets>\S+))|(Too bigs: (?P<too_bigs>\S+))|(No such names: (?P<no_such_names>\S+))'
            r'|(Bad values: (?P<bad_values>\S+))|(General errors: (?P<general_errors>\S+))'
            r'|(Get requests: (?P<get_requests>\S+))|(Get nexts: (?P<get_nexts>\S+))|(Set requests: (?P<set_requests>\S+))'
            r'|(Get responses: (?P<get_responses>\S+))|(Traps: (?P<traps>\S+))$')

        # Performance:
        p8 = re.compile(r'^Performance:$')

        # Average response time(ms): 10.91
        p9 = re.compile(r'^(Average response time\(ms\): (?P<average_response_time>\S+))$')

        # Number of requests dispatched to subagents in last:
        p10 = re.compile(r'Number of requests dispatched to subagents in last:$')

        # 1 minute:0, 5 minutes:0, 15 minutes:0
        p11 = re.compile(r'(1 minute:(?P<one_minute_request_throughput>\S+))'
                        r'|(5 minutes:(?P<five_minute_request_throughput>\S+))'
                        r'|(15 minutes:(?P<fifteen_minute_request_throughput>\S+))$')

        # Number of responses dispatched to NMS in last:
        p12 = re.compile(r'Number of responses dispatched to NMS in last:$')

        # 1 minute:0, 5 minutes:0, 15 minutes:0
        p13 = re.compile(r'(1 minute:(?P<one_minute_response_throughput>\S+))'
                        r'|(5 minutes:(?P<five_minute_response_throughput>\S+))'
                        r'|(15 minutes:(?P<fifteen_minute_response_throughput>\S+))$')

        ret_dict = {}
        performance_request = False
        snmp_statistics = {}

        for line in out.splitlines():
            line = line.strip()
            line = line.split(',')
            for elem in line:
                elem = elem.strip()

                # SNMP statistics:
                m = p1.match(elem)
                if m:
                    snmp_statistics = ret_dict.setdefault("snmp-statistics", {})
                    continue

                # Input:
                m = p2.match(elem)
                if m:
                    snmp_input_statistics = snmp_statistics.setdefault("snmp-input-statistics", {})
                    continue

                # Packets: 8, Bad versions: 0, Bad community names: 0,
                # Bad community uses: 0, ASN parse errors: 0,
                # Too bigs: 0, No such names: 0, Bad values: 0,
                # Read onlys: 0, General errors: 0,
                # Total request varbinds: 8, Total set varbinds: 0,
                # Get requests: 0, Get nexts: 8, Set requests: 0,
                # Get responses: 0, Traps: 0,
                # Silent drops: 0, Proxy drops: 0, Commit pending drops: 0,
                # Throttle drops: 0, Duplicate request drops: 0
                if snmp_statistics and 'snmp-v3-input-statistics' not in snmp_statistics and \
                        'snmp-output-statistics' not in snmp_statistics and \
                        'snmp-performance-statistics' not in snmp_statistics:
                    m = p3.match(elem)
                    if m:
                        group = m.groupdict()
                        for key, value in group.items():
                            if value:
                                snmp_input_statistics[key.replace('_', '-')] = value
                        continue

                # V3 Input:
                m = p4.match(elem)
                if m:
                    snmp_v3_input_statistics = snmp_statistics.setdefault("snmp-v3-input-statistics", {})
                    continue

                # Unknown security models: 0, Invalid messages: 0
                # Unknown pdu handlers: 0, Unavailable contexts: 0
                # Unknown contexts: 0, Unsupported security levels: 0
                # Not in time windows: 0, Unknown user names: 0
                # Unknown engine ids: 0, Wrong digests: 0, Decryption errors: 0
                if snmp_statistics and 'snmp-output-statistics' not in snmp_statistics and \
                        'snmp-performance-statistics' not in snmp_statistics:
                    m = p5.match(elem)
                    if m:
                        group = m.groupdict()
                        for key, value in group.items():
                            if value:
                                snmp_v3_input_statistics[key.replace('_', '-')] = value
                        continue

                # Output:
                m = p6.match(elem)
                if m:
                    snmp_output_statistics = snmp_statistics.setdefault("snmp-output-statistics", {})
                    continue

                # Packets: 8, Too bigs: 0, No such names: 0,
                # Bad values: 0, General errors: 0,
                #   Get requests: 0, Get nexts: 0, Set requests: 0,
                # Get responses: 8, Traps: 0
                if snmp_statistics and 'snmp-performance-statistics' not in snmp_statistics:
                    m = p7.match(elem)
                    if m:
                        group = m.groupdict()
                        for key, value in group.items():
                            if value:
                                snmp_output_statistics[key.replace('_', '-')] = value
                        continue

                # Performance:
                m = p8.match(elem)
                if m:
                    snmp_performance_statistics = snmp_statistics.setdefault("snmp-performance-statistics", {})
                    continue

                # Average response time(ms): 10.91
                m = p9.match(elem)
                if m:
                    group = m.groupdict()
                    for key, value in group.items():
                        if value:
                            snmp_performance_statistics[key.replace('_', '-')] = value
                    continue

                # Number of requests dispatched to subagents in last:
                m = p10.match(elem)
                if m:
                    performance_request = True
                    continue

                # 1 minute:0, 5 minutes:0, 15 minutes:0
                if performance_request:
                    m = p11.match(elem)
                    if m:
                        group = m.groupdict()
                        for key, value in group.items():
                            if value:
                                snmp_performance_statistics[key.replace('_', '-')] = value
                        continue

                # Number of responses dispatched to NMS in last:
                m = p12.match(elem)
                if m:
                    performance_request = False
                    continue

                # 1 minute:0, 5 minutes:0, 15 minutes:0
                m = p13.match(elem)
                if m:
                    group = m.groupdict()
                    for key, value in group.items():
                        if value:
                            snmp_performance_statistics[key.replace('_', '-')] = value
                    continue

        return ret_dict
