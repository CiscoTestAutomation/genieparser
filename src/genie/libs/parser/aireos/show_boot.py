""" show_boot.py

AireOS parser for the following command:
    * 'show boot'

"""

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

log = logging.getLogger(__name__)

class ShowBootSchema(MetaParser):
    """ Schema for show boot """

    schema = {
        'primary_boot_image': {
            'version_num': str,
            'default': str,
            Optional('status'): str,
        },
        'backup_boot_image': {
            'version_num': str,
            Optional('status'): str,
        }
    }

class ShowBoot(ShowBootSchema):
    """ Parser for show boot """

    cli_command = 'show boot'

    def cli(self, output=None):
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        boot_dict = {}
        pri_dict = {}
        bk_dict = {}

        # Primary Boot Image............................... 8.2.170.0 (default) (active)
        # Backup Boot Image................................ 8.2.170.0
        # Primary Boot Image............................... 8.10.151.0 (default)
        # Backup Boot Image................................ 8.2.170.0 (active)
        p1 = re.compile(r'^(?P<pri_bk>[P|p]rimary|[B|b]ackup) +[B|b]oot '
                        r'+[I|i]mage\.+ +(?P<version_num>[\d\.]+)(( '
                        r'+\((?P<default>default)\)?|)( +\((?P<status>active)\))?)?$')

        for line in out.splitlines():
            line = line.strip()

            # Primary Boot Image............................... 8.2.170.0 (default) (active)
            # Backup Boot Image................................ 8.2.170.0
            # Primary Boot Image............................... 8.10.151.0 (default)
            # Backup Boot Image................................ 8.2.170.0 (active)
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                pri_dict = boot_dict.setdefault('primary_boot_image', {})
                bk_dict = boot_dict.setdefault('backup_boot_image', {})

                if 'primary' in group['pri_bk'].lower():
                    pri_dict.update({
                        'version_num': group['version_num'],
                        'default': group['default'],
                    })
                    if group['status']:
                        pri_dict.update({'status': group['status']})
                
                elif 'backup' in group['pri_bk'].lower():
                    bk_dict.update({
                        'version_num': group['version_num']
                    })
                    if group['status']:
                        bk_dict.update({'status': group['status']})

                continue

        return boot_dict
