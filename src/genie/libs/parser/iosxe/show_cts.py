import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==================
# Schema for:
#  * 'show cts pacs'
# ==================
class ShowCtsPacsSchema(MetaParser):
    """Schema for show cts pacs."""

    schema = {
        "aid": str,
        "pac_info": {
            "aid": str,
            "pac_type": str,
            "i_id": str,
            "a_id_info": str,
            "credential_lifetime": str,
        },
        "pac_opaque": str,
        "refresh_timer": str,
    }


# ==================
# Parser for:
#  * 'show cts pacs'
# ==================
class ShowCtsPacs(ShowCtsPacsSchema):
    """Parser for show cts pacs"""

    cli_command = 'show cts pacs'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # AID: 1100E046659D4275B644BF946EFA49CD
        # PAC-Info:
        #   PAC-type = Cisco Trustsec
        #   AID: 1100E046659D4275B644BF946EFA49CD
        #   I-ID: gw1
        #   A-ID-Info: Identity Services Engine
        #   Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
        # PAC-Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
        # Refresh timer is set for 6w3d

        cts_pacs_dict = {}

        # AID: 1100E046659D4275B644BF946EFA49CD
        aid_capture = re.compile(r"^AID:\s+(?P<aid>\S+)")
        #   PAC-type = Cisco Trustsec
        pac_type_capture = re.compile(r"^PAC-type\s=\s(?P<pac_type>.*$)")
        #     I-ID: gw1
        iid_capture = re.compile(r"^I-ID:\s+(?P<iid>\S+)")
        #   A-ID-Info: Identity Services Engine
        aid_info_capture = re.compile(r"^A-ID-Info:\s+(?P<aid_info>.*$)")
        #   Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
        credential_lifetime_capture = re.compile(
            r"^Credential\s+Lifetime:\s+(?P<time>\d+:\d+:\d+)\s+(?P<time_zone>\S+)\s+(?P<day>\S+)\s+(?P<month>\S+)\s+(?P<date>\d+)\s+(?P<year>\d+)")
        # PAC - Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
        pac_opaque_capture = re.compile(r"^PAC-Opaque:\s+(?P<pac_opaque>.*$)")
        # Refresh timer is set for 6w3d
        refresh_timer_capture = re.compile(r"^Refresh\s+timer\s+is\s+set\s+for\s+(?P<refresh_timer>\S+)")

        remove_lines = ('PAC-Info:')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # print(clean_line)
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        for line in out:
            # AID: 1100E046659D4275B644BF946EFA49CD
            aid_match = aid_capture.match(line)
            if aid_match:
                groups = aid_match.groupdict()
                aid = groups['aid']
                if not cts_pacs_dict.get('aid', {}):
                    cts_pacs_dict['aid'] = aid
                if not cts_pacs_dict.get('pac_info', {}):
                    cts_pacs_dict['pac_info'] = {}
                    cts_pacs_dict['pac_info']['aid'] = aid
                continue
            #   PAC-type = Cisco Trustsec
            pac_type_match = pac_type_capture.match(line)
            if pac_type_match:
                groups = pac_type_match.groupdict()
                pac_type = groups['pac_type']
                if not cts_pacs_dict.get('pac_info', {}):
                    cts_pacs_dict['pac_info'] = {}
                cts_pacs_dict['pac_info']['pac_type'] = pac_type
                continue
            #     I-ID: gw1
            iid_match = iid_capture.match(line)
            if iid_match:
                groups = iid_match.groupdict()
                iid = groups['iid']
                cts_pacs_dict['pac_info']['i_id'] = iid
                continue
            #   A-ID-Info: Identity Services Engine
            aid_info_match = aid_info_capture.match(line)
            if aid_info_match:
                groups = aid_info_match.groupdict()
                aid_info = groups['aid_info']
                cts_pacs_dict['pac_info']['a_id_info'] = aid_info
                continue
            #   Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
            credential_lifetime_match = credential_lifetime_capture.match(line)
            if credential_lifetime_match:
                groups = credential_lifetime_match.groupdict()
                time = groups['time']
                time_zone = groups['time_zone']
                day = groups['day']
                month = groups['month']
                date = groups['date']
                year = groups['year']
                full_date = f"{day}, {month}/{date}/{year}"
                cts_pacs_dict['pac_info']['credential_lifetime'] = full_date
                continue
            # PAC - Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
            pac_opaque_match = pac_opaque_capture.match(line)
            if pac_opaque_match:
                groups = pac_opaque_match.groupdict()
                pac_opaque = groups['pac_opaque']
                cts_pacs_dict['pac_opaque'] = pac_opaque
                continue
            # Refresh timer is set for 6w3d
            refresh_timer_match = refresh_timer_capture.match(line)
            if refresh_timer_match:
                groups = refresh_timer_match.groupdict()
                refresh_timer = groups['refresh_timer']
                cts_pacs_dict['refresh_timer'] = refresh_timer
                continue

        return cts_pacs_dict



