'''show_platform.py

JunOS parsers for the following show commands:
    * file list

'''

# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ======================
# Schema for 'file list'
# ======================
class FileListSchema(MetaParser):
    ''' Schema for 'file list' '''

    schema = {
        'dir': 
            {Any(): 
                {'files': 
                    {Any(): 
                        {Optional('path'): str,
                        },
                    },
                },
            },
        }

# ======================
# Parser for 'file list'
# ======================
class FileList(FileListSchema):
    ''' Parser for 'file list' '''

    cli_command = ['file list']
    exclude = []

    def cli(self, output=None):

        # Execute command
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init
        ret_dict = {}

        # /root/:
        p1 = re.compile(r'^\/(?P<dir>(\S+))\:$')

        # filename
        p2 = re.compile(r'^(?P<file>([a-zA-Z0-9\-\_]+))$')

        # .profile@ -> /packages/mnt/os-runtime/root/.profile
        p3 = re.compile(r'^\.(?P<file>([a-zA-Z0-9\-\_]+))\@ *\-\> *(?P<path>(.*))$')


        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            # /root/:
            m = p1.match(line)
            if m:
                dir_dict = ret_dict.setdefault('dir', {}).\
                                    setdefault(m.groupdict()['dir'].strip(), {})
                continue

            # filename
            m = p2.match(line)
            if m:
                files_dict = dir_dict.setdefault('files', {}).\
                                      setdefault(m.groupdict()['file'], {})
                continue

            # .profile@ -> /packages/mnt/os-runtime/root/.profile
            m = p3.match(line)
            if m:
                group = m.groupdict()
                files_dict = dir_dict.setdefault('files', {}).\
                                      setdefault(group['file'], {})
                files_dict['path'] = group['path']

        return ret_dict

