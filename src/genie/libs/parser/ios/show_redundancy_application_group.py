# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowRedundancyApplicationGroupSchema(MetaParser):
    """
    Schema for show redundancy application group {group_id} show redundancy application group all
    """

    schema = {
        Optional('fault_states_group'): {
            Any(): {  # group id
                Optional('runtime_priority'): int,
                Optional('rg_faults_rg_state'): str,
                Optional('switchovers_from_faults'): int,
                Optional('down/up_state_changes_from_faults'): int
            }
        },
        'group_id': {
            Any(): {  # group id
                'group_name': str,
                'administrative_state': str,
                'aggregate_operational_state': str,
                'my_role': str,
                'peer_role': str,
                'peer_presence': str,
                'peer_comm': str,
                'peer_prgression_started': str,
                'rf_domain': {  # domain name
                    'rf_state': str,
                    'peer_rf_state': str
                },
                Optional('rg_protocol'): {
                    Any(): {  # group id
                        'role': str,
                        'negotiation': str,
                        'priority': int,
                        'protocol_state': str,
                        'ctrl_interfaces_state': str,
                        'active_peer': {
                            Optional('local'): str,
                            Optional('address'): str,
                            Optional('priority'): int,
                            Optional('interface'): str
                        },
                        'standby_peer': {
                            Optional('local'): str,
                            Optional('address'): str,
                            Optional('priority'): int,
                            Optional('interface'): str
                        },
                        'log_counters': {
                            'role_change_to_active': int,
                            'role_change_to_standby': int,
                            'disable_events': {
                                'rg_down_state': int,
                                'rg_shut': int
                            },
                            'ctrl_interface_events': {
                                'up': int,
                                'down': int,
                                'admin_down': int
                            },
                            'reload_events': {
                                'local_request': int,
                                'peer_request': int
                            }
                        }
                    },
                    Optional('rg_media_context'): {
                        Any(): {  # group id
                            'ctx_state': str,
                            'protocol_id': int,
                            'media_type': str,
                            'ctrl_interface': str,
                            'timers': {
                                'current_hello_timer': int,
                                'configured_hello_timer': int,
                                'hold_timer': int,
                                'peer_hello_timer': int,
                                'peer_hold_timer': int
                            },
                            'stats': {
                                'pkts': int,
                                'bytes': int,
                                'ha_seq': int,
                                'seq_number': int,
                                'packet_loss': int,
                                'authentication': str,
                                'authentication_failures': int,
                                'reload_peer': {
                                    'tx': int,
                                    'rx': int
                                },
                                'resign': {
                                    'tx': int,
                                    'rx': int
                                }
                            },
                            'active_peer': {
                                'status': str,
                                'hold_timer': int,
                                'pkts': int,
                                'bytes': int,
                                'ha_seq': int,
                                'seq_number': int,
                                'packet_loss': int
                            }
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
        p1 = re.compile(r'^Faults +states +Group +(?P<fault_group_id>\w+) +info+\:')

        # Runtime priority: [200]
        p2 = re.compile(r'^Runtime priority: +\[(?P<runtime_priority>(\d+))]$')

        # RG Faults RG State: Up
        p3 = re.compile(r'^RG Faults RG State\: +(?P<rg_fault_state>\w+)$/gm')

        # Total # of switchovers due to faults:           0
        p4 = re.compile(r'^Total # of switchovers due to faults: +(?P<fault_switchovers>\d+)$/gm')

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
        p19 = re.compile(r'^Role\: +(?P<role>[\w-]+)$')

        # Negotiation: Enabled
        p20 = re.compile(r'^Negotiation\: +(?P<negotiation>[\w]+)$')

        # Priority: 200
        p21 = re.compile(r'^Priority\: +(?P<priority>[\d]+)$')

        # Protocol state: Standby-hot
        p22 = re.compile(r'^Protocol state\: +(?P<protocol_state>[\w-]+)$')

        # Ctrl Intf(s) state: Up
        p23 = re.compile(r'^Ctrl Intf\(s\)\ state: +(?P<ctrl_intf_state>[\w-]+)$')

        # Active Peer: address 9.1.1.1, priority 200, intf Po10.100
        # Active Peer: Local
        p24 = re.compile(r'^Active Peer\: +((?P<local>Local$)|address +(?P<address>\S+), '
                         r'+priority +(?P<priority>\d+), +intf +(?P<intf>\S+)$)')

        # Standby Peer: address 9.1.1.1, priority 200, intf Po10.100
        # Standby Peer: Local
        p25 = re.compile(r'^Standby Peer\: +((?P<local>Local$)|address +(?P<address>\S+), '
                         r'+priority +(?P<priority>\d+), +intf +(?P<intf>\S+)$)')

        # Log counters:
        p26 = re.compile(r'\s*Log+\s+counters+\:')

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
        p33 = re.compile(r'^Ctx State\: +(?P<ctx_state>[\w-]+)$')

        # Protocol ID: 1
        p34 = re.compile(r'^Protocol +ID\: +(?P<protocol_id>\d+)$')

        # Media type: Default
        p35 = re.compile(r'^Media type\: +(?P<media_type>\w+)$')

        # Control Interface: Port-channel10.100
        p36 = re.compile(r'^Control Interface\: +(?P<control_interface>\S+)$')

        # Current Hello timer: 3000
        p37 = re.compile(r'^Current Hello timer\: +(?P<current_hello_timer>\d+)$')

        # Configured Hello timer: 3000, Hold timer: 9000
        p38 = re.compile(r'^Configured Hello timer\: +(?P<conf_hello_timer>\d+), +Hold timer\: +(?P<hold_timer>\d+)$')

        # Peer Hello timer: 3000, Peer Hold timer: 9000
        p39 = re.compile(r'^Peer Hello timer\: +(?P<peer_hello_timer>\d+), '
                         r'+Peer Hold timer\: +(?P<peer_hold_timer>\d+)$')

        # Stats:
        p40 = re.compile(r'\s*Stats+\:')

        # Pkts 144780, Bytes 8976360, HA Seq 0, Seq Number 144780, Pkt Loss 0
        p41 = re.compile(r'^Pkts +(?P<pkts>\d+), +Bytes +(?P<bytes>\d+), +HA Seq +(?P<ha_seq>\d+), '
                         r'+Seq Number +(?P<seq_number>\d+), Pkt Loss +(?P<pkt_loss>\d+)$')

        # Authentication not configured
        p42 = re.compile(r'^Authentication +(?P<auth_status>configured|not configured)$')

        # Authentication Failure: 0
        p43 = re.compile(r'^Authentication Failure\: +(?P<auth_failure>[\d]+)$')

        # Reload Peer: TX 0, RX 0
        p44 = re.compile(r'^Reload Peer\: +TX +(?P<tx>\d+), +RX +(?P<rx>\d+)$')

        # Resign: TX 0, RX 0
        p45 = re.compile(r'^Resign\: +TX +(?P<tx>\d+), +RX +(?P<rx>\d+)$')

        # Active Peer: Present. Hold Timer: 9000
        p46 = re.compile(r'^Active Peer\: +(?P<active_peer>\S+)\. +Hold Timer\: +(?P<hold_timer>\d+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            pass

        return ret_dict
