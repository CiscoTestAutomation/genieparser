"""show_system.py

JunOS parsers for the following show commands:
    - 'show system boot-messages no-forwarding'
    - 'show sysyem commit'
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use
from genie.metaparser.util.exceptions import SchemaTypeError

class ShowSystemBufferSchema(MetaParser):
    """ Schema for:
            - 'show system buffer'
    """

    schema = {
        "memory-statistics": {
            "cached-bytes": str,
            "cached-jumbo-clusters-16k": str,
            "cached-jumbo-clusters-4k": str,
            "cached-jumbo-clusters-9k": str,
            "cached-mbuf-clusters": str,
            "cached-mbufs": str,
            "cluster-failures": str,
            "current-bytes-in-use": str,
            "current-jumbo-clusters-16k": str,
            "current-jumbo-clusters-4k": str,
            "current-jumbo-clusters-9k": str,
            "current-mbuf-clusters": str,
            "current-mbufs": str,
            "io-initiated": str,
            "jumbo-cluster-failures-16k": str,
            "jumbo-cluster-failures-4k": str,
            "jumbo-cluster-failures-9k": str,
            "max-jumbo-clusters-16k": str,
            "max-jumbo-clusters-4k": str,
            "max-jumbo-clusters-9k": str,
            "max-mbuf-clusters": str,
            "mbuf-failures": str,
            "packet-count": str,
            "packet-failures": str,
            "packet-free": str,
            "sfbuf-requests-delayed": str,
            "sfbuf-requests-denied": str,
            "total-bytes": str,
            "total-jumbo-clusters-16k": str,
            "total-jumbo-clusters-4k": str,
            "total-jumbo-clusters-9k": str,
            "total-mbuf-clusters": str,
            "total-mbufs": str
        }
    }


class ShowSystemBuffer(ShowSystemBufferSchema):
    """ Parser for:
            - 'show system buffer'
    """

    cli_command = "show system buffers"

    def cli(self, node_id=None, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init vars
        ret_dict = {}

        # 588/2142/2730 mbufs in use (current/cache/total)
        p1 = re.compile(r'^(?P<current_mbufs>\S+)/(?P<cached_mbufs>\S+)/(?P<total_mbufs>\S+) +mbufs +in +use +\(current/cache/total\)$')
        # p1 = re.compile(r'^588/2142/2730 mbufs in use (current/cache/total)$')

        # 516/714/1230/124756 mbuf clusters in use (current/cache/total/max)
        p2 = re.compile(r'^(?P<current_mbuf_clusters>\S+)/(?P<cached_mbuf_clusters>\S+)/(?P<total_mbuf_clusters>\S+)/(?P<max_mbuf_clusters>\S+) +mbuf +clusters +in use +\(current/cache/total/max\)$')

        # 513/499 mbuf+clusters out of packet secondary zone in use (current/cache)
        p3 = re.compile(r'^(?P<packet_count>\S+)/(?P<packet_free>\S+) +mbuf\+clusters +out +of +packet +secondary +zone +in +use +\(current/cache\)$')

        # 0/2/2/62377 4k (page size) jumbo clusters in use (current/cache/total/max)
        p4 = re.compile(r'^(?P<current_jumbo_clusters_4k>\S+)/(?P<cached_jumbo_clusters_4k>\S+)/(?P<total_jumbo_clusters_4k>\S+)/(?P<max_jumbo_clusters_4k>\S+) +4k +\(page +size\) +jumbo +clusters +in +use +\(current/cache/total/max\)$')

        # 0/0/0/18482 9k (page size) jumbo clusters in use (current/cache/total/max)
        p5 = re.compile(r'^(?P<current_jumbo_clusters_9k>\S+)/(?P<cached_jumbo_clusters_9k>\S+)/(?P<total_jumbo_clusters_9k>\S+)/(?P<max_jumbo_clusters_9k>\S+) +9k +\(page +size\) +jumbo +clusters +in +use +\(current/cache/total/max\)$')

        # 0/0/0/10396 16k (page size) jumbo clusters in use (current/cache/total/max)
        p6 = re.compile(r'^(?P<current_jumbo_clusters_16k>\S+)/(?P<cached_jumbo_clusters_16k>\S+)/(?P<total_jumbo_clusters_16k>\S+)/(?P<max_jumbo_clusters_16k>\S+) +16k +\(page +size\) +jumbo +clusters +in +use +\(current/cache/total/max\)$')

        # 1179K/1971K/3150K bytes allocated to network (current/cache/total)
        p7 =re.compile(r'^(?P<current_bytes_in_use>\S+)K/(?P<cached_bytes>\S+)K/(?P<total_bytes>\S+)K +bytes +allocated +to +network +\(current/cache/total\)$')

        # 0/0/0 requests for mbufs denied (mbufs/clusters/mbuf+clusters)
        p8 = re.compile(r'^(?P<mbuf_failures>\S+)/(?P<cluster_failures>\S+)/(?P<packet_failures>\S+) +requests +for +mbufs +denied +\(mbufs/clusters/mbuf\+clusters\)$')

        # 0/0/0 requests for jumbo clusters denied (4k/9k/16k)
        p9 =re.compile(r'^(?P<jumbo_cluster_failures_4k>\S+)/(?P<jumbo_cluster_failures_9k>\S+)/(?P<jumbo_cluster_failures_16k>\S+) +requests +for +jumbo +clusters +denied +\(4k/9k/16k\)$')

        # 0 requests for sfbufs denied
        p10 = re.compile(r'^(?P<sfbuf_requests_denied>\S+) +requests +for +sfbufs +denied$')

        # 0 requests for sfbufs delayed
        p11 = re.compile(r'^(?P<sfbuf_requests_delayed>\S+) +requests +for +sfbufs +delayed$')

        # 0 requests for I/O initiated by sendfile
        p12 = re.compile(r'^(?P<io_initiated>\S+) +requests +for +I/O +initiated +by +sendfile$')

        for line in out.splitlines():
            line = line.strip()

            # 588/2142/2730 mbufs in use (current/cache/total)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 516/714/1230/124756 mbuf clusters in use (current/cache/total/max)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 513/499 mbuf+clusters out of packet secondary zone in use (current/cache)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 0/2/2/62377 4k (page size) jumbo clusters in use (current/cache/total/max)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 0/0/0/18482 9k (page size) jumbo clusters in use (current/cache/total/max)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 0/0/0/10396 16k (page size) jumbo clusters in use (current/cache/total/max)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 1179K/1971K/3150K bytes allocated to network (current/cache/total)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 0/0/0 requests for mbufs denied (mbufs/clusters/mbuf+clusters)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 0/0/0 requests for jumbo clusters denied (4k/9k/16k)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 0 requests for sfbufs denied
            m = p10.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 0 requests for sfbufs delayed
            m = p11.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # 0 requests for I/O initiated by sendfile
            m = p12.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

        return ret_dict

class ShowSystemCommitSchema(MetaParser):
    """ Schema for:
            * show sysyem commit
    """

    # Sub Schema commit-history
    def validate_commit_history_list(value):
        # Pass commit-history list as value
        if not isinstance(value, list):
            raise SchemaTypeError('commit-history is not a list')
        commit_history_schema = Schema({
                    "client": str,
                    "date-time": {
                        "#text": str
                    },
                    "sequence-number": str,
                    "user": str
                })
        # Validate each dictionary in list
        for item in value:
            commit_history_schema.validate(item)
        return value

    schema = {
        "commit-information": {
            "commit-history": Use(validate_commit_history_list)
        }
    }

class ShowSystemCommit(ShowSystemCommitSchema):
    """ Parser for:
            * show sysyem commit
    """
    cli_command = 'show system commit'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 0   2020-03-05 16:04:34 UTC by kddi via cli
        p1 = re.compile(r'^(?P<sequence_number>\d+) +(?P<date_time>([\d\-]+) +(([\d\:]+)) (\S+)) +by +(?P<user>\S+) +via +(?P<client>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 0   2020-03-05 16:04:34 UTC by kddi via cli
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("commit-information", {}).setdefault("commit-history", [])
                entry = {}
                entry['client'] = group['client']
                entry['date-time'] = {"#text": group['date_time']}
                entry['sequence-number'] = group['sequence_number']
                entry['user'] = group['user']

                entry_list.append(entry)
                continue

        return ret_dict


class ShowSystemQueuesSchema(MetaParser):
    """ Schema for:
            * show sysyem queues
    """

    """
        {
        "queues-statistics": {
            "interface-queues-statistics": {
                "interface-queue": [
                    {
                        "max-octets-allowed": str,
                        "max-packets-allowed": str,
                        "name": str,
                        "number-of-queue-drops": str,
                        "octets-in-queue": str,
                        "packets-in-queue": str
                    }
                ]
            },
            "protocol-queues-statistics": {
                "protocol-queue": [
                    {}
                ]
            }
        }
    }
    """

    # Sub Schema interface-queue
    def validate_interface_queue_list(value):
        # Pass interface-queue list as value
        if not isinstance(value, list):
            raise SchemaTypeError('commit-history is not a list')
        interface_queue_schema = Schema({
                    "max-octets-allowed": str,
                        "max-packets-allowed": str,
                        "name": str,
                        "number-of-queue-drops": str,
                        "octets-in-queue": str,
                        "packets-in-queue": str
                })
        # Validate each dictionary in list
        for item in value:
            interface_queue_schema.validate(item)
        return value

    schema = {
        "queues-statistics": {
            "interface-queues-statistics": {
                "interface-queue": Use(validate_interface_queue_list)
            },
            "protocol-queues-statistics": {
                "protocol-queue": Use(validate_interface_queue_list)
            }
        }
    }

class ShowSystemQueues(ShowSystemQueuesSchema):
    """ Parser for:
            * show system queues
    """
    cli_command = 'show system queues'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # lsi                             0        12500        0       41        0
        p1 = re.compile(r'^(?P<name>\S+) +(?P<octets_in_queue>\d+) +(?P<max_octets_allowed>\d+) +(?P<packets_in_queue>\d+) +(?P<max_packets_allowed>\d+) +(?P<number_of_queue_drops>\d+)$')

        # input protocol              bytes          max  packets      max    drops
        p2 = re.compile(r'^input +protocol +bytes +max +packets +max +drops$')

        interface_flag = True
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # lsi                             0        12500        0       41        0
            m = p1.match(line)
            if m:
                group = m.groupdict()

                if interface_flag:
                    entry_list = ret_dict.setdefault("queues-statistics", {}).setdefault("interface-queues-statistics", {}).setdefault("interface-queue", [])
                else:
                    entry_list = ret_dict.setdefault("queues-statistics", {}).setdefault("protocol-queues-statistics", {}).setdefault("protocol-queue", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                entry_list.append(entry)
                continue

            # input protocol              bytes          max  packets      max    drops
            m = p2.match(line)
            if m:
                interface_flag = False

        # print()
        # print("heerereee")
        # import pprint
        # pprint.pprint(ret_dict)

        return ret_dict
