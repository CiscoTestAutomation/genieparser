"""show_system.py

JunOS parsers for the following show commands:
    - 'show system commit'
    - 'show system queues'
    - 'show system queues no-forwarding'
    - 'show system buffers'
    - 'show system buffers no-forwarding'
    - 'show system core-dumps'
    - 'show system core-dumps no-forwarding'
    - 'show system users'
    - 'show system storage'
    - 'show system storage no-forwarding'
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use
from genie.metaparser.util.exceptions import SchemaTypeError

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
            "total-mbufs": str
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
        p1 = re.compile(r'^(?P<name>\S+) +(?P<octets_in_queue>\d+)'
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
                    entry_key = group_key.replace('_','-')
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

    # Sub Schema filesystem
    def validate_filesystem_list(value):
        # Pass filesystem list as value
        if not isinstance(value, list):
            raise SchemaTypeError('filesystem is not a list')
        filesystem_schema = Schema(
            {
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
        # Validate each dictionary in list
        for item in value:
            filesystem_schema.validate(item)
        return value

    schema = {
        "system-storage-information": {
            "filesystem": Use(validate_filesystem_list)
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
        p1 = re.compile(r'^(?P<filesystem_name>\S+) +(?P<total_blocks>\S+) +'
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
    # Sub Schema file-information
    def validate_file_information_list(value):
        # Pass file-information list as value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-interface is not a list')
        file_information_schema = Schema({
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
                    })
        # Validate each dictionary in list
        for item in value:
            file_information_schema.validate(item)
        return value

    schema = {
        "directory-list": {
            "directory": {
                "file-information": Use(validate_file_information_list),
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
        p1 = re.compile(r'^(?P<file_permissions>\S+) +(?P<file_links>\S+) +'
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
                entry["file-permissions"] = {"@junos:format": group['file_permissions']}
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
        "time-source": str,
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
                        r'\w+\s\d+\:\d+) ago\) by (?P<user>\S+)$')

        #8:16AM  up 209 days, 23:14, 5 users, load averages: 0.43, 0.43, 0.42
        p6 = re.compile(r'^(?P<date_time>\d+\:\w+)\s+up\s+'
                        r'(?P<days>\d+)\s+days,\s+(?P<mins>'
                        r'[\w\:]+)[^,]*,\s+(?P<user_count>\d+)'
                        r'\s+users,\s+load\s+averages:\s+'
                        r'(?P<avg1>[\d\.]+),\s+(?P<avg2>[\d\.]+),'
                        r'\s+(?P<avg3>[\d\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            #Current time: 2020-03-26 08:16:41 UTC
            m = p1.match(line)
            if m:
                group = m.groupdict()
                user_table_entry_list = ret_dict.setdefault('system-uptime-information', {})

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

                user_table_entry_list["system-booted-time"] = current_system_dict
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
                current_protocol_dict["time-length"] = current_protocol_time_dict

                user_table_entry_list["protocols-started-time"] = current_protocol_dict
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

                last_user_entry_dict = user_table_entry_list.setdefault("last-configured-time",{})
                last_user_entry_dict.update({'user' :group["user"] })

                last_user_entry_dict.update({'date-time' :current_last_date_dict})
                last_user_entry_dict.update({'time-length' :current_last_time_dict})
                continue

            #8:16AM  up 209 days, 23:14, 5 users, load averages: 0.43, 0.43, 0.42
            m = p6.match(line)
            if m:
                group = m.groupdict()
                current_up_dict = {}
                current_up_date_dict = {}
                current_up_date_dict["#text"] = group["date_time"]

                current_up_time_dict = {}
                current_up_time_dict["#text"] = group["days"]+" days,"+" "+group["mins"]+" mins,"

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
