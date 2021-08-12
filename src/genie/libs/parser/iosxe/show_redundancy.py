"""
IOSXE Parsers for the following show commands:
    * show redundancy switchover history
    * show redundancy application group {group_id}
    * show redundancy application group all
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =======================================
# Schema for:
#  * 'show redundancy switchover history'
# =======================================
class ShowRedundancySwitchoverHistorySchema(MetaParser):
    """Schema for show redundancy switchover history."""

    schema = {
        Optional("index"): {
            Any(): {
                "current_active": int,
                "previous_active": int,
                "switchover_reason": str,
                "switchover_time": str,
            },
        }
    }


# =======================================
# Parser for:
#  * 'show redundancy switchover history'
# =======================================
class ShowRedundancySwitchoverHistory(ShowRedundancySwitchoverHistorySchema):
    """Parser for show redundancy switchover history"""

    cli_command = ['show redundancy switchover history']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Index  Previous  Current  Switchover             Switchover
        #        active    active   reason                 time
        # -----  --------  -------  ----------             ----------
        #    1       1        2     Active lost GW         03:26:09 UTC Wed Sep 23 2020
        #    2       2        1     user forced            05:40:13 UTC Thu Oct 1 2020


        #    1       1        2     Active lost GW         03:26:09 UTC Wed Sep 23 2020
        switchover_history_capture = re.compile(
            # 1
            r"^(?P<index>\d+)\s+"
            # 1
            r"(?P<previous_active>\d+)\s+"
            # 2
            r"(?P<current_active>\d+)\s+"
            # Active lost GW
            r"(?P<switchover_reason>.+)\s+"
            # 03:26:09 UTC Wed Sep 23 2020
            r"(?P<switchover_time>\d+:\d+:\d+\s\S+\s\S+\s\S+\s\d+\s\d+)$"
        )

        redundancy_info_obj = {}

        for line in output.splitlines():
            line = line.strip()

            if switchover_history_capture.match(line):
                match = switchover_history_capture.match(line)
                group = match.groupdict()
                
                # remove trailing spaces from regex capture
                group["switchover_reason"] = group["switchover_reason"].strip()

                # convert str to int
                key_list = ["index", "current_active", "previous_active"]
                for key in key_list:
                    group[key] = int(group[key])    

                # pull a key from dict to use as new_key
                new_key = "index"
                info_dict = {group[new_key]: {}}

                # update then pop new_key from the dict
                info_dict[group[new_key]].update(group)
                info_dict[group[new_key]].pop(new_key)

                if not redundancy_info_obj.get(new_key):
                    # initialize the dict with new_key
                    redundancy_info_obj[new_key] = {}

                redundancy_info_obj[new_key].update(info_dict)

        return redundancy_info_obj



class ShowRedundancyApplicationGroupSchema(MetaParser):
    """
    Schema for:
        * show redundancy application group {group_id}
        * show redundancy application group all
    """

    schema = {
        'group_id': {
            Any(): {  # group id
                "group_name": str,
                Optional("fault_states_group"): {
                    Any(): {
                        Optional("runtime_priority"): int,
                        Optional("rg_faults_rg_state"): str,
                        Optional("total_switchovers_due_to_faults"): int,
                        Optional("total_down_or_up_state_changes_due_to_faults"): int
                    }
                },
                "administrative_state": str,
                "aggregate_operational_state": str,
                "my_role": str,
                "peer_role": str,
                "peer_presence": str,
                "peer_comm": str,
                "peer_progression_started": str,
                "rf_domain": {
                    Any(): {"rf_state": str, "peer_rf_state": str}  # domain name
                },
                Optional("rg_protocol"): {
                    Any(): {  # group id
                        "role": str,
                        "negotiation": str,
                        "priority": int,
                        "protocol_state": str,
                        "ctrl_interfaces_state": str,
                        "active_peer": {
                            Optional("address"): str,
                            Optional("priority"): int,
                            Optional("interface"): str,
                        },
                        "standby_peer": {
                            Optional("address"): str,
                            Optional("priority"): int,
                            Optional("interface"): str,
                        },
                        "log_counters": {
                            "role_change_to_active": int,
                            "role_change_to_standby": int,
                            "disable_events": {"rg_down_state": int, "rg_shut": int},
                            "ctrl_interface_events": {
                                "up": int,
                                "down": int,
                                "admin_down": int,
                            },
                            "reload_events": {"local_request": int, "peer_request": int},
                        },
                    },
                },
                Optional("rg_media_context"): {
                    Any(): {  # group id
                        "ctx_state": str,
                        "protocol_id": int,
                        "media_type": str,
                        "ctrl_interface": str,
                        "timers": {
                            "current_hello_timer": int,
                            "configured_hello_timer": int,
                            "hold_timer": int,
                            "peer_hello_timer": int,
                            "peer_hold_timer": int,
                        },
                        "stats": {
                            "pkts": int,
                            "bytes": int,
                            "ha_seq": int,
                            "seq_number": int,
                            "pkt_loss": int,
                            "authentication": str,
                            "authentication_failures": int,
                            "reload_peer": {"tx": int, "rx": int},
                            "resign": {"tx": int, "rx": int},
                        },
                        "active_peer": {
                            "pkts": int,
                            "bytes": int,
                            "ha_seq": int,
                            "seq_number": int,
                            "pkt_loss": int,
                            "status": str,
                            "hold_timer": int
                        }
                    }
                }
            }
        }
    }


class ShowRedundancyApplicationGroup(ShowRedundancyApplicationGroupSchema):
    """
    Parser for
     * show redundancy application group {group_id}
     * show redundancy application group all
    """

    cli_command = ['show redundancy application group {group_id}', 'show redundancy application group all']

    def cli(self, group_id='', output=None):
        if output is None:
            if group_id:
                out = self.device.execute(self.cli_command[0].format(group_id=group_id))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        # Faults states Group 1 info:
        p1 = re.compile(r'^Faults +states +Group +(?P<fault_group_id>\w+) +info+:$')

        # Runtime priority: [200]
        p2 = re.compile(r'^Runtime priority: +\[(?P<runtime_priority>(\d+))]$')

        # RG Faults RG State: Up
        p3 = re.compile(r'^RG Faults RG State: +(?P<rg_fault_state>\w+)')

        # Total # of switchovers due to faults:           0
        p4 = re.compile(r'^Total # of switchovers due to faults: +(?P<fault_switchovers>\d+)$')

        # Total # of down/up state changes due to faults: 0
        p5 = re.compile(r'^Total # of down\/up state changes due to faults: +(?P<fault_state_changes>\d+)$')

        # Group ID:1
        p6 = re.compile(r'^Group ID:(?P<group_id>\d+)$')

        # Group Name:group1
        p7 = re.compile(r'^Group Name:(?P<group_name>\S+)$')

        # Administrative State: No Shutdown
        p8 = re.compile(r'^Administrative State: +(?P<admin_state>[\w\s]+)$')

        # Aggregate operational state : Up
        p9 = re.compile(r'^Aggregate operational state : +(?P<aggregate_state>[\w]+)$')

        # My Role: ACTIVE
        p10 = re.compile(r'^My Role: +(?P<my_role>\w+)$')

        # Peer Role: STANDBY
        p11 = re.compile(r'^Peer Role: +(?P<peer_role>\w+)$')

        # Peer Presence: Yes
        p12 = re.compile(r'^Peer Presence: +(?P<peer_presence>\w+)$')

        # Peer Comm: Yes
        p13 = re.compile(r'^Peer Comm: +(?P<peer_comm>\w+)$')

        # Peer Progression Started: Yes
        p14 = re.compile(r'^Peer Progression Started: +(?P<peer_progress>\w+)$')

        # RF Domain: btob-one
        p15 = re.compile(r'^RF Domain: +(?P<rf_domain>\S+)$')

        # RF state: ACTIVE
        p16 = re.compile(r'^RF state: +(?P<rf_state>[\w\s]+)$')

        # Peer RF state: STANDBY HOT
        p17 = re.compile(r'^Peer RF state: +(?P<peer_rf_state>[\w\s]+)$')

        # RG Protocol RG 1
        p18 = re.compile(r'^RG +Protocol +RG +(?P<rg_protocol_id>\w+)$')

        # Role: Standby
        p19 = re.compile(r'^Role: +(?P<role>[\w-]+)$')

        # Negotiation: Enabled
        p20 = re.compile(r'^Negotiation: +(?P<negotiation>[\w]+)$')

        # Priority: 200
        p21 = re.compile(r'^Priority: +(?P<priority>[\d]+)$')

        # Protocol state: Standby-hot
        p22 = re.compile(r'^Protocol state: +(?P<protocol_state>[\w-]+)$')

        # Ctrl Intf(s) state: Up
        p23 = re.compile(r'^Ctrl Intf\(s\) state: +(?P<ctrl_intf_state>[\w-]+)$')

        # Active Peer: address 9.1.1.1, priority 200, intf Po10.100
        # Active Peer: Local
        p24 = re.compile(r'^Active Peer: +((?P<local>Local$)|address +(?P<address>\S+), '
                         r'+priority +(?P<priority>\d+), +intf +(?P<intf>\S+)$)')

        # Standby Peer: address 9.1.1.1, priority 200, intf Po10.100
        # Standby Peer: Local
        p25 = re.compile(r'^Standby Peer: +((?P<local>Local$)|address +(?P<address>\S+), '
                         r'+priority +(?P<priority>\d+), +intf +(?P<intf>\S+)$)')

        # Log counters:
        p26 = re.compile(r'\s*Log+\s+counters+:')

        # role change to active: 0
        p27 = re.compile(r'^role change to active: +(?P<role_to_active>\d+)$')

        # role change to standby: 1
        p28 = re.compile(r'^role change to standby: +(?P<role_to_standby>\d+)$')

        # disable events: rg down state 0, rg shut 0
        p29 = re.compile(r'^disable events: +rg down state (?P<rg_down>(\d+)), +rg shut (?P<rg_shut>(\d+))$')

        # ctrl intf events: up 1, down 1, admin_down 0
        p30 = re.compile(r'^ctrl intf events: +up (?P<up>(\d+)), +down (?P<down>(\d+)), '
                         r'+admin_down (?P<admin_down>(\d+))$')

        # reload events: local request 0, peer request 0
        p31 = re.compile(r'^reload events: +local request (?P<local>(\d+)), +peer request (?P<peer>(\d+))$')

        # RG Media Context for RG 1
        p32 = re.compile(r'^RG Media Context for RG +(?P<rg_media_id>\d+)$')

        # Ctx State: Standby
        p33 = re.compile(r'^Ctx State: +(?P<ctx_state>[\w-]+)$')

        # Protocol ID: 1
        p34 = re.compile(r'^Protocol +ID: +(?P<protocol_id>\d+)$')

        # Media type: Default
        p35 = re.compile(r'^Media type: +(?P<media_type>\w+)$')

        # Control Interface: Port-channel10.100
        p36 = re.compile(r'^Control Interface: +(?P<control_interface>\S+)$')

        # Current Hello timer: 3000
        p37 = re.compile(r'^Current Hello timer: +(?P<current_hello_timer>\d+)$')

        # Configured Hello timer: 3000, Hold timer: 9000
        p38 = re.compile(r'^Configured Hello timer: +(?P<conf_hello_timer>\d+), +Hold timer: +(?P<hold_timer>\d+)$')

        # Peer Hello timer: 3000, Peer Hold timer: 9000
        p39 = re.compile(r'^Peer Hello timer: +(?P<peer_hello_timer>\d+), '
                         r'+Peer Hold timer: +(?P<peer_hold_timer>\d+)$')

        # Stats:
        p40 = re.compile(r'\s*Stats+:')

        # Pkts 144780, Bytes 8976360, HA Seq 0, Seq Number 144780, Pkt Loss 0
        p41 = re.compile(r'^Pkts +(?P<pkts>\d+), +Bytes +(?P<bytes>\d+), +HA Seq +(?P<ha_seq>\d+), '
                         r'+Seq Number +(?P<seq_number>\d+), Pkt Loss +(?P<pkt_loss>\d+)$')

        # Authentication not configured
        p42 = re.compile(r'^Authentication +(?P<auth_status>configured|not configured)$')

        # Authentication Failure: 0
        p43 = re.compile(r'^Authentication Failure: +(?P<auth_failure>[\d]+)$')

        # Reload Peer: TX 0, RX 0
        p44 = re.compile(r'^Reload Peer: +TX +(?P<tx>\d+), +RX +(?P<rx>\d+)$')

        # Resign: TX 0, RX 0
        p45 = re.compile(r'^Resign: +TX +(?P<tx>\d+), +RX +(?P<rx>\d+)$')

        # Active Peer: Present. Hold Timer: 9000
        p46 = re.compile(r'^Active Peer: +(?P<active_peer>\S+)\. +Hold Timer: +(?P<hold_timer>\d+)$')

        # return dictionary
        ret_dict = {}
        # flags
        fault_group_data = None
        recorded_stats = False

        for line in out.splitlines():
            line = line.strip()

            # Faults states Group 1 info:
            m = p1.match(line)
            if m:
                fault_states_group = m.groupdict()['fault_group_id']
                continue

            # Runtime priority: [200]
            m = p2.match(line)
            if m:
                runtime_priority = int(m.groupdict()['runtime_priority'])
                continue

            # RG Faults RG State: Up
            m = p3.match(line)
            if m:
                rg_faults_rg_state = m.groupdict()['rg_fault_state']
                continue

            # Total # of switchovers due to faults:           0
            m = p4.match(line)
            if m:
                total_switchovers = int(m.groupdict()['fault_switchovers'])
                continue

            # Total # of down/up state changes due to faults: 0
            m = p5.match(line)
            if m:
                total_state_changes = int(m.groupdict()['fault_state_changes'])
                fault_group_data = {'fault_states_group': {
                    fault_states_group: {
                        'runtime_priority': runtime_priority,
                        'rg_faults_rg_state': rg_faults_rg_state,
                        'total_switchovers_due_to_faults': total_switchovers,
                        'total_down_or_up_state_changes_due_to_faults': total_state_changes
                    }
                }}
                continue

            # Group ID:1
            m = p6.match(line)
            if m:
                group_id = m.groupdict()['group_id']
                group_dict = ret_dict.setdefault('group_id', {}).setdefault(group_id, {})
                if fault_group_data:
                    group_dict.update(fault_group_data)
                    fault_group_data.clear()
                continue

            # Group Name:group1
            m = p7.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue

            # Administrative State: No Shutdown
            m = p8.match(line)
            if m:
                group_dict.update({'administrative_state': m.groupdict()['admin_state']})
                continue

            # Aggregate operational state : Up
            m = p9.match(line)
            if m:
                group_dict.update({'aggregate_operational_state': m.groupdict()['aggregate_state']})
                continue

            # My Role: ACTIVE
            m = p10.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue

            # Peer Role: STANDBY
            m = p11.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue

            # Peer Presence: Yes
            m = p12.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue

            # Peer Comm: Yes
            m = p13.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue

            # Peer Progression Started: Yes
            m = p14.match(line)
            if m:
                group_dict.update({'peer_progression_started': m.groupdict()['peer_progress']})
                continue

            # RF Domain: btob-one
            m = p15.match(line)
            if m:
                rf_dict = group_dict.setdefault('rf_domain', {}).setdefault(m.groupdict()['rf_domain'], {})
                continue

            # RF state: ACTIVE
            m = p16.match(line)
            if m:
                rf_dict.update(m.groupdict())
                continue

            # Peer RF state: STANDBY HOT
            m = p17.match(line)
            if m:
                rf_dict.update(m.groupdict())
                continue

            # RG Protocol RG 1
            m = p18.match(line)
            if m:
                rg_protocol_dict = group_dict.setdefault('rg_protocol', {}).\
                    setdefault(int(m.groupdict()['rg_protocol_id']), {})
                continue

            # Role: Standby
            m = p19.match(line)
            if m:
                rg_protocol_dict.update(m.groupdict())
                continue

            # Negotiation: Enabled
            m = p20.match(line)
            if m:
                rg_protocol_dict.update(m.groupdict())
                continue

            # Priority: 200
            m = p21.match(line)
            if m:
                rg_protocol_dict.update({'priority': int(m.groupdict()['priority'])})
                continue

            # Protocol state: Standby-hot
            m = p22.match(line)
            if m:
                rg_protocol_dict.update(m.groupdict())
                continue

            # Ctrl Intf(s) state: Up
            m = p23.match(line)
            if m:
                rg_protocol_dict.update({'ctrl_interfaces_state': m.groupdict()['ctrl_intf_state']})
                continue

            # Active Peer: address 9.1.1.1, priority 200, intf Po10.100
            # Active Peer: Local
            m = p24.match(line)
            if m:
                active_peer = rg_protocol_dict.setdefault('active_peer', {})
                if m.groupdict()['local']:
                    active_peer.update({'local': m.groupdict()['local']})

                if m.groupdict()['address'] and m.groupdict()['priority'] and m.groupdict()['intf']:
                    active_peer.update({'address': m.groupdict()['address']})
                    active_peer.update({'priority': int(m.groupdict()['priority'])})
                    active_peer.update({'interface': m.groupdict()['intf']})
                continue

            # Standby Peer: address 9.1.1.1, priority 200, intf Po10.100
            # Standby Peer: Local
            m = p25.match(line)
            if m:
                standby_peer = rg_protocol_dict.setdefault('standby_peer', {})
                if m.groupdict()['local']:
                    standby_peer.update({'address': m.groupdict()['local']})

                if m.groupdict()['address'] and m.groupdict()['priority'] and m.groupdict()['intf']:
                    standby_peer.update({'address': m.groupdict()['address']})
                    standby_peer.update({'priority': int(m.groupdict()['priority'])})
                    standby_peer.update({'interface': m.groupdict()['intf']})
                continue

            # Log counters:
            m = p26.match(line)
            if m:
                log_dict = rg_protocol_dict.setdefault('log_counters', {})
                continue

            # role change to active: 0
            m = p27.match(line)
            if m:
                log_dict.update({'role_change_to_active': int(m.groupdict()['role_to_active'])})
                continue

            # role change to standby: 1
            m = p28.match(line)
            if m:
                log_dict.update({'role_change_to_standby': int(m.groupdict()['role_to_standby'])})
                continue

            # disable events: rg down state 0, rg shut 0
            m = p29.match(line)
            if m:
                log_dict.update({
                    'disable_events': {
                        'rg_down_state': int(m.groupdict()['rg_down']),
                        'rg_shut': int(m.groupdict()['rg_shut'])
                    }
                })
                continue

            # ctrl intf events: up 1, down 1, admin_down 0
            m = p30.match(line)
            if m:
                log_dict.update({
                    'ctrl_interface_events': {
                        'up': int(m.groupdict()['up']),
                        'down': int(m.groupdict()['down']),
                        'admin_down': int(m.groupdict()['admin_down'])
                    }
                })
                continue

            # reload events: local request 0, peer request 0
            m = p31.match(line)
            if m:
                log_dict.update({
                    'reload_events': {
                        'local_request': int(m.groupdict()['local']),
                        'peer_request': int(m.groupdict()['peer'])
                    }
                })

            # RG Media Context for RG 1
            m = p32.match(line)
            if m:
                rg_media_dict = group_dict.setdefault('rg_media_context', {}).\
                    setdefault(int(m.groupdict()['rg_media_id']), {})
                continue

            # Ctx State: Standby
            m = p33.match(line)
            if m:
                rg_media_dict.update(m.groupdict())
                continue

            # Protocol ID: 1
            m = p34.match(line)
            if m:
                rg_media_dict.update({'protocol_id': int(m.groupdict()['protocol_id'])})
                continue

            # Media type: Default
            m = p35.match(line)
            if m:
                rg_media_dict.update({'media_type': m.groupdict()['media_type']})
                continue

            # Control Interface: Port-channel10.100
            m = p36.match(line)
            if m:
                rg_media_dict.update({'ctrl_interface': m.groupdict()['control_interface']})
                continue

            # Current Hello timer: 3000
            m = p37.match(line)
            if m:
                timer_dict = rg_media_dict.setdefault('timers', {})
                timer_dict.update({'current_hello_timer': int(m.groupdict()['current_hello_timer'])})
                continue

            # Configured Hello timer: 3000, Hold timer: 9000
            m = p38.match(line)
            if m:
                timer_dict.update({'configured_hello_timer': int(m.groupdict()['conf_hello_timer']),
                                   'hold_timer': int(m.groupdict()['hold_timer'])})
                continue

            # Peer Hello timer: 3000, Peer Hold timer: 9000
            m = p39.match(line)
            if m:
                timer_dict.update({'peer_hello_timer': int(m.groupdict()['peer_hello_timer']),
                                   'peer_hold_timer': int(m.groupdict()['peer_hold_timer'])})
                continue

            # Stats:
            m = p40.match(line)
            if m:
                stats_dict = rg_media_dict.setdefault('stats', {})
                continue

            # Pkts 144780, Bytes 8976360, HA Seq 0, Seq Number 144780, Pkt Loss 0
            m = p41.match(line)
            if m:
                if not recorded_stats:
                    stats_dict.update(
                        {
                            'pkts': int(m.groupdict()['pkts']),
                            'bytes': int(m.groupdict()['bytes']),
                            'ha_seq': int(m.groupdict()['ha_seq']),
                            'seq_number': int(m.groupdict()['seq_number']),
                            'pkt_loss': int(m.groupdict()['pkt_loss'])
                        })
                    recorded_stats = True
                elif recorded_stats:
                    media_active_peer.update(
                        {
                            'pkts': int(m.groupdict()['pkts']),
                            'bytes': int(m.groupdict()['bytes']),
                            'ha_seq': int(m.groupdict()['ha_seq']),
                            'seq_number': int(m.groupdict()['seq_number']),
                            'pkt_loss': int(m.groupdict()['pkt_loss'])
                        })
                    recorded_stats = False

                continue

            # Authentication not configured
            m = p42.match(line)
            if m:
                stats_dict.update({'authentication': m.groupdict()['auth_status']})
                continue

            # Authentication Failure: 0
            m = p43.match(line)
            if m:
                stats_dict.update({'authentication_failures': int(m.groupdict()['auth_failure'])})
                continue

            # Reload Peer: TX 0, RX 0
            m = p44.match(line)
            if m:
                stats_dict.update({
                    'reload_peer': {
                        'tx': int(m.groupdict()['tx']),
                        'rx': int(m.groupdict()['rx'])
                    }
                })
                continue

            # Resign: TX 0, RX 0
            m = p45.match(line)
            if m:
                stats_dict.update({
                    'resign': {
                        'tx': int(m.groupdict()['tx']),
                        'rx': int(m.groupdict()['rx'])
                    }
                })
                continue

            # Active Peer: Present. Hold Timer: 9000
            m = p46.match(line)
            if m:
                media_active_peer = rg_media_dict.setdefault('active_peer', {})
                media_active_peer.update({'status': m.groupdict()['active_peer'],
                                          'hold_timer': int(m.groupdict()['hold_timer'])})
                continue

        return ret_dict
