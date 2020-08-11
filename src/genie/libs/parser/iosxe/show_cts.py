import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


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
          Optional("retry_timer_status"): str
        }
    }



# ==============================
# Parser for:
#  * 'show cts environment-data'
# ==============================
class ShowCtsEnvironmentData(ShowCtsEnvironmentDataSchema):
    """Parser for show cts environment-data"""

    cli_command = ['show cts environment-data']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        cts_env_dict = {}

        current_state_capture = re.compile(r"^Current\s+state\s=\s+(?P<state>.*$)", re.MULTILINE)
        last_status_capture = re.compile(r"^Last\s+status\s+=\s+(?P<last_status>.*$)", re.MULTILINE)
        # Optional
        tags_capture = re.compile(r"^SGT\s+tag\s+=\s+(?P<sgt_tags>\d+-\d+):(?P<tag_status>\w+)", re.MULTILINE)
        # Optional
        server_list_capture = re.compile(
            r"^Installed\s+list:\s+(?P<server_list_name>\S+),\s+(?P<server_count>\d+)\s+server\(s\):", re.MULTILINE)
        # Optional
        servers_capture = re.compile(
            r"^(\*|)Server:\s+(?P<server_ip>\d+\.\d+\.\d+\.\d+),\s+port\s+(?P<port>\d+),\s+A-ID\s+(?P<aid>\S+)",
            re.MULTILINE)
        # Optional
        server_status_capture = re.compile(r"^Status\s+=\s+(?P<server_status>\S+)", re.MULTILINE)
        # Optional
        keywrap_capture = re.compile(
            r"^auto-test\s+=\s+(?P<auto_test>(TRUE|FALSE)),\s+keywrap-enable\s+=\s+(?P<keywrap_enable>(TRUE|FALSE)),\s+idle-time\s+=\s+(?P<idle_time_mins>\d+)\s+mins,\s+deadtime\s+=\s+(?P<dead_time_secs>\d+)\s+secs",
            re.MULTILINE)
        # Optional
        sec_group_capture = re.compile(r"^(?P<sec_group>\S+):(?P<sec_group_name>\S+)", re.MULTILINE)
        # Optional
        env_data_capture = re.compile(r"^Environment\s+Data\s+Lifetime\s+=\s+(?P<env_data_lifetime_secs>\d+)\s+secs",
                                      re.MULTILINE)
        # Optional
        last_update_capture = re.compile(
            r"^Last\s+update\s+time\s+=\s+(?P<time>\d+:\d+:\d+)\s+(?P<time_zone>\w+)\s+(?P<day>\S+)\s+(?P<month>\S+)\s+(?P<date>\d+)\s+(?P<year>\d+)",
            re.MULTILINE)
        # Optional
        expiration_capture = re.compile(r"^Env-data\s+expires\s+in\s+(?P<expiration>\d+:\d+:\d+:\d+)\s+\S+",
                                        re.MULTILINE)
        # Optional
        refresh_capture = re.compile(r"^Env-data\s+refreshes\s+in\s+(?P<refresh>\d+:\d+:\d+:\d+)\s+\S+", re.MULTILINE)
        state_machine_capture = re.compile(r"^State\s+Machine\s+is\s+(?P<state_machine_status>\S+)", re.MULTILINE)
        # Optional
        retry_capture = re.compile(
            r"^Retry_timer\s+\((?P<retry_timer_secs>\d+)\s+secs\)\s+is\s+(?P<retry_timer_status>.*$)", re.MULTILINE)

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
            current_state_match = current_state_capture.match(line)
            if current_state_match:
                groups = current_state_match.groupdict()
                current_state = groups['state']
                if not cts_env_dict.get('cts_env', {}):
                    cts_env_dict['cts_env'] = {}
                cts_env_dict['cts_env']['current_state'] = current_state
                continue
            last_status_match = last_status_capture.match(line)
            if last_status_match:
                groups = last_status_match.groupdict()
                last_status = groups['last_status']
                cts_env_dict['cts_env']['last_status'] = last_status
                continue
            tags_match = tags_capture.match(line)
            if tags_match:
                groups = tags_match.groupdict()
                sgt_tags = groups['sgt_tags']
                tag_status = groups['tag_status']
                cts_env_dict['cts_env']['sgt_tags'] = sgt_tags
                cts_env_dict['cts_env']['tag_status'] = tag_status
                continue
            server_list_match = server_list_capture.match(line)
            if server_list_match:
                groups = server_list_match.groupdict()
                server_list_name = groups['server_list_name']
                server_count = int(groups['server_count'])
                cts_env_dict['cts_env']['server_list_name'] = server_list_name
                cts_env_dict['cts_env']['server_count'] = server_count
                continue
            servers_match = servers_capture.match(line)
            if servers_match:
                groups = servers_match.groupdict()
                server_ip = groups['server_ip']
                port = int(groups['port'])
                aid = groups['aid']
                server_data = {'server_ip': server_ip, 'port': port, 'aid': aid}
                continue
            server_status_match = server_status_capture.match(line)
            if server_status_match:
                groups = server_status_match.groupdict()
                server_status = groups['server_status']
                server_data.update({'server_status': server_status})
                if not cts_env_dict['cts_env'].get('servers', {}):
                    cts_env_dict['cts_env']['servers'] = []
                continue
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
            expiration_match = expiration_capture.match(line)
            if expiration_match:
                groups = expiration_match.groupdict()
                expiration = groups['expiration']
                cts_env_dict['cts_env']['expiration'] = expiration
                continue
            refresh_match = refresh_capture.match(line)
            if refresh_match:
                groups = refresh_match.groupdict()
                refresh = groups['refresh']
                cts_env_dict['cts_env']['refresh'] = refresh
                continue
            state_machine_match = state_machine_capture.match(line)
            if state_machine_match:
                groups = state_machine_match.groupdict()
                state_machine_status = groups['state_machine_status']
                cts_env_dict['cts_env']['state_machine_status'] = state_machine_status
                continue
            retry_match = retry_capture.match(line)
            if retry_match:
                groups = retry_match.groupdict()
                retry_timer_secs = int(groups['retry_timer_secs'])
                retry_timer_status = groups['retry_timer_status']
                cts_env_dict['cts_env']['state_machine_status'] = state_machine_status
                cts_env_dict['cts_env']['retry_timer_status'] = retry_timer_status
                continue

        return cts_env_dict
