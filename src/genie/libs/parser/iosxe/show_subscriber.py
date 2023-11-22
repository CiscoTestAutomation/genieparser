"""
show_subscriber.py


IOSXE parsers for the following show commands:

    * 'show subscriber session'
    * 'show subscriber lite-session'
    * 'show subscriber statistics'
"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

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

