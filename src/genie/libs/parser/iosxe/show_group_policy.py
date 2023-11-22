import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any

# ==============================
# Schema for:
#  * 'show group-policy traffic-steering policy sgt'
# ==============================
class ShowGroupPolicyTrafficSteeringPolicySchema(MetaParser):
    """Schema for show group-policy traffic-steering policy sgt."""

    schema = {
        "traffic_steering_policy": {
            Any(): {
                "sgt_policy_flag": str,
                "source_sgt": int,
                "destination_sgt": int,
                "steer_type": int,
                "steer_index": int,
                "contract_name": str,
                "ip_version": str,
                "refcnt": int,
                "flag": str,
                "stale": bool,
                "traffic_steering_ace": {
                    Any(): {
                        "protocol_number": int,
                        "source_port": str,
                        "destination_port": str,
                        "service_name": str,
                    }
                },
                "traffic_steering_destination_list": str,
                "traffic_steering_multicast_list": str,
                "traffic_steering_policy_lifetime_secs": int,
                "policy_last_update_time": str,
                "policy_expires_in": str,
                "policy_refreshes_in": str
            }
        }
    }

# ==============================
# Parser for:
# 'show group-policy traffic-steering policy sgt'
# ==============================
class ShowGroupPolicyTrafficSteeringPolicy(ShowGroupPolicyTrafficSteeringPolicySchema):
    """Schema for show group-policy traffic-steering policy sgt"""

    cli_command = 'show group-policy traffic-steering policy sgt'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}

        # SGT: 3053-01
        p1 = re.compile(r"^SGT:\s*(?P<sgt>\d+)-\d+$")

        # SGT Policy Flag: 0x41400001
        p2 = re.compile(r"^SGT Policy Flag:\s*(?P<sgt_policy_flag>0x[A-Fa-f\d]+)$")

        # Source SGT: 3053-01, Destination SGT: 4003-01
        p3 = re.compile(r"^Source SGT:\s*(?P<source_sgt>\d+)-\d+,"
                         r"\s*Destination SGT:\s*"
                         r"(?P<destination_sgt>\d+)-\d+$")

        # steer_type = 80
        p4 = re.compile(r"^steer_type\s*=\s*(?P<steer_type>\d+)$")

        # steer_index = 1
        p5 = re.compile(r"^steer_index\s*=\s*(?P<steer_index>\d+)$")

        # name   = Contract2-03
        p6 = re.compile(r"^name\s*=\s*(?P<contract_name>\w+)-\d+$")

        # IP protocol version = IPV4
        p7 = re.compile(r"^IP protocol version\s*=\s*"
                        r"(?P<ip_version>\w+)$")

        # refcnt = 1
        p8 = re.compile(r"^refcnt\s*=\s*(?P<refcnt>\d+)$")

        # flag   = 0x41400000
        p9 = re.compile(r"^flag\s*=\s*(?P<flag>0x[A-Fa-f\d]+)$")

        # stale  = FALSE
        p10 = re.compile(r"^stale\s*=\s*(?P<stale>\w+)$")

        # 1 redirect 6 any 16000 service service_INFRA_VN
        p11 = re.compile(r"^(?P<s_no>\d+)\s*redirect\s*"
                         r"(?P<protocol_number>\d+)\s*"
                         r"(?P<source_port>\w+)\s*"
                         r"(?P<destination_port>\w+)\s*service\s*"
                         r"(?P<service_name>\w+)$")

        # Traffic-Steering Destination List: Not exist
        p12 = re.compile(r"^Traffic-Steering Destination List:\s*"
                         r"(?P<traffic_steering_destination_list>[\w ]+)$")

        # Traffic-Steering Multicast List: Not exist
        p13 = re.compile(r"^Traffic-Steering Multicast List:\s*"
                         r"(?P<traffic_steering_multicast_list>[\w ]+)$")

        # Traffic-Steering Policy Lifetime = 86400 secs
        p14 = re.compile(r"^Traffic-Steering Policy Lifetime\s*=\s*"
                         r"(?P<traffic_steering_policy_lifetime_secs>\d+)\s*secs$")

        # Traffic-Steering Policy Last update time = 05:51:21 UTC Wed Sep 29 2021
        p15 = re.compile(r"^Traffic-Steering Policy Last update time\s*=\s*"
                         r"(?P<policy_last_update_time>[\d:]+\s+[\w ]+)$")

        # Policy expires in 0:23:58:12 (dd:hr:mm:sec)
        p16 = re.compile(r"^Policy expires in\s*"
                         r"(?P<policy_expires_in>[\d:]+)\s*\(dd:hr:mm:sec\)$")

        # Policy refreshes in 0:23:58:12 (dd:hr:mm:sec)
        p17 = re.compile(r"^Policy refreshes in\s*(?P<policy_refreshes_in>[\d:]+)\s*\(dd:hr:mm:sec\)$")

        ace_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # SGT: 3053-01
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                sgt = int(groups['sgt'])
                traffic_dict = ret_dict.setdefault('traffic_steering_policy', {})
                group_policy_dict = traffic_dict.setdefault(sgt,{})
                continue

            # SGT Policy Flag: 0x41400001
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                sgt_policy_flag = groups['sgt_policy_flag']
                group_policy_dict['sgt_policy_flag'] = sgt_policy_flag
                continue

            # Source SGT: 3053-01, Destination SGT: 4003-01
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                src_sgt = int(groups['source_sgt'])
                dst_sgt = int(groups['destination_sgt'])
                group_policy_dict['source_sgt'] = src_sgt
                group_policy_dict['destination_sgt'] = dst_sgt
                continue

            # steer_type = 80
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                steer_type = int(groups['steer_type'])
                group_policy_dict['steer_type'] = steer_type
                continue

            # steer_index = 1
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                steer_index = int(groups['steer_index'])
                group_policy_dict['steer_index'] = steer_index
                continue

            # name   = Contract2-03
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                contract_name = groups['contract_name']
                group_policy_dict['contract_name'] = contract_name
                continue

            # IP protocol version = IPV4
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                ip_version = groups['ip_version']
                group_policy_dict['ip_version'] = ip_version
                continue

            # refcnt = 1
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                refcnt = int(groups['refcnt'])
                group_policy_dict['refcnt'] = refcnt
                continue

            # flag   = 0x41400000
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                flag = groups['flag']
                group_policy_dict['flag'] = flag
                continue

            # stale  = FALSE
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                stale = groups['stale']
                group_policy_dict['stale'] = stale == 'TRUE'
                continue

            # 1 redirect 6 any 16000 service service_INFRA_VN
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                s_no = int(groups['s_no'])
                protocol_number = int(groups['protocol_number'])
                source_port = groups['source_port']
                destination_port = groups['destination_port']
                service_name = groups['service_name']
                ace_dict.update({s_no:{'protocol_number': protocol_number, \
                        'source_port': source_port, \
                        'destination_port': destination_port, \
                        'service_name': service_name}})
                group_policy_dict['traffic_steering_ace'] = ace_dict
                continue

            # Traffic-Steering Destination List: Not exist
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                traffic_steering_destination_list = \
                        groups['traffic_steering_destination_list']
                group_policy_dict['traffic_steering_destination_list'] \
                        = traffic_steering_destination_list
                continue

            # Traffic-Steering Multicast List: Not exist
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                traffic_steering_multicast_list = \
                        groups['traffic_steering_multicast_list']
                group_policy_dict['traffic_steering_multicast_list'] \
                        = traffic_steering_multicast_list
                continue

            # Traffic-Steering Policy Lifetime = 86400 secs
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                traffic_steering_policy_lifetime_secs = \
                        int(groups['traffic_steering_policy_lifetime_secs'])
                group_policy_dict['traffic_steering_policy_lifetime_secs'] \
                        = traffic_steering_policy_lifetime_secs
                continue

            # Traffic-Steering Policy Last update time = 05:51:21 UTC Wed Sep 29 2021
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                policy_last_update_time = \
                        groups['policy_last_update_time']
                group_policy_dict['policy_last_update_time'] \
                        = policy_last_update_time
                continue

            # Policy expires in 0:23:58:12 (dd:hr:mm:sec)
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                policy_expires_in = groups['policy_expires_in']
                group_policy_dict['policy_expires_in'] = policy_expires_in
                continue

            # Policy refreshes in 0:23:58:12 (dd:hr:mm:sec)
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                policy_refreshes_in = groups['policy_refreshes_in']
                group_policy_dict['policy_refreshes_in'] = policy_refreshes_in
                continue

        return ret_dict

