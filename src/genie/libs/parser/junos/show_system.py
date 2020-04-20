"""show_system.py

JunOS parsers for the following show commands:
    - 'show system commit'
    - 'show system queues'
    - 'show system queues no-forwarding'
    - 'show system buffers'
    - 'show system users'
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use
from genie.metaparser.util.exceptions import SchemaTypeError

class ShowSystemBufferSchema(MetaParser):
    """ Schema for:
            - 'show system buffers'
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
            - 'show system buffers'
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
        p1 = re.compile(r'^(?P<current_mbufs>\S+)/(?P<cached_mbufs>\S+)/'
        r'(?P<total_mbufs>\S+) +mbufs +in +use +\(current/cache/total\)$')

        # 516/714/1230/124756 mbuf clusters in use (current/cache/total/max)
        p2 = re.compile(r'^(?P<current_mbuf_clusters>\S+)/(?P<cached_mbuf_clusters>\S+)'
        r'/(?P<total_mbuf_clusters>\S+)/(?P<max_mbuf_clusters>\S+) +mbuf +clusters'
        r' +in use +\(current/cache/total/max\)$')

        # 513/499 mbuf+clusters out of packet secondary zone in use (current/cache)
        p3 = re.compile(r'^(?P<packet_count>\S+)/(?P<packet_free>\S+) +mbuf\+clusters'
        r' +out +of +packet +secondary +zone +in +use +\(current/cache\)$')

        # 0/2/2/62377 4k (page size) jumbo clusters in use (current/cache/total/max)
        p4 = re.compile(r'^(?P<current_jumbo_clusters_4k>\S+)/'
        r'(?P<cached_jumbo_clusters_4k>\S+)/(?P<total_jumbo_clusters_4k>\S+)/'
        r'(?P<max_jumbo_clusters_4k>\S+) +4k +\(page +size\) +jumbo +clusters +in'
        r' +use +\(current/cache/total/max\)$')

        # 0/0/0/18482 9k (page size) jumbo clusters in use (current/cache/total/max)
        p5 = re.compile(r'^(?P<current_jumbo_clusters_9k>\S+)/'
        r'(?P<cached_jumbo_clusters_9k>\S+)/(?P<total_jumbo_clusters_9k>\S+)/'
        r'(?P<max_jumbo_clusters_9k>\S+) +9k +\(page +size\) +jumbo +clusters +in'
        r' +use +\(current/cache/total/max\)$')

        # 0/0/0/10396 16k (page size) jumbo clusters in use (current/cache/total/max)
        p6 = re.compile(r'^(?P<current_jumbo_clusters_16k>\S+)/(?P<cached_jumbo_clusters_16k>\S+)'
        r'/(?P<total_jumbo_clusters_16k>\S+)/(?P<max_jumbo_clusters_16k>\S+) +16k +'
        r'\(page +size\) +jumbo +clusters +in +use +\(current/cache/total/max\)$')

        # 1179K/1971K/3150K bytes allocated to network (current/cache/total)
        p7 =re.compile(r'^(?P<current_bytes_in_use>\S+)K/(?P<cached_bytes>\S+)K/'
        r'(?P<total_bytes>\S+)K +bytes +allocated +to +network +\(current/cache/total\)$')

        # 0/0/0 requests for mbufs denied (mbufs/clusters/mbuf+clusters)
        p8 = re.compile(r'^(?P<mbuf_failures>\S+)/(?P<cluster_failures>\S+)/(?P<packet_failures>\S+)'
        r' +requests +for +mbufs +denied +\(mbufs/clusters/mbuf\+clusters\)$')

        # 0/0/0 requests for jumbo clusters denied (4k/9k/16k)
        p9 =re.compile(r'^(?P<jumbo_cluster_failures_4k>\S+)/(?P<jumbo_cluster_failures_9k>\S+)/'
        r'(?P<jumbo_cluster_failures_16k>\S+) +requests +for +jumbo +clusters +denied +\(4k/9k/16k\)$')

        # 0 requests for sfbufs denied
        p10 = re.compile(r'^(?P<sfbuf_requests_denied>\S+) +'
        r'requests +for +sfbufs'
        r' +denied$')

        # 0 requests for sfbufs delayed
        p11 = re.compile(r'^(?P<sfbuf_requests_delayed>\S+) +requests +for'
        r' +sfbufs +delayed$')

        # 0 requests for I/O initiated by sendfile
        p12 = re.compile(r'^(?P<io_initiated>\S+) +requests +for +I/O +initiated'
        r' +by +sendfile$')

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

