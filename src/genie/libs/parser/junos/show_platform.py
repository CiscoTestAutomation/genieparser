'''show_platform.py

JunOS parsers for the following show commands:
    * file list
    * file list {filename}

'''

# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ===========================
# Schema for:
#   * 'file list'
#   * 'file list {filename}'
# ===========================
class FileListSchema(MetaParser):
    ''' Schema for:
        * 'file list'
        * 'file list {filename}'
    '''

    schema = {
        'dir': 
            {Any(): 
                {Optional('files'): 
                    {Any(): 
                        {Optional('path'): str,
                        },
                    },
                },
            },
        }

# ===========================
# Parser for:
#   * 'file list'
#   * 'file list {filename}'
# ===========================
class FileList(FileListSchema):
    ''' Parser for:
        * 'file list'
        * 'file list {filename}'
    '''

    cli_command = ['file list', 'file list {filename}']
    exclude = []

    def cli(self, filename='', output=None):

        # Execute command
        if output is None:
            if filename:
                out = self.device.execute(self.cli_command[1].format(filename=filename))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init
        ret_dict = {}

        # /root/:
        p1 = re.compile(r'^\/(?P<dir>(\S+))\/\:$')

        # filename
        # .profile@ -> /packages/mnt/os-runtime/root/.profile
        p2 = re.compile(r'^(?P<file>([a-zA-Z0-9\-\_\.\@]+))(?: +\-\> +(?P<path>(.*)))?$')

        # /root/filename999
        # /root/filename999: No such file or directory
        p3 = re.compile(r'^\/(?P<dir>(\S+))\/(?P<file>([a-zA-Z0-9\-\_\/]+))'
                         '(?P<missing>(?:\: +No +such +file +or +directory)?)$')

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
            # .profile@ -> /packages/mnt/os-runtime/root/.profile
            m = p2.match(line)
            if m:
                group = m.groupdict()
                files_dict = dir_dict.setdefault('files', {}).\
                                      setdefault(group['file'].strip(), {})
                if group['path']:
                    files_dict['path'] = group['path'].strip()
                continue

            # /root/filename999
            m = p3.match(line)
            if m:
                group = m.groupdict()
                dir_dict = ret_dict.setdefault('dir', {}).\
                                    setdefault(group['dir'].strip(), {})
                if group['missing']:
                    continue
                files_dict = dir_dict.setdefault('files', {}).\
                                      setdefault(group['file'].strip(), {})
                continue

        return ret_dict