# ==============================
# Schema for 'show group-policy traffic-steering entries'
# ==============================
class ShowGroupPolicyTrafficSteeringEntriesSchema(MetaParser):

    ''' Schema for "show group-policy traffic-steering entries" '''

    schema = {
        'steering_entries': {
            'sgt': {
                Any(): {
                    'peer_name': str,
                    'peer_sgt': str,
                    'entry_state': str,
                    'entry_last_refresh': str,
                    'requested_elements': str,
                    'policy_rbacl_src_list': {
                        'received_elements': str,
                        'installed_elements': str,
                        'received_peer_policy': {
                            'peer_policy': str,
                            'policy_flag': str,
                        },
                        'installed_peer_policy': {
                            'peer_policy': str,
                            'policy_flag': str,
                        },
                        'staled_peer_policy': {
                            'peer_policy': str,
                            'policy_flag': str,
                        },
                        Optional('installed_sgt_policy'): {
                            'peer_policy': str,
                            'policy_flag': str,
                        },
                        Optional('sgt_policy_last_refresh'): str,
                        Optional('sgt_policy_refresh_time_secs'): int,
                        Optional('policy_expires_in'): str,
                        Optional('policy_refreshes_in'): str,
                        Optional('refresh_timer'): str,
                        'retry_timer': str,
                        'entry_status': str,
                    }
                }
            }
        }
    }

