"""show_system.py

JunOS parsers for the following show commands:
    - 'show system commit'
    - 'show system queues'
    - 'show system queues no-forwarding'
    - 'show system buffers'
    - 'show system statistics'
    - 'show system statistics no-forwarding'
    - 'show system buffers no-forwarding'
    - 'show system core-dumps'
    - 'show system core-dumps no-forwarding'
    - 'show system users'
    - 'show system storage'
    - 'show system storage no-forwarding'
    - 'show system connections'
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use, ListOf


class ShowSystemBuffersSchema(MetaParser):
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
            "total-mbufs": str,
        }
    }


class ShowSystemBuffers(ShowSystemBuffersSchema):
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
        p1 = re.compile(
            r"^(?P<current_mbufs>\S+)/(?P<cached_mbufs>\S+)/"
            r"(?P<total_mbufs>\S+) +mbufs +in +use +\(current/cache/total\)$")

        # 516/714/1230/124756 mbuf clusters in use (current/cache/total/max)
        p2 = re.compile(
            r"^(?P<current_mbuf_clusters>\S+)/(?P<cached_mbuf_clusters>\S+)"
            r"/(?P<total_mbuf_clusters>\S+)/(?P<max_mbuf_clusters>\S+) +mbuf +clusters"
            r" +in use +\(current/cache/total/max\)$")

        # 513/499 mbuf+clusters out of packet secondary zone in use (current/cache)
        p3 = re.compile(
            r"^(?P<packet_count>\S+)/(?P<packet_free>\S+) +mbuf\+clusters"
            r" +out +of +packet +secondary +zone +in +use +\(current/cache\)$")

        # 0/2/2/62377 4k (page size) jumbo clusters in use (current/cache/total/max)
        p4 = re.compile(
            r"^(?P<current_jumbo_clusters_4k>\S+)/"
            r"(?P<cached_jumbo_clusters_4k>\S+)/(?P<total_jumbo_clusters_4k>\S+)/"
            r"(?P<max_jumbo_clusters_4k>\S+) +4k +\(page +size\) +jumbo +clusters +in"
            r" +use +\(current/cache/total/max\)$")

        # 0/0/0/18482 9k (page size) jumbo clusters in use (current/cache/total/max)
        p5 = re.compile(
            r"^(?P<current_jumbo_clusters_9k>\S+)/"
            r"(?P<cached_jumbo_clusters_9k>\S+)/(?P<total_jumbo_clusters_9k>\S+)/"
            r"(?P<max_jumbo_clusters_9k>\S+) +9k +\(page +size\) +jumbo +clusters +in"
            r" +use +\(current/cache/total/max\)$")

        # 0/0/0/10396 16k (page size) jumbo clusters in use (current/cache/total/max)
        p6 = re.compile(
            r"^(?P<current_jumbo_clusters_16k>\S+)/"
            r"(?P<cached_jumbo_clusters_16k>\S+)/(?P<total_jumbo_clusters_16k>\S+)/"
            r"(?P<max_jumbo_clusters_16k>\S+) +16k +\(page +size\) +jumbo +clusters"
            r" +in +use +\(current/cache/total/max\)$")

        # 1179K/1971K/3150K bytes allocated to network (current/cache/total)
        p7 = re.compile(
            r"^(?P<current_bytes_in_use>\S+)K/(?P<cached_bytes>\S+)K/"
            r"(?P<total_bytes>\S+)K +bytes +allocated +to +network +\(current/cache/total\)$"
        )

        # 0/0/0 requests for mbufs denied (mbufs/clusters/mbuf+clusters)
        p8 = re.compile(
            r"^(?P<mbuf_failures>\S+)/(?P<cluster_failures>\S+)/"
            r"(?P<packet_failures>\S+) +requests +for +mbufs +denied +\(mbufs/clusters/mbuf\+clusters\)$"
        )

        # 0/0/0 requests for jumbo clusters denied (4k/9k/16k)
        p9 = re.compile(
            r"^(?P<jumbo_cluster_failures_4k>\S+)/(?P<jumbo_cluster_failures_9k>\S+)"
            r"/(?P<jumbo_cluster_failures_16k>\S+) +requests +for +jumbo +clusters +denied +\(4k/9k/16k\)$"
        )

        # 0 requests for sfbufs denied
        p10 = re.compile(
            r"^(?P<sfbuf_requests_denied>\S+) +requests +for +sfbufs"
            r" +denied$")

        # 0 requests for sfbufs delayed
        p11 = re.compile(r"^(?P<sfbuf_requests_delayed>\S+) +requests +for"
                         r" +sfbufs +delayed$")

        # 0 requests for I/O initiated by sendfile
        p12 = re.compile(
            r"^(?P<io_initiated>\S+) +requests +for +I/O +initiated"
            r" +by +sendfile$")

        for line in out.splitlines():
            line = line.strip()

            # 588/2142/2730 mbufs in use (current/cache/total)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 516/714/1230/124756 mbuf clusters in use (current/cache/total/max)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 513/499 mbuf+clusters out of packet secondary zone in use (current/cache)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 0/2/2/62377 4k (page size) jumbo clusters in use (current/cache/total/max)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 0/0/0/18482 9k (page size) jumbo clusters in use (current/cache/total/max)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 0/0/0/10396 16k (page size) jumbo clusters in use (current/cache/total/max)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 1179K/1971K/3150K bytes allocated to network (current/cache/total)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 0/0/0 requests for mbufs denied (mbufs/clusters/mbuf+clusters)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 0/0/0 requests for jumbo clusters denied (4k/9k/16k)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 0 requests for sfbufs denied
            m = p10.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 0 requests for sfbufs delayed
            m = p11.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # 0 requests for I/O initiated by sendfile
            m = p12.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("memory-statistics", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

        return ret_dict


class ShowSystemBuffersNoForwarding(ShowSystemBuffers):
    """ Parser for:
            - 'show system buffers no-forwarding'
    """

    cli_command = "show system buffers no-forwarding"

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


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
                    "user-entry": ListOf({
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

        # 9:38AM up 209 days, 37 mins, 3 users, load averages: 0.28, 0.39, 0.37
        # 12:58PM up 2 days, 5:30, 2 users, load averages: 0.36, 0.33, 0.35
        # 10:08PM up 7 days, 10:56, 1 user, load averages: 0.02, 0.02, 0.00
        # 1:08AM up 8 days, 5 hrs, 1 user, load averages: 0.07, 0.02, 0.01
        # 9:38AM up 209 day, 37 mins, 3 users, load averages: 0.28, 0.39, 0.37
        p1 = re.compile(
            r'^(?P<time>[\d\:a-zA-Z]+) +up +'
            r'(?P<up_time>(\d+ +(days|day), +)?([\d:]+( +mins)?( +hrs)?)), +'
            r'(?P<user_count>\d+) +user(s)?, +'
            r'load +averages: (?P<avg1>[\d\.]+), +'
            r'(?P<avg2>[\d\.]+), +(?P<avg3>[\d\.]+)$')

        p1_2 = re.compile(r'^USER +TTY +FROM +LOGIN@ +IDLE +WHAT *$')

        #cisco     pts/0    10.1.0.1                          2:35AM      - -cl
        p2 = re.compile(r'^(?P<user>\S+) +(?P<tty>\S+) +(?P<from>\S+) +'
                        r'(?P<login>\S+) +(?P<idle>\S+) +(?P<command>.*)$')

        for line in out.splitlines():
            line = line.strip()

            # 9:38AM up 209 days, 37 mins, 3 users, load averages: 0.28, 0.39, 0.37
            # 12:58PM up 2 days, 5:30, 2 users, load averages: 0.36, 0.33, 0.35
            # 10:08PM up 7 days, 10:56, 1 user, load averages: 0.02, 0.02, 0.00
            # 9:38AM up 209 day, 37 mins, 3 users, load averages: 0.28, 0.39, 0.37
            m = p1.match(line)
            if m:
                group = m.groupdict()
                user_table_entry_list = ret_dict.setdefault('system-users-information', {}). \
                    setdefault('uptime-information', {})

                user_entry_list = []
                user_table_entry_list["user-table"] = {
                    "user-entry": user_entry_list
                }
                date_time_entry_dict = {}
                up_time_entry_dict = {}
                active_users_count = {}

                date_time_entry_dict["#text"] = group['time']
                up_time_entry_dict["#text"] = group['up_time']
                active_users_count["#text"] = group['user_count']

                user_table_entry_list['active-user-count'] = active_users_count
                user_table_entry_list['up-time'] = up_time_entry_dict
                user_table_entry_list['date-time'] = date_time_entry_dict

                user_table_entry_list["load-average-1"] = group['avg1']
                user_table_entry_list["load-average-15"] = group['avg2']
                user_table_entry_list["load-average-5"] = group['avg3']

                continue

            # USER     TTY      FROM                              LOGIN@  IDLE WHAT
            m = p1_2.match(line)
            if m:
                continue

            #cisco     pts/0    10.1.0.1                          2:35AM      - -cl
            m = p2.match(line)
            if m:
                group = m.groupdict()

                entry_dict = {}

                entry_dict["command"] = group["command"]
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

    schema = {
        "commit-information": {
            "commit-history": ListOf({
                "client": str,
                "date-time": {
                    "#text": str
                },
                "sequence-number": str,
                "user": str
            })
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
        p1 = re.compile(
            r'^(?P<sequence_number>\d+) +(?P<date_time>([\d\-]+) +'
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
                    {
                        "max-octets-allowed": str,
                        "max-packets-allowed": str,
                        "name": str,
                        "number-of-queue-drops": str,
                        "octets-in-queue": str,
                        "packets-in-queue": str
                    }
                ]
            }
        }
    }
    """

    schema = {
        "queues-statistics": {
            "interface-queues-statistics": {
                "interface-queue": ListOf({
                    "max-octets-allowed": str,
                    "max-packets-allowed": str,
                    "name": str,
                    "number-of-queue-drops": str,
                    "octets-in-queue": str,
                    "packets-in-queue": str
                })
            },
            "protocol-queues-statistics": {
                "protocol-queue": ListOf({
                    "max-octets-allowed": str,
                    "max-packets-allowed": str,
                    "name": str,
                    "number-of-queue-drops": str,
                    "octets-in-queue": str,
                    "packets-in-queue": str
                })
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
        p1 = re.compile(
            r'^(?P<name>\S+) +(?P<octets_in_queue>\d+)'
            r' +(?P<max_octets_allowed>\d+) +(?P<packets_in_queue>\d+) +'
            r'(?P<max_packets_allowed>\d+) +(?P<number_of_queue_drops>\d+)$')

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
                    entry_list = ret_dict.setdefault("queues-statistics", {})\
                        .setdefault("interface-queues-statistics", {})\
                            .setdefault("interface-queue", [])
                else:
                    entry_list = ret_dict.setdefault("queues-statistics", {})\
                        .setdefault("protocol-queues-statistics", {})\
                            .setdefault("protocol-queue", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                entry_list.append(entry)
                continue

            # input protocol              bytes          max  packets      max    drops
            m = p2.match(line)
            if m:
                interface_flag = False

        return ret_dict


class ShowSystemQueuesNoForwarding(ShowSystemQueues):
    """ Parser for:
            * show system queues no-forwarding
    """
    cli_command = 'show system queues no-forwarding'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowSystemStorageSchema(MetaParser):
    """ Schema for:
            * show system storage
    """
    """
    schema = {
        "system-storage-information": {
            "filesystem": [
                {
                    "available-blocks": {
                        "#text": str
                    },
                    "filesystem-name": str,
                    "mounted-on": str,
                    "total-blocks": {
                        "#text": str
                    },
                    "used-blocks": {
                        "#text": str
                    },
                    "used-percent": str
                }
            ]
        }
    }
    """

    schema = {
        "system-storage-information": {
            "filesystem": ListOf({
                "available-blocks": {
                    "junos:format": str
                },
                "filesystem-name": str,
                "mounted-on": str,
                "total-blocks": {
                    Optional("#text"): str,
                    "junos:format": str
                },
                "used-blocks": {
                    "junos:format": str
                },
                "used-percent": str
            })
        }
    }


class ShowSystemStorage(ShowSystemStorageSchema):
    """ Parser for:
            * show system storage
    """
    cli_command = 'show system storage'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # /dev/gpt/junos           20G       1.2G        17G        7%  /.mount
        p1 = re.compile(
            r'^(?P<filesystem_name>\S+) +(?P<total_blocks>\S+) +'
            r'(?P<used_blocks>\S+) +(?P<available_blocks>\S+) +(?P<used_percent>\S+)'
            r' +(?P<mounted_on>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # /dev/gpt/junos           20G       1.2G        17G        7%  /.mount
            m = p1.match(line)
            if m:

                filesystem_list = ret_dict.setdefault("system-storage-information", {})\
                    .setdefault("filesystem", [])

                group = m.groupdict()
                entry = {
                    "available-blocks": {
                        "junos:format": group["available_blocks"]
                    },
                    "filesystem-name": group["filesystem_name"],
                    "mounted-on": group["mounted_on"],
                    "total-blocks": {
                        "junos:format": group["total_blocks"]
                    },
                    "used-blocks": {
                        "junos:format": group["used_blocks"]
                    },
                    "used-percent": group["used_percent"]
                }

                filesystem_list.append(entry)
                continue

        return ret_dict


class ShowSystemStorageNoForwarding(ShowSystemStorage):
    """ Parser for:
            * show system storage no-forwarding
    """
    cli_command = 'show system storage no-forwarding'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)


class ShowSystemCoreDumpsSchema(MetaParser):
    """ Schema for:
            * show system core-dumps
    """
    '''
    schema = {
        "directory-list": {
            "directory": {
                "file-information": [
                    {
                        "file-date": {
                            "#text": str,
                            "junos:format": str
                        },
                        "file-group": str,
                        "file-links": str,
                        "file-name": str,
                        "file-owner": str,
                        "file-permissions": {
                            "#text": str,
                            "junos:format": str
                        },
                        "file-size": str
                    }
                ],
                "output": "list",
                "total-files": str
            }
        }
    }
    '''

    schema = {
        "directory-list": {
            "directory": {
                "file-information": ListOf({
                    "file-date": {
                        Optional("#text"): str,
                        "@junos:format": str
                    },
                    "file-group": str,
                    "file-links": str,
                    "file-name": str,
                    "file-owner": str,
                    "file-permissions": {
                        Optional("#text"): str,
                        "@junos:format": str
                    },
                    "file-size": str
                }),
                "output": list,
                "total-files": str
            }
        }
    }


class ShowSystemCoreDumps(ShowSystemCoreDumpsSchema):
    """ Parser for:
            * show system core-dumps
    """
    cli_command = 'show system core-dumps'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # -rw-r--r--  1 root  wheel    1252383 Aug 8   2019 /var/crash/core.riot.mpc0.1565307741.1716.gz
        p1 = re.compile(
            r'^(?P<file_permissions>\S+) +(?P<file_links>\S+) +'
            r'(?P<file_owner>\S+)  +(?P<file_group>\S+) +(?P<file_size>\S+) +'
            r'(?P<file_date>\S+ +\d+ +\d+) +(?P<file_name>\S+)$')

        # /var/tmp/*core*: No such file or directory
        p2 = re.compile(r'^(?P<output>\S+: +No +such +file +or +directory)$')

        # total files: 6
        p3 = re.compile(r'^total +files: +(?P<total_files>\d)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # -rw-r--r--  1 root  wheel    1252383 Aug 8   2019 /var/crash/core.riot.mpc0.1565307741.1716.gz
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("directory-list", {})\
                    .setdefault("directory", {}).setdefault("file-information", [])
                entry = {}
                entry["file-date"] = {"@junos:format": group['file_date']}
                entry["file-group"] = group['file_group']
                entry["file-links"] = group['file_links']
                entry["file-name"] = group['file_name']
                entry["file-owner"] = group['file_owner']
                entry["file-permissions"] = {
                    "@junos:format": group['file_permissions']
                }
                entry["file-size"] = group['file_size']

                entry_list.append(entry)
                continue

            # /var/tmp/*core*: No such file or directory
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("directory-list", {})\
                    .setdefault("directory", {}).setdefault("output", [])

                entry_list.append(group['output'])
                continue

            # total files: 6
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("directory-list", {})\
                    .setdefault("directory", {})

                entry['total-files'] = group['total_files']
                continue

        return ret_dict


class ShowSystemCoreDumpsNoForwarding(ShowSystemCoreDumps):
    """ Parser for:
            - 'show system core-dumps no-forwarding'
    """

    cli_command = "show system core-dumps no-forwarding"

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)


class ShowSystemUptimeSchema(MetaParser):
    """ Schema for:
            * show system users
    """
    schema = {
        Optional("@xmlns:junos"): str,
        "system-uptime-information": {
            Optional("@xmlns"): str,
            "current-time": {
                "date-time": {
                    "#text": str,
                    Optional("@junos:seconds"): str
                }
            },
            "last-configured-time": {
                "date-time": {
                    "#text": str,
                    Optional("@junos:seconds"): str
                },
                "time-length": {
                    "#text": str,
                    Optional("@junos:seconds"): str
                },
                "user": str
            },
            "protocols-started-time": {
                "date-time": {
                    "#text": str,
                    Optional("@junos:seconds"): str
                },
                "time-length": {
                    "#text": str,
                    Optional("@junos:seconds"): str
                }
            },
            "system-booted-time": {
                "date-time": {
                    "#text": str,
                    Optional("@junos:seconds"): str
                },
                "time-length": {
                    "#text": str,
                    Optional("@junos:seconds"): str
                }
            },
            Optional("time-source"): str,
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
                }
            }
        }
    }


class ShowSystemUptime(ShowSystemUptimeSchema):
    """ Parser for:
            * show system uptime
    """
    cli_command = 'show system uptime'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #Current time: 2020-03-26 08:16:41 UTC
        p1 = re.compile(r'^Current time: +(?P<current_time>[\S\s]+)$')

        #Time Source:  LOCAL CLOCK
        p2 = re.compile(r'^Time Source: +(?P<time_source>[\w\s\.]+)$')

        #System booted: 2019-08-29 09:02:22 UTC (29w6d 23:14 ago)
        p3 = re.compile(r'^System booted: +(?P<date_time>[\w\s\-\:]+) '
                        r'+\((?P<time_length>[\w\s\:]+)\s+ago\)$')

        #Protocols started: 2019-08-29 09:03:25 UTC (29w6d 23:13 ago)
        p4 = re.compile(r'^Protocols started: +(?P<date_time>[\w\s\-\:]+) '
                        r'+\((?P<time_length>[\w\s\:]+)\s+ago\)$')

        #Last configured: 2020-03-05 16:04:34 UTC (2w6d 16:12 ago) by cisco
        p5 = re.compile(r'^Last configured: +(?P<date_time>'
                        r'[A-Za-z\t .\d\-\:]+)+\((?P<time_length>'
                        r'[\w+\s\d+\:\d]+) ago\) by (?P<user>\S+)$')

        # 8:16AM  up 209 days, 23:14, 5 users, load averages: 0.43, 0.43, 0.42
        # 2:08PM  up 11:03, 1 users, load averages: 0.31, 0.48, 0.50
        # 3:57AM  up 1 day, 16:57, 1 users, load averages: 0.55, 0.46, 0.44
        # 12:31PM  up 15 days, 5 mins, 1 user, load averages: 0.07, 0.09, 0.04
        p6 = re.compile(r'^(?P<date_time>\d+\:\w+)\s+up\s+((?P<days>\d+)\s+day(s)?,\s+)?'
                        r'(?P<mins>((\d+ mins|[\w\:]+)))[^,]*,\s+(?P<user_count>\d+)\s+user(s)?'
                        r',\s+load\s+averages:\s+(?P<avg1>[\d\.]+),\s+(?P<avg2>[\d\.]+)'
                        r',\s+(?P<avg3>[\d\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            #Current time: 2020-03-26 08:16:41 UTC
            m = p1.match(line)
            if m:
                group = m.groupdict()
                user_table_entry_list = ret_dict.setdefault(
                    'system-uptime-information', {})

                current_time_dict = {}
                last_configured_time_dict = {}
                protocols_started_time_dict = {}
                system_booted_time_dict = {}
                uptime_information_dict = {}

                current_date_dict = {}
                current_date_dict["#text"] = group["current_time"]
                current_time_dict["date-time"] = current_date_dict

                user_table_entry_list["current-time"] = current_time_dict
                continue

            #Time Source:  LOCAL CLOCK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                user_table_entry_list["time-source"] = group["time_source"]
                continue

            #System booted: 2019-08-29 09:02:22 UTC (29w6d 23:14 ago)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                current_system_dict = {}
                current_system_date_dict = {}
                current_system_date_dict["#text"] = group["date_time"]

                current_system_time_dict = {}
                current_system_time_dict["#text"] = group["time_length"]

                current_system_dict["date-time"] = current_system_date_dict
                current_system_dict["time-length"] = current_system_time_dict

                user_table_entry_list[
                    "system-booted-time"] = current_system_dict
                continue

            #Protocols started: 2019-08-29 09:03:25 UTC (29w6d 23:13 ago)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                current_protocol_dict = {}
                current_protocol_date_dict = {}
                current_protocol_date_dict["#text"] = group["date_time"]

                current_protocol_time_dict = {}
                current_protocol_time_dict["#text"] = group["time_length"]

                current_protocol_dict["date-time"] = current_protocol_date_dict
                current_protocol_dict[
                    "time-length"] = current_protocol_time_dict

                user_table_entry_list[
                    "protocols-started-time"] = current_protocol_dict
                continue

            #Last configured: 2020-03-05 16:04:34 UTC (2w6d 16:12 ago) by cisco
            m = p5.match(line)
            if m:
                group = m.groupdict()
                current_last_dict = {}
                current_last_date_dict = {}
                current_last_date_dict["#text"] = group["date_time"]

                current_last_time_dict = {}
                current_last_time_dict["#text"] = group["time_length"]

                current_last_dict["date-time"] = current_last_date_dict
                current_last_dict["time-length"] = current_last_time_dict

                last_user_entry_dict = user_table_entry_list.setdefault(
                    "last-configured-time", {})
                last_user_entry_dict.update({'user': group["user"]})

                last_user_entry_dict.update(
                    {'date-time': current_last_date_dict})
                last_user_entry_dict.update(
                    {'time-length': current_last_time_dict})
                continue

            #8:16AM  up 209 days, 23:14, 5 users, load averages: 0.43, 0.43, 0.42
            # 2:08PM  up 11:03, 1 users, load averages: 0.31, 0.48, 0.50
            m = p6.match(line)
            if m:
                group = m.groupdict()
                current_up_dict = {}
                current_up_date_dict = {}
                current_up_date_dict["#text"] = group["date_time"]

                current_up_time_dict = {}

                # 8:16AM  up 209 days, 23:14, 5 users, load averages: 0.43, 0.43, 0.42
                if group["days"]:
                    if "min" in group["mins"]:
                        current_up_time_dict["#text"] = group[
                            "days"] + " days," + " " + group["mins"]
                        current_up_time_dict["@junos:seconds"] = str(
                            (int(group['days']) * 86400) +
                            (int(group['mins'].split(' ')[0]) * 60)
                            )
                    else:
                        current_up_time_dict["#text"] = group[
                            "days"] + " days," + " " + group["mins"] + " mins,"
                        current_up_time_dict["@junos:seconds"] = str(
                            (int(group['days']) * 86400) + \
                            (int(group['mins'].split(':')[0]) * 3600) + \
                            ((int(group['mins'].split(':')[1]) if len(group['mins'].split(':')) == 2 else 0) * 60)
                        )

                # 2:08PM  up 11:03, 1 users, load averages: 0.31, 0.48, 0.50
                else:
                    if "min" in group["mins"]:
                        current_up_time_dict["#text"] = group["mins"]
                        current_up_time_dict["@junos:seconds"] = str(
                            int(group['mins'].split(' ')[0]) * 60
                            )
                    else:
                        current_up_time_dict["#text"] = group["mins"] + " mins,"
                        current_up_time_dict["@junos:seconds"] = str(
                            (int(group['mins'].split(':')[0]) * 3600) + \
                            ((int(group['mins'].split(':')[1]) if len(group['mins'].split(':')) == 2 else 0) * 60)
                        )

                current_active_dict = {}
                current_active_dict["#text"] = group["user_count"]

                current_up_dict["date-time"] = current_up_date_dict
                current_up_dict["active-user-count"] = current_active_dict
                current_up_dict["up-time"] = current_up_time_dict

                current_up_dict["load-average-1"] = group["avg1"]
                current_up_dict["load-average-15"] = group["avg2"]
                current_up_dict["load-average-5"] = group["avg3"]
                user_table_entry_list["uptime-information"] = current_up_dict

                continue

        return ret_dict


class ShowSystemUptimeNoForwarding(ShowSystemUptime):
    """ Parser for:
            * show system uptime no-forwarding
    """

    cli_command = 'show system uptime no-forwarding'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowSystemStatisticsSchema(MetaParser):
    """ Schema for:
            * show system statistics
    """
    """
    schema = {
        "statistics": [
            {
                "ah": {
                    "bytes-in": str,
                    "bytes-out": str,
                    "crypto-processing-failure": str,
                    "packets-blocked-due-to-policy": str,
                    "packets-dropped-as-bad-authentication-detected": str,
                    "packets-dropped-as-larger-than-ip-maxpacket": str,
                    "packets-dropped-as-protocol-unsupported": str,
                    "packets-dropped-due-to-bad-authentication-length": str,
                    "packets-dropped-due-to-bad-kcr": str,
                    "packets-dropped-due-to-invalid-tdb": str,
                    "packets-dropped-due-to-no-tdb": str,
                    "packets-dropped-due-to-no-transform": str,
                    "packets-dropped-due-to-queue-full": str,
                    "packets-in": str,
                    "packets-out": str,
                    "packets-shorter-than-header-shows": str,
                    "possible-replay-packets-detected": str,
                    "replay-counter-wrap": str,
                    "tunnel-sanity-check-failures": str
                },
                "arp": {
                    "arp-iri-cnt": str,
                    "arp-iri-drop": str,
                    "arp-iri-max": str,
                    "arp-mgt-cnt": str,
                    "arp-mgt-drop": str,
                    "arp-mgt-max": str,
                    "arp-packets-are-dropped-as-driver-call-failed": str,
                    "arp-packets-are-dropped-as-nexthop-allocation-failed": str,
                    "arp-packets-are-dropped-as-source-is-not-validated": str,
                    "arp-packets-are-dropped-from-peer-vrrp": str,
                    "arp-packets-are-rejected-as-target-ip-arp-resolve-is-in-progress": str,
                    "arp-packets-received-from-peer-vrrp-router-and-discarded": str,
                    "arp-packets-rejected-as-family-is-configured-with-deny-arp": str,
                    "arp-probe-for-proxy-address-reachable-from-the-incoming-interface": str,
                    "arp-public-cnt": str,
                    "arp-public-drop": str,
                    "arp-public-max": str,
                    "arp-replies-are-rejected-as-source-and-destination-is-same": str,
                    "arp-replies-received": str,
                    "arp-replies-sent": str,
                    "arp-request-discarded-for-vrrp-source-address": str,
                    "arp-requests-received": str,
                    "arp-requests-sent": str,
                    "arp-response-packets-are-rejected-on-mace-icl-interface": str,
                    "arp-system-drop": str,
                    "arp-system-max": str,
                    "datagrams-for-an-address-not-on-the-interface": str,
                    "datagrams-for-non-ip-protocol": str,
                    "datagrams-received": str,
                    "datagrams-which-were-not-for-me": str,
                    "datagrams-with-a-broadcast-source-address": str,
                    "datagrams-with-bad-hardware-address-length": str,
                    "datagrams-with-bad-protocol-address-length": str,
                    "datagrams-with-bogus-interface": str,
                    "datagrams-with-incorrect-length": str,
                    "datagrams-with-multicast-source-address": str,
                    "datagrams-with-multicast-target-address": str,
                    "datagrams-with-my-own-hardware-address": str,
                    "datagrams-with-source-address-duplicate-to-mine": str,
                    "datagrams-with-unsupported-opcode": str,
                    "grat-arp-packets-are-ignored-as-mac-address-is-not-changed": str,
                    "new-requests-on-unnumbered-interfaces": str,
                    "packets-discarded-waiting-for-resolution": str,
                    "packets-sent-after-waiting-for-resolution": str,
                    "proxy-arp-request-discarded-as-source-ip-is-a-proxy-target": str,
                    "proxy-requests-not-proxied": str,
                    "received-proxy-requests": str,
                    "replies-from-unnumbered-interface-with-non-subnetted-donor": str,
                    "replies-from-unnumbered-interfaces": str,
                    "requests-dropped-due-to-interface-deletion": str,
                    "requests-dropped-during-retry": str,
                    "requests-dropped-on-entry": str,
                    "requests-for-memory-denied": str,
                    "requests-on-unnumbered-interface-with-non-subnetted-donor": str,
                    "requests-on-unnumbered-interfaces": str,
                    "resolution-request-dropped": str,
                    "resolution-request-received": str,
                    "restricted-proxy-requests": str,
                    "restricted-proxy-requests-not-proxied": str,
                    "self-arp-request-packet-received-on-irb-interface": str,
                    "unrestricted-proxy-requests": str
                },
                "clnl": {
                    "address-fields-were-not-reasonable": str,
                    "bad-version-packets": str,
                    "er-pdu-generation-failure": str,
                    "error-pdu-rate-drops": str,
                    "forwarded-packets": str,
                    "fragmentation-prohibited": str,
                    "fragments-discarded": str,
                    "fragments-sent": str,
                    "fragments-timed-out": str,
                    "mcopy-failure": str,
                    "no-free-memory-in-socket-buffer": str,
                    "non-forwarded-packets": str,
                    "output-packets-discarded": str,
                    "packets-delivered": str,
                    "packets-destined-to-dead-nexthop": str,
                    "packets-discarded-due-to-no-route": str,
                    "packets-fragmented": str,
                    "packets-reconstructed": str,
                    "packets-with-bad-checksum": str,
                    "packets-with-bad-header-length": str,
                    "packets-with-bogus-sdl-size": str,
                    "sbappend-failure": str,
                    "segment-information-forgotten": str,
                    "send-packets-discarded": str,
                    "too-small-packets": str,
                    "total-clnl-packets-received": str,
                    "total-packets-sent": str,
                    "unknown-or-unsupported-protocol-packets": str
                },
                "esis": {
                    "iso-family-not-configured": str,
                    "pdus-received-with-bad-checksum": str,
                    "pdus-received-with-bad-type-field": str,
                    "pdus-received-with-bad-version-number": str,
                    "pdus-with-bad-header-length": str,
                    "pdus-with-bogus-sdl-size": str,
                    "pdus-with-unknown-or-unsupport-protocol": str,
                    "short-pdus-received": str,
                    "total-esis-packets-received": str,
                    "total-packets-consumed-by-protocol": str
                },
                "esp": {
                    "esp-bytes-in": str,
                    "esp-bytes-out": str,
                    "esp-crypto-processing-failure": str,
                    "esp-packets-blocked-due-to-policy": str,
                    "esp-packets-dropped-as-bad-authentication-detected": str,
                    "esp-packets-dropped-as-bad-encryption-detected": str,
                    "esp-packets-dropped-as-bad-ilen": str,
                    "esp-packets-dropped-as-invalid-tdb": str,
                    "esp-packets-dropped-as-larger-than-ip-maxpacket": str,
                    "esp-packets-dropped-as-protocol-not-supported": str,
                    "esp-packets-dropped-due-to-bad-kcr": str,
                    "esp-packets-dropped-due-to-no-tdb": str,
                    "esp-packets-dropped-due-to-no-transform": str,
                    "esp-packets-dropped-due-to-queue-full": str,
                    "esp-packets-in": str,
                    "esp-packets-out": str,
                    "esp-packets-shorter-than-header-shows": str,
                    "esp-possible-replay-packets-detected": str,
                    "esp-replay-counter-wrap": str,
                    "esp-tunnel-sanity-check-failures": str
                },
                "ethoamcfm": {
                    "flood-requests-dropped": str,
                    "flood-requests-forwarded-to-pfe": str,
                    "input-packets-drop-bad-interface-state": str,
                    "output-packets-drop-bad-interface-state": str,
                    "packets-sent": str,
                    "received-packets-forwarded": str,
                    "total-packets-received": str,
                    "total-packets-transmitted": str
                },
                "ethoamlfm": {
                    "input-packets-drop-bad-interface-state": str,
                    "output-packets-drop-bad-interface-state": str,
                    "packets-sent": str,
                    "received-packets-forwarded": str,
                    "total-packets-received": str,
                    "total-packets-transmitted": str
                },
                "icmp": {
                    "calls-to-icmp-error": str,
                    "drops-due-to-rate-limit": str,
                    "echo-drops-with-broadcast-or-multicast-destinaton-address": str,
                    "errors-not-generated-because-old-message-was-icmp": str,
                    "histogram": [
                        {
                            "destination-unreachable": str,
                            "icmp-echo": str,
                            "icmp-echo-reply": str,
                            "time-exceeded": str,
                            "type-of-histogram": str
                        }
                    ],
                    "message-responses-generated": str,
                    "messages-less-than-the-minimum-length": str,
                    "messages-with-bad-checksum": str,
                    "messages-with-bad-code-fields": str,
                    "messages-with-bad-length": str,
                    "messages-with-bad-source-address": str,
                    "timestamp-drops-with-broadcast-or-multicast-destination-address": str
                },
                "icmp6": {
                    "address-unreachable": str,
                    "administratively-prohibited": str,
                    "bad-checksums": str,
                    "beyond-scope": str,
                    "calls-to-icmp6-error": str,
                    "erroneous-header-field": str,
                    "errors-not-generated-because-old-message-was-icmp-error": str,
                    "errors-not-generated-because-rate-limitation": str,
                    "histogram-of-error-messages-to-be-generated": str,
                    "icmp6-message-responses-generated": str,
                    "icmp6-messages-with-bad-code-fields": str,
                    "icmp6-messages-with-bad-length": str,
                    "input-histogram": {
                        "histogram-type": str,
                        "neighbor-advertisement": str,
                        "neighbor-solicitation": str,
                        "router-advertisement-icmp6-packets": str,
                        "router-solicitation-icmp6-packets": str,
                        "time-exceeded-icmp6-packets": str,
                        "unreachable-icmp6-packets": str
                    },
                    "messages-less-than-minimum-length": str,
                    "messages-with-too-many-nd-options": str,
                    "nd-iri-cnt": str,
                    "nd-iri-drop": str,
                    "nd-iri-max": str,
                    "nd-mgt-cnt": str,
                    "nd-mgt-drop": str,
                    "nd-mgt-max": str,
                    "nd-public-cnt": str,
                    "nd-public-drop": str,
                    "nd-public-max": str,
                    "nd-system-drop": str,
                    "nd-system-max": str,
                    "nd6-dad-proxy-conflicts": str,
                    "nd6-dad-proxy-eqmac-drop": str,
                    "nd6-dad-proxy-nomac-drop": str,
                    "nd6-dad-proxy-requests": str,
                    "nd6-dad-proxy-resolve-cnt": str,
                    "nd6-dup-proxy-responses": str,
                    "nd6-ndp-proxy-requests": str,
                    "nd6-ndp-proxy-resolve-cnt": str,
                    "nd6-ndp-proxy-responses": str,
                    "nd6-requests-dropped-during-retry": str,
                    "nd6-requests-dropped-on-entry": str,
                    "no-route": str,
                    "output-histogram": {},
                    "packet-too-big": str,
                    "port-unreachable": str,
                    "protocol-name": str,
                    "redirect": str,
                    "time-exceed-reassembly": str,
                    "time-exceed-transit": str,
                    "unknown": str,
                    "unrecognized-next-header": str,
                    "unrecognized-option": str
                },
                "igmp": {
                    "membership-queries-received": str,
                    "membership-queries-received-with-invalid-fields": str,
                    "membership-reports-received": str,
                    "membership-reports-received-for-groups-to-which-we-belong": str,
                    "membership-reports-received-with-invalid-fields": str,
                    "membership-reports-sent": str,
                    "messages-received": str,
                    "messages-received-with-bad-checksum": str,
                    "messages-received-with-too-few-bytes": str
                },
                "ip": {
                    "bad-header-checksums": str,
                    "datagrams-that-can-not-be-fragmented": str,
                    "fragments-created": str,
                    "fragments-dropped-after-timeout": str,
                    "fragments-dropped-due-to-outofspace-or-dup": str,
                    "fragments-dropped-due-to-queueoverflow": str,
                    "fragments-received": str,
                    "incoming-rawip-packets-dropped-no-socket-buffer": str,
                    "incoming-ttpoip-packets-dropped": str,
                    "incoming-ttpoip-packets-received": str,
                    "incoming-virtual-node-packets-delivered": str,
                    "loose-source-and-record-route-options": str,
                    "multicast-packets-dropped": str,
                    "option-packets-dropped-due-to-rate-limit": str,
                    "outgoing-ttpoip-packets-dropped": str,
                    "outgoing-ttpoip-packets-sent": str,
                    "output-datagrams-fragmented": str,
                    "output-packets-discarded-due-to-no-route": str,
                    "output-packets-dropped-due-to-no-bufs": str,
                    "packets-destined-to-dead-next-hop": str,
                    "packets-dropped": str,
                    "packets-for-this-host": str,
                    "packets-for-unknown-or-unsupported-protocol": str,
                    "packets-forwarded": str,
                    "packets-not-forwardable": str,
                    "packets-reassembled-ok": str,
                    "packets-received": str,
                    "packets-sent-from-this-host": str,
                    "packets-sent-with-fabricated-ip-header": str,
                    "packets-used-first-nexthop-in-ecmp-unilist": str,
                    "packets-with-bad-options": str,
                    "packets-with-data-length-less-than-headerlength": str,
                    "packets-with-data-size-less-than-datalength": str,
                    "packets-with-header-length-less-than-data-size": str,
                    "packets-with-incorrect-version-number": str,
                    "packets-with-options-handled-without-error": str,
                    "packets-with-size-smaller-than-minimum": str,
                    "record-route-options": str,
                    "redirects-sent": str,
                    "router-alert-options": str,
                    "strict-source-and-record-route-options": str,
                    "timestamp-and-address-options": str,
                    "timestamp-and-prespecified-address-options": str,
                    "timestamp-options": str,
                    "transit-re-packets-dropped-on-mgmt-interface": str
                },
                "ip6": {
                    "duplicate-or-out-of-space-fragments-dropped": str,
                    "failures-of-source-address-selection": str,
                    "forward-cache-hit": str,
                    "forward-cache-miss": str,
                    "fragments-that-exceeded-limit": str,
                    "header-type": [
                        {
                            "globals": str,
                            "header-for-source-address-selection": str,
                            "link-locals": str
                        }
                    ],
                    "histogram": str,
                    "ip6-datagrams-that-can-not-be-fragmented": str,
                    "ip6-fragments-created": str,
                    "ip6-fragments-dropped-after-timeout": str,
                    "ip6-fragments-received": str,
                    "ip6-option-packets-dropped-due-to-rate-limit": str,
                    "ip6-output-datagrams-fragmented": str,
                    "ip6-output-packets-discarded-due-to-no-route": str,
                    "ip6-output-packets-dropped-due-to-no-bufs": str,
                    "ip6-packets-destined-to-dead-next-hop": str,
                    "ip6-packets-dropped": str,
                    "ip6-packets-for-this-host": str,
                    "ip6-packets-forwarded": str,
                    "ip6-packets-not-forwardable": str,
                    "ip6-packets-reassembled-ok": str,
                    "ip6-packets-sent-from-this-host": str,
                    "ip6-packets-sent-with-fabricated-ip-header": str,
                    "ip6-packets-with-bad-options": str,
                    "ip6-packets-with-incorrect-version-number": str,
                    "ip6-packets-with-size-smaller-than-minimum": str,
                    "ip6-redirects-sent": str,
                    "ip6nh-icmp6": str,
                    "ip6nh-ospf": str,
                    "ip6nh-tcp": str,
                    "ip6nh-udp": str,
                    "multicast-packets-which-we-do-not-join": str,
                    "packets-discarded-due-to-too-may-headers": str,
                    "packets-dropped-due-to-bad-protocol": str,
                    "packets-that-violated-scope-rules": str,
                    "packets-whose-headers-are-not-continuous": str,
                    "packets-with-datasize-less-than-data-length": str,
                    "transit-re-packet-dropped-on-mgmt-interface": str,
                    "tunneling-packets-that-can-not-find-gif": str
                },
                "ipcomp": {
                    "ipcomp-bytes-in": str,
                    "ipcomp-bytes-out": str,
                    "ipcomp-crypto-processing-failure": str,
                    "ipcomp-packets-blocked-due-to-policy": str,
                    "ipcomp-packets-dropped-as-invalid-tdb": str,
                    "ipcomp-packets-dropped-as-larger-than-ip-maxpacket": str,
                    "ipcomp-packets-dropped-as-protocol-not-supported": str,
                    "ipcomp-packets-dropped-due-to-bad-kcr": str,
                    "ipcomp-packets-dropped-due-to-no-tdb": str,
                    "ipcomp-packets-dropped-due-to-no-transform": str,
                    "ipcomp-packets-dropped-due-to-queue-full": str,
                    "ipcomp-packets-in": str,
                    "ipcomp-packets-out": str,
                    "ipcomp-packets-shorter-than-header-shows": str,
                    "ipcomp-replay-counter-wrap": str,
                    "packets-sent-uncompressed-threshold": str,
                    "packets-sent-uncompressed-useless": str
                },
                "ipsec": {
                    "cluster-coalesced-during-clone": str,
                    "cluster-copied-during-clone": str,
                    "inbound-packets-violated-process-security-policy": str,
                    "invalid-outbound-packets": str,
                    "mbuf-coalesced-during-clone": str,
                    "mbuf-inserted-during-makespace": str,
                    "outbound-packets-failed-due-to-insufficient-memory": str,
                    "outbound-packets-violated-process-security-policy": str,
                    "outbound-packets-with-bundled-sa": str,
                    "outbound-packets-with-no-route": str,
                    "outbound-packets-with-no-sa-available": str
                },
                "ipsec6": {
                    "cluster-coalesced-during-clone": str,
                    "cluster-copied-during-clone": str,
                    "inbound-packets-violated-process-security-policy": str,
                    "invalid-outbound-packets": str,
                    "mbuf-coalesced-during-clone": str,
                    "mbuf-inserted-during-makespace": str,
                    "outbound-packets-failed-due-to-insufficient-memory": str,
                    "outbound-packets-violated-process-security-policy": str,
                    "outbound-packets-with-bundled-sa": str,
                    "outbound-packets-with-no-route": str,
                    "outbound-packets-with-no-sa-available": str
                },
                "mpls": {
                    "after-tagging-packets-can-not-fit-link-mtu": str,
                    "lsp-ping-packets": str,
                    "packets-dropped-at-mpls-socket-send": str,
                    "packets-dropped-at-p2mp-cnh-output": str,
                    "packets-dropped-due-to-ifl-down": str,
                    "packets-forwarded-at-mpls-socket-send": str,
                    "packets-with-header-too-small": str,
                    "packets-with-ipv4-explicit-null-checksum-errors": str,
                    "packets-with-ipv4-explicit-null-tag": str,
                    "packets-with-router-alert-tag": str,
                    "packets-with-tag-encoding-error": str,
                    "packets-with-ttl-expired": str,
                    "total-mpls-packets-received": str
                },
                "pfkey": {
                    "bytes-sent-from-userland": str,
                    "bytes-sent-to-userland": str,
                    "incoming-messages-with-memory-allocation-failure": str,
                    "input-histogram": {
                        "add": str,
                        "dump": str,
                        "reserved": str
                    },
                    "messages-too-short": str,
                    "messages-toward-all-sockets": str,
                    "messages-toward-registered-sockets": str,
                    "messages-toward-single-socket": str,
                    "messages-with-duplicate-extension": str,
                    "messages-with-invalid-address-extension": str,
                    "messages-with-invalid-extension-type": str,
                    "messages-with-invalid-length-field": str,
                    "messages-with-invalid-message-type-field": str,
                    "messages-with-invalid-sa-type": str,
                    "messages-with-invalid-version-field": str,
                    "outgoing-messages-with-memory-allocation-failure": str,
                    "output-histogram": {},
                    "requests-sent-from-userland": str,
                    "requests-sent-to-userland": str
                },
                "raw-interface": {
                    "dialer-packets-received": str,
                    "dialer-packets-transmitted": str,
                    "faboam-packets-dropped": str,
                    "faboam-packets-received": str,
                    "faboam-packets-transmitted": str,
                    "fibre-channel-packets-dropped": str,
                    "fibre-channel-packets-received": str,
                    "fibre-channel-packets-transmitted": str,
                    "fip-packets-dropped": str,
                    "fip-packets-received": str,
                    "fip-packets-transmitted": str,
                    "igmpl2-packets-received": str,
                    "igmpl2-packets-transmitted": str,
                    "input-drops-due-to-bogus-protocol": str,
                    "input-drops-due-to-no-mbufs-available": str,
                    "input-drops-due-to-no-socket": str,
                    "input-drops-due-to-no-space-in-socket": str,
                    "isdn-packets-received": str,
                    "isdn-packets-transmitted": str,
                    "lacp-packets-dropped": str,
                    "lacp-packets-received": str,
                    "lacp-packets-transmitted": str,
                    "mldl2-packets-received": str,
                    "mldl2-packets-transmitted": str,
                    "mpu-packets-received": str,
                    "mpu-packets-transmitted": str,
                    "output-drops-due-to-transmit-error": str,
                    "ppoe-packets-transmitted": str,
                    "ppp-packets-received-from-jppd": str,
                    "ppp-packets-received-from-pppd": str,
                    "ppp-packets-transmitted-to-jppd": str,
                    "ppp-packets-transmitted-to-pppd": str,
                    "pppoe-packets-received": str,
                    "raw-packets-transmitted": str,
                    "stp-packets-dropped": str,
                    "stp-packets-received": str,
                    "stp-packets-transmitted": str,
                    "vccp-packets-dropped": str,
                    "vccp-packets-received": str,
                    "vccp-packets-transmitted": str
                },
                "rdp": {
                    "acks-received": str,
                    "acks-sent": str,
                    "closes": str,
                    "connects": str,
                    "input-packets": str,
                    "keepalives-received": str,
                    "keepalives-sent": str,
                    "output-packets": str,
                    "packets-discarded-due-to-bad-sequence-number": str,
                    "packets-discarded-for-bad-checksum": str,
                    "packets-dropped-due-to-full-socket-buffers": str,
                    "packets-dropped-full-repl-sock-buf": str,
                    "refused-connections": str,
                    "retransmits": str
                },
                "tcp": {
                    "aborted": str,
                    "ack-header-predictions": str,
                    "acks-bytes": str,
                    "acks-sent-in-response-but-not-exact-rsts": str,
                    "acks-sent-in-response-to-syns-on-established-connections": str,
                    "attempts": str,
                    "bad-connection-attempts": str,
                    "badack": str,
                    "bucket-overflow": str,
                    "byte-retransmits": str,
                    "bytes": str,
                    "cache-overflow": str,
                    "completed": str,
                    "connection-accepts": str,
                    "connection-requests": str,
                    "connections-closed": str,
                    "connections-dropped-by-persist-timeout": str,
                    "connections-dropped-by-retransmit-timeout": str,
                    "connections-established": str,
                    "connections-updated-rtt-on-close": str,
                    "connections-updated-ssthresh-on-close": str,
                    "connections-updated-variance-on-close": str,
                    "cookies-received": str,
                    "cookies-sent": str,
                    "data-packet-header-predictions": str,
                    "data-packets-bytes": str,
                    "dropped": str,
                    "drops": str,
                    "duplicate-in-bytes": str,
                    "dupsyn": str,
                    "embryonic-connections-dropped": str,
                    "icmp-packets-ignored": str,
                    "in-sequence-bytes": str,
                    "keepalive-connections-dropped": str,
                    "keepalive-probes-sent": str,
                    "keepalive-timeouts": str,
                    "listen-queue-overflows": str,
                    "out-of-order-in-bytes": str,
                    "out-of-sequence-segment-drops": str,
                    "outgoing-segments-dropped": str,
                    "packets-received-after-close": str,
                    "packets-received-in-sequence": str,
                    "persist-timeouts": str,
                    "rcv-packets-dropped": str,
                    "rcv-packets-dropped-due-to-bad-address": str,
                    "received-acks": str,
                    "received-acks-for-unsent-data": str,
                    "received-completely-duplicate-packet": str,
                    "received-discarded-because-packet-too-short": str,
                    "received-discarded-for-bad-checksum": str,
                    "received-discarded-for-bad-header-offset": str,
                    "received-duplicate-acks": str,
                    "received-old-duplicate-packets": str,
                    "received-out-of-order-packets": str,
                    "received-packets-of-data-after-window": str,
                    "received-packets-with-some-dupliacte-data": str,
                    "received-window-probes": str,
                    "received-window-update-packets": str,
                    "reset": str,
                    "retransmit-timeouts": str,
                    "retransmitted": str,
                    "retransmitted-bytes": str,
                    "rst-packets": str,
                    "sack-opitions-sent": str,
                    "sack-options-received": str,
                    "sack-recovery-episodes": str,
                    "sack-scoreboard-overflow": str,
                    "segment-retransmits": str,
                    "segments-updated-rtt": str,
                    "send-packets-dropped": str,
                    "sent-ack-only-packets": str,
                    "sent-control-packets": str,
                    "sent-data-packets": str,
                    "sent-data-packets-retransmitted": str,
                    "sent-packets-delayed": str,
                    "sent-resends-by-mtu-discovery": str,
                    "sent-urg-only-packets": str,
                    "sent-window-probe-packets": str,
                    "sent-window-update-packets": str,
                    "some-duplicate-in-bytes": str,
                    "stale": str,
                    "syncache-entries-added": str,
                    "unreach": str,
                    "zone-failures": str
                },
                "tnp": {
                    "broadcast-packets-received": str,
                    "broadcast-packets-sent": str,
                    "control-packets-received": str,
                    "control-packets-sent": str,
                    "fragment-reassembly-queue-flushes": str,
                    "fragmented-packets-received": str,
                    "fragmented-packets-sent": str,
                    "hello-packets-received": str,
                    "hello-packets-sent": str,
                    "input-packets-discarded-with-no-protocol": str,
                    "packets-of-version-unspecified-received": str,
                    "packets-of-version-unspecified-sent": str,
                    "packets-of-version1-received": str,
                    "packets-of-version1-sent": str,
                    "packets-of-version2-received": str,
                    "packets-of-version2-sent": str,
                    "packets-of-version3-received": str,
                    "packets-of-version3-sent": str,
                    "packets-sent-with-unknown-protocol": str,
                    "packets-with-tnp-src-address-collision-received": str,
                    "rdp-packets-received": str,
                    "rdp-packets-sent": str,
                    "received-fragments-dropped": str,
                    "received-hello-packets-dropped": str,
                    "sent-fragments-dropped": str,
                    "sent-hello-packets-dropped": str,
                    "tunnel-packets-received": str,
                    "tunnel-packets-sent": str,
                    "udp-packets-received": str,
                    "udp-packets-sent": str,
                    "unicast-packets-received": str,
                    "unicast-packets-sent": str
                },
                "ttp": {
                    "arp-l3-packets-received": str,
                    "clnp-l3-packets-received": str,
                    "cyclotron-cycle-l3-packets-received": str,
                    "cyclotron-send-l3-packets-received": str,
                    "input-packets-could-not-get-buffer": str,
                    "input-packets-for-which-route-lookup-is-bypassed": str,
                    "input-packets-tlv-dropped": str,
                    "input-packets-with-bad-af": str,
                    "input-packets-with-bad-tlv-header": str,
                    "input-packets-with-bad-tlv-type": str,
                    "input-packets-with-bad-type": str,
                    "input-packets-with-discard-type": str,
                    "input-packets-with-too-many-tlvs": str,
                    "input-packets-with-ttp-tlv-p2mp-nbr-nhid-type": str,
                    "input-packets-with-unknown-p2mp-nbr-nhid": str,
                    "input-packets-with-vxlan-bfd-pkts": str,
                    "ipv4-l3-packets-received": str,
                    "ipv4-to-mpls-l3-packets-received": str,
                    "ipv6-l3-packets-received": str,
                    "l2-packets-received": str,
                    "l3-packets-dropped": str,
                    "l3-packets-sent-could-not-get-buffer": str,
                    "mpls-l3-packets-received": str,
                    "mpls-to-ipv4-l3-packets-received": str,
                    "null-l3-packets-received": str,
                    "openflow-packets-received": str,
                    "packets-received-from-unknown-ifl": str,
                    "packets-received-while-unconnected": str,
                    "packets-sent-could-not-find-neighbor": str,
                    "packets-sent-could-not-get-buffer": str,
                    "packets-sent-when-host_unreachable": str,
                    "packets-sent-when-transmit-disabled": str,
                    "packets-sent-while-interface-down": str,
                    "packets-sent-while-unconnected": str,
                    "packets-sent-with-bad-af": str,
                    "packets-sent-with-bad-ifl": str,
                    "tnp-l3-packets-received": str,
                    "ttp-packets-sent": str,
                    "unknown-l3-packets-received": str,
                    "vpls-l3-packets-received": str
                },
                "tudp": {
                    "broadcast-or-multicast-datagrams-dropped-due-to-no-socket": str,
                    "datagrams-dropped-due-to-full-socket-buffers": str,
                    "datagrams-dropped-due-to-no-socket": str,
                    "datagrams-output": str,
                    "datagrams-with-bad-checksum": str,
                    "datagrams-with-bad-data-length-field": str,
                    "datagrams-with-incomplete-header": str,
                    "delivered": str
                },
                "udp": {
                    "datagrams-delivered": str,
                    "datagrams-not-for-hashed-pcb": str,
                    "datagrams-with-bad-datalength-field": str
                }
            }
        ]
    }
    """

    schema = {"statistics": ListOf(
        {
            Optional("ah"): {
                "bytes-in": str,
                "bytes-out": str,
                "crypto-processing-failure": str,
                "packets-blocked-due-to-policy": str,
                "packets-dropped-as-bad-authentication-detected": str,
                "packets-dropped-as-larger-than-ip-maxpacket": str,
                "packets-dropped-as-protocol-unsupported": str,
                "packets-dropped-due-to-bad-authentication-length": str,
                "packets-dropped-due-to-bad-kcr": str,
                "packets-dropped-due-to-invalid-tdb": str,
                "packets-dropped-due-to-no-tdb": str,
                "packets-dropped-due-to-no-transform": str,
                "packets-dropped-due-to-queue-full": str,
                "packets-in": str,
                "packets-out": str,
                "packets-shorter-than-header-shows": str,
                "possible-replay-packets-detected": str,
                "replay-counter-wrap": str,
                "tunnel-sanity-check-failures": str,
            },
            Optional("arp"): {
                "arp-iri-cnt": str,
                "arp-iri-drop": str,
                "arp-iri-max": str,
                "arp-mgt-cnt": str,
                "arp-mgt-drop": str,
                "arp-mgt-max": str,
                "arp-packets-are-dropped-as-driver-call-failed": str,
                "arp-packets-are-dropped-as-nexthop-allocation-failed": str,
                "arp-packets-are-dropped-as-source-is-not-validated": str,
                "arp-packets-are-dropped-from-peer-vrrp": str,
                "arp-packets-are-rejected-as-target-ip-arp-resolve-is-in-progress": str,
                "arp-packets-received-from-peer-vrrp-router-and-discarded": str,
                "arp-packets-rejected-as-family-is-configured-with-deny-arp": str,
                "arp-probe-for-proxy-address-reachable-from-the-incoming-interface": str,
                "arp-public-cnt": str,
                "arp-public-drop": str,
                "arp-public-max": str,
                "arp-replies-are-rejected-as-source-and-destination-is-same": str,
                "arp-replies-received": str,
                "arp-replies-sent": str,
                "arp-request-discarded-for-vrrp-source-address": str,
                "arp-requests-received": str,
                "arp-requests-sent": str,
                "arp-response-packets-are-rejected-on-mace-icl-interface": str,
                "arp-system-drop": str,
                "arp-system-max": str,
                "datagrams-for-an-address-not-on-the-interface": str,
                "datagrams-for-non-ip-protocol": str,
                "datagrams-received": str,
                "datagrams-which-were-not-for-me": str,
                "datagrams-with-a-broadcast-source-address": str,
                "datagrams-with-bad-hardware-address-length": str,
                "datagrams-with-bad-protocol-address-length": str,
                "datagrams-with-bogus-interface": str,
                "datagrams-with-incorrect-length": str,
                "datagrams-with-multicast-source-address": str,
                "datagrams-with-multicast-target-address": str,
                "datagrams-with-my-own-hardware-address": str,
                "datagrams-with-source-address-duplicate-to-mine": str,
                "datagrams-with-unsupported-opcode": str,
                "grat-arp-packets-are-ignored-as-mac-address-is-not-changed": str,
                "new-requests-on-unnumbered-interfaces": str,
                "packets-discarded-waiting-for-resolution": str,
                "packets-sent-after-waiting-for-resolution": str,
                "proxy-arp-request-discarded-as-source-ip-is-a-proxy-target": str,
                "proxy-requests-not-proxied": str,
                "received-proxy-requests": str,
                "replies-from-unnumbered-interface-with-non-subnetted-donor": str,
                "replies-from-unnumbered-interfaces": str,
                "requests-dropped-due-to-interface-deletion": str,
                "requests-dropped-during-retry": str,
                "requests-dropped-on-entry": str,
                "requests-for-memory-denied": str,
                "requests-on-unnumbered-interface-with-non-subnetted-donor": str,
                "requests-on-unnumbered-interfaces": str,
                "resolution-request-dropped": str,
                "resolution-request-received": str,
                "restricted-proxy-requests": str,
                "restricted-proxy-requests-not-proxied": str,
                "self-arp-request-packet-received-on-irb-interface": str,
                "unrestricted-proxy-requests": str,
            },
            Optional("clnl"): {
                "address-fields-were-not-reasonable": str,
                "bad-version-packets": str,
                "er-pdu-generation-failure": str,
                "error-pdu-rate-drops": str,
                "forwarded-packets": str,
                "fragmentation-prohibited": str,
                "fragments-discarded": str,
                "fragments-sent": str,
                "fragments-timed-out": str,
                "mcopy-failure": str,
                "no-free-memory-in-socket-buffer": str,
                "non-forwarded-packets": str,
                "output-packets-discarded": str,
                "packets-delivered": str,
                "packets-destined-to-dead-nexthop": str,
                "packets-discarded-due-to-no-route": str,
                "packets-fragmented": str,
                "packets-reconstructed": str,
                "packets-with-bad-checksum": str,
                "packets-with-bad-header-length": str,
                "packets-with-bogus-sdl-size": str,
                "sbappend-failure": str,
                "segment-information-forgotten": str,
                "send-packets-discarded": str,
                "too-small-packets": str,
                "total-clnl-packets-received": str,
                "total-packets-sent": str,
                "unknown-or-unsupported-protocol-packets": str,
            },
            Optional("esis"): {
                "iso-family-not-configured": str,
                "mcopy-failure": str,
                "no-free-memory-in-socket-buffer": str,
                "pdus-received-with-bad-checksum": str,
                "pdus-received-with-bad-type-field": str,
                "pdus-received-with-bad-version-number": str,
                "pdus-with-bad-header-length": str,
                "pdus-with-bogus-sdl-size": str,
                "pdus-with-unknown-or-unsupport-protocol": str,
                "sbappend-failure": str,
                "send-packets-discarded": str,
                "short-pdus-received": str,
                "total-esis-packets-received": str,
                "total-packets-consumed-by-protocol": str,
            },
            Optional("esp"): {
                "esp-bytes-in": str,
                "esp-bytes-out": str,
                "esp-crypto-processing-failure": str,
                "esp-packets-blocked-due-to-policy": str,
                "esp-packets-dropped-as-bad-authentication-detected": str,
                "esp-packets-dropped-as-bad-encryption-detected": str,
                "esp-packets-dropped-as-bad-ilen": str,
                "esp-packets-dropped-as-invalid-tdb": str,
                "esp-packets-dropped-as-larger-than-ip-maxpacket": str,
                "esp-packets-dropped-as-protocol-not-supported": str,
                "esp-packets-dropped-due-to-bad-kcr": str,
                "esp-packets-dropped-due-to-no-tdb": str,
                "esp-packets-dropped-due-to-no-transform": str,
                "esp-packets-dropped-due-to-queue-full": str,
                "esp-packets-in": str,
                "esp-packets-out": str,
                "esp-packets-shorter-than-header-shows": str,
                "esp-possible-replay-packets-detected": str,
                "esp-replay-counter-wrap": str,
                "esp-tunnel-sanity-check-failures": str,
            },
            Optional("ethoamcfm"): {
                "flood-requests-dropped": str,
                "flood-requests-forwarded-to-pfe": str,
                "input-packets-drop-bad-interface-state": str,
                "output-packets-drop-bad-interface-state": str,
                "packets-sent": str,
                "received-packets-forwarded": str,
                "total-packets-received": str,
                "total-packets-transmitted": str,
            },
            Optional("ethoamlfm"): {
                "input-packets-drop-bad-interface-state": str,
                "output-packets-drop-bad-interface-state": str,
                "packets-sent": str,
                "received-packets-forwarded": str,
                "total-packets-received": str,
                "total-packets-transmitted": str,
            },
            Optional("icmp"): {
                "calls-to-icmp-error": str,
                "drops-due-to-rate-limit": str,
                "echo-drops-with-broadcast-or-multicast-destinaton-address": str,
                "errors-not-generated-because-old-message-was-icmp": str,
                "histogram": ListOf({
                    "destination-unreachable": str,
                    "icmp-echo": str,
                    "icmp-echo-reply": str,
                    "time-exceeded": str,
                    "type-of-histogram": str,
                }),
                "message-responses-generated": str,
                "messages-less-than-the-minimum-length": str,
                "messages-with-bad-checksum": str,
                "messages-with-bad-code-fields": str,
                "messages-with-bad-length": str,
                "messages-with-bad-source-address": str,
                "timestamp-drops-with-broadcast-or-multicast-destination-address": str,
            },
            Optional("icmp6"): {
                "address-unreachable": str,
                "administratively-prohibited": str,
                "bad-checksums": str,
                "beyond-scope": str,
                "calls-to-icmp6-error": str,
                "erroneous-header-field": str,
                "errors-not-generated-because-old-message-was-icmp-error": str,
                "errors-not-generated-because-rate-limitation": str,
                "histogram-of-error-messages-to-be-generated": str,
                "icmp6-message-responses-generated": str,
                "icmp6-messages-with-bad-code-fields": str,
                "icmp6-messages-with-bad-length": str,
                "input-histogram": {
                    "histogram-type": str,
                    "neighbor-advertisement": str,
                    "neighbor-solicitation": str,
                    "router-advertisement-icmp6-packets": str,
                    "router-solicitation-icmp6-packets": str,
                    "time-exceeded-icmp6-packets": str,
                    "unreachable-icmp6-packets": str,
                },
                "messages-less-than-minimum-length": str,
                "messages-with-too-many-nd-options": str,
                "nd-iri-cnt": str,
                "nd-iri-drop": str,
                "nd-iri-max": str,
                "nd-mgt-cnt": str,
                "nd-mgt-drop": str,
                "nd-mgt-max": str,
                "nd-public-cnt": str,
                "nd-public-drop": str,
                "nd-public-max": str,
                "nd-system-drop": str,
                "nd-system-max": str,
                "nd6-dad-proxy-conflicts": str,
                "nd6-dad-proxy-eqmac-drop": str,
                "nd6-dad-proxy-nomac-drop": str,
                "nd6-dad-proxy-requests": str,
                "nd6-dad-proxy-resolve-cnt": str,
                "nd6-dup-proxy-responses": str,
                "nd6-ndp-proxy-requests": str,
                "nd6-ndp-proxy-resolve-cnt": str,
                "nd6-ndp-proxy-responses": str,
                "nd6-requests-dropped-during-retry": str,
                "nd6-requests-dropped-on-entry": str,
                "no-route": str,
                "output-histogram": {
                    "histogram-type": str,
                    "neighbor-advertisement": str,
                    "neighbor-solicitation": str,
                    "unreachable-icmp6-packets": str,
                },
                Optional("packet-too-big"): str,
                "port-unreachable": str,
                "protocol-name": str,
                Optional("redirect"): str,
                "time-exceed-reassembly": str,
                "time-exceed-transit": str,
                "unknown": str,
                "unrecognized-next-header": str,
                "unrecognized-option": str,
            },
            Optional("igmp"): {
                "membership-queries-received": str,
                "membership-queries-received-with-invalid-fields": str,
                "membership-reports-received": str,
                "membership-reports-received-for-groups-to-which-we-belong": str,
                "membership-reports-received-with-invalid-fields": str,
                "membership-reports-sent": str,
                "messages-received": str,
                "messages-received-with-bad-checksum": str,
                "messages-received-with-too-few-bytes": str,
            },
            Optional("ip"): {
                "bad-header-checksums": str,
                "datagrams-that-can-not-be-fragmented": str,
                "fragments-created": str,
                "fragments-dropped-after-timeout": str,
                "fragments-dropped-due-to-outofspace-or-dup": str,
                "fragments-dropped-due-to-queueoverflow": str,
                "fragments-received": str,
                "incoming-rawip-packets-dropped-no-socket-buffer": str,
                "incoming-ttpoip-packets-dropped": str,
                "incoming-ttpoip-packets-received": str,
                "incoming-virtual-node-packets-delivered": str,
                "loose-source-and-record-route-options": str,
                "multicast-packets-dropped": str,
                "option-packets-dropped-due-to-rate-limit": str,
                "outgoing-ttpoip-packets-dropped": str,
                "outgoing-ttpoip-packets-sent": str,
                "output-datagrams-fragmented": str,
                "output-packets-discarded-due-to-no-route": str,
                "output-packets-dropped-due-to-no-bufs": str,
                "packets-destined-to-dead-next-hop": str,
                "packets-dropped": str,
                "packets-for-this-host": str,
                "packets-for-unknown-or-unsupported-protocol": str,
                "packets-forwarded": str,
                "packets-not-forwardable": str,
                "packets-reassembled-ok": str,
                "packets-received": str,
                "packets-sent-from-this-host": str,
                "packets-sent-with-fabricated-ip-header": str,
                "packets-used-first-nexthop-in-ecmp-unilist": str,
                "packets-with-bad-options": str,
                "packets-with-data-length-less-than-headerlength": str,
                "packets-with-data-size-less-than-datalength": str,
                "packets-with-header-length-less-than-data-size": str,
                "packets-with-incorrect-version-number": str,
                "packets-with-options-handled-without-error": str,
                "packets-with-size-smaller-than-minimum": str,
                "record-route-options": str,
                "redirects-sent": str,
                "router-alert-options": str,
                "strict-source-and-record-route-options": str,
                "timestamp-and-address-options": str,
                "timestamp-and-prespecified-address-options": str,
                "timestamp-options": str,
                "transit-re-packets-dropped-on-mgmt-interface": str,
            },
            Optional("ip6"): {
                "total-packets-received": str,
                "duplicate-or-out-of-space-fragments-dropped": str,
                "failures-of-source-address-selection": str,
                "forward-cache-hit": str,
                "forward-cache-miss": str,
                "fragments-that-exceeded-limit": str,
                "header-type": ListOf({
                    "globals": str,
                    "header-for-source-address-selection": str,
                    Optional("link-locals"): str,
                }),
                "histogram": str,
                "ip6-datagrams-that-can-not-be-fragmented": str,
                "ip6-fragments-created": str,
                "ip6-fragments-dropped-after-timeout": str,
                "ip6-fragments-received": str,
                "ip6-option-packets-dropped-due-to-rate-limit": str,
                "ip6-output-datagrams-fragmented": str,
                "ip6-output-packets-discarded-due-to-no-route": str,
                "ip6-output-packets-dropped-due-to-no-bufs": str,
                "ip6-packets-destined-to-dead-next-hop": str,
                "ip6-packets-dropped": str,
                "ip6-packets-for-this-host": str,
                "ip6-packets-forwarded": str,
                "ip6-packets-not-forwardable": str,
                "ip6-packets-reassembled-ok": str,
                "ip6-packets-sent-from-this-host": str,
                "ip6-packets-sent-with-fabricated-ip-header": str,
                "ip6-packets-with-bad-options": str,
                "ip6-packets-with-incorrect-version-number": str,
                "ip6-packets-with-size-smaller-than-minimum": str,
                "ip6-redirects-sent": str,
                "ip6nh-icmp6": str,
                "ip6nh-ospf": str,
                "ip6nh-tcp": str,
                "ip6nh-udp": str,
                "multicast-packets-which-we-do-not-join": str,
                "packets-discarded-due-to-too-may-headers": str,
                "packets-dropped-due-to-bad-protocol": str,
                "packets-that-violated-scope-rules": str,
                "packets-whose-headers-are-not-continuous": str,
                "packets-with-datasize-less-than-data-length": str,
                "transit-re-packet-dropped-on-mgmt-interface": str,
                "tunneling-packets-that-can-not-find-gif": str,
            },
            Optional("ipcomp"): {
                "ipcomp-bytes-in": str,
                "ipcomp-bytes-out": str,
                "ipcomp-crypto-processing-failure": str,
                "ipcomp-packets-blocked-due-to-policy": str,
                "ipcomp-packets-dropped-as-invalid-tdb": str,
                "ipcomp-packets-dropped-as-larger-than-ip-maxpacket": str,
                "ipcomp-packets-dropped-as-protocol-not-supported": str,
                "ipcomp-packets-dropped-due-to-bad-kcr": str,
                "ipcomp-packets-dropped-due-to-no-tdb": str,
                "ipcomp-packets-dropped-due-to-no-transform": str,
                "ipcomp-packets-dropped-due-to-queue-full": str,
                "ipcomp-packets-in": str,
                "ipcomp-packets-out": str,
                "ipcomp-packets-shorter-than-header-shows": str,
                "ipcomp-replay-counter-wrap": str,
                "packets-sent-uncompressed-threshold": str,
                "packets-sent-uncompressed-useless": str,
            },
            Optional("ipsec"): {
                "cluster-coalesced-during-clone": str,
                "cluster-copied-during-clone": str,
                "inbound-packets-violated-process-security-policy": str,
                "invalid-outbound-packets": str,
                "mbuf-coalesced-during-clone": str,
                "mbuf-inserted-during-makespace": str,
                "outbound-packets-failed-due-to-insufficient-memory": str,
                "outbound-packets-violated-process-security-policy": str,
                "outbound-packets-with-bundled-sa": str,
                "outbound-packets-with-no-route": str,
                "outbound-packets-with-no-sa-available": str,
            },
            Optional("ipsec6"): {
                "cluster-coalesced-during-clone": str,
                "cluster-copied-during-clone": str,
                "inbound-packets-violated-process-security-policy": str,
                "invalid-outbound-packets": str,
                "mbuf-coalesced-during-clone": str,
                "mbuf-inserted-during-makespace": str,
                "outbound-packets-failed-due-to-insufficient-memory": str,
                "outbound-packets-violated-process-security-policy": str,
                "outbound-packets-with-bundled-sa": str,
                "outbound-packets-with-no-route": str,
                "outbound-packets-with-no-sa-available": str,
            },
            Optional("mpls"): {
                "after-tagging-packets-can-not-fit-link-mtu": str,
                "lsp-ping-packets": str,
                "packets-dropped-at-mpls-socket-send": str,
                "packets-dropped-at-p2mp-cnh-output": str,
                "packets-dropped-due-to-ifl-down": str,
                "packets-forwarded-at-mpls-socket-send": str,
                "packets-with-header-too-small": str,
                "packets-with-ipv4-explicit-null-checksum-errors": str,
                "packets-with-ipv4-explicit-null-tag": str,
                "packets-with-router-alert-tag": str,
                "packets-with-tag-encoding-error": str,
                "packets-with-ttl-expired": str,
                "total-mpls-packets-received": str,
                "packets-discarded-due-to-no-route": str,
                "packets-dropped": str,
                "packets-forwarded": str,
                "packets-used-first-nexthop-in-ecmp-unilist": str,
            },
            Optional("pfkey"): {
                "bytes-sent-from-userland": str,
                "bytes-sent-to-userland": str,
                "incoming-messages-with-memory-allocation-failure": str,
                "input-histogram": {
                    "add": str,
                    "dump": str,
                    "reserved": str,
                    "histogram": str,
                },
                "messages-too-short": str,
                "messages-toward-all-sockets": str,
                "messages-toward-registered-sockets": str,
                "messages-toward-single-socket": str,
                "messages-with-duplicate-extension": str,
                "messages-with-invalid-address-extension": str,
                "messages-with-invalid-extension-type": str,
                "messages-with-invalid-length-field": str,
                "messages-with-invalid-message-type-field": str,
                "messages-with-invalid-sa-type": str,
                "messages-with-invalid-version-field": str,
                "outgoing-messages-with-memory-allocation-failure": str,
                "output-histogram": {
                    "add": str,
                    "dump": str,
                    "histogram": str,
                    "reserved": str,
                },
                "requests-sent-from-userland": str,
                "requests-sent-to-userland": str,
            },
            Optional("raw-interface"): {
                "dialer-packets-received": str,
                "dialer-packets-transmitted": str,
                "faboam-packets-dropped": str,
                "faboam-packets-received": str,
                "faboam-packets-transmitted": str,
                "fibre-channel-packets-dropped": str,
                "fibre-channel-packets-received": str,
                "fibre-channel-packets-transmitted": str,
                "fip-packets-dropped": str,
                "fip-packets-received": str,
                "fip-packets-transmitted": str,
                "igmpl2-packets-received": str,
                "igmpl2-packets-transmitted": str,
                "input-drops-due-to-bogus-protocol": str,
                "input-drops-due-to-no-mbufs-available": str,
                "input-drops-due-to-no-socket": str,
                "input-drops-due-to-no-space-in-socket": str,
                "isdn-packets-received": str,
                "isdn-packets-transmitted": str,
                "lacp-packets-dropped": str,
                "lacp-packets-received": str,
                "lacp-packets-transmitted": str,
                "mldl2-packets-received": str,
                "mldl2-packets-transmitted": str,
                "mpu-packets-received": str,
                "mpu-packets-transmitted": str,
                "output-drops-due-to-transmit-error": str,
                "ppoe-packets-transmitted": str,
                "ppp-packets-received-from-jppd": str,
                "ppp-packets-received-from-pppd": str,
                "ppp-packets-transmitted-to-jppd": str,
                "ppp-packets-transmitted-to-pppd": str,
                "pppoe-packets-received": str,
                "raw-packets-transmitted": str,
                "stp-packets-dropped": str,
                "stp-packets-received": str,
                "stp-packets-transmitted": str,
                "vccp-packets-dropped": str,
                "vccp-packets-received": str,
                "vccp-packets-transmitted": str,
            },
            Optional("rdp"): {
                "acks-received": str,
                "acks-sent": str,
                "closes": str,
                "connects": str,
                "input-packets": str,
                "keepalives-received": str,
                "keepalives-sent": str,
                "output-packets": str,
                "packets-discarded-due-to-bad-sequence-number": str,
                "packets-discarded-for-bad-checksum": str,
                "packets-dropped-due-to-full-socket-buffers": str,
                "packets-dropped-full-repl-sock-buf": str,
                "refused-connections": str,
                "retransmits": str,
            },
            Optional("tcp"): {
                "aborted": str,
                "packets-received": str,
                "packets-sent": str,
                "ack-header-predictions": str,
                "acks-bytes": str,
                "acks-sent-in-response-but-not-exact-rsts": str,
                "acks-sent-in-response-to-syns-on-established-connections": str,
                "attempts": str,
                "bad-connection-attempts": str,
                "badack": str,
                "bucket-overflow": str,
                "byte-retransmits": str,
                "bytes": str,
                "cache-overflow": str,
                "completed": str,
                "connection-accepts": str,
                "connection-requests": str,
                "connections-closed": str,
                "connections-dropped-by-persist-timeout": str,
                "connections-dropped-by-retransmit-timeout": str,
                "connections-established": str,
                "connections-updated-rtt-on-close": str,
                "connections-updated-ssthresh-on-close": str,
                "connections-updated-variance-on-close": str,
                "cookies-received": str,
                "cookies-sent": str,
                "data-packet-header-predictions": str,
                "data-packets-bytes": str,
                "dropped": str,
                "drops": str,
                "duplicate-in-bytes": str,
                "dupsyn": str,
                "embryonic-connections-dropped": str,
                "icmp-packets-ignored": str,
                "in-sequence-bytes": str,
                "keepalive-connections-dropped": str,
                "keepalive-probes-sent": str,
                "keepalive-timeouts": str,
                "listen-queue-overflows": str,
                "out-of-order-in-bytes": str,
                "out-of-sequence-segment-drops": str,
                "outgoing-segments-dropped": str,
                "packets-received-after-close": str,
                "packets-received-in-sequence": str,
                "persist-timeouts": str,
                "rcv-packets-dropped": str,
                "rcv-packets-dropped-due-to-bad-address": str,
                "received-acks": str,
                "received-acks-for-unsent-data": str,
                "received-completely-duplicate-packet": str,
                "received-discarded-because-packet-too-short": str,
                "received-discarded-for-bad-checksum": str,
                "received-discarded-for-bad-header-offset": str,
                "received-duplicate-acks": str,
                "received-old-duplicate-packets": str,
                "received-out-of-order-packets": str,
                "received-packets-of-data-after-window": str,
                "received-packets-with-some-dupliacte-data": str,
                "received-window-probes": str,
                "received-window-update-packets": str,
                "reset": str,
                "retransmit-timeouts": str,
                "retransmitted": str,
                "retransmitted-bytes": str,
                "rst-packets": str,
                "sack-opitions-sent": str,
                "sack-options-received": str,
                "sack-recovery-episodes": str,
                "sack-scoreboard-overflow": str,
                "segment-retransmits": str,
                "segments-updated-rtt": str,
                "send-packets-dropped": str,
                "sent-ack-only-packets": str,
                "sent-control-packets": str,
                "sent-data-packets": str,
                "sent-data-packets-retransmitted": str,
                "sent-packets-delayed": str,
                "sent-resends-by-mtu-discovery": str,
                "sent-urg-only-packets": str,
                "sent-window-probe-packets": str,
                "sent-window-update-packets": str,
                "some-duplicate-in-bytes": str,
                "stale": str,
                "syncache-entries-added": str,
                "unreach": str,
                "zone-failures": str,
            },
            Optional("tnp"): {
                "broadcast-packets-received": str,
                "broadcast-packets-sent": str,
                "control-packets-received": str,
                "control-packets-sent": str,
                "fragment-reassembly-queue-flushes": str,
                "fragmented-packets-received": str,
                "fragmented-packets-sent": str,
                "hello-packets-received": str,
                "hello-packets-sent": str,
                "input-packets-discarded-with-no-protocol": str,
                "packets-of-version-unspecified-received": str,
                "packets-of-version-unspecified-sent": str,
                "packets-of-version1-received": str,
                "packets-of-version1-sent": str,
                "packets-of-version2-received": str,
                "packets-of-version2-sent": str,
                "packets-of-version3-received": str,
                "packets-of-version3-sent": str,
                "packets-sent-with-unknown-protocol": str,
                "packets-with-tnp-src-address-collision-received": str,
                "rdp-packets-received": str,
                "rdp-packets-sent": str,
                "received-fragments-dropped": str,
                "received-hello-packets-dropped": str,
                "sent-fragments-dropped": str,
                "sent-hello-packets-dropped": str,
                "tunnel-packets-received": str,
                "tunnel-packets-sent": str,
                "udp-packets-received": str,
                "udp-packets-sent": str,
                "unicast-packets-received": str,
                "unicast-packets-sent": str,
            },
            Optional("ttp"): {
                "arp-l3-packets-received": str,
                "clnp-l3-packets-received": str,
                "cyclotron-cycle-l3-packets-received": str,
                "cyclotron-send-l3-packets-received": str,
                "input-packets-could-not-get-buffer": str,
                "input-packets-for-which-route-lookup-is-bypassed": str,
                "input-packets-tlv-dropped": str,
                "input-packets-with-bad-af": str,
                "input-packets-with-bad-tlv-header": str,
                "input-packets-with-bad-tlv-type": str,
                "input-packets-with-bad-type": str,
                "input-packets-with-discard-type": str,
                "input-packets-with-too-many-tlvs": str,
                "input-packets-with-ttp-tlv-p2mp-nbr-nhid-type": str,
                "input-packets-with-unknown-p2mp-nbr-nhid": str,
                "input-packets-with-vxlan-bfd-pkts": str,
                "ipv4-l3-packets-received": str,
                "ipv4-to-mpls-l3-packets-received": str,
                "ipv6-l3-packets-received": str,
                "l2-packets-received": str,
                "l3-packets-dropped": str,
                "l3-packets-sent-could-not-get-buffer": str,
                "mpls-l3-packets-received": str,
                "mpls-to-ipv4-l3-packets-received": str,
                "null-l3-packets-received": str,
                "openflow-packets-received": str,
                "packets-received-from-unknown-ifl": str,
                "packets-received-while-unconnected": str,
                "packets-sent-could-not-find-neighbor": str,
                "packets-sent-could-not-get-buffer": str,
                "packets-sent-when-host_unreachable": str,
                "packets-sent-when-transmit-disabled": str,
                "packets-sent-while-interface-down": str,
                "packets-sent-while-unconnected": str,
                "packets-sent-with-bad-af": str,
                "packets-sent-with-bad-ifl": str,
                "tnp-l3-packets-received": str,
                "ttp-packets-sent": str,
                "unknown-l3-packets-received": str,
                "vpls-l3-packets-received": str,
            },
            Optional("tudp"): {
                "broadcast-or-multicast-datagrams-dropped-due-to-no-socket": str,
                "datagrams-dropped-due-to-full-socket-buffers": str,
                "datagrams-dropped-due-to-no-socket": str,
                "datagrams-output": str,
                "datagrams-with-bad-checksum": str,
                "datagrams-with-bad-data-length-field": str,
                "datagrams-with-incomplete-header": str,
                "delivered": str,
                "datagrams-received": str,
            },
            Optional("udp"): {
                "broadcast-or-multicast-datagrams-dropped-due-to-no-socket": str,
                "datagrams-delivered": str,
                "datagrams-dropped-due-to-full-socket-buffers": str,
                "datagrams-dropped-due-to-no-socket": str,
                "datagrams-not-for-hashed-pcb": str,
                "datagrams-output": str,
                "datagrams-received": str,
                "datagrams-with-bad-checksum": str,
                "datagrams-with-bad-datalength-field": str,
                "datagrams-with-incomplete-header": str,
            },
            Optional("bridge"): {
                "aging-acks-from-pfe": str,
                "aging-non-acks-from-pfe": str,
                "aging-requests-over-max-rate": str,
                "aging-requests-timed-out-waiting-on-fes": str,
                "bogus-address-in-aging-requests": str,
                "errors-finding-peer-fes": str,
                "learning-requests-over-capacity": str,
                "learning-requests-while-learning-disabled-on-interface": str,
                "mac-route-aging-requests": str,
                "mac-route-learning-requests": str,
                "mac-routes-aged": str,
                "mac-routes-learned": str,
                "mac-routes-moved": str,
                "packets-dropped-due-to-no-l3-route-table": str,
                "packets-dropped-due-to-no-local-ifl": str,
                "packets-dropped-due-to-no-socket": str,
                "packets-for-this-host": str,
                "packets-punted": str,
                "packets-received": str,
                "packets-with-incorrect-version-number": str,
                "packets-with-no-auxiliary-table": str,
                "packets-with-no-ce-facing-entry": str,
                "packets-with-no-core-facing-entry": str,
                "packets-with-no-family": str,
                "packets-with-no-logical-interface": str,
                "packets-with-no-route-table": str,
                "packets-with-size-smaller-than-minimum": str,
                "requests-involving-multiple-peer-fes": str,
                "requests-to-age-static-route": str,
                "requests-to-learn-an-existing-route": str,
                "requests-to-move-static-route": str,
                "requests-to-re-ageout-aged-route": str,
                "unsupported-platform": str,
            },
            Optional("vpls"): {
                "aging-acks-from-pfe": str,
                "aging-non-acks-from-pfe": str,
                "aging-requests-over-max-rate": str,
                "aging-requests-timed-out-waiting-on-fes": str,
                "bogus-address-in-aging-requests": str,
                "errors-finding-peer-fes": str,
                "learning-requests-over-capacity": str,
                "learning-requests-while-learning-disabled-on-interface": str,
                "mac-route-aging-requests": str,
                "mac-route-learning-requests": str,
                "mac-routes-aged": str,
                "mac-routes-learned": str,
                "mac-routes-moved": str,
                "packets-dropped-due-to-no-l3-route-table": str,
                "packets-dropped-due-to-no-local-ifl": str,
                "packets-dropped-due-to-no-socket": str,
                "packets-for-this-host": str,
                "packets-punted": str,
                "packets-received": str,
                "packets-with-incorrect-version-number": str,
                "packets-with-no-auxiliary-table": str,
                "packets-with-no-ce-facing-entry": str,
                "packets-with-no-core-facing-entry": str,
                "packets-with-no-family": str,
                "packets-with-no-logical-interface": str,
                "packets-with-no-route-table": str,
                "packets-with-size-smaller-than-minimum": str,
                "requests-involving-multiple-peer-fes": str,
                "requests-to-age-static-route": str,
                "requests-to-learn-an-existing-route": str,
                "requests-to-move-static-route": str,
                "requests-to-re-ageout-aged-route": str,
                "unsupported-platform": str,
            },
        }
    )}


class ShowSystemStatistics(ShowSystemStatisticsSchema):
    """ Parser for:
            * show system statistics
    """

    cli_command = "show system statistics"

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Tcp:
        p1 = re.compile(r"^(?P<state>\S+):$")

        # 265063785 packets sent
        # 0 interface-restricted dad proxy duplicates
        # 4214 IPv4->MPLS L3 packets received
        # 5 LSP ping packets (ttl-expired/router alert)
        p2 = re.compile(
            r"^(?P<number_value>\d+) +(?P<key>([\w\-\'\>\,\/\.\<\s]|\([(\D+)\s]+\))+)$"
        )

        # 52538606 data packets (49634888 bytes)
        p3 = re.compile(
            r"^(?P<number_value_one>\d+) +(?P<key>[\D\s]+)\([(\D+)\s]*"
            r"(?P<number_value_two>\d+)[(\D+)\s]*\)$")

        # Output Histogram
        p4 = re.compile(r"^(?P<histogram_type>\S+) +Histogram$")

        # source addresses on an outgoing I/F
        p5 = re.compile(
            r"^(?P<header_for_source_address_selection>source +addresses +[\S\s]+)$"
        )

        # Output histogram:
        p6 = re.compile(r"^(?P<histogram_type>\S+) +histogram:$")

        # histogram by message type:
        p7 = re.compile(r"^histogram +by +message +type:$")

        ret_dict = {}

        self.state = None

        self.pfkey_state = None

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:

                if not ret_dict:
                    ret_dict["statistics"] = [{}, {}]

                group = m.groupdict()
                self.state = group["state"]

                if self.state == "icmp6":
                    self.icmp6_histogram = None

                continue

            if self.state == "Tcp":
                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("tcp", {})

                    if key == "packets_sent":
                        entry["packets-sent"] = value
                    elif key == "resends_initiated_by_MTU_discovery":
                        entry["sent-resends-by-mtu-discovery"] = value
                    elif key == "URG_only_packets":
                        entry["sent-urg-only-packets"] = value
                    elif key == "window_probe_packets":
                        entry["sent-window-probe-packets"] = value
                    elif key == "window_update_packets":
                        if not "sent-window-update-packets" in entry:
                            entry["sent-window-update-packets"] = value
                        else:
                            entry["received-window-update-packets"] = value
                    elif key == "control_packets":
                        entry["sent-control-packets"] = value
                    elif key == "packets_received":
                        entry["packets-received"] = value
                    elif key == "duplicate_acks":
                        entry["received-duplicate-acks"] = value
                    elif key == "acks_for_unsent_data":
                        entry["received-acks-for-unsent-data"] = value
                    elif key == "old_duplicate_packets":
                        entry["received-old-duplicate-packets"] = value
                    elif key == "window_probes":
                        entry["received-window-probes"] = value
                    elif key == "packets_received_after_close":
                        entry["packets-received-after-close"] = value
                    elif key == "discarded_for_bad_checksums":
                        entry["received-discarded-for-bad-checksum"] = value
                    elif key == "discarded_for_bad_header_offset_fields":
                        entry[
                            "received-discarded-for-bad-header-offset"] = value
                    elif key == "discarded_because_packet_too_short":
                        entry[
                            "received-discarded-because-packet-too-short"] = value
                    elif key == "connection_requests":
                        entry["connection-requests"] = value
                    elif key == "connection_accepts":
                        entry["connection-accepts"] = value
                    elif key == "bad_connection_attempts":
                        entry["bad-connection-attempts"] = value
                    elif key == "listen_queue_overflows":
                        entry["listen-queue-overflows"] = value
                    elif key == "connections_established_(including_accepts)":
                        entry["connections-established"] = value
                    elif key == "connections_updated_cached_RTT_on_close":
                        entry["connections-updated-rtt-on-close"] = value
                    elif key == "connections_updated_cached_RTT_variance_on_close":
                        entry["connections-updated-variance-on-close"] = value
                    elif key == "connections_updated_cached_ssthresh_on_close":
                        entry["connections-updated-ssthresh-on-close"] = value
                    elif key == "embryonic_connections_dropped":
                        entry["embryonic-connections-dropped"] = value
                    elif key == "retransmit_timeouts":
                        entry["retransmit-timeouts"] = value
                    elif key == "connections_dropped_by_retransmit_timeout":
                        entry[
                            "connections-dropped-by-retransmit-timeout"] = value
                    elif key == "persist_timeouts":
                        entry["persist-timeouts"] = value
                    elif key == "connections_dropped_by_persist_timeout":
                        entry["connections-dropped-by-persist-timeout"] = value
                    elif key == "keepalive_timeouts":
                        entry["keepalive-timeouts"] = value
                    elif key == "keepalive_probes_sent":
                        entry["keepalive-probes-sent"] = value
                    elif key == "connections_dropped_by_keepalive":
                        entry["keepalive-connections-dropped"] = value
                    elif key == "correct_ACK_header_predictions":
                        entry["ack-header-predictions"] = value
                    elif key == "correct_data_packet_header_predictions":
                        entry["data-packet-header-predictions"] = value
                    elif key == "syncache_entries_added":
                        entry["syncache-entries-added"] = value
                    elif key == "retransmitted":
                        entry["retransmitted"] = value
                    elif key == "dupsyn":
                        entry["dupsyn"] = value
                    elif key == "dropped":
                        entry["dropped"] = value
                    elif key == "completed":
                        entry["completed"] = value
                    elif key == "bucket_overflow":
                        entry["bucket-overflow"] = value
                    elif key == "cache_overflow":
                        entry["cache-overflow"] = value
                    elif key == "reset":
                        entry["reset"] = value
                    elif key == "stale":
                        entry["stale"] = value
                    elif key == "aborted":
                        entry["aborted"] = value
                    elif key == "badack":
                        entry["badack"] = value
                    elif key == "unreach":
                        entry["unreach"] = value
                    elif key == "zone_failures":
                        entry["zone-failures"] = value
                    elif key == "cookies_sent":
                        entry["cookies-sent"] = value
                    elif key == "cookies_received":
                        entry["cookies-received"] = value
                    elif key == "SACK_recovery_episodes":
                        entry["sack-recovery-episodes"] = value
                    elif key == "segment_retransmits_in_SACK_recovery_episodes":
                        entry["segment-retransmits"] = value
                    elif key == "byte_retransmits_in_SACK_recovery_episodes":
                        entry["byte-retransmits"] = value
                    elif key == "SACK_options_(SACK_blocks)_received":
                        entry["sack-options-received"] = value
                    elif key == "SACK_options_(SACK_blocks)_sent":
                        entry["sack-opitions-sent"] = value
                    elif key == "SACK_scoreboard_overflow":
                        entry["sack-scoreboard-overflow"] = value
                    elif key == "ACKs_sent_in_response_to_in-window_but_not_exact_RSTs":
                        entry[
                            "acks-sent-in-response-but-not-exact-rsts"] = value
                    elif (key ==
                          "ACKs_sent_in_response_to_in-window_SYNs_on_established_connections"
                          ):
                        entry[
                            "acks-sent-in-response-to-syns-on-established-connections"] = value
                    elif key == "rcv_packets_dropped_by_TCP_due_to_bad_address":
                        entry["rcv-packets-dropped-due-to-bad-address"] = value
                    elif (key ==
                          "out-of-sequence_segment_drops_due_to_insufficient_memory"
                          ):
                        entry["out-of-sequence-segment-drops"] = value
                    elif key == "RST_packets":
                        entry["rst-packets"] = value
                    elif key == "ICMP_packets_ignored_by_TCP":
                        entry["icmp-packets-ignored"] = value
                    elif key == "send_packets_dropped_by_TCP_due_to_auth_errors":
                        entry["send-packets-dropped"] = value
                    elif key == "rcv_packets_dropped_by_TCP_due_to_auth_errors":
                        entry["rcv-packets-dropped"] = value
                    elif key == "outgoing_segments_dropped_due_to_policing":
                        entry["outgoing-segments-dropped"] = value

                    continue

                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value_one = group["number_value_one"]
                    value_two = group["number_value_two"]

                    entry = ret_dict["statistics"][0].setdefault("tcp", {})

                    if key == "data_packets":
                        entry["sent-data-packets"] = value_one
                        entry["data-packets-bytes"] = value_two
                    elif key == "data_packets_retransmitted":
                        entry["sent-data-packets-retransmitted"] = value_one
                        entry["retransmitted-bytes"] = value_two
                    elif key == "ack_only_packets":
                        entry["sent-ack-only-packets"] = value_one
                        entry["sent-packets-delayed"] = value_two
                    elif key == "acks":
                        entry["received-acks"] = value_one
                        entry["acks-bytes"] = value_two
                    elif key == "packets_received_in-sequence":
                        entry["packets-received-in-sequence"] = value_one
                        entry["in-sequence-bytes"] = value_two
                    elif key == "completely_duplicate_packets":
                        entry[
                            "received-completely-duplicate-packet"] = value_one
                        entry["duplicate-in-bytes"] = value_two
                    elif key == "packets_with_some_duplicate_data":
                        entry[
                            "received-packets-with-some-dupliacte-data"] = value_one
                        entry["some-duplicate-in-bytes"] = value_two
                    elif key == "out-of-order_packets":
                        entry["received-out-of-order-packets"] = value_one
                        entry["out-of-order-in-bytes"] = value_two
                    elif key == "packets_of_data_after_window":
                        entry[
                            "received-packets-of-data-after-window"] = value_one
                        entry["bytes"] = value_two
                    elif key == "connections_closed":
                        entry["connections-closed"] = value_one
                        entry["drops"] = value_two
                    elif key == "segments_updated_rtt":
                        entry["segments-updated-rtt"] = value_one
                        entry["attempts"] = value_two

                    continue

            if self.state == "udp":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("udp", {})

                    if key == "datagrams_received":
                        entry["datagrams-received"] = value
                    elif key == "with_incomplete_header":
                        entry["datagrams-with-incomplete-header"] = value
                    elif key == "with_bad_data_length_field":
                        entry["datagrams-with-bad-datalength-field"] = value
                    elif key == "with_bad_checksum":
                        entry["datagrams-with-bad-checksum"] = value
                    elif key == "dropped_due_to_no_socket":
                        entry["datagrams-dropped-due-to-no-socket"] = value
                    elif (key ==
                          "broadcast/multicast_datagrams_dropped_due_to_no_socket"
                          ):
                        entry[
                            "broadcast-or-multicast-datagrams-dropped-due-to-no-socket"] = value
                    elif key == "dropped_due_to_full_socket_buffers":
                        entry[
                            "datagrams-dropped-due-to-full-socket-buffers"] = value
                    elif key == "not_for_hashed_pcb":
                        entry["datagrams-not-for-hashed-pcb"] = value
                    elif key == "delivered":
                        entry["datagrams-delivered"] = value
                    elif key == "datagrams_output":
                        entry["datagrams-output"] = value

                continue

            if self.state == "ip":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("ip", {})

                    if key == "total_packets_received":
                        entry["packets-received"] = value
                    elif key == "bad_header_checksums":
                        entry["bad-header-checksums"] = value
                    elif key == "with_size_smaller_than_minimum":
                        entry["packets-with-size-smaller-than-minimum"] = value
                    elif key == "with_data_size_<_data_length":
                        entry[
                            "packets-with-data-size-less-than-datalength"] = value
                    elif key == "with_header_length_<_data_size":
                        entry[
                            "packets-with-header-length-less-than-data-size"] = value
                    elif key == "with_data_length_<_header_length":
                        entry[
                            "packets-with-data-length-less-than-headerlength"] = value
                    elif key == "with_incorrect_version_number":
                        entry["packets-with-incorrect-version-number"] = value
                    elif key == "packets_destined_to_dead_next_hop":
                        entry["packets-destined-to-dead-next-hop"] = value
                    elif key == "fragments_received":
                        entry["fragments-received"] = value
                    elif key == "fragments_dropped_(dup_or_out_of_space)":
                        entry[
                            "fragments-dropped-due-to-outofspace-or-dup"] = value
                    elif key == "fragment_sessions_dropped_(queue_overflow)":
                        entry["fragments-dropped-due-to-queueoverflow"] = value
                    elif key == "fragments_dropped_after_timeout":
                        entry["fragments-dropped-after-timeout"] = value
                    elif key == "packets_reassembled_ok":
                        entry["packets-reassembled-ok"] = value
                    elif key == "packets_for_this_host":
                        entry["packets-for-this-host"] = value
                    elif key == "packets_for_unknown/unsupported_protocol":
                        entry[
                            "packets-for-unknown-or-unsupported-protocol"] = value
                    elif key == "packets_forwarded":
                        entry["packets-forwarded"] = value
                    elif key == "packets_not_forwardable":
                        entry["packets-not-forwardable"] = value
                    elif key == "redirects_sent":
                        entry["redirects-sent"] = value
                    elif key == "packets_sent_from_this_host":
                        entry["packets-sent-from-this-host"] = value
                    elif key == "packets_sent_with_fabricated_ip_header":
                        entry["packets-sent-with-fabricated-ip-header"] = value
                    elif key == "output_packets_dropped_due_to_no_bufs":
                        entry["output-packets-dropped-due-to-no-bufs"] = value
                    elif key == "output_packets_discarded_due_to_no_route":
                        entry[
                            "output-packets-discarded-due-to-no-route"] = value
                    elif key == "output_datagrams_fragmented":
                        entry["output-datagrams-fragmented"] = value
                    elif key == "fragments_created":
                        entry["fragments-created"] = value
                    elif key == "datagrams_that_can't_be_fragmented":
                        entry["datagrams-that-can-not-be-fragmented"] = value
                    elif key == "packets_with_bad_options":
                        entry["packets-with-bad-options"] = value
                    elif key == "packets_with_options_handled_without_error":
                        entry[
                            "packets-with-options-handled-without-error"] = value
                    elif key == "strict_source_and_record_route_options":
                        entry["strict-source-and-record-route-options"] = value
                    elif key == "loose_source_and_record_route_options":
                        entry["loose-source-and-record-route-options"] = value
                    elif key == "record_route_options":
                        entry["record-route-options"] = value
                    elif key == "timestamp_options":
                        entry["timestamp-options"] = value
                    elif key == "timestamp_and_address_options":
                        entry["timestamp-and-address-options"] = value
                    elif key == "timestamp_and_prespecified_address_options":
                        entry[
                            "timestamp-and-prespecified-address-options"] = value
                    elif key == "option_packets_dropped_due_to_rate_limit":
                        entry[
                            "option-packets-dropped-due-to-rate-limit"] = value
                    elif key == "router_alert_options":
                        entry["router-alert-options"] = value
                    elif key == "multicast_packets_dropped_(no_iflist)":
                        entry["multicast-packets-dropped"] = value
                    elif key == "packets_dropped_(src_and_int_don't_match)":
                        entry["packets-dropped"] = value
                    elif key == "transit_re_packets_dropped_on_mgmt_i/f":
                        entry[
                            "transit-re-packets-dropped-on-mgmt-interface"] = value
                    elif key == "packets_used_first_nexthop_in_ecmp_unilist":
                        entry[
                            "packets-used-first-nexthop-in-ecmp-unilist"] = value
                    elif key == "incoming_ttpoip_packets_received":
                        entry["incoming-ttpoip-packets-received"] = value
                    elif key == "incoming_ttpoip_packets_dropped":
                        entry["incoming-ttpoip-packets-dropped"] = value
                    elif key == "outgoing_TTPoIP_packets_sent":
                        entry["outgoing-ttpoip-packets-sent"] = value
                    elif key == "outgoing_TTPoIP_packets_dropped":
                        entry["outgoing-ttpoip-packets-dropped"] = value
                    elif key == "raw_packets_dropped._no_space_in_socket_recv_buffer":
                        entry[
                            "incoming-rawip-packets-dropped-no-socket-buffer"] = value
                    elif key == "packets_consumed_by_virtual-node_processing":
                        entry[
                            "incoming-virtual-node-packets-delivered"] = value

                    continue

            if self.state == "icmp":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("icmp", {})

                    if key == "drops_due_to_rate_limit":
                        entry["drops-due-to-rate-limit"] = value
                    elif key == "calls_to_icmp_error":
                        entry["calls-to-icmp-error"] = value
                    elif key == "errors_not_generated_because_old_message_was_icmp":
                        entry[
                            "errors-not-generated-because-old-message-was-icmp"] = value
                    elif key == "echo_reply":
                        entry["histogram"][-1]["icmp-echo-reply"] = value
                    elif key == "destination_unreachable":
                        entry["histogram"][-1][
                            "destination-unreachable"] = value
                    elif key == "echo":
                        entry["histogram"][-1]["icmp-echo"] = value
                    elif key == "time_exceeded":
                        entry["histogram"][-1]["time-exceeded"] = value
                    elif key == "messages_with_bad_code_fields":
                        entry["messages-with-bad-code-fields"] = value
                    elif key == "messages_less_than_the_minimum_length":
                        entry["messages-less-than-the-minimum-length"] = value
                    elif key == "messages_with_bad_checksum":
                        entry["messages-with-bad-checksum"] = value
                    elif key == "messages_with_bad_source_address":
                        entry["messages-with-bad-source-address"] = value
                    elif key == "messages_with_bad_length":
                        entry["messages-with-bad-length"] = value
                    elif (key ==
                          "echo_drops_with_broadcast_or_multicast_destinaton_address"
                          ):
                        entry[
                            "echo-drops-with-broadcast-or-multicast-destinaton-address"] = value
                    elif (key ==
                          "timestamp_drops_with_broadcast_or_multicast_destination_address"
                          ):
                        entry[
                            "timestamp-drops-with-broadcast-or-multicast-destination-address"] = value
                    elif key == "message_responses_generated":
                        entry["message-responses-generated"] = value

                    continue

                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    histogram_type = group["histogram_type"]
                    histogram_list = (ret_dict["statistics"][0].setdefault(
                        "icmp", {}).setdefault("histogram", []))
                    entry = {"type-of-histogram": line}
                    histogram_list.append(entry)
                    continue

            if self.state == "igmp":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("igmp", {})

                    if key == "messages_received":
                        entry["messages-received"] = value
                    elif key == "messages_received_with_too_few_bytes":
                        entry["messages-received-with-too-few-bytes"] = value
                    elif key == "messages_received_with_bad_checksum":
                        entry["messages-received-with-bad-checksum"] = value
                    elif key == "membership_queries_received":
                        entry["membership-queries-received"] = value
                    elif key == "membership_queries_received_with_invalid_fields":
                        entry[
                            "membership-queries-received-with-invalid-fields"] = value
                    elif key == "membership_reports_received":
                        entry["membership-reports-received"] = value
                    elif key == "membership_reports_received_with_invalid_fields":
                        entry[
                            "membership-reports-received-with-invalid-fields"] = value
                    elif (key ==
                          "membership_reports_received_for_groups_to_which_we_belong"
                          ):
                        entry[
                            "membership-reports-received-for-groups-to-which-we-belong"] = value
                    elif key == "Membership_reports_sent":
                        entry["membership-reports-sent"] = value

                    continue

            if self.state == "ipsec":

                m = p2.match(line)
                if m:

                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("ipsec", {})

                    if key == "inbound_packets_violated_process_security_policy":
                        entry[
                            "inbound-packets-violated-process-security-policy"] = value
                    elif key == "Outbound_packets_violated_process_security_policy":
                        entry[
                            "outbound-packets-violated-process-security-policy"] = value
                    elif key == "outbound_packets_with_no_SA_available":
                        entry["outbound-packets-with-no-sa-available"] = value
                    elif key == "outbound_packets_failed_due_to_insufficient_memory":
                        entry[
                            "outbound-packets-failed-due-to-insufficient-memory"] = value
                    elif key == "outbound_packets_with_no_route":
                        entry["outbound-packets-with-no-route"] = value
                    elif key == "invalid_outbound_packets":
                        entry["invalid-outbound-packets"] = value
                    elif key == "Outbound_packets_with_bundles_SAs":
                        entry["outbound-packets-with-bundled-sa"] = value
                    elif key == "mbuf_coleasced_during_clone":
                        entry["mbuf-coalesced-during-clone"] = value
                    elif key == "Cluster_coalesced_during_clone":
                        entry["cluster-coalesced-during-clone"] = value
                    elif key == "Cluster_copied_during_clone":
                        entry["cluster-copied-during-clone"] = value
                    elif key == "mbuf_inserted_during_makespace":
                        entry["mbuf-inserted-during-makespace"] = value

                    continue

            if self.state == "ah":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("ah", {})

                    if key == "packets_shorter_than_header_shows":
                        entry["packets-shorter-than-header-shows"] = value
                    elif key == "packets_dropped_protocol_unsupported":
                        entry[
                            "packets-dropped-as-protocol-unsupported"] = value
                    elif key == "packets_dropped_no_TDB":
                        entry["packets-dropped-due-to-no-tdb"] = value
                    elif key == "packets_dropped_bad_KCR":
                        entry["packets-dropped-due-to-bad-kcr"] = value
                    elif key == "packets_dropped_queue_full":
                        entry["packets-dropped-due-to-queue-full"] = value
                    elif key == "packets_dropped_no_transform":
                        entry["packets-dropped-due-to-no-transform"] = value
                    elif key == "replay_counter_wrap":
                        entry["replay-counter-wrap"] = value
                    elif key == "packets_dropped_bad_authentication_detected":
                        entry[
                            "packets-dropped-as-bad-authentication-detected"] = value
                    elif key == "packets_dropped_bad_authentication_length":
                        entry[
                            "packets-dropped-due-to-bad-authentication-length"] = value
                    elif key == "possible_replay_packets_detected":
                        entry["possible-replay-packets-detected"] = value
                    elif key == "packets_in":
                        entry["packets-in"] = value
                    elif key == "packets_out":
                        entry["packets-out"] = value
                    elif key == "packets_dropped_invalid_TDB":
                        entry["packets-dropped-due-to-invalid-tdb"] = value
                    elif key == "bytes_in":
                        entry["bytes-in"] = value
                    elif key == "bytes_out":
                        entry["bytes-out"] = value
                    elif key == "packets_dropped_larger_than_maxpacket":
                        entry[
                            "packets-dropped-as-larger-than-ip-maxpacket"] = value
                    elif key == "packets_blocked_due_to_policy":
                        entry["packets-blocked-due-to-policy"] = value
                    elif key == "crypto_processing_failure":
                        entry["crypto-processing-failure"] = value
                    elif key == "tunnel_sanity_check_failures":
                        entry["tunnel-sanity-check-failures"] = value

                    continue

            if self.state == "esp":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("esp", {})

                    if key == "packets_shorter_than_header_shows":
                        entry["esp-packets-shorter-than-header-shows"] = value
                    elif key == "packets_dropped_protocol_not_supported":
                        entry[
                            "esp-packets-dropped-as-protocol-not-supported"] = value
                    elif key == "packets_dropped_no_TDB":
                        entry["esp-packets-dropped-due-to-no-tdb"] = value
                    elif key == "packets_dropped_bad_KCR":
                        entry["esp-packets-dropped-due-to-bad-kcr"] = value
                    elif key == "packets_dropped_queue_full":
                        entry["esp-packets-dropped-due-to-queue-full"] = value
                    elif key == "packets_dropped_no_transform":
                        entry[
                            "esp-packets-dropped-due-to-no-transform"] = value
                    elif key == "packets_dropped_bad_ilen":
                        entry["esp-packets-dropped-as-bad-ilen"] = value
                    elif key == "replay_counter_wrap":
                        entry["esp-replay-counter-wrap"] = value
                    elif key == "packets_dropped_bad_encryption_detected":
                        entry[
                            "esp-packets-dropped-as-bad-encryption-detected"] = value
                    elif key == "packets_dropped_bad_authentication_detected":
                        entry[
                            "esp-packets-dropped-as-bad-authentication-detected"] = value
                    elif key == "possible_replay_packets_detected":
                        entry["esp-possible-replay-packets-detected"] = value
                    elif key == "packets_in":
                        entry["esp-packets-in"] = value
                    elif key == "packets_out":
                        entry["esp-packets-out"] = value
                    elif key == "packets_dropped_invalid_TDB":
                        entry["esp-packets-dropped-as-invalid-tdb"] = value
                    elif key == "bytes_in":
                        entry["esp-bytes-in"] = value
                    elif key == "bytes_out":
                        entry["esp-bytes-out"] = value
                    elif key == "packets_dropped_larger_than_maxpacket":
                        entry[
                            "esp-packets-dropped-as-larger-than-ip-maxpacket"] = value
                    elif key == "packets_blocked_due_to_policy":
                        entry["esp-packets-blocked-due-to-policy"] = value
                    elif key == "crypto_processing_failure":
                        entry["esp-crypto-processing-failure"] = value
                    elif key == "tunnel_sanity_check_failures":
                        entry["esp-tunnel-sanity-check-failures"] = value

                    continue

            if self.state == "ipcomp":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("ipcomp", {})

                    if key == "packets_shorter_than_header_shows":
                        entry[
                            "ipcomp-packets-shorter-than-header-shows"] = value
                    elif key == "packets_dropped_protocol_not_supported":
                        entry[
                            "ipcomp-packets-dropped-as-protocol-not-supported"] = value
                    elif key == "packets_dropped_no_TDB":
                        entry["ipcomp-packets-dropped-due-to-no-tdb"] = value
                    elif key == "packets_dropped_bad_KCR":
                        entry["ipcomp-packets-dropped-due-to-bad-kcr"] = value
                    elif key == "packets_dropped_queue_full":
                        entry[
                            "ipcomp-packets-dropped-due-to-queue-full"] = value
                    elif key == "packets_dropped_no_transform":
                        entry[
                            "ipcomp-packets-dropped-due-to-no-transform"] = value
                    elif key == "replay_counter_wrap":
                        entry["ipcomp-replay-counter-wrap"] = value
                    elif key == "packets_in":
                        entry["ipcomp-packets-in"] = value
                    elif key == "packets_out":
                        entry["ipcomp-packets-out"] = value
                    elif key == "packets_dropped_invalid_TDB":
                        entry["ipcomp-packets-dropped-as-invalid-tdb"] = value
                    elif key == "bytes_in":
                        entry["ipcomp-bytes-in"] = value
                    elif key == "bytes_out":
                        entry["ipcomp-bytes-out"] = value
                    elif key == "packets_dropped_larger_than_maxpacket":
                        entry[
                            "ipcomp-packets-dropped-as-larger-than-ip-maxpacket"] = value
                    elif key == "packets_blocked_due_to_policy":
                        entry["ipcomp-packets-blocked-due-to-policy"] = value
                    elif key == "crypto_processing_failure":
                        entry["ipcomp-crypto-processing-failure"] = value
                    elif key == "packets_sent_uncompressed_threshold":
                        entry["packets-sent-uncompressed-threshold"] = value
                    elif key == "packets_sent_uncompressed_useless":
                        entry["packets-sent-uncompressed-useless"] = value

                    continue

            if self.state == "raw_if":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault(
                        "raw-interface", {})

                    if key == "RAW_packets_transmitted":
                        entry["raw-packets-transmitted"] = value
                    elif key == "PPPOE_packets_transmitted":
                        entry["ppoe-packets-transmitted"] = value
                    elif key == "ISDN_packets_transmitted":
                        entry["isdn-packets-transmitted"] = value
                    elif key == "DIALER_packets_transmitted":
                        entry["dialer-packets-transmitted"] = value
                    elif key == "PPP_packets_transmitted_to_pppd":
                        entry["ppp-packets-transmitted-to-pppd"] = value
                    elif key == "PPP_packets_transmitted_to_jppd":
                        entry["ppp-packets-transmitted-to-jppd"] = value
                    elif key == "IGMPL2_packets_transmitted":
                        entry["igmpl2-packets-transmitted"] = value
                    elif key == "MLDL2_packets_transmitted":
                        entry["mldl2-packets-transmitted"] = value
                    elif key == "Fibre_Channel_packets_transmitted":
                        entry["fibre-channel-packets-transmitted"] = value
                    elif key == "FIP_packets_transmitted":
                        entry["fip-packets-transmitted"] = value
                    elif key == "STP_packets_transmitted":
                        entry["stp-packets-transmitted"] = value
                    elif key == "LACP_packets_transmitted":
                        entry["lacp-packets-transmitted"] = value
                    elif key == "VCCP_packets_transmitted":
                        entry["vccp-packets-transmitted"] = value
                    elif key == "Fabric_OAM_packets_transmitted":
                        entry["faboam-packets-transmitted"] = value
                    elif key == "output_drops_due_to_tx_error":
                        entry["output-drops-due-to-transmit-error"] = value
                    elif key == "MPU_packets_transmitted":
                        entry["mpu-packets-transmitted"] = value
                    elif key == "PPPOE_packets_received":
                        entry["pppoe-packets-received"] = value
                    elif key == "ISDN_packets_received":
                        entry["isdn-packets-received"] = value
                    elif key == "DIALER_packets_received":
                        entry["dialer-packets-received"] = value
                    elif key == "PPP_packets_received_from_pppd":
                        entry["ppp-packets-received-from-pppd"] = value
                    elif key == "MPU_packets_received":
                        entry["mpu-packets-received"] = value
                    elif key == "PPP_packets_received_from_jppd":
                        entry["ppp-packets-received-from-jppd"] = value
                    elif key == "IGMPL2_packets_received":
                        entry["igmpl2-packets-received"] = value
                    elif key == "MLDL2_packets_received":
                        entry["mldl2-packets-received"] = value
                    elif key == "Fibre_Channel_packets_received":
                        entry["fibre-channel-packets-received"] = value
                    elif key == "FIP_packets_received":
                        entry["fip-packets-received"] = value
                    elif key == "STP_packets_received":
                        entry["stp-packets-received"] = value
                    elif key == "LACP_packets_received":
                        entry["lacp-packets-received"] = value
                    elif key == "VCCP_packets_received":
                        entry["vccp-packets-received"] = value
                    elif key == "Fabric_OAM_packets_received":
                        entry["faboam-packets-received"] = value
                    elif key == "Fibre_Channel_packets_dropped":
                        entry["fibre-channel-packets-dropped"] = value
                    elif key == "FIP_packets_dropped":
                        entry["fip-packets-dropped"] = value
                    elif key == "STP_packets_dropped":
                        entry["stp-packets-dropped"] = value
                    elif key == "LACP_packets_dropped":
                        entry["lacp-packets-dropped"] = value
                    elif key == "Fabric_OAM_packets_dropped":
                        entry["faboam-packets-dropped"] = value
                    elif key == "VCCP_packets_dropped":
                        entry["vccp-packets-dropped"] = value
                    elif key == "Input_drops_due_to_bogus_protocol":
                        entry["input-drops-due-to-bogus-protocol"] = value
                    elif key == "input_drops_due_to_no_mbufs_available":
                        entry["input-drops-due-to-no-mbufs-available"] = value
                    elif key == "input_drops_due_to_no_space_in_socket":
                        entry["input-drops-due-to-no-space-in-socket"] = value
                    elif key == "input_drops_due_to_no_socket":
                        entry["input-drops-due-to-no-socket"] = value

                    continue

            if self.state == "arp":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("arp", {})

                    if key == "datagrams_received":
                        entry["datagrams-received"] = value
                    elif key == "ARP_requests_received":
                        entry["arp-requests-received"] = value
                    elif key == "ARP_replies_received":
                        entry["arp-replies-received"] = value
                    elif key == "resolution_request_received":
                        entry["resolution-request-received"] = value
                    elif key == "resolution_request_dropped":
                        entry["resolution-request-dropped"] = value
                    elif key == "unrestricted_proxy_requests":
                        entry["unrestricted-proxy-requests"] = value
                    elif key == "restricted_proxy_requests":
                        entry["restricted-proxy-requests"] = value
                    elif key == "received_proxy_requests":
                        entry["received-proxy-requests"] = value
                    elif key == "unrestricted_proxy_requests_not_proxied":
                        entry["proxy-requests-not-proxied"] = value
                    elif key == "restricted_proxy_requests_not_proxied":
                        entry["restricted-proxy-requests-not-proxied"] = value
                    elif key == "datagrams_with_bogus_interface":
                        entry["datagrams-with-bogus-interface"] = value
                    elif key == "datagrams_with_incorrect_length":
                        entry["datagrams-with-incorrect-length"] = value
                    elif key == "datagrams_for_non-IP_protocol":
                        entry["datagrams-for-non-ip-protocol"] = value
                    elif key == "datagrams_with_unsupported_op_code":
                        entry["datagrams-with-unsupported-opcode"] = value
                    elif key == "datagrams_with_bad_protocol_address_length":
                        entry[
                            "datagrams-with-bad-protocol-address-length"] = value
                    elif key == "datagrams_with_bad_hardware_address_length":
                        entry[
                            "datagrams-with-bad-hardware-address-length"] = value
                    elif key == "datagrams_with_multicast_source_address":
                        entry[
                            "datagrams-with-multicast-source-address"] = value
                    elif key == "datagrams_with_multicast_target_address":
                        entry[
                            "datagrams-with-multicast-target-address"] = value
                    elif key == "datagrams_with_my_own_hardware_address":
                        entry["datagrams-with-my-own-hardware-address"] = value
                    elif key == "datagrams_for_an_address_not_on_the_interface":
                        entry[
                            "datagrams-for-an-address-not-on-the-interface"] = value
                    elif key == "datagrams_with_a_broadcast_source_address":
                        entry[
                            "datagrams-with-a-broadcast-source-address"] = value
                    elif key == "datagrams_with_source_address_duplicate_to_mine":
                        entry[
                            "datagrams-with-source-address-duplicate-to-mine"] = value
                    elif key == "datagrams_which_were_not_for_me":
                        entry["datagrams-which-were-not-for-me"] = value
                    elif key == "packets_discarded_waiting_for_resolution":
                        entry[
                            "packets-discarded-waiting-for-resolution"] = value
                    elif key == "packets_sent_after_waiting_for_resolution":
                        entry[
                            "packets-sent-after-waiting-for-resolution"] = value
                    elif key == "ARP_requests_sent":
                        entry["arp-requests-sent"] = value
                    elif key == "ARP_replies_sent":
                        entry["arp-replies-sent"] = value
                    elif key == "requests_for_memory_denied":
                        entry["requests-for-memory-denied"] = value
                    elif key == "requests_dropped_on_entry":
                        entry["requests-dropped-on-entry"] = value
                    elif key == "requests_dropped_during_retry":
                        entry["requests-dropped-during-retry"] = value
                    elif key == "requests_dropped_due_to_interface_deletion":
                        entry[
                            "requests-dropped-due-to-interface-deletion"] = value
                    elif key == "requests_on_unnumbered_interfaces":
                        entry["requests-on-unnumbered-interfaces"] = value
                    elif key == "new_requests_on_unnumbered_interfaces":
                        entry["new-requests-on-unnumbered-interfaces"] = value
                    elif key == "replies_for_from_unnumbered_interfaces":
                        entry["replies-from-unnumbered-interfaces"] = value
                    elif (key ==
                          "requests_on_unnumbered_interface_with_non-subnetted_donor"
                          ):
                        entry[
                            "requests-on-unnumbered-interface-with-non-subnetted-donor"] = value
                    elif (key ==
                          "replies_from_unnumbered_interface_with_non-subnetted_donor"
                          ):
                        entry[
                            "replies-from-unnumbered-interface-with-non-subnetted-donor"] = value
                    elif (key ==
                          "arp_packets_rejected_as_family_is_configured_with_deny_arp"
                          ):
                        entry[
                            "arp-packets-rejected-as-family-is-configured-with-deny-arp"] = value
                    elif (key ==
                          "arp_response_packets_are_rejected_on_mace_icl_interface"
                          ):
                        entry[
                            "arp-response-packets-are-rejected-on-mace-icl-interface"] = value
                    elif (key ==
                          "arp_replies_are_rejected_as_source_and_destination_is_same"
                          ):
                        entry[
                            "arp-replies-are-rejected-as-source-and-destination-is-same"] = value
                    elif (key ==
                          "arp_probe_for_proxy_address_reachable_from_the_incoming_interface"
                          ):
                        entry[
                            "arp-probe-for-proxy-address-reachable-from-the-incoming-interface"] = value
                    elif key == "arp_request_discarded_for_vrrp_source_address":
                        entry[
                            "arp-request-discarded-for-vrrp-source-address"] = value
                    elif key == "self_arp_request_packet_received_on_irb_interface":
                        entry[
                            "self-arp-request-packet-received-on-irb-interface"] = value
                    elif (key ==
                          "proxy_arp_request_discarded_as_source_ip_is_a_proxy_target"
                          ):
                        entry[
                            "proxy-arp-request-discarded-as-source-ip-is-a-proxy-target"] = value
                    elif key == "arp_packets_are_dropped_as_nexthop_allocation_failed":
                        entry[
                            "arp-packets-are-dropped-as-nexthop-allocation-failed"] = value
                    elif (key ==
                          "arp_packets_received_from_peer_vrrp_rotuer_and_discarded"
                          ):
                        entry[
                            "arp-packets-received-from-peer-vrrp-router-and-discarded"] = value
                    elif (key ==
                          "arp_packets_are_rejected_as_target_ip_arp_resolve_is_in_progress"
                          ):
                        entry[
                            "arp-packets-are-rejected-as-target-ip-arp-resolve-is-in-progress"] = value
                    elif (key ==
                          "grat_arp_packets_are_ignored_as_mac_address_is_not_changed"
                          ):
                        entry[
                            "grat-arp-packets-are-ignored-as-mac-address-is-not-changed"] = value
                    elif key == "arp_packets_are_dropped_from_peer_vrrp":
                        entry["arp-packets-are-dropped-from-peer-vrrp"] = value
                    elif key == "arp_packets_are_dropped_as_driver_call_failed":
                        entry[
                            "arp-packets-are-dropped-as-driver-call-failed"] = value
                    elif key == "arp_packets_are_dropped_as_source_is_not_validated":
                        entry[
                            "arp-packets-are-dropped-as-source-is-not-validated"] = value
                    elif key == "Max_System_ARP_nh_cache_limit":
                        entry["arp-system-max"] = value
                    elif key == "Max_Public_ARP_nh_cache_limit":
                        entry["arp-public-max"] = value
                    elif key == "Max_IRI_ARP_nh_cache_limit":
                        entry["arp-iri-max"] = value
                    elif key == "Max_Management_intf_ARP_nh_cache_limit":
                        entry["arp-mgt-max"] = value
                    elif key == "Current_Public_ARP_nexthops_present":
                        entry["arp-public-cnt"] = value
                    elif key == "Current_IRI_ARP_nexthops_present":
                        entry["arp-iri-cnt"] = value
                    elif key == "Current_Management_ARP_nexthops_present":
                        entry["arp-mgt-cnt"] = value
                    elif key == "Total_ARP_nexthops_creation_failed_as_limit_reached":
                        entry["arp-system-drop"] = value
                    elif (key ==
                          "Public_ARP_nexthops_creation_failed_as_public_limit_reached"
                          ):
                        entry["arp-public-drop"] = value
                    elif key == "IRI_ARP_nexthops_creation_failed_as_iri_limit_reached":
                        entry["arp-iri-drop"] = value
                    elif (key ==
                          "Management_ARP_nexthops_creation_failed_as_mgt_limit_reached"
                          ):
                        entry["arp-mgt-drop"] = value

                    continue

            if self.state == "ip6":

                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    header_type_list = (ret_dict["statistics"][0].setdefault(
                        "ip6", {}).setdefault("header-type", []))
                    entry = {
                        "header-for-source-address-selection":
                        group["header_for_source_address_selection"]
                    }
                    header_type_list.append(entry)
                    continue

                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict["statistics"][0]["ip6"]["histogram"] = line
                    continue

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("ip6", {})

                    if key == "total_packets_received":
                        entry["total-packets-received"] = value
                    elif key == "packets_with_size_smaller_than_minimum":
                        entry[
                            "ip6-packets-with-size-smaller-than-minimum"] = value
                    elif key == "packets_with_data_size_<_data_length":
                        entry[
                            "packets-with-datasize-less-than-data-length"] = value
                    elif key == "packets_with_bad_options":
                        entry["ip6-packets-with-bad-options"] = value
                    elif key == "packets_with_incorrect_version_number":
                        entry[
                            "ip6-packets-with-incorrect-version-number"] = value
                    elif key == "fragments_received":
                        entry["ip6-fragments-received"] = value
                    elif key == "fragments_dropped_(dup_or_out_of_space)":
                        entry[
                            "duplicate-or-out-of-space-fragments-dropped"] = value
                    elif key == "fragments_dropped_after_timeout":
                        entry["ip6-fragments-dropped-after-timeout"] = value
                    elif key == "fragment_sessions_dropped_(queue_overflow)":
                        entry["fragments-that-exceeded-limit"] = value
                    elif key == "packets_reassembled_ok":
                        entry["ip6-packets-reassembled-ok"] = value
                    elif key == "packets_for_this_host":
                        entry["ip6-packets-for-this-host"] = value
                    elif key == "packets_forwarded":
                        entry["ip6-packets-forwarded"] = value
                    elif key == "packets_not_forwardable":
                        entry["ip6-packets-not-forwardable"] = value
                    elif key == "redirects_sent":
                        entry["ip6-redirects-sent"] = value
                    elif key == "packets_sent_from_this_host":
                        entry["ip6-packets-sent-from-this-host"] = value
                    elif key == "packets_sent_with_fabricated_ip_header":
                        entry[
                            "ip6-packets-sent-with-fabricated-ip-header"] = value
                    elif key == "output_packets_dropped_due_to_no_bufs,_etc.":
                        entry[
                            "ip6-output-packets-dropped-due-to-no-bufs"] = value
                    elif key == "output_packets_discarded_due_to_no_route":
                        entry[
                            "ip6-output-packets-discarded-due-to-no-route"] = value
                    elif key == "output_datagrams_fragmented":
                        entry["ip6-output-datagrams-fragmented"] = value
                    elif key == "fragments_created":
                        entry["ip6-fragments-created"] = value
                    elif key == "datagrams_that_can't_be_fragmented":
                        entry[
                            "ip6-datagrams-that-can-not-be-fragmented"] = value
                    elif key == "packets_that_violated_scope_rules":
                        entry["packets-that-violated-scope-rules"] = value
                    elif key == "multicast_packets_which_we_don't_join":
                        entry["multicast-packets-which-we-do-not-join"] = value
                    elif key == "TCP":
                        entry["ip6nh-tcp"] = value
                    elif key == "UDP":
                        entry["ip6nh-udp"] = value
                    elif key == "ICMP6":
                        entry["ip6nh-icmp6"] = value
                    elif key == "OSPF":
                        entry["ip6nh-ospf"] = value
                    elif key == "packets_whose_headers_are_not_continuous":
                        entry[
                            "packets-whose-headers-are-not-continuous"] = value
                    elif key == "tunneling_packets_that_can't_find_gif":
                        entry[
                            "tunneling-packets-that-can-not-find-gif"] = value
                    elif key == "packets_discarded_due_to_too_may_headers":
                        entry[
                            "packets-discarded-due-to-too-may-headers"] = value
                    elif key == "failures_of_source_address_selection":
                        entry["failures-of-source-address-selection"] = value
                    elif key == "link-locals":
                        entry["header-type"][-1]["link-locals"] = value
                    elif key == "globals":
                        entry["header-type"][-1]["globals"] = value
                    elif key == "forward_cache_hit":
                        entry["forward-cache-hit"] = value
                    elif key == "forward_cache_miss":
                        entry["forward-cache-miss"] = value
                    elif key == "Packets_destined_to_dead_next_hop":
                        entry["ip6-packets-destined-to-dead-next-hop"] = value
                    elif key == "option_packets_dropped_due_to_rate_limit":
                        entry[
                            "ip6-option-packets-dropped-due-to-rate-limit"] = value
                    elif key == "Packets_dropped_(src_and_int_don't_match)":
                        entry["ip6-packets-dropped"] = value
                    elif key == "packets_dropped_due_to_bad_protocol":
                        entry["packets-dropped-due-to-bad-protocol"] = value
                    elif key == "transit_re_packet(null)_dropped_on_mgmt_i/f":
                        entry[
                            "transit-re-packet-dropped-on-mgmt-interface"] = value

                    continue

            if self.state == "icmp6":

                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    self.icmp6_histogram = group["histogram_type"].lower()
                    entry = ret_dict["statistics"][0].setdefault("icmp6", {})
                    histo = entry.setdefault(
                        self.icmp6_histogram + "-histogram", {})
                    histo["histogram-type"] = line
                    continue

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("icmp6", {})
                    entry["protocol-name"] = "icmp6:"
                    entry[
                        "histogram-of-error-messages-to-be-generated"] = "Histogram of error messages to be generated:"

                    if key == "Calls_to_icmp_error":
                        entry["calls-to-icmp6-error"] = value
                    elif (key ==
                          "Errors_not_generated_because_old_message_was_icmp_error"
                          ):
                        entry[
                            "errors-not-generated-because-old-message-was-icmp-error"] = value
                    elif key == "Errors_not_generated_because_rate_limitation":
                        entry[
                            "errors-not-generated-because-rate-limitation"] = value
                    elif key == "unreach":
                        if self.icmp6_histogram == "output":
                            entry["output-histogram"][
                                "unreachable-icmp6-packets"] = value
                        elif self.icmp6_histogram == "input":
                            entry["input-histogram"][
                                "unreachable-icmp6-packets"] = value
                    elif key == "neighbor_solicitation":
                        if self.icmp6_histogram == "output":
                            entry["output-histogram"][
                                "neighbor-solicitation"] = value
                        elif self.icmp6_histogram == "input":
                            entry["input-histogram"][
                                "neighbor-solicitation"] = value
                    elif key == "neighbor_advertisement":
                        if self.icmp6_histogram == "output":
                            entry["output-histogram"][
                                "neighbor-advertisement"] = value
                        elif self.icmp6_histogram == "input":
                            entry["input-histogram"][
                                "neighbor-advertisement"] = value
                    elif key == "Messages_with_bad_code_fields":
                        entry["icmp6-messages-with-bad-code-fields"] = value
                    elif key == "Messages_<_minimum_length":
                        entry["messages-less-than-minimum-length"] = value
                    elif key == "Bad_checksums":
                        entry["bad-checksums"] = value
                    elif key == "Messages_with_bad_length":
                        entry["icmp6-messages-with-bad-length"] = value
                    elif key == "time_exceeded":
                        if self.icmp6_histogram == "output":
                            entry["output-histogram"][
                                "time-exceeded-icmp6-packets"] = value
                        elif self.icmp6_histogram == "input":
                            entry["input-histogram"][
                                "time-exceeded-icmp6-packets"] = value
                    elif key == "router_solicitation":
                        if self.icmp6_histogram == "output":
                            entry["output-histogram"][
                                "router-solicitation-icmp6-packets"] = value
                        elif self.icmp6_histogram == "input":
                            entry["input-histogram"][
                                "router-solicitation-icmp6-packets"] = value
                    elif key == "router_advertisment":
                        if self.icmp6_histogram == "output":
                            entry["output-histogram"][
                                "router-advertisement-icmp6-packets"] = value
                        elif self.icmp6_histogram == "input":
                            entry["input-histogram"][
                                "router-advertisement-icmp6-packets"] = value
                    elif key == "neighbor_advertisement":
                        if self.icmp6_histogram == "output":
                            entry["output-histogram"][
                                "neighbor-advertisement"] = value
                        elif self.icmp6_histogram == "input":
                            entry["input-histogram"][
                                "neighbor-advertisement"] = value
                    elif key == "No_route":
                        entry["no-route"] = value
                    elif key == "Administratively_prohibited":
                        entry["administratively-prohibited"] = value
                    elif key == "Beyond_scope":
                        entry["beyond-scope"] = value
                    elif key == "Address_unreachable":
                        entry["address-unreachable"] = value
                    elif key == "Port_unreachable":
                        entry["port-unreachable"] = value
                    elif key == "Time_exceed_transit":
                        entry["time-exceed-transit"] = value
                    elif key == "Time_exceed_reassembly":
                        entry["time-exceed-reassembly"] = value
                    elif key == "Erroneous_header_field":
                        entry["erroneous-header-field"] = value
                    elif key == "Unrecognized_next_header":
                        entry["unrecognized-next-header"] = value
                    elif key == "Unrecognized_option":
                        entry["unrecognized-option"] = value
                    elif key == "Unknown":
                        entry["unknown"] = value
                    elif key == "Message_responses_generated":
                        entry["icmp6-message-responses-generated"] = value
                    elif key == "Messages_with_too_many_ND_options":
                        entry["messages-with-too-many-nd-options"] = value
                    elif key == "Max_System_ND_nh_cache_limit":
                        entry["nd-system-max"] = value
                    elif key == "Max_Public_ND_nh_cache_limit":
                        entry["nd-public-max"] = value
                    elif key == "Max_IRI_ND_nh_cache_limit":
                        entry["nd-iri-max"] = value
                    elif key == "Max_Management_intf_ND_nh_cache_limit":
                        entry["nd-mgt-max"] = value
                    elif key == "Current_Public_ND_nexthops_present":
                        entry["nd-public-cnt"] = value
                    elif key == "Current_IRI_ND_nexthops_present":
                        entry["nd-iri-cnt"] = value
                    elif key == "Current_Management_ND_nexthops_present":
                        entry["nd-mgt-cnt"] = value
                    elif key == "Total_ND_nexthops_creation_failed_as_limit_reached":
                        entry["nd-system-drop"] = value
                    elif (key ==
                          "Public_ND_nexthops_creation_failed_as_public_limit_reached"
                          ):
                        entry["nd-public-drop"] = value
                    elif key == "IRI_ND_nexthops_creation_failed_as_iri_limit_reached":
                        entry["nd-iri-drop"] = value
                    elif (key ==
                          "Management_ND_nexthops_creation_failed_as_mgt_limit_reached"
                          ):
                        entry["nd-mgt-drop"] = value
                    elif key == "interface-restricted_ndp_proxy_requests":
                        entry["nd6-ndp-proxy-requests"] = value
                    elif key == "interface-restricted_dad_proxy_requests":
                        entry["nd6-dad-proxy-requests"] = value
                    elif key == "interface-restricted_ndp_proxy_responses":
                        entry["nd6-ndp-proxy-responses"] = value
                    elif key == "interface-restricted_dad_proxy_conflicts":
                        entry["nd6-dad-proxy-conflicts"] = value
                    elif key == "interface-restricted_dad_proxy_duplicates":
                        entry["nd6-dup-proxy-responses"] = value
                    elif key == "interface-restricted_ndp_proxy_resolve_requests":
                        entry["nd6-ndp-proxy-resolve-cnt"] = value
                    elif key == "interface-restricted_dad_proxy_resolve_requests":
                        entry["nd6-dad-proxy-resolve-cnt"] = value
                    elif (key ==
                          "interface-restricted_dad_packets_from_same_node_dropped"
                          ):
                        entry["nd6-dad-proxy-eqmac-drop"] = value
                    elif key == "interface-restricted_proxy_packets_dropped_with_nomac":
                        entry["nd6-dad-proxy-nomac-drop"] = value
                    elif key == "ND_hold_nexthops_dropped_on_entry_by_RED_mark":
                        entry["nd6-requests-dropped-on-entry"] = value
                    elif key == "ND_hold_nexthops_dropped_on_timer_expire_by_RED_mark":
                        entry["nd6-requests-dropped-during-retry"] = value

                    continue

            if self.state == "ipsec6":

                m = p2.match(line)

                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("ipsec6", {})

                    if key == "Inbound_packets_violated_process_security_policy":
                        entry[
                            "inbound-packets-violated-process-security-policy"] = value
                    elif key == "Outbound_packets_violated_process_security_policy":
                        entry[
                            "outbound-packets-violated-process-security-policy"] = value
                    elif key == "Outbound_packets_with_no_SA_available":
                        entry["outbound-packets-with-no-sa-available"] = value
                    elif key == "Outbound_packets_failed_due_to_insufficient_memory":
                        entry[
                            "outbound-packets-failed-due-to-insufficient-memory"] = value
                    elif key == "Outbound_packets_with_no_route":
                        entry["outbound-packets-with-no-route"] = value
                    elif key == "Invalid_outbound_packets":
                        entry["invalid-outbound-packets"] = value
                    elif key == "Outbound_packets_with_bundles_SAs":
                        entry["outbound-packets-with-bundled-sa"] = value
                    elif key == "mbuf_coleasced_during_clone":
                        entry["mbuf-coalesced-during-clone"] = value
                    elif key == "Cluster_coalesced_during_clone":
                        entry["cluster-coalesced-during-clone"] = value
                    elif key == "Cluster_copied_during_clone":
                        entry["cluster-copied-during-clone"] = value
                    elif key == "mbuf_inserted_during_makespace":
                        entry["mbuf-inserted-during-makespace"] = value

                    continue

            if self.state == "pfkey":

                m = p7.match(line)
                if m:
                    entry = ret_dict["statistics"][0].setdefault("pfkey", {})
                    if self.pfkey_state == None:
                        self.pfkey_state = False
                        entry.setdefault("output-histogram",
                                         {})["histogram"] = line
                    else:
                        self.pfkey_state = True
                        entry.setdefault("input-histogram",
                                         {})["histogram"] = line

                    continue

                m = p2.match(line)
                if m:

                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("pfkey", {})

                    if key == "Requests_sent_from_userland":
                        entry["requests-sent-from-userland"] = value
                    elif key == "Bytes_sent_from_userland":
                        entry["bytes-sent-from-userland"] = value
                    elif key == "reserved":
                        if self.pfkey_state:
                            entry["input-histogram"]["reserved"] = value
                        else:
                            entry["output-histogram"]["reserved"] = value
                    elif key == "add":
                        if self.pfkey_state:
                            entry["input-histogram"]["add"] = value
                        else:
                            entry["output-histogram"]["add"] = value
                    elif key == "dump":
                        if self.pfkey_state:
                            entry["input-histogram"]["dump"] = value
                        else:
                            entry["output-histogram"]["dump"] = value
                    elif key == "Messages_with_invalid_length_field":
                        entry["messages-with-invalid-length-field"] = value
                    elif key == "Messages_with_invalid_version_field":
                        entry["messages-with-invalid-version-field"] = value
                    elif key == "Messages_with_invalid_message_type_field":
                        entry[
                            "messages-with-invalid-message-type-field"] = value
                    elif key == "Messages_too_short":
                        entry["messages-too-short"] = value
                    elif key == "Messages_with_memory_allocation_failure":
                        if (not "outgoing-messages-with-memory-allocation-failure"
                                in entry):
                            entry[
                                "outgoing-messages-with-memory-allocation-failure"] = value
                        else:
                            entry[
                                "incoming-messages-with-memory-allocation-failure"] = value
                    elif key == "Messages_with_duplicate_extension":
                        entry["messages-with-duplicate-extension"] = value
                    elif key == "Messages_with_invalid_extension_type":
                        entry["messages-with-invalid-extension-type"] = value
                    elif key == "Messages_with_invalid_sa_type":
                        entry["messages-with-invalid-sa-type"] = value
                    elif key == "Messages_with_invalid_address_extension":
                        entry[
                            "messages-with-invalid-address-extension"] = value
                    elif key == "Requests_sent_to_userland":
                        entry["requests-sent-to-userland"] = value
                    elif key == "Bytes_sent_to_userland":
                        entry["bytes-sent-to-userland"] = value
                    elif key == "Messages_toward_single_socket":
                        entry["messages-toward-single-socket"] = value
                    elif key == "Messages_toward_all_sockets":
                        entry["messages-toward-all-sockets"] = value
                    elif key == "Messages_toward_registered_sockets":
                        entry["messages-toward-registered-sockets"] = value

                    continue

            if self.state == "clnl":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("clnl", {})

                    if key == "Total_packets_received":
                        entry["total-clnl-packets-received"] = value
                    elif key == "Packets_delivered":
                        entry["packets-delivered"] = value
                    elif key == "Too_small_packets":
                        entry["too-small-packets"] = value
                    elif key == "Packets_with_bad_header_length":
                        entry["packets-with-bad-header-length"] = value
                    elif key == "Packets_with_bad_checksum":
                        entry["packets-with-bad-checksum"] = value
                    elif key == "Bad_version_packets":
                        entry["bad-version-packets"] = value
                    elif key == "Unknown_or_unsupported_protocol_packets":
                        entry[
                            "unknown-or-unsupported-protocol-packets"] = value
                    elif key == "Packets_with_bogus_sdl_size":
                        entry["packets-with-bogus-sdl-size"] = value
                    elif key == "No_free_memory_in_socket_buffer":
                        entry["no-free-memory-in-socket-buffer"] = value
                    elif key == "Send_packets_discarded":
                        entry["send-packets-discarded"] = value
                    elif key == "Sbappend_failure":
                        entry["sbappend-failure"] = value
                    elif key == "Mcopy_failure":
                        entry["mcopy-failure"] = value
                    elif key == "Address_fields_were_not_reasonable":
                        entry["address-fields-were-not-reasonable"] = value
                    elif key == "Segment_information_forgotten":
                        entry["segment-information-forgotten"] = value
                    elif key == "Forwarded_packets":
                        entry["forwarded-packets"] = value
                    elif key == "Total_packets_sent":
                        entry["total-packets-sent"] = value
                    elif key == "Output_packets_discarded":
                        entry["output-packets-discarded"] = value
                    elif key == "Non-forwarded_packets":
                        entry["non-forwarded-packets"] = value
                    elif key == "Packets_fragmented":
                        entry["packets-fragmented"] = value
                    elif key == "Fragments_sent":
                        entry["fragments-sent"] = value
                    elif key == "Fragments_discarded":
                        entry["fragments-discarded"] = value
                    elif key == "Fragments_timed_out":
                        entry["fragments-timed-out"] = value
                    elif key == "Fragmentation_prohibited":
                        entry["fragmentation-prohibited"] = value
                    elif key == "Packets_reconstructed":
                        entry["packets-reconstructed"] = value
                    elif key == "Packets_destined_to_dead_nexthop":
                        entry["packets-destined-to-dead-nexthop"] = value
                    elif key == "Packets_discarded_due_to_no_route":
                        entry["packets-discarded-due-to-no-route"] = value
                    elif key == "Error_pdu_rate_drops":
                        entry["error-pdu-rate-drops"] = value
                    elif key == "ER_pdu_generation_failure":
                        entry["er-pdu-generation-failure"] = value

                    continue

            if self.state == "esis":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("esis", {})

                    if key == "Total_pkts_received":
                        entry["total-esis-packets-received"] = value
                    elif key == "Total_packets_consumed_by_protocol":
                        entry["total-packets-consumed-by-protocol"] = value
                    elif key == "Pdus_received_with_bad_checksum":
                        entry["pdus-received-with-bad-checksum"] = value
                    elif key == "Pdus_received_with_bad_version_number":
                        entry["pdus-received-with-bad-version-number"] = value
                    elif key == "Pdus_received_with_bad_type_field":
                        entry["pdus-received-with-bad-type-field"] = value
                    elif key == "Short_pdus_received":
                        entry["short-pdus-received"] = value
                    elif key == "Pdus_withbogus_sdl_size":
                        entry["pdus-with-bogus-sdl-size"] = value
                    elif key == "Pdus_with_bad_header_length":
                        entry["pdus-with-bad-header-length"] = value
                    elif key == "Pdus_with_unknown_or_unsupport_protocol":
                        entry[
                            "pdus-with-unknown-or-unsupport-protocol"] = value
                    elif key == "No_free_memory_in_socket_buffer":
                        entry["no-free-memory-in-socket-buffer"] = value
                    elif key == "Send_packets_discarded":
                        entry["send-packets-discarded"] = value
                    elif key == "Sbappend_failure":
                        entry["sbappend-failure"] = value
                    elif key == "Mcopy_failure":
                        entry["mcopy-failure"] = value
                    elif key == "ISO_family_not_configured":
                        entry["iso-family-not-configured"] = value

                    continue

            if self.state == "tnp":

                m = p2.match(line)
                if m:

                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("tnp", {})

                    if key == "Unicast_packets_received":
                        entry["unicast-packets-received"] = value
                    elif key == "Broadcast_packets_received":
                        entry["broadcast-packets-received"] = value
                    elif key == "Fragmented_packets_received":
                        entry["fragmented-packets-received"] = value
                    elif key == "Hello_packets_dropped":
                        if not "received-hello-packets-dropped" in entry:
                            entry["received-hello-packets-dropped"] = value
                        else:
                            entry["sent-hello-packets-dropped"] = value
                    elif key == "Fragments_dropped":
                        if not "received-fragments-dropped" in entry:
                            entry["received-fragments-dropped"] = value
                        else:
                            entry["sent-fragments-dropped"] = value
                    elif key == "Fragment_reassembly_queue_flushes":
                        entry["fragment-reassembly-queue-flushes"] = value
                    elif key == "Packets_with_tnp_src_address_collision_received":
                        entry[
                            "packets-with-tnp-src-address-collision-received"] = value
                    elif key == "Hello_packets_received":
                        entry["hello-packets-received"] = value
                    elif key == "Control_packets_received":
                        entry["control-packets-received"] = value
                    elif key == "Rdp_packets_received":
                        entry["rdp-packets-received"] = value
                    elif key == "Udp_packets_received":
                        entry["udp-packets-received"] = value
                    elif key == "Tunnel_packets_received":
                        entry["tunnel-packets-received"] = value
                    elif key == "Input_packets_discarded_with_no_protocol":
                        entry[
                            "input-packets-discarded-with-no-protocol"] = value
                    elif key == "Packets_of_version_unspecified_received":
                        entry[
                            "packets-of-version-unspecified-received"] = value
                    elif key == "Packets_of_version_1_received":
                        entry["packets-of-version1-received"] = value
                    elif key == "Packets_of_version_2_received":
                        entry["packets-of-version2-received"] = value
                    elif key == "Packets_of_version_3_received":
                        entry["packets-of-version3-received"] = value
                    elif key == "Unicast_packets_sent":
                        entry["unicast-packets-sent"] = value
                    elif key == "Broadcast_packets_sent":
                        entry["broadcast-packets-sent"] = value
                    elif key == "Fragmented_packets_sent":
                        entry["fragmented-packets-sent"] = value
                    elif key == "Hello_packets_sent":
                        entry["hello-packets-sent"] = value
                    elif key == "Control_packets_sent":
                        entry["control-packets-sent"] = value
                    elif key == "Rdp_packets_sent":
                        entry["rdp-packets-sent"] = value
                    elif key == "Udp_packets_sent":
                        entry["udp-packets-sent"] = value
                    elif key == "Tunnel_packets_sent":
                        entry["tunnel-packets-sent"] = value
                    elif key == "Packets_sent_with_unknown_protocol":
                        entry["packets-sent-with-unknown-protocol"] = value
                    elif key == "Packets_of_version_unspecified_sent":
                        entry["packets-of-version-unspecified-sent"] = value
                    elif key == "Packets_of_version_1_sent":
                        entry["packets-of-version1-sent"] = value
                    elif key == "Packets_of_version_2_sent":
                        entry["packets-of-version2-sent"] = value
                    elif key == "Packets_of_version_3_sent":
                        entry["packets-of-version3-sent"] = value

                    continue

            if self.state == "rdp":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("rdp", {})
                    entry["packets-dropped-full-repl-sock-buf"] = "0"

                    if key == "Input_packets":
                        entry["input-packets"] = value
                    elif key == "Packets_discarded_for_bad_checksum":
                        entry["packets-discarded-for-bad-checksum"] = value
                    elif key == "Packets_discarded_due_to_bad_sequence_number":
                        entry[
                            "packets-discarded-due-to-bad-sequence-number"] = value
                    elif key == "Refused_connections":
                        entry["refused-connections"] = value
                    elif key == "Acks_received":
                        entry["acks-received"] = value
                    elif key == "Packets_dropped_due_to_full_socket_buffers":
                        entry[
                            "packets-dropped-due-to-full-socket-buffers"] = value
                    elif key == "Retransmits":
                        entry["retransmits"] = value
                    elif key == "Output_packets":
                        entry["output-packets"] = value
                    elif key == "Acks_sent":
                        entry["acks-sent"] = value
                    elif key == "Connects":
                        entry["connects"] = value
                    elif key == "Closes":
                        entry["closes"] = value
                    elif key == "Keepalives_received":
                        entry["keepalives-received"] = value
                    elif key == "Keepalives_sent":
                        entry["keepalives-sent"] = value

                    continue

            if self.state == "tudp":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("tudp", {})

                    if key == "Datagrams_received":
                        entry["datagrams-received"] = value
                    elif key == "Datagrams_with_incomplete_header":
                        entry["datagrams-with-incomplete-header"] = value
                    elif key == "Datagrams_with_bad_data_length_field":
                        entry["datagrams-with-bad-data-length-field"] = value
                    elif key == "Datagrams_with_bad_checksum":
                        entry["datagrams-with-bad-checksum"] = value
                    elif key == "Datagrams_dropped_due_to_no_socket":
                        entry["datagrams-dropped-due-to-no-socket"] = value
                    elif (key ==
                          "Broadcast/multicast_datagrams_dropped_due_to_no_socket"
                          ):
                        entry[
                            "broadcast-or-multicast-datagrams-dropped-due-to-no-socket"] = value
                    elif key == "Datagrams_dropped_due_to_full_socket_buffers":
                        entry[
                            "datagrams-dropped-due-to-full-socket-buffers"] = value
                    elif key == "Delivered":
                        entry["delivered"] = value
                    elif key == "Datagrams_output":
                        entry["datagrams-output"] = value

                    continue

            if self.state == "ttp":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("ttp", {})

                    if key == "Packets_sent":
                        entry["ttp-packets-sent"] = value
                    elif key == "Packets_sent_while_unconnected":
                        entry["packets-sent-while-unconnected"] = value
                    elif key == "Packets_sent_while_interface_down":
                        entry["packets-sent-while-interface-down"] = value
                    elif key == "Packets_sent_couldn't_get_buffer":
                        entry["packets-sent-could-not-get-buffer"] = value
                    elif key == "Packets_sent_couldn't_find_neighbor":
                        entry["packets-sent-could-not-find-neighbor"] = value
                    elif key == "Packets_sent_when_transmit_is_disable":
                        entry["packets-sent-when-transmit-disabled"] = value
                    elif key == "Packets_sent_when_host_unreachable":
                        entry["packets-sent-when-host_unreachable"] = value
                    elif key == "L3_Packets_sent_could_not_get_buffer":
                        entry["l3-packets-sent-could-not-get-buffer"] = value
                    elif key == "L3_Packets_dropped":
                        entry["l3-packets-dropped"] = value
                    elif key == "Packets_sent_with_bad_logical_interface":
                        entry["packets-sent-with-bad-ifl"] = value
                    elif key == "Packets_sent_with_bad_address_family":
                        entry["packets-sent-with-bad-af"] = value
                    elif key == "L2_packets_received":
                        entry["l2-packets-received"] = value
                    elif key == "Unknown_L3_packets_received":
                        entry["unknown-l3-packets-received"] = value
                    elif key == "IPv4_L3_packets_received":
                        entry["ipv4-l3-packets-received"] = value
                    elif key == "MPLS_L3_packets_received":
                        entry["mpls-l3-packets-received"] = value
                    elif key == "MPLS->IPV4_L3_packets_received":
                        entry["mpls-to-ipv4-l3-packets-received"] = value
                    elif key == "IPv4->MPLS_L3_packets_received":
                        entry["ipv4-to-mpls-l3-packets-received"] = value
                    elif key == "VPLS_L3_packets_received":
                        entry["vpls-l3-packets-received"] = value
                    elif key == "IPv6_L3_packets_received":
                        entry["ipv6-l3-packets-received"] = value
                    elif key == "ARP_L3_packets_received":
                        entry["arp-l3-packets-received"] = value
                    elif key == "CLNP_L3_packets_received":
                        entry["clnp-l3-packets-received"] = value
                    elif key == "TNP_L3_packets_received":
                        entry["tnp-l3-packets-received"] = value
                    elif key == "NULL_L3_packets_received":
                        entry["null-l3-packets-received"] = value
                    elif key == "Cyclotron_cycle_L3_packets_received":
                        entry["cyclotron-cycle-l3-packets-received"] = value
                    elif key == "Cyclotron_send_L3_packets_received":
                        entry["cyclotron-send-l3-packets-received"] = value
                    elif key == "Openflow_packets_received":
                        entry["openflow-packets-received"] = value
                    elif key == "Packets_received_while_unconnected":
                        entry["packets-received-while-unconnected"] = value
                    elif key == "Packets_received_from_unknown_ifl":
                        entry["packets-received-from-unknown-ifl"] = value
                    elif key == "Input_packets_couldn't_get_buffer":
                        entry["input-packets-could-not-get-buffer"] = value
                    elif key == "Input_packets_with_bad_type":
                        entry["input-packets-with-bad-type"] = value
                    elif key == "Input_packets_with_discard_type":
                        entry["input-packets-with-discard-type"] = value
                    elif key == "Input_packets_with_too_many_tlvs":
                        entry["input-packets-with-too-many-tlvs"] = value
                    elif key == "Input_packets_with_bad_tlv_header":
                        entry["input-packets-with-bad-tlv-header"] = value
                    elif key == "Input_packets_with_bad_tlv_type":
                        entry["input-packets-with-bad-tlv-type"] = value
                    elif key == "Input_packets_dropped_based_on_tlv_result":
                        entry["input-packets-tlv-dropped"] = value
                    elif key == "Input_packets_with_bad_address_family":
                        entry["input-packets-with-bad-af"] = value
                    elif key == "Input_packets_for_which_rt_lookup_is_bypassed":
                        entry[
                            "input-packets-for-which-route-lookup-is-bypassed"] = value
                    elif (key ==
                          "Input_packets_with_ttp_tlv_of_type_TTP_TLV_P2MP_NBR_NHID"
                          ):
                        entry[
                            "input-packets-with-ttp-tlv-p2mp-nbr-nhid-type"] = value
                    elif key == "Input_packets_with_unknown_p2mp_nbr_nhid_value":
                        entry[
                            "input-packets-with-unknown-p2mp-nbr-nhid"] = value
                    elif key == "Input_packets_of_type_vxlan_bfd":
                        entry["input-packets-with-vxlan-bfd-pkts"] = value

                    continue

            if self.state == "mpls":

                m = p2.match(line)
                if m:

                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault("mpls", {})

                    if key == "Total_MPLS_packets_received":
                        entry["total-mpls-packets-received"] = value
                    elif key == "Packets_forwarded":
                        entry["packets-forwarded"] = value
                    elif key == "Packets_dropped":
                        entry["packets-dropped"] = value
                    elif key == "Packets_with_header_too_small":
                        entry["packets-with-header-too-small"] = value
                    elif key == "After_tagging,_packets_can't_fit_link_MTU":
                        entry[
                            "after-tagging-packets-can-not-fit-link-mtu"] = value
                    elif key == "Packets_with_IPv4_explicit_NULL_tag":
                        entry["packets-with-ipv4-explicit-null-tag"] = value
                    elif key == "Packets_with_IPv4_explicit_NULL_cksum_errors":
                        entry[
                            "packets-with-ipv4-explicit-null-checksum-errors"] = value
                    elif key == "Packets_with_router_alert_tag":
                        entry["packets-with-router-alert-tag"] = value
                    elif key == "LSP_ping_packets_(ttl-expired/router_alert)":
                        entry["lsp-ping-packets"] = value
                    elif key == "Packets_with_ttl_expired":
                        entry["packets-with-ttl-expired"] = value
                    elif key == "Packets_with_tag_encoding_error":
                        entry["packets-with-tag-encoding-error"] = value
                    elif key == "Packets_discarded_due_to_no_route":
                        entry["packets-discarded-due-to-no-route"] = value
                    elif key == "Packets_used_first_nexthop_in_ecmp_unilist":
                        entry[
                            "packets-used-first-nexthop-in-ecmp-unilist"] = value
                    elif key == "Packets_dropped_due_to_ifl_down":
                        entry["packets-dropped-due-to-ifl-down"] = value
                    elif key == "Packets_dropped_at_mpls_socket_send_op":
                        entry["packets-dropped-at-mpls-socket-send"] = value
                    elif key == "Packets_forwarded_at_mpls_socket_send_op":
                        entry["packets-forwarded-at-mpls-socket-send"] = value
                    elif key == "Packets_dropped,_over_p2mp_composite_nexthop":
                        entry["packets-dropped-at-p2mp-cnh-output"] = value

                    continue

            if self.state == "ethoamlfm":

                m = p2.match(line)
                if m:

                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault(
                        "ethoamlfm", {})

                    if key == "total_received_packets":
                        entry["total-packets-received"] = value
                    elif key == "input_drops_due_to_bad_interface_state":
                        entry["input-packets-drop-bad-interface-state"] = value
                    elif key == "received_packets_forwarded":
                        entry["received-packets-forwarded"] = value
                    elif key == "total_transmitted_packets":
                        entry["total-packets-transmitted"] = value
                    elif key == "sent_packets":
                        entry["packets-sent"] = value
                    elif key == "output_drops_due_to_bad_interface_state":
                        entry[
                            "output-packets-drop-bad-interface-state"] = value

                    continue

            if self.state == "ethoamcfm":

                m = p2.match(line)
                if m:

                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][0].setdefault(
                        "ethoamcfm", {})

                    if key == "total_received_packets":
                        entry["total-packets-received"] = value
                    elif key == "input_drops_due_to_bad_interface_state":
                        entry["input-packets-drop-bad-interface-state"] = value
                    elif key == "received_packets_forwarded":
                        entry["received-packets-forwarded"] = value
                    elif key == "total_transmitted_packets":
                        entry["total-packets-transmitted"] = value
                    elif key == "sent_packets":
                        entry["packets-sent"] = value
                    elif key == "output_drops_due_to_bad_interface_state":
                        entry[
                            "output-packets-drop-bad-interface-state"] = value
                    elif key == "flood_requests_forwarded_to_PFE":
                        entry["flood-requests-forwarded-to-pfe"] = value
                    elif key == "flood_requests_dropped":
                        entry["flood-requests-dropped"] = value

                    continue

            if self.state == "vpls":

                m = p2.match(line)
                if m:

                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][1].setdefault("vpls", {})

                    if key == "Total_packets_received":
                        entry["packets-received"] = value
                    elif key == "Packets_with_size_smaller_than_minimum":
                        entry["packets-with-size-smaller-than-minimum"] = value
                    elif key == "Packets_with_incorrect_version_number":
                        entry["packets-with-incorrect-version-number"] = value
                    elif key == "Packets_for_this_host":
                        entry["packets-for-this-host"] = value
                    elif key == "Packets_with_no_logical_interface":
                        entry["packets-with-no-logical-interface"] = value
                    elif key == "Packets_with_no_family":
                        entry["packets-with-no-family"] = value
                    elif key == "Packets_with_no_route_table":
                        entry["packets-with-no-route-table"] = value
                    elif key == "Packets_with_no_auxiliary_table":
                        entry["packets-with-no-auxiliary-table"] = value
                    elif key == "Packets_with_no_core-facing_entry":
                        entry["packets-with-no-core-facing-entry"] = value
                    elif key == "packets_with_no_CE-facing_entry":
                        entry["packets-with-no-ce-facing-entry"] = value
                    elif key == "MAC_route_learning_requests":
                        entry["mac-route-learning-requests"] = value
                    elif key == "MAC_routes_learnt":
                        entry["mac-routes-learned"] = value
                    elif key == "Requests_to_learn_an_existing_route":
                        entry["requests-to-learn-an-existing-route"] = value
                    elif (key ==
                          "Learning_requests_while_learning_disabled_on_interface"
                          ):
                        entry[
                            "learning-requests-while-learning-disabled-on-interface"] = value
                    elif key == "Learning_requests_over_capacity":
                        entry["learning-requests-over-capacity"] = value
                    elif key == "MAC_routes_moved":
                        entry["mac-routes-moved"] = value
                    elif key == "Requests_to_move_static_route":
                        entry["requests-to-move-static-route"] = value
                    elif key == "MAC_route_aging_requests":
                        entry["mac-route-aging-requests"] = value
                    elif key == "MAC_routes_aged":
                        entry["mac-routes-aged"] = value
                    elif key == "Bogus_address_in_aging_requests":
                        entry["bogus-address-in-aging-requests"] = value
                    elif key == "Requests_to_age_static_route":
                        entry["requests-to-age-static-route"] = value
                    elif key == "Requests_to_re-ageout_aged_route":
                        entry["requests-to-re-ageout-aged-route"] = value
                    elif key == "Requests_involving_multiple_peer_FEs":
                        entry["requests-involving-multiple-peer-fes"] = value
                    elif key == "Aging_acks_from_PFE":
                        entry["aging-acks-from-pfe"] = value
                    elif key == "Aging_non-acks_from_PFE":
                        entry["aging-non-acks-from-pfe"] = value
                    elif key == "Aging_requests_timed_out_waiting_on_FEs":
                        entry[
                            "aging-requests-timed-out-waiting-on-fes"] = value
                    elif key == "Aging_requests_over_max-rate":
                        entry["aging-requests-over-max-rate"] = value
                    elif key == "Errors_finding_peer_FEs":
                        entry["errors-finding-peer-fes"] = value
                    elif key == "Unsupported_platform":
                        entry["unsupported-platform"] = value
                    elif key == "Packets_dropped_due_to_no_l3_route_table":
                        entry[
                            "packets-dropped-due-to-no-l3-route-table"] = value
                    elif key == "Packets_dropped_due_to_no_local_ifl":
                        entry["packets-dropped-due-to-no-local-ifl"] = value
                    elif key == "Packets_punted":
                        entry["packets-punted"] = value
                    elif key == "Packets_dropped_due_to_no_socket":
                        entry["packets-dropped-due-to-no-socket"] = value

                    continue

            if self.state == "bridge":

                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group["key"]
                    key = key.strip()
                    key = key.replace(" ", "_")
                    value = group["number_value"]
                    entry = ret_dict["statistics"][1].setdefault("bridge", {})

                    if key == "Total_packets_received":
                        entry["packets-received"] = value
                    elif key == "Packets_with_size_smaller_than_minimum":
                        entry["packets-with-size-smaller-than-minimum"] = value
                    elif key == "Packets_with_incorrect_version_number":
                        entry["packets-with-incorrect-version-number"] = value
                    elif key == "Packets_for_this_host":
                        entry["packets-for-this-host"] = value
                    elif key == "Packets_with_no_logical_interface":
                        entry["packets-with-no-logical-interface"] = value
                    elif key == "Packets_with_no_family":
                        entry["packets-with-no-family"] = value
                    elif key == "Packets_with_no_route_table":
                        entry["packets-with-no-route-table"] = value
                    elif key == "Packets_with_no_auxiliary_table":
                        entry["packets-with-no-auxiliary-table"] = value
                    elif key == "Packets_with_no_core-facing_entry":
                        entry["packets-with-no-core-facing-entry"] = value
                    elif key == "packets_with_no_CE-facing_entry":
                        entry["packets-with-no-ce-facing-entry"] = value
                    elif key == "MAC_route_learning_requests":
                        entry["mac-route-learning-requests"] = value
                    elif key == "MAC_routes_learnt":
                        entry["mac-routes-learned"] = value
                    elif key == "Requests_to_learn_an_existing_route":
                        entry["requests-to-learn-an-existing-route"] = value
                    elif (key ==
                          "Learning_requests_while_learning_disabled_on_interface"
                          ):
                        entry[
                            "learning-requests-while-learning-disabled-on-interface"] = value
                    elif key == "Learning_requests_over_capacity":
                        entry["learning-requests-over-capacity"] = value
                    elif key == "MAC_routes_moved":
                        entry["mac-routes-moved"] = value
                    elif key == "Requests_to_move_static_route":
                        entry["requests-to-move-static-route"] = value
                    elif key == "MAC_route_aging_requests":
                        entry["mac-route-aging-requests"] = value
                    elif key == "MAC_routes_aged":
                        entry["mac-routes-aged"] = value
                    elif key == "Bogus_address_in_aging_requests":
                        entry["bogus-address-in-aging-requests"] = value
                    elif key == "Requests_to_age_static_route":
                        entry["requests-to-age-static-route"] = value
                    elif key == "Requests_to_re-ageout_aged_route":
                        entry["requests-to-re-ageout-aged-route"] = value
                    elif key == "Requests_involving_multiple_peer_FEs":
                        entry["requests-involving-multiple-peer-fes"] = value
                    elif key == "Aging_acks_from_PFE":
                        entry["aging-acks-from-pfe"] = value
                    elif key == "Aging_non-acks_from_PFE":
                        entry["aging-non-acks-from-pfe"] = value
                    elif key == "Aging_requests_timed_out_waiting_on_FEs":
                        entry[
                            "aging-requests-timed-out-waiting-on-fes"] = value
                    elif key == "Aging_requests_over_max-rate":
                        entry["aging-requests-over-max-rate"] = value
                    elif key == "Errors_finding_peer_FEs":
                        entry["errors-finding-peer-fes"] = value
                    elif key == "Unsupported_platform":
                        entry["unsupported-platform"] = value
                    elif key == "Packets_dropped_due_to_no_l3_route_table":
                        entry[
                            "packets-dropped-due-to-no-l3-route-table"] = value
                    elif key == "Packets_dropped_due_to_no_local_ifl":
                        entry["packets-dropped-due-to-no-local-ifl"] = value
                    elif key == "Packets_punted":
                        entry["packets-punted"] = value
                    elif key == "Packets_dropped_due_to_no_socket":
                        entry["packets-dropped-due-to-no-socket"] = value

                    continue

        return ret_dict


class ShowSystemStatisticsNoForwarding(ShowSystemStatistics):
    """ Parser for:
            * show system statistics no-forwarding
    """

    cli_command = "show system statistics no-forwarding"

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)

