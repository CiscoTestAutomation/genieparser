"""starOS implementation of show_plugin_p2p.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowPluginP2PSchema(MetaParser):
    """Schema for show plugin p2p"""

    schema = {
        'plugin_p2p': {
            'patch-directory': str,
            'base-directory': str,
            'base-version': str
        }     
    }


class ShowPluginP2P(ShowPluginP2PSchema):
    """Parser for show plugin p2p"""

    cli_command = 'show plugin p2p'

    """
plugin p2p
  patch-directory /var/opt/lib
  base-directory /lib
  base-version 2.41.1091
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        plugin_p2p_dict = {}
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'^(patch-directory (?P<patch_directory>\S+))')
        p1 = re.compile(r'^(base-directory (?P<base_directory>\S+))')
        p2 = re.compile(r'^(base-version (?P<base_version>\S+))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'plugin_p2p' not in plugin_p2p_dict:
                    result_dict = plugin_p2p_dict.setdefault('plugin_p2p',{})
                modulePriority = m.groupdict()['patch_directory']
                result_dict['patch-directory'] = modulePriority
                
            m = p1.match(line)
            if m:
                if 'plugin_p2p' not in plugin_p2p_dict:
                    result_dict = plugin_p2p_dict.setdefault('plugin_p2p',{})
                pluginVersion = m.groupdict()['base_directory']
                result_dict['base-directory'] = pluginVersion
            
            m = p2.match(line)
            if m:
                if 'plugin_p2p' not in plugin_p2p_dict:
                    result_dict = plugin_p2p_dict.setdefault('plugin_p2p',{})
                pluginVersion = m.groupdict()['base_version']
                result_dict['base-version'] = pluginVersion
                continue

        return plugin_p2p_dict