# ==============================
# Parser for:
# 'show group-policy traffic-steering entries'
# ==============================
class ShowGroupPolicyTrafficSteeringEntries(ShowGroupPolicyTrafficSteeringEntriesSchema):
    """Schema for show group-policy traffic-steering entries"""

    cli_command = 'show group-policy traffic-steering entries'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Peer name                = Unknown-2057
        p1 = re.compile(r"^Peer name\s*=\s*(?P<peer_name>\w+)-(?P<sgt>\d+)$")

        # Peer SGT                 = 2057-01
        p2 = re.compile(r"^Peer SGT\s*=\s*(?P<peer_sgt>[\d-]+)$")

        # Entry State              = COMPLETE
        p3 = re.compile(r"^Entry State\s*=\s*(?P<entry_state>\w+)$")

        # Entry last refresh       = 20:04:10 UTC Sun Sep 26 2021
        p4 = re.compile(r"^Entry last refresh\s*=\s*(?P<entry_last_refresh>[\w:]+)\s*[\w ]+$")

        # Requested_elements       = 0x00001001
        p5 = re.compile(r"^Requested_elements\s*=\s*(?P<requested_elements>0x[A-Fa-d\d]+)$")

        # Received_elements        = 0x00000880
        p6 = re.compile(r"^Received_elements\s*=\s*(?P<received_elements>0x[A-Fa-d\d]+)$")

        # Installed_elements        = 0x00000880
        p7 = re.compile(r"^Installed_elements\s*=\s*(?P<installed_elements>0x[A-Fa-d\d]+)$")

        # Received peer policy   (0x00000000), policy_flag = 0x00000000
        p8 = re.compile(r"^Received peer policy\s*\((?P<peer_policy>0x[A-Fa-d\d]+)\),\s*policy_flag\s*=\s*(?P<policy_flag>0x[A-Fa-d\d]+)$")

        # Installed peer policy (0x7F561AFC4D80), policy_flag = 0x00400001
        p9 = re.compile(r"^Installed peer policy\s*\((?P<peer_policy>0x[A-Fa-d\d]+)\),\s*policy_flag\s*=\s*(?P<policy_flag>0x[A-Fa-d\d]+)$")

        # Staled peer policy (0x00000000), policy_flag = 0x00000000
        p10 = re.compile(r"^Staled peer policy\s*\((?P<peer_policy>0x[A-Fa-d\d]+)\),\s*policy_flag\s*=\s*(?P<policy_flag>0x[A-Fa-d\d]+)$")

        # Installed sgt policy  (0x7F561AFC6F10), policy_flag = 0x41400001
        p11 = re.compile(r"^Installed sgt policy  \s*\((?P<peer_policy>0x[A-Fa-d\d]+)\),\s*policy_flag\s*=\s*(?P<policy_flag>0x[A-Fa-d\d]+)$")

        # SGT  policy last refresh = 20:04:10 UTC Sun Sep 26 2021
        p12 = re.compile(r"^SGT  policy last refresh\s*=\s*(?P<sgt_policy_last_refresh>[\w: ]+)$")

        # SGT policy refresh time  = 86400
        p13 = re.compile(r"^SGT policy refresh time\s*=\s*(?P<sgt_policy_refresh_time_secs>\d+)$")

        # Policy expires in   0:23:51:50 (dd:hr:mm:sec)
        p14 = re.compile(r"^Policy expires in\s*(?P<policy_expires_in>[\w:]+)\s*\([\w:]+\)$")

        # Policy refreshes in 0:23:51:50 (dd:hr:mm:sec)
        p15 = re.compile(r"^Policy refreshes in\s*(?P<policy_refreshes_in>[\w:]+)\s*\([\w:]+\)$")

        # Refresh_timer            = not running
        p16 = re.compile(r"^Refresh_timer\s*=\s*(?P<refresh_timer>[\w ]+)$")

        # Retry_timer                  = not running
        p17 = re.compile(r"^Retry_timer\s*=\s*(?P<retry_timer>[\w ]+)$")

        # Entry status                 = UNKNOWN
        p18 = re.compile(r"^Entry status\s*=\s*(?P<entry_status>\w+)$")

        for line in output.splitlines():
            line = line.strip()

            # Peer name                = Unknown-2057
            m = p1.match(line)
            if m:
                steering_entries_dict = ret_dict.setdefault('steering_entries',{}).setdefault('sgt',{})
                groups = m.groupdict()
                peer_name = groups['peer_name']
                sgt = int(groups['sgt'])
                entry_dict = steering_entries_dict.setdefault(sgt,{})
                entry_dict['peer_name'] = peer_name+'-'+groups['sgt']
                continue

            # Peer SGT                 = 2057-01
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                peer_sgt = groups['peer_sgt']
                entry_dict['peer_sgt'] = peer_sgt
                continue

            # Entry State              = COMPLETE
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                entry_state = groups['entry_state']
                entry_dict['entry_state'] = entry_state
                continue

            # Entry last refresh       = 20:04:10 UTC Sun Sep 26 2021
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                entry_last_refresh = groups['entry_last_refresh']
                entry_dict['entry_last_refresh'] = entry_last_refresh
                continue

            # Requested_elements       = 0x00001001
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                requested_elements = groups['requested_elements']
                entry_dict['requested_elements'] = requested_elements
                continue

            # Received_elements        = 0x00000880
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                received_elements = groups['received_elements']
                rbacl_dict = entry_dict.setdefault('policy_rbacl_src_list',{})
                rbacl_dict['received_elements'] = received_elements
                continue

            # Installed_elements        = 0x00000880
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                installed_elements = groups['installed_elements']
                rbacl_dict['installed_elements'] = installed_elements
                continue

            # Received peer policy   (0x00000000), policy_flag = 0x00000000
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                peer_policy = groups['peer_policy']
                policy_flag = groups['policy_flag']
                received_peer_policy_dict = rbacl_dict.setdefault('received_peer_policy',{})
                received_peer_policy_dict['peer_policy'] = peer_policy
                received_peer_policy_dict['policy_flag'] = policy_flag
                continue

            # Installed peer policy (0x7F561AFC4D80), policy_flag = 0x00400001
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                peer_policy = groups['peer_policy']
                policy_flag = groups['policy_flag']
                installed_peer_policy_dict = rbacl_dict.setdefault('installed_peer_policy',{})
                installed_peer_policy_dict['peer_policy'] = peer_policy
                installed_peer_policy_dict['policy_flag'] = policy_flag
                continue

            # Staled peer policy (0x00000000), policy_flag = 0x00000000
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                peer_policy = groups['peer_policy']
                policy_flag = groups['policy_flag']
                staled_peer_policy_dict = rbacl_dict.setdefault('staled_peer_policy',{})
                staled_peer_policy_dict['peer_policy'] = peer_policy
                staled_peer_policy_dict['policy_flag'] = policy_flag
                continue

            # Installed sgt policy  (0x7F561AFC6F10), policy_flag = 0x41400001
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                peer_policy = groups['peer_policy']
                policy_flag = groups['policy_flag']
                installed_sgt_policy_dict = rbacl_dict.setdefault('installed_sgt_policy',{})
                installed_sgt_policy_dict['peer_policy'] = peer_policy
                installed_sgt_policy_dict['policy_flag'] = policy_flag
                continue

            # SGT  policy last refresh = 20:04:10 UTC Sun Sep 26 2021
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                sgt_policy_last_refresh = groups['sgt_policy_last_refresh']
                rbacl_dict['sgt_policy_last_refresh'] = sgt_policy_last_refresh
                continue

            # SGT policy refresh time  = 86400
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                sgt_policy_refresh_time = int(groups['sgt_policy_refresh_time_secs'])
                rbacl_dict['sgt_policy_refresh_time_secs'] = sgt_policy_refresh_time
                continue

            # Policy expires in   0:23:51:50 (dd:hr:mm:sec)
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                policy_expires_in = groups['policy_expires_in']
                rbacl_dict['policy_expires_in'] = policy_expires_in
                continue

            # Policy refreshes in 0:23:51:50 (dd:hr:mm:sec)
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                policy_refreshes_in = groups['policy_refreshes_in']
                rbacl_dict['policy_refreshes_in'] = policy_refreshes_in
                continue

            # Refresh_timer            = not running
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                refresh_timer = groups['refresh_timer']
                rbacl_dict['refresh_timer'] = refresh_timer
                continue

            # Retry_timer                  = not running
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                retry_timer = groups['retry_timer']
                rbacl_dict['retry_timer'] = retry_timer
                continue

            # Entry status                 = UNKNOWN
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                entry_status = groups['entry_status']
                rbacl_dict['entry_status'] = entry_status
                continue

        return ret_dict

