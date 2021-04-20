
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class LsSchema(MetaParser):
    schema = {
        'total': int,
        'files': {
            Any(): {
                'mode': str,
                'links': int,
                'user': str,
                'group': str,
                'size': int,
                Optional('year'): int,
                'month': str,
                'day': int,
                Optional('hour'): int,
                Optional('minute'): int,
                'filename': str,
                Optional('linked_filename'): str
            }
        }
    }


class Ls(LsSchema):

    cli_command = ['ls -l', 'ls -l {directory}']

    def cli(self, directory='', output=None):

        if output is None:
            if directory:
                out = self.device.execute(self.cli_command[1].format(directory=directory))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # total 426296
        p0 = re.compile(r'^\s*total\s+(?P<total>\d+)')

        # file mode, number of links, owner name, group name, number of bytes in the file
        # lrwxrwxrwx 1 root  root          12 Mar 23 23:36 aci -> /.aci/viewfs
        # lrwxrwxrwx 1 root  root          12 Mar 23  2009 nonaci
        p1 = re.compile(r'(?P<mode>\S+)\s+(?P<links>\d+)\s+(?P<user>\S+)\s+(?P<group>\S+)\s+(?P<size>\d+)\s+(?P<month>\w+)\s+(?P<day>\d+)\s+(?:(?:(?P<hour>\d+):(?P<minute>\d+))|(?P<year>\d+))\s+(?P<filename>.*?)$')

        ls_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                ls_dict['total'] = int(m.groupdict()['total'])

            m = p1.match(line)

            if m:
                groups = m.groupdict()
                filename = groups['filename']
                if ' -> ' in filename:
                    filename, linked_filename = filename.split(' -> ')
                else:
                    linked_filename = None
                file_dict = ls_dict.setdefault('files', {}).setdefault(filename, {})
                if linked_filename:
                    file_dict.update({'linked_filename': linked_filename})
                file_dict.update({'filename': filename})
                file_dict.update({'mode': groups['mode']})
                file_dict.update({'links': int(groups['links'])})
                file_dict.update({'user': groups['user']})
                file_dict.update({'group': groups['group']})
                file_dict.update({'size': int(groups['size'])})
                if groups['year']:
                    file_dict.update({'year': int(groups['year'])})
                file_dict.update({'month': groups['month']})
                file_dict.update({'day': int(groups['day'])})
                if groups['hour']:
                    file_dict.update({'hour': int(groups['hour'])})
                if groups['minute']:
                    file_dict.update({'minute': int(groups['minute'])})

        return ls_dict
