"""show_system.py

JunOS parsers for the following show commands:
    - 'show system buffers'
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


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
        p1 = re.compile(r'^Current time: +(?P<current_time>[\d\-\s\:]+\S+)$')

        #Time Source:  LOCAL CLOCK 
        p2 = re.compile(r'^Time Source: +(?P<time_source>[A-Za-z\t .]+)$')

        #System booted: 2019-08-29 09:02:22 UTC (29w6d 23:14 ago) 
        p3 = re.compile(r'^System booted: +(?P<date_time>'
                        r'[A-Za-z\t .\d\-\:]+)+\((?P<time_length>'
                        r'\w+\s\d+\:\d+)\s+ago\)$')

        #Protocols started: 2019-08-29 09:03:25 UTC (29w6d 23:13 ago) 
        p4 = re.compile(r'^Protocols started: +(?P<date_time>'
                        r'[A-Za-z\t .\d\-\:]+)+\((?P<time_length>'
                        r'\w+\s\d+\:\d+)\s+ago\)$')

        #Last configured: 2020-03-05 16:04:34 UTC (2w6d 16:12 ago) by kddi 
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

            #Last configured: 2020-03-05 16:04:34 UTC (2w6d 16:12 ago) by kddi
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