# ==============================
# Schema for 'show group-policy traffic-steering counters'
# ==============================
class ShowGroupPolicyTrafficSteeringCountersSchema(MetaParser):

    ''' Schema for "show group-policy traffic-steering counters" '''

    schema = {
        'sgt': {
            Any(): {
                'source_sgt': int,
                'destination_sgt': int,
                'hw_redirect': int,
            },
        }
    }


# ==============================
# Parser for:
# 'show group-policy traffic-steering counters'
# ==============================
class ShowGroupPolicyTrafficSteeringCounters(ShowGroupPolicyTrafficSteeringCountersSchema):
    """Schema for show group-policy traffic-steering counters"""

    cli_command = 'show group-policy traffic-steering counters'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # 2057            3003                 0
        p1 = re.compile(r'^(?P<sgt>\d+)\s+(?P<dgt>\d+)\s+(?P<count>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # 2057            3003                 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                sgt = int(groups['sgt'])
                dgt = int(groups['dgt'])
                count = int(groups['count'])
                sgt_counters_dict = ret_dict.setdefault('sgt',{}).setdefault(sgt,{})
                sgt_counters_dict['source_sgt'] = sgt
                sgt_counters_dict['destination_sgt'] = dgt
                sgt_counters_dict['hw_redirect'] = count

        return ret_dict

# ==============================
# Schema for 'show group-policy traffic-steering permissions'
# ==============================
class ShowGroupPolicyTrafficSteeringPermissionsSchema(MetaParser):

    ''' Schema for "show group-policy traffic-steering permissions" '''

    schema = {
        'policy_permissions': {
            'sgt': {
                Any(): {
                    'source_sgt': int,
                    'destination_sgt': int,
                    'steering_policy': str,
                },
            }
        }
    }

# ==============================
# Parser for:
# 'show group-policy traffic-steering permissions'
# ==============================
class ShowGroupPolicyTrafficSteeringPermissions(ShowGroupPolicyTrafficSteeringPermissionsSchema):
    """Schema for show group-policy traffic-steering permissions"""

    cli_command = 'show group-policy traffic-steering permissions'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # 2057              3003            Contract1-01
        p1 = re.compile(r'^(?P<sgt>\d+)\s+(?P<dgt>\d+)\s+(?P<policy>[\w-]+)$')

        for line in output.splitlines():
            line = line.strip()

            # 2057              3003            Contract1-01
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                sgt = int(groups['sgt'])
                dgt = int(groups['dgt'])
                policy = groups['policy']
                steering_permission_dict = ret_dict.setdefault('policy_permissions',{}).setdefault('sgt',{}).setdefault(sgt,{})
                steering_permission_dict['source_sgt'] = sgt
                steering_permission_dict['destination_sgt'] = dgt
                steering_permission_dict['steering_policy'] = policy

        return ret_dict