class ShowSystemUsersSchema(MetaParser):
    """ Schema for:
            * show system users
    """
    """ schema = {
    Optional("@xmlns:junos"): str,
    "system-users-information": {
        Optional("@xmlns"): str,
        "uptime-information": {
            "active-user-count": {
                "#text": str,
                Optional("@junos:format"): str
            },
            "date-time": {
                "#text": str,
                Optional("@junos:seconds"): str
            },
            "load-average-1": str,
            "load-average-15": str,
            "load-average-5": str,
            "up-time": {
                "#text": str,
                Optional("@junos:seconds"): str
            },
            "user-table": {
                "user-entry": [
                    {
                        "command": str,
                        "from": str,
                        "idle-time": {
                            "#text": str,
                            Optional("@junos:seconds"): str
                        },
                        "login-time": {
                            "#text": str,
                            Optional("@junos:seconds"): str
                        },
                        "tty": str,
                        "user": str
                    }
                ]
            }
        }
    }
} """


    def validate_system_user_list(value):
            if not isinstance(value, list):
                raise SchemaTypeError('ospf-neighbor is not a list')
            neighbor_schema = Schema({
                "command": str,
                            "from": str,
                            "idle-time": {
                                "#text": str,
                                Optional("@junos:seconds"): str
                            },
                            "login-time": {
                                "#text": str,
                                Optional("@junos:seconds"): str
                            },
                            "tty": str,
                            "user": str
            })
            for item in value:
                neighbor_schema.validate(item)
            return value
    schema = {
            Optional("@xmlns:junos"): str,
        "system-users-information": {
            Optional("@xmlns"): str,
            "uptime-information": {
                "active-user-count": {
                    "#text": str,
                    Optional("@junos:format"): str
                },
                "date-time": {
                    "#text": str,
                    Optional("@junos:seconds"): str
                },
                "load-average-1": str,
                "load-average-15": str,
                "load-average-5": str,
                "up-time": {
                    "#text": str,
                    Optional("@junos:seconds"): str
                },
                "user-table": {
                    "user-entry": Use(validate_system_user_list)
                }
            }
        }
        }


class ShowSystemUsers(ShowSystemUsersSchema):
    """ Parser for:
            * show system users
    """
    cli_command = 'show system users'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}


        #9:38AM  up 209 days, 37 mins, 3 users, load averages: 0.28, 0.39, 0.37
        p1 = re.compile(r'^(?P<time>[\d\:a-zA-Z]+) +up '
                        r'(?P<days>\w+\s\w+), +(?P<mins>\d+\s+\w+), +'
                        r'(?P<user_count>\d+) +users, +load +averages: '
                        r'(?P<avg1>[\d\.]+), +(?P<avg2>[\d\.]+), +(?P<avg3>[\d\.]+)$')

        #cisco     pts/0    10.1.0.1                          2:35AM      - -cl
        p2 = re.compile(r'^(?P<user>\S+)\s+(?P<tty>\S+)\s+'
                        r'(?P<from>[\d\.]+)\s+(?P<login>\S+)'
                        r'\s+(?P<idle>\S+)\s+(?P<what>\S+)$')


        for line in out.splitlines():
            line = line.strip()

            #9:38AM  up 209 days, 37 mins, 3 users, load averages: 0.28, 0.39, 0.37
            m = p1.match(line)
            if m:
                group = m.groupdict()
                user_table_entry_list = ret_dict.setdefault('system-users-information', {}). \
                    setdefault('uptime-information', {})

                user_entry_list = []
                user_table_entry_list["user-table"] = {"user-entry": user_entry_list}
                date_time_entry_dict = {}
                up_time_entry_dict = {}
                active_users_count = {}

                date_time_entry_dict["#text"] = group['time']
                up_time_entry_dict["#text"] = group['days'] + ', ' + group['mins']
                active_users_count["#text"] = group['user_count']

                user_table_entry_list['active-user-count'] = active_users_count
                user_table_entry_list['up-time'] = up_time_entry_dict
                user_table_entry_list['date-time'] = date_time_entry_dict

                user_table_entry_list["load-average-1"] = group['avg1']
                user_table_entry_list["load-average-15"] = group['avg2']
                user_table_entry_list["load-average-5"] = group['avg3']

                continue

            #cisco     pts/0    10.1.0.1                          2:35AM      - -cl
            m = p2.match(line)
            if m:
                group = m.groupdict()

                entry_dict = {}

                entry_dict["command"] = group["what"]
                entry_dict["from"] = group["from"]
                entry_dict["tty"] = group["tty"]
                entry_dict["user"] = group["user"]

                idle_dict = {}
                login_dict = {}
                idle_dict["#text"] = group['idle']
                login_dict["#text"] = group['login']

                entry_dict["login-time"] = login_dict
                entry_dict["idle-time"] = idle_dict

                user_entry_list.append(entry_dict)

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

        # 0   2020-03-05 16:04:34 UTC by cisco via cli
        p1 = re.compile(r'^(?P<sequence_number>\d+) +(?P<date_time>([\d\-]+) +'
        r'(([\d\:]+)) (\S+)) +by +(?P<user>\S+) +via +(?P<client>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 0   2020-03-05 16:04:34 UTC by cisco via cli
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("commit-information", {})\
                    .setdefault("commit-history", [])
                entry = {}
                entry['client'] = group['client']
                entry['date-time'] = {"#text": group['date_time']}
                entry['sequence-number'] = group['sequence_number']
                entry['user'] = group['user']

                entry_list.append(entry)
                continue

        return ret_dict

