"""show_system.py

JunOS parsers for the following show commands:
    - 'show system buffers'
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use, SchemaTypeError


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
        p6 = re.compile(r'^(?P<current_jumbo_clusters_16k>\S+)/'
        r'(?P<cached_jumbo_clusters_16k>\S+)/(?P<total_jumbo_clusters_16k>\S+)/'
        r'(?P<max_jumbo_clusters_16k>\S+) +16k +\(page +size\) +jumbo +clusters'
        r' +in +use +\(current/cache/total/max\)$')

        # 1179K/1971K/3150K bytes allocated to network (current/cache/total)
        p7 =re.compile(r'^(?P<current_bytes_in_use>\S+)K/(?P<cached_bytes>\S+)K/'
        r'(?P<total_bytes>\S+)K +bytes +allocated +to +network +\(current/cache/total\)$')

        # 0/0/0 requests for mbufs denied (mbufs/clusters/mbuf+clusters)
        p8 = re.compile(r'^(?P<mbuf_failures>\S+)/(?P<cluster_failures>\S+)/'
        r'(?P<packet_failures>\S+) +requests +for +mbufs +denied +\(mbufs/clusters/mbuf\+clusters\)$')

        # 0/0/0 requests for jumbo clusters denied (4k/9k/16k)
        p9 =re.compile(r'^(?P<jumbo_cluster_failures_4k>\S+)/(?P<jumbo_cluster_failures_9k>\S+)'
        r'/(?P<jumbo_cluster_failures_16k>\S+) +requests +for +jumbo +clusters +denied +\(4k/9k/16k\)$')

        # 0 requests for sfbufs denied
        p10 = re.compile(r'^(?P<sfbuf_requests_denied>\S+) +requests +for +sfbufs'
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
        p1 = re.compile(r'^(?P<file_permissions>\S+) +(?P<file_links>\S+) +(?P<file_owner>\S+)  +(?P<file_group>\S+) +(?P<file_size>\S+) +(?P<file_date>\S+ +\d+ +\d+) +(?P<file_name>\S+)$')

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
                entry_list = ret_dict.setdefault("directory-list", {}).setdefault("directory", {}).setdefault("file-information", [])
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
                entry_list = ret_dict.setdefault("directory-list", {}).setdefault("directory", {}).setdefault("output", [])

                entry_list.append(group['output'])
                continue

            # total files: 6
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict.setdefault("directory-list", {}).setdefault("directory", {})

                entry['total-files'] = group['total_files']
                continue

        return ret_dict
