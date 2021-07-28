"""
show variables system
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, Any, Optional)

# Parser Utils
from genie.libs.parser.utils.common import Common


class ShowVariablesSystemSchema(MetaParser):
    """
    Schema for show variables system
    """

    schema = {
        'paths':
            {
                'path': str,
                'loadpath': str,
                'ld_library_path': str,
                Optional('bfm_config_path'): str,
                'bgp_path': str,
                'configs_path': str,
                Optional('craft_path'): str,
                Optional('ctf_path'): str,
                Optional('dm_rules_path'): str,
                'etc_path': str,
                Optional('fpd_path'): str,
                'im_rules_path': str,
                'init_startup_path': str,
                Optional('insthelper_path'): str,
                Optional('man_path'): str,
                'mib_library_path': str,
                'mib_path': str,
                Optional('netio_script_path'): str,
                'parser_path': str,
                'partitions_path': str,
                Optional('pkg_path'): str,
                Optional('placement_path'): str,
                Optional('qos_path'): str,
                'schema_path': str,
                'startup_path': str,
                Optional('ucode_path'): str,
                Optional('ucode_root_path'): str,
                Optional('vcm_rules_path'): str,
            },
        Optional('hostname'): str,
        'term': list,
        'gdb_pdebug': str,
        Optional('dir_prefix'): str,
        Optional('tcl_library'): str,
        'job_id': int,
        'instance_id': int,
        Optional('sysmgr_tuple'): str,
        'sysmgr_node': str,
        'exit_status': int,
        'sysmgr_restart_reason': int,
        'aaa_user': str,
        'exec_pid': int,
        'taskid_map_size': int,
        'home': str,
        'tmpdir': str,
        'pwd': str,
        Optional('node_watcher'): int,
        Optional('tty_uart_driver'): str,
        Optional('ld_preload'): str,
        Optional('boot_dir'): str,
        Optional('dir'): str,
        Optional('user'): str,
        Optional('libvirt_default_uri'): str,
        Optional('iox_disable_startup'): int,
        Optional('ps1'): str,
        Optional('iox_disable_sysmgr'): int,
        Optional('memdbg_blacklist'): str,
        Optional('shlvl'): int,
        Optional('terminfo'): str,
        Optional('connect_dir'): str,
        Optional('upstart_instance'): str,
        Optional('memdbg_enable'): int,
        Optional('upstart_events'): str,
        Optional('iox'): int,
        Optional('rlimit'): int,
        Optional('connect_command'): str,
        Optional('boot_iox'): int,
        Optional('upstart_job'): str,
        Optional('iox_no_config'): int,
        Optional('confreg'): int,
        Optional('pcie_debug'): str,
        Optional('_'): str,
        Optional('sysmgr_vs_started'): int,
        Optional('respawn_count'): int,
        Optional('tty_category'): int,
        Optional('tty_port'): int
    }


class ShowVariablesSystem(ShowVariablesSystemSchema):
    """
    Parser for show variables system
    """

    cli_command = "show variables system"

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # MIB_PATH = / pkg / mib
        p1 = re.compile(r'^.+_PATH=.+$')

        # GDB_PDEBUG=-P1
        # parse every basic key value pair
        p2 = re.compile(r'^(?P<key>.+)=(?P<value>.+$)')

        term_list = []
        ret_dict = {}
        path_dict = {}

        for line in out.splitlines():
            line.strip()

            # MIB_PATH=/pkg/mib
            m = p1.match(line)
            if m:
                # use p2 to get a capture group of the prefix and the path
                mp = p2.match(line)
                path_name = mp.groupdict()['key'].lower()
                path_value = mp.groupdict()['value']

                path_dict = ret_dict.setdefault('paths', {})
                path_dict.update({path_name: path_value})
                continue

            # GDB_PDEBUG=-P1
            m = p2.match(line)
            if m:
                key = m.groupdict()['key'].lower()
                value = m.groupdict()['value']

                if key == 'term':
                    term_list.append(value)
                    ret_dict.update({'term': term_list})
                    continue

                if 'path' in key:
                    path_dict = ret_dict.setdefault('paths', {})
                    path_dict.update({key: value})
                    continue

                try:
                    ret_dict.update({key: int(value)})
                except ValueError as e:
                    ret_dict.update({key: value})

        return ret_dict