class ShowSystemInformationSchema(MetaParser):
    """ Schema for:
            * show system information
    """
    schema = {
        Optional("@xmlns:junos"): str,
        "system-information": {
            "hardware-model": str,
            "host-name": str,
            "os-name": str,
            "os-version": str,
            Optional("serial-number"): str
        }
    }


class ShowSystemInformation(ShowSystemInformationSchema):
    """ Parser for:
            * show system information
    """
    cli_command = 'show system information'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Model: vmx
        p1 = re.compile(r'^Model: +(?P<hardware_model>\S+)$')

        # Family: junos
        p2 = re.compile(r'^Family: +(?P<os_name>\S+)$')

        # Junos: 19.2R1.8
        p3 = re.compile(r'^Junos: +(?P<os_version>\S+)$')

        # Hostname: P4
        p4 = re.compile(r'^Hostname: +(?P<host_name>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Model: vmx
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("system-information", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # Family: junos
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("system-information", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # Junos: 19.2R1.8
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("system-information", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

            # Hostname: P4
            m = p4.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("system-information", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

        return ret_dict

class ShowSystemConnectionsSchema(MetaParser):
    """ Schema for:
            * show system connections
    """
    """ schema = {
        "output": {
            "connections-table": [
                {
                    "proto": str,
                    "recv-q": str,
                    "send-q": str,
                    "local-address": str,
                    "foreign-address": str,
                    "state": str,
                }
            ]
        }
    } """

    schema = {
        "output": {
            "connections-table": ListOf({
                "proto": str,
                "recv-q": str,
                "send-q": str,
                "local-address": str,
                "foreign-address": str,
                "state": str,
            })
        }
    }


class ShowSystemConnections(ShowSystemConnectionsSchema):
    """ Parser for:
            * show system connections
    """
    cli_command = 'show system connections'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Active Internet connections (including servers)
        p1 = re.compile(r'^Active +Internet +connections +\(including servers\) *$')

        # Proto Recv-Q Send-Q  Local Address                                 Foreign Address                               (state)
        p2 = re.compile(r'^Proto +Recv-Q +Send-Q +Local +Address +Foreign +Address +\(state\) *$')

        # tcp4       0      0  10.1.0.192.22                                  10.1.0.1.56714                                 ESTABLISHED
        p3 = re.compile(r'^(?P<proto>\S+) +(?P<recv_q>\S+) +(?P<send_q>\S+) +'
                        r'(?P<local_address>\S+) +(?P<foreign_address>\S+) +(?P<state>.*)$')

        for line in out.splitlines():
            line = line.strip()

            # Active Internet connections (including servers)
            m = p1.match(line)
            if m:
                continue

            # Proto Recv-Q Send-Q  Local Address
            m = p2.match(line)
            if m:
                continue

            # tcp4       0      0  10.1.0.192.22                                  10.1.0.1.56714                                 ESTABLISHED
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                connections_table_entry_list = ret_dict.setdefault('output', {}).\
                    setdefault('connections-table', [])

                entry_dict["proto"] = group["proto"]
                entry_dict["recv-q"] = group["recv_q"]
                entry_dict["send-q"] = group["send_q"]
                entry_dict["local-address"] = group["local_address"]
                entry_dict["foreign-address"] = group["foreign_address"]
                entry_dict["state"] = group["state"]

                connections_table_entry_list.append(entry_dict)

                continue

        return ret_dict