# ==============================
# Schema for:
#  * 'show cts environment-data'
# ==============================
class ShowCtsEnvironmentDataSchema(MetaParser):
    """Schema for show cts environment-data."""

    schema = {
        "cts_env": {
            "current_state": str,
            "last_status": str,
            Optional("sgt_tags"): str,
            Optional("tag_status"): str,
            Optional("server_list_name"): str,
            Optional("server_count"): int,
            Optional("servers"): {
                Optional(int): {
                    Optional("server_ip"): str,
                    Optional("port"): int,
                    Optional("aid"): str,
                    Optional("server_status"): str,
                    Optional("auto_test"): str,
                    Optional("keywrap_enable"): str,
                    Optional("idle_time_mins"): int,
                    Optional("dead_time_secs"): int
                }
          },
            Optional("security_groups"): {
                Optional(int): {
                    Optional("sec_group"): str,
                    Optional("sec_group_name"): str
              }
          },
          Optional("env_data_lifetime_secs"): str,
          Optional("last_update"): {
                Optional("date"): str,
                Optional("time"): str,
                Optional("time_zone"): str
          },
          Optional("expiration"): str,
          Optional("refresh"): str,
          "state_machine_status": str,
          Optional("retry_timer_status"): str,
          Optional("cache_data_status"): str
        }
    }



