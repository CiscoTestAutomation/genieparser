"""
show_subscriber.py


IOSXE parsers for the following show commands:

    * 'show subscriber session'
    * 'show subscriber lite-session'
    * 'show subscriber statistics'
    * show subscriber session detailed
    * show subscriber session uid <uid> detailed
    * show subscriber session feature l4redirect
    * show subscriber session uid <uid> feature l4redirect
    * show subscriber session feature access-list
    * show subscriber session uid <uid> feature access-list
    * show subscriber service
    * 'show subscriber default-session'
"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf, Optional, Or, Schema, Use
from genie.libs.parser.utils.common import Common

class ShowSubscriberSessionSchema(MetaParser):

    """Schema for show subscriber session"""

    schema = {
        Optional('total_sessions'): int,
        Optional('no_active_session'): bool,
        Optional('uniq_ID'): {
            Any(): {
                Optional('interface'): str,
                Optional('state'): str,
                Optional('service'): str,
                Optional('identifier'): str,
            }
        }
    }

# ==============================
# Parser for 'show subscriber session'
# ==============================

# The parser class inherits from the schema class
class ShowSubscriberSession(ShowSubscriberSessionSchema):

    ''' Parser for "show subscriber session"'''

    cli_command = 'show subscriber session'

    # Defines a function to run the cli_command
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # Current Subscriber Information: Total sessions 1
        p1 = re.compile(r'^Current\s+Subscriber\s+Information:\s+Total\s+sessions\s+(?P<total_sessions>\d+)')

        # Uniq ID Interface    State    Service     Up-time  TC Ct. Identifier
        # 5476    Vi2.1        authen   Lterm       00:21:04 0      user1@airtel.com
        p2 = re.compile(r'^(?P<uniq_ID>(\d+))\s+(?P<interface>(PPPoE|Vi\d+\.\d+))\s+(?P<state>(authen|unauthen))\s+(?P<service>(Lterm|Fwd))\s+(\d+\:\d+\:\d+)\s+\d+\s+(?P<identifier>(\S+$))')

        # %No active Subscriber Sessions
        p3 = re.compile(r'^\%(?P<no_active_session>No\s+active\s+Subscriber\s+Sessions)')

        for line in output.splitlines():
            line = line.strip()

            # Current Subscriber Information: Total sessions 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['total_sessions'] = int(group['total_sessions'])
                continue

            # 5476    Vi2.1        authen   Lterm       00:21:04 0      user1@airtel.com
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('uniq_ID', {})
                parsed_dict['uniq_ID'].setdefault(group['uniq_ID'], {})
                parsed_dict['uniq_ID'][group['uniq_ID']]['interface'] = group['interface']
                parsed_dict['uniq_ID'][group['uniq_ID']]['state'] = group['state']
                parsed_dict['uniq_ID'][group['uniq_ID']]['service'] = group['service']
                parsed_dict['uniq_ID'][group['uniq_ID']]['identifier'] = group['identifier']
                continue

            # %No active Subscriber Sessions
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['no_active_session'] = True
                continue

        return parsed_dict

class ShowSubscriberLiteSessionSchema(MetaParser):

    """Schema for show subscriber lite-session"""

    schema = {
        Optional('total_sessions'): int,
        Optional('no_lite_session'): int,
        Optional('lite_sessions'): {
            Any(): {
                Optional('src_ip'): str,
                Optional('vrf'): str,
                Optional('s_vrf'): str,
                Optional('interface'): str,
                Optional('pbhk'): str
            }
        }
    }

# =========================================#
# Parser for 'show subscriber lite session'#
# =========================================#

class ShowSubscriberLiteSession(ShowSubscriberLiteSessionSchema):

    ''' Parser for "show subscriber lite-session"'''

    cli_command = 'show subscriber lite-session'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # Total lite sessions up: 1
        p1 = re.compile(r'^Total\s+lite\s+sessions\s+up\: +(?P<total_sessions>(\d+))')

        # Src-IP       VRF      S-VRF   Up-time(sec) Interface    PBHK
        # 100.0.0.10   Default  Default  34          Te1/0/3.100  0.0.0.0:0

        p2 = re.compile(r'^(?P<src_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<vrf>\w+)\s+(?P<s_vrf>\w+)\s+\d+\s+(?P<interface>[a-zA-Z0-9/\.]+)\s+(?P<pbhk>\d+\.\d+\.\d+\.\d+\:\d+)')

        # # Total lite sessions up: 0
        p3 = re.compile(r'^Total\s+lite\s+sessions\s+up\: +(?P<no_lite_session>(\d+))')

        counter = 1

        for line in output.splitlines():
            line = line.strip()

            # Total lite sessions up: 1
            m = p1.match(line)

            if m:
                group = m.groupdict()
                parsed_dict['total_sessions'] = int(group['total_sessions'])
                continue

            # 100.0.0.10   Default  Default  34          Te1/0/3.100  0.0.0.0:0
            m = p2.match(line)

            if m:
                group = m.groupdict()
                parsed_dict.setdefault('lite_sessions', {})
                parsed_dict['lite_sessions'].setdefault(counter, {})
                parsed_dict['lite_sessions'][counter]['src_ip'] = group['src_ip']
                parsed_dict['lite_sessions'][counter]['vrf'] = group['vrf']
                parsed_dict['lite_sessions'][counter]['s_vrf'] = group['s_vrf']
                parsed_dict['lite_sessions'][counter]['interface'] = group['interface']
                parsed_dict['lite_sessions'][counter]['pbhk'] = group['pbhk']
                counter += 1
                continue

            # # Total lite sessions up: 0
            m = p3.match(line)

            if m:
                group = m.groupdict()
                parsed_dict['no_lite_session'] = int(group['no_lite_session'])
                continue

        return parsed_dict

class ShowSubscriberStatisticsSchema(MetaParser):

    """Schema for show subscriber statistics"""

    schema = {

        'subscriber_statistics': {
            'sessions_currently_up': int,
            'sessions_currently_pending': int,
            'sessions_currently_authenticated': int,
            'sessions_currently_unauthenticated': int,
            'highest_number_of_sessions': int,
            'mean_up_time_duration_session': str,
            'number_of_sessions_up_so_far': int,
            'mean_call_rate_per_minute': int,
            'mean_call_rate_per_hour': int,
            'number_of_calls_in_last_one_hour': int,
            'number_of_sessions_failed': int
        },

        Optional('lite_session_statistics'): {
            Optional('lite_sessions_currently_up'): int,
            Optional('lite_number_of_sessions_up_so_far'): int,
            Optional('full_session'): int,
            Optional('conversion_in_progress'): int,
            Optional('failed_to_convert'): int,
            Optional('account_logons_failed'): int,
            Optional('mean_call_rate_per_minute'): int,
            Optional('mean_call_rate_per_hour'): int,
            Optional('number_of_sessions_failed'): int,
            Optional('pbhk_zero'): int,
            Optional('not_in_connected_state'): int
        },

        'current_flow_statistics': {
            'number_of_flows_currently_up': int,
            'highest_number_of_flows_ever_up': int,
            'mean_up_time_duration_flow': str,
            'number_of_flows_failed': int,
            'flows_up_so_far': int
        },
        Optional('access_type_based_session_count'): {
            Optional('ip_interface'): int,
            Optional('ppp'): int,
            Optional('pppoe'): int,
            Optional('vpdn'): int,
        },

        Optional('ip_dhcp_session_type_count'): {
            Optional('dhcpv4'): int
        },

        Optional('feature_installation_count'): {
            Any(): {
                Optional('feature_name'): str,
                Optional('none'): int,
                Optional('direction_inbound'): int,
                Optional('direction_outbound'): int
            },
        },

        Optional('switch_id_cleanup_statistics'): {
            Optional('invalid_smgr_handle'): int,
            Optional('invalid_policy_handle'): int,
            Optional('invalid_lterm_handle'): int,
            Optional('invalid_sip_handle'): int
        },
        Optional('lterm_session_delete_errors'): {
            Optional('l2hw_switch'): int
        },
        Optional('shdbs_in_use'): int,
        Optional('shdbs_allocated'): int,
        Optional('shdbs_freed'): int,
        Optional('shdb_handle_with_client_counts'): {
            Any(): int,
        },
    }

# ===============================
# Parser for 'show subscriber statistics'
# ===============================

# The parser class inherits from the schema class
class ShowSubscriberStatistics(ShowSubscriberStatisticsSchema):

    ''' Parser for "show subscriber statistics"'''

    cli_command = 'show subscriber statistics'

    # Defines a function to run the cli_command
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Initializes the Python dictionary variable
        parsed_dict = {}
        installation_count = 1

        # Current Subscriber Statistics:
        # Number of sessions currently up: 2
        p1 = re.compile(r'^Number\s+of\s+sessions\s+currently\s+up\:\s+(?P<sessions_currently_up>\d+)$')

        # Number of sessions currently pending: 0
        p2 = re.compile(r'^Number\s+of\s+sessions\s+currently\s+pending\:\s+(?P<sessions_currently_pending>\d+)$')

        # Number of sessions currently authenticated: 0
        p3 = re.compile(r'^Number\s+of\s+sessions\s+currently\s+authenticated\:\s+(?P<sessions_currently_authenticated>\d+)$')

        # Number of sessions currently unauthenticated: 2
        p4 = re.compile(r'^Number\s+of\s+sessions\s+currently\s+unauthenticated\:\s+(?P<sessions_currently_unauthenticated>\d+)$')

        # Highest number of sessions ever up at one time: 31998
        p5 = re.compile(r'^Highest\s+number\s+of\s+sessions\s+ever\s+up\s+at\s+one\s+time\:\s+(?P<highest_number_of_sessions>\d+)$')

        # Mean up-time duration of sessions: 00:14:58
        p6 = re.compile(r'^Mean\s+up\-time\s+duration\s+of\s+sessions\:\s+(?P<mean_up_time_duration_session>(\d+\:\d+\:\d+))$')

        # Total number of sessions up so far: 64132
        p7 = re.compile(r'^Total\s+number\s+of\s+sessions\s+up\s+so\s+far\:\s+(?P<number_of_sessions_up_so_far>\d+)$')

        # Mean call rate per minute: 203, per hour: 12826
        p8 = re.compile(r'^Mean\s+call\s+rate\s+per\s+minute\:\s+(?P<mean_call_rate_per_minute>\d+),\s+per\s+hour\:\s+(?P<mean_call_rate_per_hour>\d+)$')

        # Number of calls in last one hour: 4
        p9 = re.compile(r'^Number\s+of\s+calls\s+in\s+last\s+one\s+hour\:\s+(?P<number_of_calls_in_last_one_hour>\d+)$')

        # Number of sessions failed to come up: 32045
        p10 = re.compile(r'^Number\s+of\s+sessions\s+failed\s+to\s+come\s+up\:\s+(?P<number_of_sessions_failed>\d+)$')

        # Current Lite Session Statistics:
        # Number of lite sessions currently up: 0
        p11 = re.compile(r'^Number\s+of\s+lite\s+sessions\s+currently\s+up\:\s+(?P<lite_sessions_currently_up>\d+)$')

        # Number of lite sessions up so far: 32024
        p12 = re.compile(r'^Number\s+of\s+lite\s+sessions\s+up\s+so\s+far\:\s+(?P<lite_number_of_sessions_up_so_far>\d+)$')

        # Number of lite sessions converted to full session: 32014
        p13 = re.compile(r'^Number\s+of\s+lite\s+sessions\s+converted\s+to\s+full\s+session\:\s+(?P<full_session>\d+)$')

        # Number of lite sessions conversion in progress: 0
        p14 = re.compile(r'^Number\s+of\s+lite\s+sessions\s+conversion\s+in\s+progress\:\s+(?P<conversion_in_progress>\d+)$')

        # Number of lite sessions failed to convert to dedicated sessions: 5
        p15 = re.compile(r'^Number\s+of\s+lite\s+sessions\s+failed\s+to\s+convert\s+to\s+dedicated\s+sessions\:\s+(?P<failed_to_convert>\d+)$')

        # Number of account logons failed to find lite sessions: 0
        p16 = re.compile(r'^Number\s+of\s+account\s+logons\s+failed\s+to\s+find\s+lite\s+sessions\:\s+(?P<account_logons_failed>\d+)$')

        # Mean call rate per minute: 101, per hour: 6404
        p17 = re.compile(r'^Mean\s+call\s+rate\s+per\s+minute\:\s+(?P<mean_call_rate_per_minute>\d+),\s+per\s+hour\:\s+(?P<mean_call_rate_per_hour>\d+)$')

        # Number of lite session failed to come up: 0
        p18 = re.compile(r'^Number\s+of\s+lite\s+session\s+failed\s+to\s+come\s+up\:\s+(?P<number_of_sessions_failed>\d+)$')

        #  PBHK zero: 0
        p19 = re.compile(r'^PBHK\s+zero\:\s+(?P<pbhk_zero>\d+)$')

        #  Default Session not in Connected State 0
        p20 = re.compile(r'^\s*Default\s+Session\s+not\s+in\s+Connected\s+State\s+(?P<not_in_connected_state>\d+)$')

        # Current Flow Statistics:
        # Number of flows currently up: 32
        p21 = re.compile(r'^Number\s+of\s+flows\s+currently\s+up\:\s+(?P<number_of_flows_currently_up>\d+)$')

        # Highest number of flows ever up at one time: 71855
        p22 = re.compile(r'^Highest\s+number\s+of\s+flows\s+ever\s+up\s+at\s+one\s+time\:\s+(?P<highest_number_of_flows_ever_up>\d+)$')

        # Mean up-time duration of flows: 00:13:19
        p23 = re.compile(r'^Mean\s+up\-time\s+duration\s+of\s+flows\:\s+(?P<mean_up_time_duration_flow>(\d+\:\d+\:\d+))$')

        # Number of flows failed to come up: 0
        p24 = re.compile(r'^Number\s+of\s+flows\s+failed\s+to\s+come\s+up\:\s+(?P<number_of_flows_failed>\d+)$')

        # Total number of flows up so far: 160306
        p25 = re.compile(r'^Total\s+number\s+of\s+flows\s+up\s+so\s+far:\s+(?P<flows_up_so_far>\d+)$')

        # Access type based session count:
        # IP-Interface sessions = 2
        p26 = re.compile(r'^(?P<access_type_sessions>(IP\-Interface|PPP|PPPoE|VPDN))\s+sessions\s+\=\s+(?P<access_type_sessions_count>\d+)$')

        # IP/DHCP session type count:
        # DHCPv4 sessions = 13271
        p27 = re.compile(r'^(?P<sessions>(DHCPv4))\s+sessions\s*\=\s*(?P<session_type_count>\d+)$')

        # Feature Installation Count:
        #                                     Direction
        # Feature Name              None       Inbound    Outbound
        # L4 Redirect               0          4          2
        p28 = re.compile(r'^(?P<feature_name>(\w+|\w+\s\w+|\w+\s\w+\s\w+))\s+(?P<none>\d+)\s+(?P<direction_inbound>\d+)\s+(?P<direction_outbound>\d+)$')

        # Switch Id Cleanup Statistics:
        # Number of sessions having invalid SIP handle: 0
        p29 = re.compile(r'^Number\s+of\s+sessions\s+having\s+invalid\s+SMGR\s+handle\:\s+(?P<invalid_smgr_handle>\d+)$')

        # Number of sessions having invalid policy handle: 0
        p30 = re.compile(r'^Number\s+of\s+sessions\s+having\s+invalid\s+policy\s+handle\:\s+(?P<invalid_policy_handle>\d+)$')

        # Number of sessions having invalid LTERM handle: 0
        p31 = re.compile(r'^Number\s+of\s+sessions\s+having\s+invalid\s+LTERM\s+handle\:\s+(?P<invalid_lterm_handle>\d+)$')

        # Number of sessions having invalid SMGR handle: 0
        p32 = re.compile(r'^Number\s+of\s+sessions\s+having\s+invalid\s+SIP\s+handle\:\s+(?P<invalid_sip_handle>\d+)$')

        # Lterm session delete errors:
        # L2hw Switch:   17
        p33 = re.compile(r'^L2hw\s+Switch:\s+(?P<l2hw_switch>\d+)$')

        # SHDBs in use    : 8
        p34 = re.compile(r'^SHDBs\s+in\s+use\s+\:\s+(?P<shdbs_in_use>\d+)$')

        # SHDBs allocated : 64132
        p35 = re.compile(r'^SHDBs\s+allocated\s+\:\s+(?P<shdbs_allocated>\d+)$')

        # SHDBs freed     : 64124
        p36 = re.compile(r'^SHDBs\s+freed\s+\:\s+(?P<shdbs_freed>\d+)$')

        # SHDB handles associated with each client type

        # Client Name     Count
        # ===========    =======
        # LTerm          2
        # AAA            2
        # CCM            2
        # SSS FM         8
        # IPSUB          0
        p37 = re.compile(r'^(?P<client_name>(\w+|\w+\s{0,1}\w*))\s+(?P<count>\d+)$')

        mean_call_count = 0

        for line in output.splitlines():
            line = line.strip()

            parsed_dict.setdefault('subscriber_statistics', {})
            # Number of sessions currently up: 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['sessions_currently_up'] = int(group['sessions_currently_up'])
                continue

            # Number of sessions currently pending: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['sessions_currently_pending'] = int(group['sessions_currently_pending'])
                continue

            # Number of sessions currently authenticated: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['sessions_currently_authenticated'] = int(group['sessions_currently_authenticated'])
                continue

            # Number of sessions currently unauthenticated: 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['sessions_currently_unauthenticated'] = int(group['sessions_currently_unauthenticated'])
                continue

            # Highest number of sessions ever up at one time: 31998
            m = p5.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['highest_number_of_sessions'] = int(group['highest_number_of_sessions'])
                continue

            # Mean up-time duration of sessions: 00:14:58
            m = p6.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['mean_up_time_duration_session'] = group['mean_up_time_duration_session']
                continue

            # Total number of sessions up so far: 64132
            m = p7.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['number_of_sessions_up_so_far'] = int(group['number_of_sessions_up_so_far'])
                continue

            # Mean call rate per minute: 203, per hour: 12826
            m = p8.match(line)
            if m and mean_call_count == 0:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['mean_call_rate_per_minute'] = int(group['mean_call_rate_per_minute'])
                parsed_dict['subscriber_statistics']['mean_call_rate_per_hour'] = int(group['mean_call_rate_per_hour'])
                mean_call_count=mean_call_count+1
                continue

            # Number of calls in last one hour: 4
            m = p9.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['number_of_calls_in_last_one_hour'] = int(group['number_of_calls_in_last_one_hour'])
                continue

            # Number of sessions failed to come up: 32045
            m = p10.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['subscriber_statistics']['number_of_sessions_failed'] = int(group['number_of_sessions_failed'])
                continue

            # Number of lite sessions currently up: 0
            parsed_dict.setdefault('lite_session_statistics', {})
            m = p11.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['lite_sessions_currently_up'] = int(group['lite_sessions_currently_up'])
                continue

            # Number of lite sessions up so far: 32024
            m = p12.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['lite_number_of_sessions_up_so_far'] = int(group['lite_number_of_sessions_up_so_far'])
                continue

            # Number of lite sessions converted to full session: 32014
            m = p13.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['full_session'] = int(group['full_session'])
                continue

            # Number of lite sessions conversion in progress: 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['conversion_in_progress'] = int(group['conversion_in_progress'])
                continue

            # Number of lite sessions failed to convert to dedicated sessions: 5
            m = p15.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['failed_to_convert'] = int(group['failed_to_convert'])
                continue

            # Number of account logons failed to find lite sessions: 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['account_logons_failed'] = int(group['account_logons_failed'])
                continue

            # Mean call rate per minute: 101, per hour: 6404
            m = p17.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['mean_call_rate_per_minute'] = int(group['mean_call_rate_per_minute'])
                parsed_dict['lite_session_statistics']['mean_call_rate_per_hour'] = int(group['mean_call_rate_per_hour'])
                continue

            # Number of lite session failed to come up: 0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['number_of_sessions_failed'] = int(group['number_of_sessions_failed'])
                continue

            #  PBHK zero: 0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['pbhk_zero'] = int(group['pbhk_zero'])
                continue

            #  Default Session not in Connected State 0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lite_session_statistics']['not_in_connected_state'] = int(group['not_in_connected_state'])
                continue

            # Number of flows currently up: 32
            parsed_dict.setdefault('current_flow_statistics', {})
            m = p21.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['current_flow_statistics']['number_of_flows_currently_up'] = int(group['number_of_flows_currently_up'])
                continue

            # Highest number of flows ever up at one time: 71855
            m = p22.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['current_flow_statistics']['highest_number_of_flows_ever_up'] = int(group['highest_number_of_flows_ever_up'])
                continue

            # Mean up-time duration of flows: 00:13:19
            m = p23.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['current_flow_statistics']['mean_up_time_duration_flow'] = group['mean_up_time_duration_flow']
                continue

            # Number of flows failed to come up: 0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['current_flow_statistics']['number_of_flows_failed'] = int(group['number_of_flows_failed'])
                continue

            # Total number of flows up so far: 160306
            m = p25.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['current_flow_statistics']['flows_up_so_far'] = int(group['flows_up_so_far'])
                continue

            # IP-Interface sessions = 2
            parsed_dict.setdefault('access_type_based_session_count', {})
            m = p26.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['access_type_based_session_count'][group['access_type_sessions'].lower().replace("-","_")] = int(group['access_type_sessions_count'])
                continue

            # DHCPv4 sessions = 13271
            parsed_dict.setdefault('ip_dhcp_session_type_count', {})
            m = p27.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['ip_dhcp_session_type_count'][group['sessions'].lower().replace("-","_")] = int(group['session_type_count'])
                continue

            # Feature Name              None       Inbound    Outbound
            # L4 Redirect               0          4          2
            m = p28.match(line)
            if m:
                parsed_dict.setdefault('feature_installation_count', {})
                parsed_dict['feature_installation_count'].setdefault(installation_count, {})
                group = m.groupdict()
                parsed_dict['feature_installation_count'][installation_count]['feature_name'] = group['feature_name']
                parsed_dict['feature_installation_count'][installation_count]['none'] = int(group['none'])
                parsed_dict['feature_installation_count'][installation_count]['direction_inbound'] = int(group['direction_inbound'])
                parsed_dict['feature_installation_count'][installation_count]['direction_outbound'] = int(group['direction_outbound'])
                installation_count += 1
                continue

            # Number of sessions having invalid SIP handle: 0
            parsed_dict.setdefault('switch_id_cleanup_statistics', {})
            m = p29.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['switch_id_cleanup_statistics']['invalid_smgr_handle'] = int(group['invalid_smgr_handle'])
                continue

            # Number of sessions having invalid policy handle: 0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['switch_id_cleanup_statistics']['invalid_policy_handle'] = int(group['invalid_policy_handle'])
                continue

            # Number of sessions having invalid LTERM handle: 0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['switch_id_cleanup_statistics']['invalid_lterm_handle'] = int(group['invalid_lterm_handle'])
                continue

            # Number of sessions having invalid SMGR handle: 0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['switch_id_cleanup_statistics']['invalid_sip_handle'] = int(group['invalid_sip_handle'])
                continue

            # L2hw Switch:   17
            parsed_dict.setdefault('lterm_session_delete_errors', {})
            m = p33.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lterm_session_delete_errors']['l2hw_switch'] = int(group['l2hw_switch'])
                continue

            # SHDBs in use    : 8
            m = p34.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['shdbs_in_use'] = int(group['shdbs_in_use'])
                continue

            # SHDBs allocated : 64132
            m = p35.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['shdbs_allocated'] = int(group['shdbs_allocated'])
                continue

            # SHDBs freed     : 64124
            m = p36.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['shdbs_freed'] = int(group['shdbs_freed'])
                continue

            # Client Name     Count
            # ===========    =======
            # LTerm          2
            # AAA            2
            # CCM            2
            # SSS FM         8
            # IPSUB          0
            m = p37.match(line)
            if m:
                parsed_dict.setdefault('shdb_handle_with_client_counts',{})
                group = m.groupdict()
                parsed_dict['shdb_handle_with_client_counts'][group['client_name'].lower().replace("-","_")] = int(group['count'])
                continue

        return parsed_dict



class ShowSubscriberSessionDetailedSchema(MetaParser):

    schema = {
        "total_sessions": int,
        Optional("sessions"): {
            Any(): {
                "uid": int,
                "type": str,
                "state": str,
                "identity": str,
                Optional("ipv4_address"): str,
                Optional("ipv6_address"): str,
                "session_up_time": str,
                "last_changed": str,
                "switch_id": int,
                Optional("policy_information"): {
                    "context": str,
                    "handle": str,
                    "aaa_id": str,
                    "flow_handle": int,
                    "authentication_status": str,
                    Optional("downloaded_user_profile"): {
                        Optional("excluding_services"): {
                            Optional("service_type"): {
                                "value1": int,
                                "value2": int,
                                "description": str
                            },
                            Optional("prefix"): {
                                "index": int,
                                "value": str
                            }
                        },
                        Optional("including_services"): {
                            Optional("service_type"): {
                                "value1": int,
                                "value2": int,
                                "description": str
                            },
                            Optional("prefix"): {
                                "index": int,
                                "value": str
                            }
                        }
                    },
                    Optional("config_history"): {
                        "access_type": str,
                        "client": str,
                        Optional("policy_event"): str,
                        Optional("profile_name"): str,
                        Optional("references"): int,
                        Optional("profile_attributes"): {
                            Optional("service_type"): {
                                "value1": int,
                                "value2": int,
                                "description": str
                            },
                            Optional("prefix"): {
                                "index": int,
                                "value": str
                            }
                        }
                    },
                    Optional("rules_actions_conditions_executed"): {
                        Optional("subscriber_rule_map"): str,
                        Optional("conditions"): ListOf({
                            "condition": str,
                            "event": str,
                            Optional("actions"): ListOf({
                                "sequence": int,
                                "command": str
                            })
                        })
                    }
                },
                Optional("classifiers"): {
                    Any(): {
                        "direction": str,
                        "packets": int,
                        "bytes": int,
                        "priority": int,
                        "definition": str
                    }
                },
                Optional("template_id"): int,
                Optional("policing"): {
                    int: {
                        "direction": str,
                        "avg_rate": int,
                        "normal_burst": int,
                        "excess_burst": int,
                        "source": str
                    }
                },
                Optional("configuration_sources"): {
                    Any(): {
                        "active_time": str,
                        "aaa_service_id": str,
                        "name": str
                    }
                }
            }
        }
    }


class ShowSubscriberSessionDetailed(ShowSubscriberSessionDetailedSchema):

    cli_command = ["show subscriber session detailed",
                   "show subscriber session uid {uid} detailed"]

    def cli(self, uid=None, output=None):
        if output is None:
            cmd = self.cli_command[0]
            if uid:
                cmd = self.cli_command[1].format(uid=uid)
            output = self.device.execute(cmd)

        ret_dict = {}
        if not output:
            return ret_dict

        current_uid_key = None
        current_session = None
        current_section = None  # 'excluding', 'including', 'config_history', 'rules', 'classifiers', 'config_sources'

        # Current Subscriber Information: Total sessions 1
        p1 = re.compile(r"^Current\s+Subscriber\s+Information:\s+Total\s+sessions\s+(?P<total_sessions>\d+)$")

        # Type: IPv4/IPv6, UID: 915, State: authen, Identity: aaaa.bbbb.cccc
        p2 = re.compile(r"^Type\s*:\s*(?P<type>[^,]+),\s*UID\s*:\s*(?P<uid>\d+),\s*State\s*:\s*(?P<state>[^,]+),\s*Identity\s*:\s*(?P<identity>.+)$")

        # IPv4 Address: 11.11.11.2
        p3 = re.compile(r"^IPv4\s+Address\s*:\s*(?P<ipv4_address>\S+)$")

        # IPv6 Address: 8001::
        p4 = re.compile(r"^IPv6\s+Address\s*:\s*(?P<ipv6_address>\S+)$")

        # Session Up-time: 00:00:18, Last Changed: 00:00:06
        p5 = re.compile(r"^Session\s+Up\-time\s*:\s*(?P<session_up_time>[^,]+),\s*Last\s+Changed\s*:\s*(?P<last_changed>.+)$")

        # Switch-ID: 4717
        p6 = re.compile(r"^Switch\-ID\s*:\s*(?P<switch_id>\d+)$")

        # Policy information:
        p7 = re.compile(r"^Policy\s+information:")

        #   Context 7F2190EB88D0: Handle 1D00041D
        p8 = re.compile(r"^\s*Context\s+(?P<context>\S+)\s*:\s*Handle\s+(?P<handle>\S+)$")

        #   AAA_id 000003A9: Flow_handle 0
        p9 = re.compile(r"^\s*AAA_id\s+(?P<aaa_id>\S+)\s*:\s*Flow_handle\s+(?P<flow_handle>\d+)$")

        #   Authentication status: authen
        p10 = re.compile(r"^\s*Authentication\s+status\s*:\s*(?P<authentication_status>\S+)$")

        #   Downloaded User profile, excluding services:
        p11 = re.compile(r"^\s*Downloaded\s+User\s+profile,\s+excluding\s+services:")

        #     service-type         0   2 [Framed]
        p12 = re.compile(r"^\s{4}service\-type\s+(?P<value1>\d+)\s+(?P<value2>\d+)\s+\[(?P<description>.+)\]$")

        #     prefix               0   00 40 80 01 00 00 00 00 00 00
        p13 = re.compile(r"^\s{4}prefix\s+(?P<index>\d+)\s+(?P<value>.+)$")

        #   Downloaded User profile, including services:
        p14 = re.compile(r"^\s*Downloaded\s+User\s+profile,\s+including\s+services:")

        #   Config history for session (recent to oldest):
        p15 = re.compile(r"^\s*Config\s+history\s+for\s+session\s+\(recent\s+to\s+oldest\):")

        #     Access-type: IP Client: SM
        p16 = re.compile(
            r"^\s{4}Access\-type\s*:\s*(?P<access_type>.+?)\s+Client\s*:\s*(?P<client>.+)$"
        )

        #      Policy event: Service Selection Request
        p17 = re.compile(r"^\s{5,}Policy\s+event\s*:\s*(?P<policy_event>.+)$")

        #       Profile name: aaaa.bbbb.cccc, 2 references
        p18 = re.compile(r"^\s{6,}Profile\s+name\s*:\s*(?P<profile_name>[^,]+),\s*(?P<references>\d+)\s+references$")

        #         service-type         0   2 [Framed]
        p19 = re.compile(r"^\s{8}service\-type\s+(?P<value1>\d+)\s+(?P<value2>\d+)\s+\[(?P<description>.+)\]$")

        #         prefix               0   00 40 80 01 00 00 00 00 00 00
        p20 = re.compile(r"^\s{8}prefix\s+(?P<index>\d+)\s+(?P<value>.+)$")

        #   Rules, actions and conditions executed:
        p21 = re.compile(r"^\s*Rules,\s+actions\s+and\s+conditions\s+executed:")

        #     subscriber rule-map TAL
        p22 = re.compile(r"^\s{4}subscriber\s+rule\-map\s+(?P<rule_map>\S+)$")

        #       condition always event session-start
        p23 = re.compile(r"^\s{6}condition\s+(?P<condition>\S+)\s+event\s+(?P<event>\S+)$")

        #         10 authorize identifier mac-address
        p24 = re.compile(r"^\s{8}(?P<sequence>\d+)\s+(?P<command>.+)$")

        # Classifiers:
        p25 = re.compile(r"^Classifiers:")

        # 0           In    5          542                    0    Match Any
        p26 = re.compile(r"^(?P<class_id>\d+)\s+(?P<direction>\S+)\s+(?P<packets>\d+)\s+(?P<bytes>\d+)\s+(?P<priority>\d+)\s+(?P<definition>.+)$")

        # Template Id : 69
        p27 = re.compile(r"^Template\s+Id\s*:\s*(?P<template_id>\d+)$")

        # Policing:
        p30 = re.compile(r"^Policing:$")

        # Class-id   Dir  Avg. Rate   Normal Burst  Excess Burst Source
        p31 = re.compile(r"^Class-id\s+Dir\s+Avg\.\s*Rate")

        # 50         In   8000        1000          2000         V4DRL
        p32 = re.compile(
            r"^(?P<class_id>\d+)\s+(?P<direction>\S+)\s+(?P<avg_rate>\d+)\s+(?P<normal_burst>\d+)\s+(?P<excess_burst>\d+)\s+(?P<source>\S+)$"
        )

        # Configuration Sources:
        p28 = re.compile(r"^Configuration\s+Sources:")

        # USR   00:00:18     -               Peruser
        p29 = re.compile(r"^(?P<type>[A-Z]+)\s+(?P<active_time>\S+)\s+(?P<aaa_service_id>\S+)\s+(?P<name>.+)$")

        for line in output.splitlines():
            line = line.rstrip()
            if not line:
                continue

            # Current Subscriber Information: Total sessions 1
            m = p1.match(line)
            if m:
                ret_dict["total_sessions"] = int(m.group("total_sessions"))
                continue

            # Type: IPv4/IPv6, UID: 915, State: authen, Identity: aaaa.bbbb.cccc
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sessions = ret_dict.setdefault("sessions", {})
                current_uid_key = group["uid"]
                current_session = sessions.setdefault(current_uid_key, {})
                current_session["type"] = group["type"].strip()
                current_session["uid"] = int(group["uid"])
                current_session["state"] = group["state"].strip()
                current_session["identity"] = group["identity"].strip()
                current_section = None
                continue

            if current_session is None:
                continue

            # IPv4 Address: 11.11.11.2
            m = p3.match(line)
            if m:
                current_session["ipv4_address"] = m.group("ipv4_address")
                continue

            # IPv6 Address: 8001::
            m = p4.match(line)
            if m:
                current_session["ipv6_address"] = m.group("ipv6_address")
                continue

            # Session Up-time: 00:00:18, Last Changed: 00:00:06
            m = p5.match(line)
            if m:
                current_session["session_up_time"] = m.group("session_up_time")
                current_session["last_changed"] = m.group("last_changed")
                continue

            # Switch-ID: 4717
            m = p6.match(line)
            if m:
                current_session["switch_id"] = int(m.group("switch_id"))
                continue

            # Policy information:
            m = p7.match(line)
            if m:
                policy_info = current_session.setdefault("policy_information", {})
                current_section = None
                continue

            #   Context 7F2190EB88D0: Handle 1D00041D
            m = p8.match(line)
            if m:
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                policy_info["context"] = group["context"]
                policy_info["handle"] = group["handle"]
                continue

            #   AAA_id 000003A9: Flow_handle 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                policy_info["aaa_id"] = group["aaa_id"]
                policy_info["flow_handle"] = int(group["flow_handle"])
                continue

            #   Authentication status: authen
            m = p10.match(line)
            if m:
                policy_info = current_session.setdefault("policy_information", {})
                policy_info["authentication_status"] = m.group("authentication_status")
                continue

            #   Downloaded User profile, excluding services:
            m = p11.match(line)
            if m:
                policy_info = current_session.setdefault("policy_information", {})
                dup = policy_info.setdefault("downloaded_user_profile", {})
                dup.setdefault("excluding_services", {})
                current_section = "excluding"
                continue

            #     service-type         0   2 [Framed]
            m = p12.match(line)
            if m and current_section in ("excluding", "including"):
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                dup = policy_info.setdefault("downloaded_user_profile", {})
                target = dup.setdefault(
                    "excluding_services" if current_section == "excluding" else "including_services", {}
                )
                st = target.setdefault("service_type", {})
                st["value1"] = int(group["value1"])
                st["value2"] = int(group["value2"])
                st["description"] = group["description"]
                continue

            #     prefix               0   00 40 80 01 00 00 00 00 00 00
            m = p13.match(line)
            if m and current_section in ("excluding", "including"):
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                dup = policy_info.setdefault("downloaded_user_profile", {})
                target = dup.setdefault(
                    "excluding_services" if current_section == "excluding" else "including_services", {}
                )
                pr = target.setdefault("prefix", {})
                pr["index"] = int(group["index"])
                pr["value"] = group["value"].strip()
                continue

            #   Downloaded User profile, including services:
            m = p14.match(line)
            if m:
                policy_info = current_session.setdefault("policy_information", {})
                dup = policy_info.setdefault("downloaded_user_profile", {})
                dup.setdefault("including_services", {})
                current_section = "including"
                continue

            #   Config history for session (recent to oldest):
            m = p15.match(line)
            if m:
                policy_info = current_session.setdefault("policy_information", {})
                policy_info.setdefault("config_history", {})
                current_section = "config_history"
                continue

            #     Access-type: IP Client: SM
            m = p16.match(line)
            if m and current_section == "config_history":
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                ch = policy_info.setdefault("config_history", {})
                ch["access_type"] = group["access_type"].strip()
                ch["client"] = group["client"].strip()
                continue

            #      Policy event: Service Selection Request
            m = p17.match(line)
            if m and current_section == "config_history":
                policy_info = current_session.setdefault("policy_information", {})
                ch = policy_info.setdefault("config_history", {})
                ch["policy_event"] = m.group("policy_event")
                continue

            #       Profile name: aaaa.bbbb.cccc, 2 references
            m = p18.match(line)
            if m and current_section == "config_history":
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                ch = policy_info.setdefault("config_history", {})
                ch["profile_name"] = group["profile_name"].strip()
                ch["references"] = int(group["references"])
                continue

            #         service-type         0   2 [Framed]
            m = p19.match(line)
            if m and current_section == "config_history":
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                ch = policy_info.setdefault("config_history", {})
                pa = ch.setdefault("profile_attributes", {})
                st = pa.setdefault("service_type", {})
                st["value1"] = int(group["value1"])
                st["value2"] = int(group["value2"])
                st["description"] = group["description"]
                continue

            #         prefix               0   00 40 80 01 00 00 00 00 00 00
            m = p20.match(line)
            if m and current_section == "config_history":
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                ch = policy_info.setdefault("config_history", {})
                pa = ch.setdefault("profile_attributes", {})
                pr = pa.setdefault("prefix", {})
                pr["index"] = int(group["index"])
                pr["value"] = group["value"].strip()
                continue

            #   Rules, actions and conditions executed:
            m = p21.match(line)
            if m:
                policy_info = current_session.setdefault("policy_information", {})
                rac = policy_info.setdefault("rules_actions_conditions_executed", {})
                rac.setdefault("conditions", [])
                current_section = "rules"
                continue

            #     subscriber rule-map TAL
            m = p22.match(line)
            if m and current_section == "rules":
                policy_info = current_session.setdefault("policy_information", {})
                rac = policy_info.setdefault("rules_actions_conditions_executed", {})
                rac["subscriber_rule_map"] = m.group("rule_map")
                continue

            #       condition always event session-start
            m = p23.match(line)
            if m and current_section == "rules":
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                rac = policy_info.setdefault("rules_actions_conditions_executed", {})
                conditions = rac.setdefault("conditions", [])
                cond_entry = {"condition": group["condition"], "event": group["event"], "actions": []}
                conditions.append(cond_entry)
                continue

            #         10 authorize identifier mac-address
            m = p24.match(line)
            if m and current_section == "rules":
                group = m.groupdict()
                policy_info = current_session.setdefault("policy_information", {})
                rac = policy_info.setdefault("rules_actions_conditions_executed", {})
                conditions = rac.setdefault("conditions", [])
                if conditions:
                    action = {"sequence": int(group["sequence"]), "command": group["command"]}
                    # Ensure actions list exists
                    if "actions" not in conditions[-1]:
                        conditions[-1]["actions"] = []
                    conditions[-1]["actions"].append(action)
                continue

            # Classifiers:
            m = p25.match(line)
            if m:
                current_section = "classifiers"
                continue

            # 0           In    5          542                    0    Match Any
            m = p26.match(line)
            if m and current_section == "classifiers":
                group = m.groupdict()
                classifiers = current_session.setdefault("classifiers", {})
                class_id = int(group["class_id"])
                entry = classifiers.setdefault(class_id, {})
                entry["direction"] = group["direction"]
                entry["packets"] = int(group["packets"])
                entry["bytes"] = int(group["bytes"])
                entry["priority"] = int(group["priority"])
                entry["definition"] = group["definition"].strip()
                continue

            # Template Id : 69
            m = p27.match(line)
            if m:
                current_session["template_id"] = int(m.group("template_id"))
                continue

            # Policing:
            m = p30.match(line)
            if m:
                current_section = "policing"
                continue

            # Class-id   Dir  Avg. Rate   Normal Burst  Excess Burst Source
            m = p31.match(line)
            if m:
                continue

            # 50         In   8000        1000          2000         V4DRL
            m = p32.match(line)
            if m and current_section == "policing":
                group = m.groupdict()
                policing = current_session.setdefault("policing", {})
                class_id = int(group["class_id"])
                entry = policing.setdefault(class_id, {})
                entry["direction"] = group["direction"]
                entry["avg_rate"] = int(group["avg_rate"])
                entry["normal_burst"] = int(group["normal_burst"])
                entry["excess_burst"] = int(group["excess_burst"])
                entry["source"] = group["source"]
                continue

            # Configuration Sources:
            m = p28.match(line)
            if m:
                current_section = "config_sources"
                continue

            # USR   00:00:18     -               Peruser
            m = p29.match(line)
            if m and current_section == "config_sources":
                group = m.groupdict()
                cfg = current_session.setdefault("configuration_sources", {})
                entry = cfg.setdefault(group["type"], {})
                entry["active_time"] = group["active_time"]
                entry["aaa_service_id"] = group["aaa_service_id"]
                entry["name"] = group["name"].strip()
                continue

        return ret_dict


class ShowSubscriberSessionDetailSchema(MetaParser):

    schema = {
        'sessions': {
            Any(): {
                'uid': int,
                Optional('type'): str,
                Optional('state'): str,
                Optional('identity'): str,
                Optional('ipv4_address'): str,
                Optional('session_uptime'): str,
                Optional('last_changed'): str,
                Optional('interface'): str,
                Optional('switch_id'): int,
                Optional('policy_information'): {
                    Optional('context'): str,
                    Optional('handle'): str,
                    Optional('aaa_id'): str,
                    Optional('flow_handle'): int,
                    Optional('authentication_status'): str,
                    Optional('downloaded_user_profile'): {
                        Optional('excluding_services'): ListOf(dict),
                        Optional('including_services'): ListOf(dict),
                    }
                },
                Optional('config_history'): ListOf(dict),
                Optional('active_services'): ListOf(dict),
                Optional('rules_actions_conditions'): ListOf(dict),
                Optional('classifiers'): {
                    Any(): {
                        'direction': str,
                        'packets': int,
                        'bytes': int,
                        'priority': int,
                        'definition': str
                    }
                },
                Optional('features'): dict,
                Optional('qos_policy_map'): {
                    Any(): {
                        'direction': str,
                        'policy_name': str,
                        'source': str
                    }
                },
                Optional('accounting'): {
                    Any(): {
                        'direction': str,
                        'packets': int,
                        'bytes': int,
                        'source': str
                    }
                },
                Optional('configuration_sources'): ListOf(dict),
            }
        }
    }


class ShowSubscriberSessionAllSchema(MetaParser):

    """Schema for show subscriber session all"""

    schema = {
        Optional('total_sessions'): int,
        Optional('no_active_session'): bool,
        Optional('sessions'): {
            Any(): {
                'uid': int,
                Optional('type'): str,
                Optional('state'): str,
                Optional('identity'): str,
                Optional('ipv4_address'): str,
                Optional('ipv6_address'): str,
                Optional('session_up_time'): str,
                Optional('last_changed'): str,
                Optional('switch_id'): int,
                Optional('policy_information'): {
                    Optional('authentication_status'): str,
                    Optional('active_services'): ListOf(str),
                    Optional('rules_actions_conditions_executed'): ListOf({
                        'type': str,
                        'name': str,
                        Optional('mode'): str,
                        Optional('matches'): ListOf({
                            'identifier': str,
                            'ip': str,
                            'mask': str,
                            'result': str
                        }),
                        Optional('condition'): {
                            'name': str,
                            'event': str,
                            Optional('actions'): ListOf({
                                'sequence': int,
                                'command': str
                            })
                        }
                    })
                },
                Optional('classifiers'): {
                    Any(): {
                        'class_id': int,
                        'direction': str,
                        'packets': int,
                        'bytes': int,
                        'priority': int,
                        'definition': str
                    }
                },
                Optional('template_id'): int,
                Optional('static_routes'): {
                    Any(): {
                        'class_id': int,
                        'configuration_status': str,
                        'source': str
                    }
                },
                Optional('prepaid_time_monitor'): {
                    Any(): {
                        'class_id': int,
                        'direction': str,
                        'threshold': int,
                        'quota': int,
                        'session_time': int,
                        'source': str
                    }
                },
                Optional('prepaid_volume_monitor'): {
                    Any(): {
                        'class_id': int,
                        'direction': str,
                        'packets': int,
                        'bytes': int,
                        'source': str
                    },
                    Optional('usage'): {
                        'since_last_update': int,
                        'total': int
                    },
                    Optional('thresholds'): {
                        'threshold': int,
                        'quota': int
                    },
                    Optional('post_tariff_thresholds'): {
                        'threshold': int,
                        'quota': int
                    },
                    Optional('current_states'): str
                },
                Optional('keepalive'): {
                    Any(): {
                        'class_id': int,
                        'idle_period': int,
                        'attempts': int,
                        'interval': int,
                        'protocol': str,
                        'source': str
                    }
                },
                Optional('configuration_sources'): ListOf({
                    'type': str,
                    'active_time': str,
                    'aaa_service_id': str,
                    'name': str
                })
            }
        }
    }


class ShowSubscriberSessionAll(ShowSubscriberSessionAllSchema):

    """Parser for show subscriber session all"""

    cli_command = "show subscriber session all"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        if not output:
            return parsed_dict

        current_session = None

        section = None
        policy_section = None
        current_rule = None
        current_condition = None

        # Current Subscriber Information: Total sessions 1
        p1 = re.compile(r'^Current\s+Subscriber\s+Information:\s+Total\s+sessions\s+(?P<total>\d+)$')

        # %No active Subscriber Sessions
        p_no_active = re.compile(r'^\%(?P<no_active_session>No\s+active\s+Subscriber\s+Sessions)')

        # Type: IPv4, UID: 2, State: authen, Identity: rouble-pppoe
        p2 = re.compile(r'^Type\s*:\s*(?P<type>\S+)\s*,\s*UID\s*:\s*(?P<uid>\d+)\s*,\s*State\s*:\s*(?P<state>\S+)\s*,\s*Identity\s*:\s*(?P<identity>.+)$')

        # IPv4 Address: 10.0.0.2
        # IPv6 Address: 2001:db8::1
        p3 = re.compile(r'^(?P<address_type>IPv4|IPv6)\s+Address\s*:\s*(?P<ip>\S+)$')

        # Session Up-time: 00:01:37, Last Changed: 00:00:02
        p4 = re.compile(r'^Session\s+Up\-time\s*:\s*(?P<uptime>\d+\:\d+\:\d+)\s*,\s*Last\s+Changed\s*:\s*(?P<last>\d+\:\d+\:\d+)$')

        # Switch-ID: 4102
        p5 = re.compile(r'^Switch\-ID\s*:\s*(?P<sid>\d+)$')

        # Policy information:
        p6 = re.compile(r'^Policy\s+information\s*:\s*$')

        #   Authentication status: authen
        p7 = re.compile(r'^\s*Authentication\s+status\s*:\s*(?P<auth>\S+)$')

        #   Active services associated with session:
        p8 = re.compile(r'^\s*Active\s+services\s+associated\s+with\s+session\s*:\s*$')

        #     name "keepAliveSvc"
        p9 = re.compile(r'^\s*name\s+"(?P<svc>[^"]+)"\s*$')

        #   Rules, actions and conditions executed:
        p10 = re.compile(r'^\s*Rules,\s+actions\s+and\s+conditions\s+executed\s*:\s*$')

        #         subscriber condition-map match-all CONDA
        p11 = re.compile(r'^\s*subscriber\s+condition\-map\s+(?P<mode>\S+)\s+(?P<name>\S+)\s*$')

        #           match identifier source-ip-address 10.0.0.2 255.255.255.255 [TRUE]
        p12 = re.compile(r'^\s*match\s+identifier\s+(?P<identifier>\S+)\s+(?P<ip>\d+\.\d+\.\d+\.\d+)\s+(?P<mask>\d+\.\d+\.\d+\.\d+)\s+\[(?P<result>\w+)\]\s*$')

        #     subscriber rule-map START_RULE
        p13 = re.compile(r'^\s*subscriber\s+rule\-map\s+(?P<name>\S+)\s*$')

        #       condition CONDA event session-start
        p14 = re.compile(r'^\s*condition\s+(?P<cname>\S+)\s+event\s+(?P<event>\S+)\s*$')

        #         1 authorize aaa list author_list identifier source-ip-address
        #         10 authorize identifier mac-address
        #         1 service-policy type service identifier service-name
        p15 = re.compile(r'^\s*(?P<seq>\d+)\s+(?P<command>.+)$')

        # Classifiers:
        p17 = re.compile(r'^Classifiers\s*:\s*$')

        # Class-id    Dir   Packets    Bytes                  Pri.  Definition
        p18 = re.compile(r'^Class\-id\s+Dir\s+Packets\s+Bytes\s+Pri\.\s+Definition$')

        # 0           In    9          1026                   0    Match Any
        p19 = re.compile(r'^\s*(?P<class_id>\d+)\s+(?P<dir>In|Out)\s+(?P<pkts>\d+)\s+(?P<bytes>\d+)\s+(?P<pri>\d+)\s+(?P<def>.+)$')

        # Template Id : 9
        p20 = re.compile(r'^Template\s+Id\s*:\s*(?P<tid>\d+)$')

        # Features:
        p21 = re.compile(r'^Features\s*:\s*$')

        # Static Routes:
        p22 = re.compile(r'^Static\s+Routes\s*:\s*$')

        # Class-id  Configuration Status           Source
        p23 = re.compile(r'^Class\-id\s+Configuration\s+Status\s+Source$')

        # 0          This feature is enabled       Peruser
        p24 = re.compile(r'^\s*(?P<class_id>\d+)\s+(?P<status>.+?)\s{2,}(?P<src>\S+)\s*$')

        # Prepaid Time Monitor:
        p25 = re.compile(r'^Prepaid\s+Time\s+Monitor\s*:\s*$')

        # Class-id   Dir  Threshold  Quota    Session Time Source
        p26 = re.compile(r'^Class\-id\s+Dir\s+Threshold\s+Quota\s+Session\s+Time\s+Source$')

        # 2          In   380        400      73           transparent-service
        p27 = re.compile(r'^\s*(?P<class_id>\d+)\s+(?P<dir>In|Out)\s+(?P<thr>\d+)\s+(?P<quota>\d+)\s+(?P<stime>\d+)\s+(?P<src>\S+)\s*$')

        # Prepaid Volume Monitor:
        p28 = re.compile(r'^Prepaid\s+Volume\s+Monitor\s*:\s*$')

        # Class-id   Dir  Packets    Bytes                  Source
        p29 = re.compile(r'^Class\-id\s+Dir\s+Packets\s+Bytes\s+Source$')

        # 2          In   0          0                      transparent-service
        p30 = re.compile(r'^\s*(?P<class_id>\d+)\s+(?P<dir>In|Out)\s+(?P<pkts>\d+)\s+(?P<bytes>\d+)\s+(?P<src>\S+)\s*$')

        #   Usage(since last update): 0 - Total: 0
        p31 = re.compile(r'^\s*Usage\(since\s+last\s+update\)\s*:\s*(?P<since>\d+)\s*-\s*Total\s*:\s*(?P<total>\d+)\s*$')

        #   Threshold:300 - Quota:500
        p32 = re.compile(r'^\s*Threshold\s*:\s*(?P<thr>\d+)\s*-\s*Quota\s*:\s*(?P<quota>\d+)\s*$')

        #   Post Tariff Threshold:800 - Quota:1000
        p33 = re.compile(r'^\s*Post\s+Tariff\s+Threshold\s*:\s*(?P<thr>\d+)\s*-\s*Quota\s*:\s*(?P<quota>\d+)\s*$')

        #   Current states: Start Tariff-switched
        p34 = re.compile(r'^\s*Current\s+states\s*:\s*(?P<state>.+)$')

        # Keepalive:
        p35 = re.compile(r'^Keepalive\s*:\s*$')

        # Class-id   Idle period Attempts Interval Protocol Source
        p36 = re.compile(r'^Class\-id\s+Idle\s+period\s+Attempts\s+Interval\s+Protocol\s+Source$')

        # 0          60          5        1        ICMP     keepAliveSvc
        p37 = re.compile(r'^\s*(?P<class_id>\d+)\s+(?P<idle>\d+)\s+(?P<attempts>\d+)\s+(?P<intv>\d+)\s+(?P<proto>\S+)\s+(?P<src>\S+)\s*$')

        # Configuration Sources:
        p38 = re.compile(r'^Configuration\s+Sources\s*:\s*$')

        # Type  Active Time  AAA Service ID  Name
        p39 = re.compile(r'^Type\s+Active\s+Time\s+AAA\s+Service\s+ID\s+Name$')

        # SVC   00:01:13     -               transparent-service
        p40 = re.compile(r'^\s*(?P<type>\S+)\s+(?P<time>\d+\:\d+\:\d+)\s+(?P<aaa>\S+)\s+(?P<name>.+)$')

        for line in output.splitlines():
            line = line.rstrip()
            if not line:
                continue

            # Current Subscriber Information: Total sessions 1
            m = p1.match(line)
            if m:
                parsed_dict["total_sessions"] = int(m.group("total"))
                continue

            # %No active Subscriber Sessions
            m = p_no_active.match(line)
            if m:
                parsed_dict["no_active_session"] = True
                continue

            # Type: IPv4, UID: 2, State: authen, Identity: rouble-pppoe
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_uid = group["uid"]
                sessions = parsed_dict.setdefault("sessions", {})
                current_session = sessions.setdefault(current_uid, {})
                current_session["type"] = group["type"]
                current_session["uid"] = int(current_uid)
                current_session["state"] = group["state"]
                current_session["identity"] = group["identity"]
                section = None
                policy_section = None
                current_rule = None
                current_condition = None
                continue

            if current_session is None:
                continue

            # IPv4 Address: 10.0.0.2
            # IPv6 Address: 2001:db8::1
            m = p3.match(line)
            if m:
                address_key = "{}_address".format(m.group('address_type').lower())
                current_session[address_key] = m.group("ip")
                continue

            # Session Up-time: 00:01:37, Last Changed: 00:00:02
            m = p4.match(line)
            if m:
                current_session["session_up_time"] = m.group("uptime")
                current_session["last_changed"] = m.group("last")
                continue

            # Switch-ID: 4102
            m = p5.match(line)
            if m:
                current_session["switch_id"] = int(m.group("sid"))
                continue

            # Policy information:
            m = p6.match(line)
            if m:
                section = "policy"
                policy_section = None
                current_rule = None
                current_condition = None
                current_session.setdefault("policy_information", {})
                continue

            #   Authentication status: authen
            m = p7.match(line)
            if m and section == "policy":
                pi = current_session.setdefault("policy_information", {})
                pi["authentication_status"] = m.group("auth")
                continue

            #   Active services associated with session:
            m = p8.match(line)
            if m and section == "policy":
                pi = current_session.setdefault("policy_information", {})
                pi.setdefault("active_services", [])
                policy_section = "active_services"
                current_rule = None
                current_condition = None
                continue

            #     name "keepAliveSvc"
            m = p9.match(line)
            if m and section == "policy" and policy_section == "active_services":
                pi = current_session.setdefault("policy_information", {})
                services = pi.setdefault("active_services", [])
                services.append(m.group("svc"))
                continue

            #   Rules, actions and conditions executed:
            m = p10.match(line)
            if m and section == "policy":
                pi = current_session.setdefault("policy_information", {})
                pi.setdefault("rules_actions_conditions_executed", [])
                policy_section = "rules"
                current_rule = None
                current_condition = None
                continue

            #         subscriber condition-map match-all CONDA
            m = p11.match(line)
            if m and section == "policy" and policy_section == "rules":
                pi = current_session.setdefault("policy_information", {})
                rac = pi.setdefault("rules_actions_conditions_executed", [])
                current_rule = {
                    "type": "subscriber condition-map",
                    "mode": m.group("mode"),
                    "name": m.group("name"),
                    "matches": []
                }
                rac.append(current_rule)
                current_condition = None
                continue

            #           match identifier source-ip-address 10.0.0.2 255.255.255.255 [TRUE]
            m = p12.match(line)
            if (
                m
                and section == "policy"
                and policy_section == "rules"
                and current_rule
                and current_rule.get("type") == "subscriber condition-map"
            ):
                match_entry = {
                    "identifier": m.group("identifier"),
                    "ip": m.group("ip"),
                    "mask": m.group("mask"),
                    "result": m.group("result")
                }
                current_rule.setdefault("matches", []).append(match_entry)
                continue

            #     subscriber rule-map START_RULE
            m = p13.match(line)
            if m and section == "policy" and policy_section == "rules":
                pi = current_session.setdefault("policy_information", {})
                rac = pi.setdefault("rules_actions_conditions_executed", [])
                current_rule = {
                    "type": "subscriber rule-map",
                    "name": m.group("name")
                }
                rac.append(current_rule)
                current_condition = None
                continue

            #       condition CONDA event session-start
            m = p14.match(line)
            if (
                m
                and section == "policy"
                and policy_section == "rules"
                and current_rule
                and current_rule.get("type") == "subscriber rule-map"
            ):
                current_condition = {
                    "name": m.group("cname"),
                    "event": m.group("event"),
                    "actions": []
                }
                current_rule["condition"] = current_condition
                continue

            #         1 authorize aaa list author_list identifier source-ip-address
            #         10 authorize identifier mac-address
            #         1 service-policy type service identifier service-name
            m = p15.match(line)
            if (
                m
                and section == "policy"
                and policy_section == "rules"
                and current_rule
                and current_rule.get("type") == "subscriber rule-map"
                and current_condition is not None
            ):
                action_entry = {
                    "sequence": int(m.group("seq")),
                    "command": m.group("command")
                }
                current_condition.setdefault("actions", []).append(action_entry)
                continue

            # Classifiers:
            m = p17.match(line)
            if m:
                section = "classifiers"
                policy_section = None
                current_rule = None
                current_condition = None
                current_session.setdefault("classifiers", {})
                continue

            # Class-id    Dir   Packets    Bytes                  Pri.  Definition
            m = p18.match(line)
            if m and section == "classifiers":
                # header line - skip
                continue

            # 0           In    9          1026                   0    Match Any
            m = p19.match(line)
            if m and section == "classifiers":
                group = m.groupdict()
                cid = int(group["class_id"])
                cls = current_session.setdefault("classifiers", {})
                entry = cls.setdefault(cid, {})
                entry["class_id"] = cid
                entry["direction"] = group["dir"]
                entry["packets"] = int(group["pkts"])
                entry["bytes"] = int(group["bytes"])
                entry["priority"] = int(group["pri"])
                entry["definition"] = group["def"]
                continue

            # Template Id : 9
            m = p20.match(line)
            if m:
                current_session["template_id"] = int(m.group("tid"))
                continue

            # Features:
            m = p21.match(line)
            if m:
                section = "features"
                policy_section = None
                current_rule = None
                current_condition = None
                continue

            # Static Routes:
            m = p22.match(line)
            if m:
                section = "static_routes"
                policy_section = None
                current_rule = None
                current_condition = None
                current_session.setdefault("static_routes", {})
                continue

            # Class-id  Configuration Status           Source
            m = p23.match(line)
            if m and section == "static_routes":
                # header line - skip
                continue

            # 0          This feature is enabled       Peruser
            m = p24.match(line)
            if m and section == "static_routes":
                group = m.groupdict()
                cid = int(group["class_id"])
                sr = current_session.setdefault("static_routes", {})
                entry = sr.setdefault(cid, {})
                entry["class_id"] = cid
                entry["configuration_status"] = group["status"].strip()
                entry["source"] = group["src"]
                continue

            # Prepaid Time Monitor:
            m = p25.match(line)
            if m:
                section = "prepaid_time"
                policy_section = None
                current_rule = None
                current_condition = None
                current_session.setdefault("prepaid_time_monitor", {})
                continue

            # Class-id   Dir  Threshold  Quota    Session Time Source
            m = p26.match(line)
            if m and section == "prepaid_time":
                # header line - skip
                continue

            # 2          In   380        400      73           transparent-service
            m = p27.match(line)
            if m and section == "prepaid_time":
                group = m.groupdict()
                cid = int(group["class_id"])
                ptm = current_session.setdefault("prepaid_time_monitor", {})
                entry = ptm.setdefault(cid, {})
                entry["class_id"] = cid
                entry["direction"] = group["dir"]
                entry["threshold"] = int(group["thr"])
                entry["quota"] = int(group["quota"])
                entry["session_time"] = int(group["stime"])
                entry["source"] = group["src"]
                continue

            # Prepaid Volume Monitor:
            m = p28.match(line)
            if m:
                section = "prepaid_volume"
                policy_section = None
                current_rule = None
                current_condition = None
                current_session.setdefault("prepaid_volume_monitor", {})
                continue

            # Class-id   Dir  Packets    Bytes                  Source
            m = p29.match(line)
            if m and section == "prepaid_volume":
                # header line - skip
                continue

            # 2          In   0          0                      transparent-service
            m = p30.match(line)
            if m and section == "prepaid_volume":
                group = m.groupdict()
                cid = int(group["class_id"])
                pvm = current_session.setdefault("prepaid_volume_monitor", {})
                entry = pvm.setdefault(cid, {})
                entry["class_id"] = cid
                entry["direction"] = group["dir"]
                entry["packets"] = int(group["pkts"])
                entry["bytes"] = int(group["bytes"])
                entry["source"] = group["src"]
                continue

            #   Usage(since last update): 0 - Total: 0
            m = p31.match(line)
            if m and section == "prepaid_volume":
                group = m.groupdict()
                pvm = current_session.setdefault("prepaid_volume_monitor", {})
                usage = pvm.setdefault("usage", {})
                usage["since_last_update"] = int(group["since"])
                usage["total"] = int(group["total"])
                continue

            #   Threshold:300 - Quota:500
            m = p32.match(line)
            if m and section == "prepaid_volume":
                group = m.groupdict()
                pvm = current_session.setdefault("prepaid_volume_monitor", {})
                th = pvm.setdefault("thresholds", {})
                th["threshold"] = int(group["thr"])
                th["quota"] = int(group["quota"])
                continue

            #   Post Tariff Threshold:800 - Quota:1000
            m = p33.match(line)
            if m and section == "prepaid_volume":
                group = m.groupdict()
                pvm = current_session.setdefault("prepaid_volume_monitor", {})
                ptt = pvm.setdefault("post_tariff_thresholds", {})
                ptt["threshold"] = int(group["thr"])
                ptt["quota"] = int(group["quota"])
                continue

            #   Current states: Start Tariff-switched
            m = p34.match(line)
            if m and section == "prepaid_volume":
                pvm = current_session.setdefault("prepaid_volume_monitor", {})
                pvm["current_states"] = m.group("state")
                continue

            # Keepalive:
            m = p35.match(line)
            if m:
                section = "keepalive"
                policy_section = None
                current_rule = None
                current_condition = None
                current_session.setdefault("keepalive", {})
                continue

            # Class-id   Idle period Attempts Interval Protocol Source
            m = p36.match(line)
            if m and section == "keepalive":
                # header line - skip
                continue

            # 0          60          5        1        ICMP     keepAliveSvc
            m = p37.match(line)
            if m and section == "keepalive":
                group = m.groupdict()
                cid = int(group["class_id"])
                ka = current_session.setdefault("keepalive", {})
                entry = ka.setdefault(cid, {})
                entry["class_id"] = cid
                entry["idle_period"] = int(group["idle"])
                entry["attempts"] = int(group["attempts"])
                entry["interval"] = int(group["intv"])
                entry["protocol"] = group["proto"]
                entry["source"] = group["src"]
                continue

            # Configuration Sources:
            m = p38.match(line)
            if m:
                section = "configuration_sources"
                policy_section = None
                current_rule = None
                current_condition = None
                current_session.setdefault("configuration_sources", [])
                continue

            # Type  Active Time  AAA Service ID  Name
            m = p39.match(line)
            if m and section == "configuration_sources":
                # header line - skip
                continue

            # SVC   00:01:13     -               transparent-service
            m = p40.match(line)
            if m and section == "configuration_sources":
                group = m.groupdict()
                cs_list = current_session.setdefault("configuration_sources", [])
                cs_list.append({
                    "type": group["type"],
                    "active_time": group["time"],
                    "aaa_service_id": group["aaa"],
                    "name": group["name"].strip()
                })
                continue

        return parsed_dict


class ShowSubscriberServiceSchema(MetaParser):

    """Schema for show subscriber service"""

    schema = {
        Optional("services"): {
            Any(): {
                "profile_name": Or(str, None),
                "references": Or(int, None),
                "attributes": ListOf(dict),
                "class_id_in": Or(str, None),
                "class_id_out": Or(str, None),
            }
        },
        Optional("current_subscriber_info"): {
            "service": str,
            "total_sessions": int,
            "sessions": ListOf(dict)
        }
    }


class ShowSubscriberSessionDetail(ShowSubscriberSessionDetailSchema):

    cli_command = "show subscriber session detail"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        if not output:
            return ret_dict

        sessions = ret_dict.setdefault('sessions', {})

        current_uid = None
        current_session = None

        in_policy_info = False
        in_download_excluding = False
        in_download_including = False

        in_config_history = False
        current_history = None
        in_profile_attributes = False

        in_active_services = False
        in_rules = False
        current_rule = None
        current_condition = None

        in_classifiers = False
        in_qos_policy_map = False
        in_accounting = False
        in_configuration_sources = False

        # Type: PPPoE, UID: 1, State: authen, Identity: qinq_customer
        p1 = re.compile(r'^Type\s*:\s*(?P<type>[^,]+)\s*,\s*UID\s*:\s*(?P<uid>\d+)\s*,\s*State\s*:\s*(?P<state>[^,]+)\s*,\s*Identity\s*:\s*(?P<identity>.+)$')

        # IPv4 Address: 135.1.1.1
        p2 = re.compile(r'^IPv4\s+Address\s*:\s*(?P<ipv4>\S+)$')

        # Session Up-time: 00:00:03, Last Changed: 00:00:00
        p3 = re.compile(r'^Session\s+Up\-time\s*:\s*(?P<uptime>\d+\:\d+\:\d+)\s*,\s*Last\s+Changed\s*:\s*(?P<last_changed>\d+\:\d+\:\d+)$')

        # Interface: Virtual-Access1.1
        p4 = re.compile(r'^Interface\s*:\s*(?P<intf>\S+)$')

        # Switch-ID: 4098
        p5 = re.compile(r'^Switch\-ID\s*:\s*(?P<switch_id>\d+)$')

        # Policy information:
        p6 = re.compile(r'^Policy\s+information\s*:\s*$')

        #   Context 7F29E1B05A38: Handle D0000001
        p7 = re.compile(r'^\s*Context\s+(?P<context>\S+)\s*:\s*Handle\s+(?P<handle>\S+)$')

        #   AAA_id 0000000D: Flow_handle 0
        p8 = re.compile(r'^\s*AAA_id\s+(?P<aaa_id>\S+)\s*:\s*Flow_handle\s+(?P<flow_handle>\d+)$')

        #   Authentication status: authen
        p9 = re.compile(r'^\s*Authentication\s+status\s*:\s*(?P<auth_status>\S+)$')

        #   Downloaded User profile, excluding services:
        p10 = re.compile(r'^\s*Downloaded\s+User\s+profile,\s+excluding\s+services\s*:\s*$')

        #   Downloaded User profile, including services:
        p11 = re.compile(r'^\s*Downloaded\s+User\s+profile,\s+including\s+services\s*:\s*$')

        #     service-type         0   2 [Framed]
        p12 = re.compile(r'^\s*(?P<attribute>[\w\-]+)\s+(?P<sequence>\d+)\s+(?P<value>.+)$')

        #   Config history for session (recent to oldest):
        p13 = re.compile(r'^\s*Config\s+history\s+for\s+session\s+\(recent\s+to\s+oldest\)\s*:\s*$')

        #     Access-type: PPP Client: Push Command-Handler
        p14 = re.compile(r'^\s*Access\-type\s*:\s*(?P<access_type>[\w\-]+)\s+Client\s*:\s*(?P<client>.+)$')

        #      Policy event: Process Config
        p15 = re.compile(r'^\s*Policy\s+event\s*:\s*(?P<policy_event>.+)$')

        #       Profile name: qinq_customer, 2 references
        p16 = re.compile(r'^\s*Profile\s+name\s*:\s*(?P<name>[^,]+)\s*,\s*(?P<references>\d+)\s+references$')

        #         qos-policy-out       0   "add-class(sub,(class-default,voip),shape(64000),queue-limit(30))"
        p17 = re.compile(r'^\s*(?P<cfg_attribute>[\w\-]+)\s+(?P<cfg_sequence>\d+)\s+(?P<cfg_value>.+)$')

        #   Active services associated with session:
        p18 = re.compile(r'^\s*Active\s+services\s+associated\s+with\s+session\s*:\s*$')

        #     name "isg_acct1"
        p19 = re.compile(r'^\s*name\s+"?(?P<svc_name>[^"]+)"?\s*$')

        #   Rules, actions and conditions executed:
        p20 = re.compile(r'^\s*Rules,\s+actions\s+and\s+conditions\s+executed\s*:\s*$')

        #     subscriber rule-map default-internal-rule
        p21 = re.compile(r'^\s*subscriber\s+rule\-map\s+(?P<rule_name>\S+)\s*$')

        #       condition always event service-start
        p22 = re.compile(r'^\s*condition\s+(?P<condition>\S+)\s+event\s+(?P<event>\S+)\s*$')

        #         1 service-policy type service identifier service-name
        p23 = re.compile(r'^\s*\d+\s+(?P<action>.+)$')

        # Classifiers:
        p24 = re.compile(r'^Classifiers\s*:\s*$')

        # 0           In    0          0                      0    Match Any
        p25 = re.compile(r'^(?P<class_id>\d+)\s+(?P<dir>In|Out)\s+(?P<packets>\d+)\s+(?P<bytes>\d+)\s+(?P<priority>\d+)\s+(?P<definition>.+)$')

        # Features:
        p26 = re.compile(r'^Features\s*:\s*$')

        # QoS Policy Map:
        p27 = re.compile(r'^QoS\s+Policy\s+Map\s*:\s*$')

        # 0           In    ISG-3       Peruser
        p28 = re.compile(r'^(?P<class_id>\d+)\s+(?P<dir>In|Out)\s+(?P<policy_name>\S+)\s+(?P<source>\S+)$')

        # Accounting:
        p29 = re.compile(r'^Accounting\s*:\s*$')

        # 2          In   0          0                     isg_acct1
        p30 = re.compile(r'^(?P<class_id>\d+)\s+(?P<dir>In|Out)\s+(?P<packets>\d+)\s+(?P<bytes>\d+)\s+(?P<source>\S+)$')

        # Configuration Sources:
        p31 = re.compile(r'^Configuration\s+Sources\s*:\s*$')

        # Type  Active Time  AAA Service ID  Name
        p32 = re.compile(r'^Type\s+Active\s+Time\s+AAA\s+Service\s+ID\s+Name$')

        # SVC   00:00:00     1090519041      isg_acct1
        p33 = re.compile(r'^(?P<type>[A-Z]{3})\s+(?P<active_time>\d+\:\d+\:\d+)\s+(?P<aaa_service_id>[\-\d]+)\s+(?P<name>.+)$')

        # example 2:
        p34 = re.compile(r'^example\s+\d+\s*:\s*$')

        for raw_line in output.splitlines():
            line = raw_line.strip()
            if not line:
                continue

            # example 2:
            m = p34.match(line)
            if m and current_session is not None:
                # finalize any open config history entry
                if in_config_history and current_history:
                    current_session.setdefault('config_history', []).append(current_history)
                    current_history = None
                    in_profile_attributes = False
                break

            # Type: PPPoE, UID: 1, State: authen, Identity: qinq_customer
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_uid = int(group['uid'])
                current_session = sessions.setdefault(current_uid, {})
                current_session['uid'] = current_uid
                current_session['type'] = group['type']
                current_session['state'] = group['state']
                current_session['identity'] = group['identity']
                # reset all section states
                in_policy_info = False
                in_download_excluding = False
                in_download_including = False
                in_config_history = False
                current_history = None
                in_profile_attributes = False
                in_active_services = False
                in_rules = False
                current_rule = None
                current_condition = None
                in_classifiers = False
                in_qos_policy_map = False
                in_accounting = False
                in_configuration_sources = False
                continue

            if current_session is None:
                # Ignore lines until we see a session header
                continue

            # IPv4 Address: 135.1.1.1
            m = p2.match(line)
            if m:
                current_session['ipv4_address'] = m.group('ipv4')
                continue

            # Session Up-time: 00:00:03, Last Changed: 00:00:00
            m = p3.match(line)
            if m:
                g = m.groupdict()
                current_session['session_uptime'] = g['uptime']
                current_session['last_changed'] = g['last_changed']
                continue

            # Interface: Virtual-Access1.1
            m = p4.match(line)
            if m:
                current_session['interface'] = m.group('intf')
                continue

            # Switch-ID: 4098
            m = p5.match(line)
            if m:
                current_session['switch_id'] = int(m.group('switch_id'))
                continue

            # Policy information:
            m = p6.match(line)
            if m:
                in_policy_info = True
                current_session.setdefault('policy_information', {})
                # reset subflags
                in_download_excluding = False
                in_download_including = False
                continue

            #   Context 7F29E1B05A38: Handle D0000001
            m = p7.match(line)
            if m and in_policy_info:
                g = m.groupdict()
                current_session.setdefault('policy_information', {})
                current_session['policy_information']['context'] = g['context']
                current_session['policy_information']['handle'] = g['handle']
                continue

            #   AAA_id 0000000D: Flow_handle 0
            m = p8.match(line)
            if m and in_policy_info:
                g = m.groupdict()
                current_session['policy_information']['aaa_id'] = g['aaa_id']
                current_session['policy_information']['flow_handle'] = int(g['flow_handle'])
                continue

            #   Authentication status: authen
            m = p9.match(line)
            if m and in_policy_info:
                current_session['policy_information']['authentication_status'] = m.group('auth_status')
                continue

            #   Downloaded User profile, excluding services:
            m = p10.match(line)
            if m and in_policy_info:
                in_download_excluding = True
                in_download_including = False
                dup = current_session['policy_information'].setdefault('downloaded_user_profile', {})
                dup.setdefault('excluding_services', [])
                continue

            #   Downloaded User profile, including services:
            m = p11.match(line)
            if m and in_policy_info:
                in_download_excluding = False
                in_download_including = True
                dup = current_session['policy_information'].setdefault('downloaded_user_profile', {})
                dup.setdefault('including_services', [])
                continue

            #     service-type         0   2 [Framed]
            m = p12.match(line)
            if m and in_policy_info and (in_download_excluding or in_download_including):
                g = m.groupdict()
                val = g['value'].strip()
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                entry = {
                    'attribute': g['attribute'],
                    'sequence': int(g['sequence']),
                    'value': val
                }
                dup = current_session['policy_information'].setdefault('downloaded_user_profile', {})
                if in_download_excluding:
                    dup.setdefault('excluding_services', []).append(entry)
                elif in_download_including:
                    dup.setdefault('including_services', []).append(entry)
                continue

            #   Config history for session (recent to oldest):
            m = p13.match(line)
            if m:
                in_config_history = True
                in_policy_info = False
                in_download_excluding = False
                in_download_including = False
                current_session.setdefault('config_history', [])
                current_history = None
                in_profile_attributes = False
                continue

            #     Access-type: PPP Client: Push Command-Handler
            m = p14.match(line)
            if m and in_config_history:
                # finalize previous block if present
                if current_history is not None:
                    current_session['config_history'].append(current_history)
                g = m.groupdict()
                current_history = {
                    'access_type': g['access_type'],
                    'client': g['client']
                }
                in_profile_attributes = False
                continue

            #      Policy event: Process Config
            m = p15.match(line)
            if m and in_config_history and current_history is not None:
                current_history['policy_event'] = m.group('policy_event')
                continue

            #       Profile name: qinq_customer, 2 references
            m = p16.match(line)
            if m and in_config_history and current_history is not None:
                g = m.groupdict()
                current_history['profile'] = {
                    'name': g['name'],
                    'references': int(g['references']),
                    'attributes': []
                }
                in_profile_attributes = True
                continue

            #         qos-policy-out       0   "add-class(sub,(class-default,voip),shape(64000),queue-limit(30))"
            m = p17.match(line)
            if m and in_config_history and current_history is not None and in_profile_attributes and 'profile' in current_history:
                g = m.groupdict()
                val = g['cfg_value'].strip()
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                current_history['profile']['attributes'].append({
                    'attribute': g['cfg_attribute'],
                    'sequence': int(g['cfg_sequence']),
                    'value': val
                })
                continue

            #   Active services associated with session:
            m = p18.match(line)
            if m:
                # finalize any open config history entry
                if in_config_history and current_history is not None:
                    current_session.setdefault('config_history', []).append(current_history)
                    current_history = None
                in_config_history = False
                in_active_services = True
                current_session.setdefault('active_services', [])
                continue

            #     name "isg_acct1"
            m = p19.match(line)
            if m and in_active_services:
                current_session['active_services'].append({'name': m.group('svc_name')})
                continue

            #   Rules, actions and conditions executed:
            m = p20.match(line)
            if m:
                in_active_services = False
                in_rules = True
                current_session.setdefault('rules_actions_conditions', [])
                current_rule = None
                current_condition = None
                continue

            #     subscriber rule-map default-internal-rule
            m = p21.match(line)
            if m and in_rules:
                # Start only when it's default-internal-rule
                rule_name = m.group('rule_name')
                current_rule = {
                    'type': 'subscriber rule-map',
                    'name': rule_name,
                    'conditions': []
                }
                current_session['rules_actions_conditions'].append(current_rule)
                current_condition = None
                continue

            #       condition always event service-start
            m = p22.match(line)
            if m and in_rules and current_rule is not None:
                g = m.groupdict()
                current_condition = {
                    'condition': g['condition'],
                    'event': g['event'],
                    'actions': []
                }
                current_rule['conditions'].append(current_condition)
                continue

            #         1 service-policy type service identifier service-name
            m = p23.match(line)
            if m and in_rules and current_condition is not None:
                current_condition['actions'].append(m.group('action'))
                continue

            # Classifiers:
            m = p24.match(line)
            if m:
                in_rules = False
                in_classifiers = True
                current_session.setdefault('classifiers', {})
                continue

            # 0           In    0          0                      0    Match Any
            m = p25.match(line)
            if m and in_classifiers:
                g = m.groupdict()
                cid = int(g['class_id'])
                current_session['classifiers'][cid] = {
                    'direction': g['dir'],
                    'packets': int(g['packets']),
                    'bytes': int(g['bytes']),
                    'priority': int(g['priority']),
                    'definition': g['definition'].strip()
                }
                continue

            # Features:
            m = p26.match(line)
            if m:
                in_classifiers = False
                current_session.setdefault('features', {})
                continue

            # QoS Policy Map:
            m = p27.match(line)
            if m:
                in_qos_policy_map = True
                current_session.setdefault('qos_policy_map', {})
                continue

            # 0           In    ISG-3       Peruser
            m = p28.match(line)
            if m and in_qos_policy_map:
                g = m.groupdict()
                cid = int(g['class_id'])
                current_session['qos_policy_map'][cid] = {
                    'direction': g['dir'],
                    'policy_name': g['policy_name'],
                    'source': g['source']
                }
                continue

            # Accounting:
            m = p29.match(line)
            if m:
                in_qos_policy_map = False
                in_accounting = True
                current_session.setdefault('accounting', {})
                continue

            # 2          In   0          0                     isg_acct1
            m = p30.match(line)
            if m and in_accounting:
                g = m.groupdict()
                cid = int(g['class_id'])
                current_session['accounting'][cid] = {
                    'direction': g['dir'],
                    'packets': int(g['packets']),
                    'bytes': int(g['bytes']),
                    'source': g['source']
                }
                continue

            # Configuration Sources:
            m = p31.match(line)
            if m:
                in_accounting = False
                in_configuration_sources = True
                current_session.setdefault('configuration_sources', [])
                continue

            # Type  Active Time  AAA Service ID  Name
            m = p32.match(line)
            if m and in_configuration_sources:
                # header line, skip
                continue

            # SVC   00:00:00     1090519041      isg_acct1
            m = p33.match(line)
            if m and in_configuration_sources:
                g = m.groupdict()
                current_session['configuration_sources'].append({
                    'type': g['type'],
                    'active_time': g['active_time'],
                    'aaa_service_id': g['aaa_service_id'],
                    'name': g['name'].strip()
                })
                continue

        # finalize any open config history entry if we reached end
        if current_session is not None and in_config_history and current_history:
            current_session.setdefault('config_history', []).append(current_history)

        return ret_dict


class ShowSubscriberService(ShowSubscriberServiceSchema):

    """Parser for show subscriber service"""

    cli_command = "show subscriber service"

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        current_service = None

        #   Service "l4rdt":
        p1 = re.compile(r'^\s*Service\s+"(?P<service>[^"]+)"\s*:$')

        #         Profile name: l4rdt, 2 references
        p2 = re.compile(r'^\s*Profile\s+name\s*:\s*(?P<profile_name>.*)\s*,\s*(?P<references>\d+)\s+references$')

        #           password             0   <hidden>
        p3 = re.compile(r'^\s*(?P<name>[\w\-]+)\s+(?P<priority>\d+)\s+(?P<value>.+)$')

        #     Class Id  In: 00000050
        p4 = re.compile(r'^\s*Class\s+Id\s*In\s*:\s*(?P<class_in>\S+)$')

        #     Class Id Out: 00000051
        p5 = re.compile(r'^\s*Class\s+Id\s*Out\s*:\s*(?P<class_out>\S+)$')

        # Current Subscriber Information using service "l4rdt(l4addr=11.1.1.1,l4dur=500)"
        p6 = re.compile(r'^Current\s+Subscriber\s+Information\s+using\s+service\s+"(?P<service>[^"]+)"$')

        # Total sessions: 1
        p7 = re.compile(r'^Total\s+sessions\s*:\s*(?P<total>\d+)$')

        # 22      Vi1.1        authen   Lterm       00:00:15 1      qinq_customer
        p8 = re.compile(r'^(?P<uniq_id>\d+)\s+(?P<interface>\S+)\s+(?P<state>\S+)\s+(?P<service_code>\S+)\s+(?P<up_time>\d+\:\d+\:\d+)\s+(?P<tc_ct>\d+)\s+(?P<identifier>.+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            #   Service "l4rdt":
            m = p1.match(line)
            if m:
                group = m.groupdict()
                services = parsed_dict.setdefault("services", {})
                svc_name = group["service"]
                if svc_name not in services:
                    services[svc_name] = {
                        "profile_name": None,
                        "references": None,
                        "attributes": [],
                        "class_id_in": None,
                        "class_id_out": None
                    }
                current_service = svc_name
                continue

            #         Profile name: l4rdt, 2 references
            m = p2.match(line)
            if m and current_service:
                group = m.groupdict()
                services = parsed_dict.setdefault("services", {})
                svc = services.setdefault(current_service, {
                    "profile_name": None,
                    "references": None,
                    "attributes": [],
                    "class_id_in": None,
                    "class_id_out": None
                })
                svc["profile_name"] = group["profile_name"].strip()
                svc["references"] = int(group["references"])
                continue

            #           password             0   <hidden>
            m = p3.match(line)
            if m and current_service:
                group = m.groupdict()
                services = parsed_dict.setdefault("services", {})
                svc = services.setdefault(current_service, {
                    "profile_name": None,
                    "references": None,
                    "attributes": [],
                    "class_id_in": None,
                    "class_id_out": None
                })
                value = group["value"].strip()
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                attr_entry = {
                    "name": group["name"],
                    "priority": int(group["priority"]),
                    "value": value
                }
                svc["attributes"].append(attr_entry)
                continue

            #     Class Id  In: 00000050
            m = p4.match(line)
            if m and current_service:
                group = m.groupdict()
                services = parsed_dict.setdefault("services", {})
                svc = services.setdefault(current_service, {
                    "profile_name": None,
                    "references": None,
                    "attributes": [],
                    "class_id_in": None,
                    "class_id_out": None
                })
                svc["class_id_in"] = group["class_in"]
                continue

            #     Class Id Out: 00000051
            m = p5.match(line)
            if m and current_service:
                group = m.groupdict()
                services = parsed_dict.setdefault("services", {})
                svc = services.setdefault(current_service, {
                    "profile_name": None,
                    "references": None,
                    "attributes": [],
                    "class_id_in": None,
                    "class_id_out": None
                })
                svc["class_id_out"] = group["class_out"]
                continue

            # Current Subscriber Information using service "l4rdt(l4addr=11.1.1.1,l4dur=500)"
            m = p6.match(line)
            if m:
                group = m.groupdict()
                cs = parsed_dict.setdefault("current_subscriber_info", {})
                cs["service"] = group["service"]
                cs.setdefault("sessions", [])
                continue

            # Total sessions: 1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                cs = parsed_dict.setdefault("current_subscriber_info", {})
                cs["total_sessions"] = int(group["total"])
                cs.setdefault("sessions", [])
                continue

            # 22      Vi1.1        authen   Lterm       00:00:15 1      qinq_customer
            m = p8.match(line)
            if m:
                group = m.groupdict()
                cs = parsed_dict.setdefault("current_subscriber_info", {})
                sessions = cs.setdefault("sessions", [])
                sessions.append({
                    "uniq_id": int(group["uniq_id"]),
                    "interface": group["interface"],
                    "state": group["state"],
                    "service_code": group["service_code"],
                    "up_time": group["up_time"],
                    "tc_ct": int(group["tc_ct"]),
                    "identifier": group["identifier"].strip()
                })
                continue

        return parsed_dict


class ShowSubscriberSessionFeatureL4RedirectSchema(MetaParser):
    """Schema for show subscriber session feature l4redirect"""

    schema = {
        Optional('total_sessions'): int,
        Optional('sessions'): {
            Any(): {
                'type': str,
                'uid': int,
                'state': str,
                'identity': str,
                Optional('ipv4_address'): str,
                Optional('ipv6_address'): str,
                'session_up_time': str,
                'last_changed': str,
                'switch_id': int,
                Optional('features'): {
                    'l4_redirect': {
                        Any(): {
                            'class_id': int,
                            'rule_cfg': str,
                            'definition': str,
                            'source': str
                        }
                    }
                }
            }
        }
    }


class ShowSubscriberSessionFeatureL4Redirect(ShowSubscriberSessionFeatureL4RedirectSchema):
    """Parser for show subscriber session feature l4redirect and uid variant"""

    cli_command = "show subscriber session feature l4redirect"
    cli_command_uid = "show subscriber session uid {uid} feature l4redirect"

    def cli(self, uid=None, output=None):
        if output is None:
            uid_value = str(uid).strip() if uid is not None else ""
            command = (
                self.cli_command_uid.format(uid=uid_value)
                if uid_value
                else self.cli_command
            )
            output = self.device.execute(command)

        ret_dict = {}
        if not output:
            return ret_dict

        sessions = ret_dict.setdefault('sessions', {})
        current_uid = None
        current_session = None
        in_l4_redirect = False

        # Current Subscriber Information: Total sessions 1
        p1 = re.compile(r'^Current\s+Subscriber\s+Information:\s+Total\s+sessions\s+(?P<total>\d+)$')

        # Type: DHCPv4, UID: 48, State: unauthen, Identity: 11.11.11.4
        p2 = re.compile(r'^Type\s*:\s*(?P<type>[^,]+),\s*UID\s*:\s*(?P<uid>\d+),\s*State\s*:\s*(?P<state>[^,]+),\s*Identity\s*:\s*(?P<identity>.+)$')

        # IPv4 Address: 11.11.11.4
        # IPv6 Address: 5001:0:0:1::
        p3 = re.compile(r'^(?P<addr_type>IPv4|IPv6)\s+Address\s*:\s*(?P<address>\S+)$')

        # Session Up-time: 00:00:07, Last Changed: 00:00:09
        p4 = re.compile(r'^Session\s+Up\-time\s*:\s*(?P<uptime>\d+:\d+:\d+),\s*Last\s+Changed\s*:\s*(?P<last_changed>\d+:\d+:\d+)$')

        # Switch-ID: 4335
        p5 = re.compile(r'^Switch\-ID\s*:\s*(?P<switch_id>\d+)$')

        # Features:
        p6 = re.compile(r'^Features\s*:$')

        # L4 Redirect:
        p7 = re.compile(r'^L4\s+Redirect\s*:$')

        # Class-id   Rule cfg  Definition                               Source
        p8 = re.compile(r'^Class\-id\s+Rule\s+cfg\s+Definition\s+Source$')

        # 98         #1   SVC  to group V4_DASHBOARD                    L4_REDIRECT_V4
        p9 = re.compile(r'^(?P<class_id>\d+)\s+(?P<rule_cfg>\S+)\s+(?P<rule_type>\S+)\s+(?P<definition>.+?)\s{2,}(?P<source>\S+)$')

        for line in output.splitlines():
            line = line.rstrip()
            if not line:
                continue

            # Current Subscriber Information: Total sessions 1
            m = p1.match(line)
            if m:
                ret_dict['total_sessions'] = int(m.group('total'))
                continue

            # Type: DHCPv4, UID: 48, State: unauthen, Identity: 11.11.11.4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_uid = int(group['uid'])
                current_session = sessions.setdefault(current_uid, {})
                current_session['type'] = group['type'].strip()
                current_session['uid'] = current_uid
                current_session['state'] = group['state'].strip()
                current_session['identity'] = group['identity'].strip()
                in_l4_redirect = False
                continue

            if current_session is None:
                continue

            # IPv4 Address: 11.11.11.4
            # IPv6 Address: 5001:0:0:1::
            m = p3.match(line)
            if m:
                addr_type = m.group('addr_type').lower()
                current_session[f'{addr_type}_address'] = m.group('address')
                continue

            # Session Up-time: 00:00:07, Last Changed: 00:00:09
            m = p4.match(line)
            if m:
                current_session['session_up_time'] = m.group('uptime')
                current_session['last_changed'] = m.group('last_changed')
                continue

            # Switch-ID: 4335
            m = p5.match(line)
            if m:
                current_session['switch_id'] = int(m.group('switch_id'))
                continue

            # Features:
            m = p6.match(line)
            if m:
                current_session.setdefault('features', {})
                in_l4_redirect = False
                continue

            # L4 Redirect:
            m = p7.match(line)
            if m:
                features = current_session.setdefault('features', {})
                features.setdefault('l4_redirect', {})
                in_l4_redirect = True
                continue

            # Class-id   Rule cfg  Definition                               Source
            m = p8.match(line)
            if m and in_l4_redirect:
                # header line - skip
                continue

            # 98         #1   SVC  to group V4_DASHBOARD                    L4_REDIRECT_V4
            m = p9.match(line)
            if m and in_l4_redirect:
                group = m.groupdict()
                class_id = int(group['class_id'])
                l4r = current_session['features']['l4_redirect']
                l4r[class_id] = {
                    'class_id': class_id,
                    'rule_cfg': group['rule_cfg'],
                    'definition': f"{group['rule_type']}  {group['definition'].strip()}",
                    'source': group['source'].strip()
                }
                continue

        return ret_dict
class ShowSubscriberSessionFeatureAccessListSchema(MetaParser):

    """Schema for show subscriber session feature access-list"""

    schema = {
        Optional("sessions"): {
            Any(): {
                "type": str,
                "uid": int,
                "state": str,
                "identity": str,
                Optional("ipv4_address"): str,
                Optional("ipv6_address"): str,
                "session_up_time": str,
                "last_changed": str,
                "switch_id": int,
                Optional("features"): {
                    "per_user_acl": {
                        Any(): {
                            "direction": str,
                            "protocol": str,
                            "acl_name": str,
                            "source": str,
                        }
                    }
                },
            }
        }
    }


class ShowSubscriberSessionFeatureAccessList(ShowSubscriberSessionFeatureAccessListSchema):

    """Parser for show subscriber session feature access-list and uid variant"""

    cli_command = ["show subscriber session feature access-list",
                   "show subscriber session uid {uid} feature access-list"]

    def cli(self, uid=None, output=None):
        if output is None:
            cmd = self.cli_command[0]
            if uid:
                cmd = self.cli_command[1].format(uid=uid)
            output = self.device.execute(cmd)

        ret_dict = {}
        if not output:
            return ret_dict

        sessions = ret_dict.setdefault("sessions", {})
        current_session = None
        in_per_user_acl = False

        # Type: DHCPv4, UID: 61, State: authen, Identity: aaaa.bbbb.1111
        p1 = re.compile(r"^Type\s*:\s*(?P<type>[^,]+),\s*UID\s*:\s*(?P<uid>\d+),\s*State\s*:\s*(?P<state>[^,]+),\s*Identity\s*:\s*(?P<identity>.+)$")

        # IPv4 Address: 11.11.11.4
        # IPv6 Address: 5001:0:0:1::
        p2 = re.compile(r"^(?P<addr_type>IPv4|IPv6)\s+Address\s*:\s*(?P<address>\S+)$")

        # Session Up-time: 00:00:05, Last Changed: 00:00:07
        p3 = re.compile(r"^Session\s+Up\-time\s*:\s*(?P<up_time>\d+:\d+:\d+),\s*Last\s+Changed\s*:\s*(?P<last_changed>\d+:\d+:\d+)$")

        # Switch-ID: 4328
        p4 = re.compile(r"^Switch\-ID\s*:\s*(?P<switch_id>\d+)$")

        # Features:
        p5 = re.compile(r"^Features\s*:$")

        # Per-User ACL:
        p6 = re.compile(r"^Per\-User\s+ACL\s*:$")

        # Class-id   Dir  Protocol  ACL Name                            Source
        p7 = re.compile(r"^Class\-id\s+Dir\s+Protocol\s+ACL\s+Name\s+Source$")

        # 0          In   IP        ACL_IN_INTERNET11                   Peruser
        p8 = re.compile(r"^(?P<class_id>\d+)\s+(?P<direction>\S+)\s+(?P<protocol>\S+)\s+(?P<acl_name>.+?)\s{2,}(?P<source>\S+)$")

        for line in output.splitlines():
            line = line.rstrip()
            if not line:
                continue

            # Type: DHCPv4, UID: 61, State: authen, Identity: aaaa.bbbb.1111
            m = p1.match(line)
            if m:
                group = m.groupdict()
                uid_key = int(group["uid"])
                current_session = sessions.setdefault(uid_key, {})
                current_session["type"] = group["type"].strip()
                current_session["uid"] = uid_key
                current_session["state"] = group["state"].strip()
                current_session["identity"] = group["identity"].strip()
                in_per_user_acl = False
                continue

            if current_session is None:
                continue

            # IPv4 Address: 11.11.11.4
            # IPv6 Address: 5001:0:0:1::
            m = p2.match(line)
            if m:
                addr_type = m.group("addr_type").lower()
                current_session["{}_address".format(addr_type)] = m.group("address")
                continue

            # Session Up-time: 00:00:05, Last Changed: 00:00:07
            m = p3.match(line)
            if m:
                current_session["session_up_time"] = m.group("up_time")
                current_session["last_changed"] = m.group("last_changed")
                continue

            # Switch-ID: 4328
            m = p4.match(line)
            if m:
                current_session["switch_id"] = int(m.group("switch_id"))
                continue

            # Features:
            m = p5.match(line)
            if m:
                current_session.setdefault("features", {})
                in_per_user_acl = False
                continue

            # Per-User ACL:
            m = p6.match(line)
            if m:
                features = current_session.setdefault("features", {})
                features.setdefault("per_user_acl", {})
                in_per_user_acl = True
                continue

            # Class-id   Dir  Protocol  ACL Name                            Source
            m = p7.match(line)
            if m and in_per_user_acl:
                # header line - skip
                continue

            # 0          In   IP        ACL_IN_INTERNET11                   Peruser
            m = p8.match(line)
            if m and in_per_user_acl:
                group = m.groupdict()
                class_id = int(group["class_id"])
                acl_table = current_session["features"]["per_user_acl"]
                acl_table[class_id] = {
                    "direction": group["direction"],
                    "protocol": group["protocol"],
                    "acl_name": group["acl_name"].strip(),
                    "source": group["source"],
                }
                continue

        return ret_dict


class ShowSubscriberDefaultSessionSchema(MetaParser):

    """Schema for show subscriber default-session"""

    schema = {
        Optional('uid'): {
            Any(): {
                'lite_sessions': int,
                'interface': str,
            }
        }
    }


class ShowSubscriberDefaultSession(ShowSubscriberDefaultSessionSchema):

    """Parser for 'show subscriber default-session'"""

    cli_command = 'show subscriber default-session'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # 50      0              GigabitEthernet0/3/0
        p1 = re.compile(
            r'^(?P<uid>\d+)\s+(?P<lite_sessions>\d+)\s+(?P<interface>\S+)$'
        )

        for line in output.splitlines():
            line = line.strip()

            # 50      0              GigabitEthernet0/3/0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                uid = int(group['uid'])
                uid_dict = ret_dict.setdefault('uid', {}).setdefault(uid, {})
                uid_dict['lite_sessions'] = int(group['lite_sessions'])
                uid_dict['interface'] = Common.convert_intf_name(group['interface'])
                continue

        return ret_dict