# ==============================
# Parser for:
#  * 'show cts environment-data'
# ==============================
class ShowCtsEnvironmentData(ShowCtsEnvironmentDataSchema):
    """Parser for show cts environment-data"""

    cli_command = 'show cts environment-data'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        cts_env_dict = {}
        # CTS Environment Data
        # ====================
        # Current state = COMPLETE
        # Last status = Successful
        # Local Device SGT:
        #   SGT tag = 0-16:Unknown
        # Server List Info:
        # Installed list: CTSServerList1-0089, 4 server(s):
        #  *Server: 10.1.100.4, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #           Status = ALIVE
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        #  *Server: 10.1.100.5, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #           Status = ALIVE
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        #  *Server: 10.1.100.6, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #           Status = ALIVE
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        #  *Server: 10.1.100.6, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #           Status = ALIVE
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        # Security Group Name Table:
        #     0-15:Unit0
        #     2-12:Unit1
        #     3-10:Unit2
        #     4-11:Device11
        #     3215-08:K2
        #     9999-06:Q1
        #     68-10:North
        #     5016-00:Quarantine
        #     8000-00:TEST_8000
        # Environment Data Lifetime = 86400 secs
        # Last update time = 20:04:42 PDT Tue Jul 21 2020
        # Env-data expires in   0:00:46:51 (dd:hr:mm:sec)
        # Env-data refreshes in 0:00:46:51 (dd:hr:mm:sec)
        # Cache data applied           = NONE
        # State Machine is running

        # Current state = COMPLETE
        current_state_capture = re.compile(r"^Current\s+state\s+=\s+(?P<state>.*$)")
        # Last status = Successful
        last_status_capture = re.compile(r"^Last\s+status\s+=\s+(?P<last_status>.*$)")
        #   SGT tag = 0-16:Unknown
        tags_capture = re.compile(r"^SGT\s+tag\s+=\s+(?P<sgt_tags>\d+-\d+):(?P<tag_status>\w+)")
        # Installed list: CTSServerList1-0089, 4 server(s):
        server_list_capture = re.compile(
            r"^Installed\s+list:\s+(?P<server_list_name>\S+),\s+(?P<server_count>\d+)\s+server\(s\):", re.MULTILINE)
        #  *Server: 10.1.100.4, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        servers_capture = re.compile(
            r"^(\*|)Server:\s+(?P<server_ip>\d+\.\d+\.\d+\.\d+),\s+port\s+(?P<port>\d+),\s+A-ID\s+(?P<aid>\S+)")
        #           Status = ALIVE
        server_status_capture = re.compile(r"^Status\s+=\s+(?P<server_status>\S+)")
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        keywrap_capture = re.compile(
            r"^auto-test\s+=\s+(?P<auto_test>(TRUE|FALSE)),\s+keywrap-enable\s+=\s+(?P<keywrap_enable>(TRUE|FALSE)),\s+idle-time\s+=\s+(?P<idle_time_mins>\d+)\s+mins,\s+deadtime\s+=\s+(?P<dead_time_secs>\d+)\s+secs")
        #     0-15:Unit0
        sec_group_capture = re.compile(r"^(?P<sec_group>\S+):(?P<sec_group_name>\S+)")
        # Environment Data Lifetime = 86400 secs
        env_data_capture = re.compile(r"^Environment\s+Data\s+Lifetime\s+=\s+(?P<env_data_lifetime_secs>\d+)\s+secs")
        # Last update time = 20:04:42 PDT Tue Jul 21 2020
        last_update_capture = re.compile(
            r"^Last\s+update\s+time\s+=\s+(?P<time>\d+:\d+:\d+)\s+(?P<time_zone>\w+)\s+(?P<day>\S+)\s+(?P<month>\S+)\s+(?P<date>\d+)\s+(?P<year>\d+)")
        # Env-data expires in   0:00:46:51 (dd:hr:mm:sec)
        expiration_capture = re.compile(r"^Env-data\s+expires\s+in\s+(?P<expiration>\d+:\d+:\d+:\d+)\s+\S+")
        # Env-data refreshes in 0:00:46:51 (dd:hr:mm:sec)
        refresh_capture = re.compile(r"^Env-data\s+refreshes\s+in\s+(?P<refresh>\d+:\d+:\d+:\d+)\s+\S+")
        # Cache data applied           = NONE
        cache_data_capture = re.compile(r"^Cache\s+data\s+applied\s+=\s+(?P<cache_data_status>\S+)")
        # State Machine is running
        state_machine_capture = re.compile(r"^State\s+Machine\s+is\s+(?P<state_machine_status>\S+)")
        # Retry_timer (60 secs) is not running
        retry_capture = re.compile(
            r"^Retry_timer\s+\((?P<retry_timer_secs>\d+)\s+secs\)\s+is\s+(?P<retry_timer_status>.*$)")

        remove_lines = (
        'CTS Environment Data', '=========', 'Local Device SGT:', 'Server List Info:', 'Security Group Name Table:')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # print(clean_line)
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        server_data = {}
        security_groups = {}
        keywrap_index = 1
        sec_group_index = 1
        for line in out:
            # Current state = COMPLETE
            current_state_match = current_state_capture.match(line)
            if current_state_match:
                groups = current_state_match.groupdict()
                current_state = groups['state']
                if not cts_env_dict.get('cts_env', {}):
                    cts_env_dict['cts_env'] = {}
                cts_env_dict['cts_env']['current_state'] = current_state
                continue
            # Last status = Successful
            last_status_match = last_status_capture.match(line)
            if last_status_match:
                groups = last_status_match.groupdict()
                last_status = groups['last_status']
                cts_env_dict['cts_env']['last_status'] = last_status
                continue
            #   SGT tag = 0-16:Unknown
            tags_match = tags_capture.match(line)
            if tags_match:
                groups = tags_match.groupdict()
                sgt_tags = groups['sgt_tags']
                tag_status = groups['tag_status']
                cts_env_dict['cts_env']['sgt_tags'] = sgt_tags
                cts_env_dict['cts_env']['tag_status'] = tag_status
                continue
            # Installed list: CTSServerList1-0089, 4 server(s):
            server_list_match = server_list_capture.match(line)
            if server_list_match:
                groups = server_list_match.groupdict()
                server_list_name = groups['server_list_name']
                server_count = int(groups['server_count'])
                cts_env_dict['cts_env']['server_list_name'] = server_list_name
                cts_env_dict['cts_env']['server_count'] = server_count
                continue
            #  *Server: 10.1.100.4, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
            servers_match = servers_capture.match(line)
            if servers_match:
                groups = servers_match.groupdict()
                server_ip = groups['server_ip']
                port = int(groups['port'])
                aid = groups['aid']
                server_data = {'server_ip': server_ip, 'port': port, 'aid': aid}
                continue
            #           Status = ALIVE
            server_status_match = server_status_capture.match(line)
            if server_status_match:
                groups = server_status_match.groupdict()
                server_status = groups['server_status']
                server_data.update({'server_status': server_status})
                if not cts_env_dict['cts_env'].get('servers', {}):
                    cts_env_dict['cts_env']['servers'] = []
                continue
            #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
            keywrap_match = keywrap_capture.match(line)
            if keywrap_match:
                groups = keywrap_match.groupdict()
                auto_test = groups['auto_test']
                keywrap_enable = groups['keywrap_enable']
                idle_time_mins = int(groups['idle_time_mins'])
                dead_time_secs = int(groups['dead_time_secs'])
                server_data.update(
                    {'auto_test': auto_test, 'keywrap_enable': keywrap_enable, 'idle_time_mins': idle_time_mins,
                     'dead_time_secs': dead_time_secs})
                if not cts_env_dict['cts_env'].get('servers', {}):
                    cts_env_dict['cts_env']['servers'] = {}
                if not cts_env_dict['cts_env']['servers'].get(keywrap_index, {}):
                    cts_env_dict['cts_env']['servers'][keywrap_index] = server_data
                keywrap_index = keywrap_index + 1
                continue
            #     0-15:Unit0
            sec_group_match = sec_group_capture.match(line)
            if sec_group_match:
                groups = sec_group_match.groupdict()
                sec_group = groups['sec_group']
                sec_group_name = groups['sec_group_name']
                sec_groups_data = {'sec_group': sec_group, 'sec_group_name': sec_group_name}
                if not cts_env_dict['cts_env'].get('security_groups', {}):
                    cts_env_dict['cts_env']['security_groups'] = {}
                if not cts_env_dict['cts_env']['security_groups'].get(sec_group_index, {}):
                    cts_env_dict['cts_env']['security_groups'][sec_group_index] = sec_groups_data
                sec_group_index = sec_group_index + 1
                continue
            # Environment Data Lifetime = 86400 secs
            env_data_match = env_data_capture.match(line)
            if env_data_match:
                groups = env_data_match.groupdict()
                if groups.get('env_empty', {}):
                    env_data = groups['env_empty']
                    cts_env_dict['cts_env']['env_data'] = env_data
                else:
                    env_data_lifetime_secs = groups['env_data_lifetime_secs']
                    cts_env_dict['cts_env']['env_data_lifetime_secs'] = env_data_lifetime_secs
                continue
            # Last update time = 20:04:42 PDT Tue Jul 21 2020
            last_update_match = last_update_capture.match(line)
            if last_update_match:
                groups = last_update_match.groupdict()
                time = groups['time']
                time_zone = groups['time_zone']
                day = groups['day']
                month = groups['month']
                date = groups['date']
                year = groups['year']
                full_date = f"{day}, {month}/{date}/{year}"
                cts_env_dict['cts_env'].update(
                    {'last_update': {'date': full_date, 'time': time, 'time_zone': time_zone}})
                continue
            # Env-data expires in   0:00:46:51 (dd:hr:mm:sec)
            expiration_match = expiration_capture.match(line)
            if expiration_match:
                groups = expiration_match.groupdict()
                expiration = groups['expiration']
                cts_env_dict['cts_env']['expiration'] = expiration
                continue
            # Env-data refreshes in 0:00:46:51 (dd:hr:mm:sec)
            refresh_match = refresh_capture.match(line)
            if refresh_match:
                groups = refresh_match.groupdict()
                refresh = groups['refresh']
                cts_env_dict['cts_env']['refresh'] = refresh
                continue
            # Cache data applied           = NONE
            cache_data_match = cache_data_capture.match(line)
            if cache_data_match:
                groups = cache_data_match.groupdict()
                cache_data_status = groups['cache_data_status']
                cts_env_dict['cts_env']['cache_data_status'] = cache_data_status
                continue
            # State Machine is running
            state_machine_match = state_machine_capture.match(line)
            if state_machine_match:
                groups = state_machine_match.groupdict()
                state_machine_status = groups['state_machine_status']
                cts_env_dict['cts_env']['state_machine_status'] = state_machine_status
                continue
            # Retry_timer (60 secs) is not running
            retry_match = retry_capture.match(line)
            if retry_match:
                groups = retry_match.groupdict()
                retry_timer_secs = int(groups['retry_timer_secs'])
                retry_timer_status = groups['retry_timer_status']
                cts_env_dict['cts_env']['state_machine_status'] = state_machine_status
                cts_env_dict['cts_env']['retry_timer_status'] = retry_timer_status
                continue

        return cts_env_dict
