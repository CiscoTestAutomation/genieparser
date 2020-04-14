'''show_platform.py

JunOS parsers for the following show commands:
    * file list
    * file list {filename}
    * show version

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

# ===========================
# Parser for show version
# ===========================

class ShowVersionSchema(MetaParser):
    """Schema for show version"""
    schema = {'hostname': str,
              'operating_system': str,
              'software_version': str,
              'model': str,
              }


# =========================
# Parser for 'show version'
# =========================


class ShowVersion(ShowVersionSchema):
    """Parser for show version"""
    cli_command = 'show version'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        show_version_dict = {}

        # regex patterns

        # Junos: 15.1R1-S1
        p1 = re.compile('\s*Junos: +(?P<software_version>.*$)')

        # Model: ex4300-24p
        p2 = re.compile('\s*Model: +(?P<model>.*$)')

        # Hostname: myJunosDevice
        p3 = re.compile('\s*Hostname: +(?P<hostname>.*$)')


        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                show_version_dict['operating_system'] = 'Junos'
                show_version_dict['software_version'] = \
                    str(m.groupdict()['software_version'])
                continue

            m = p2.match(line)
            if m:
                show_version_dict['model'] = \
                    str(m.groupdict()['model'])
                continue

            m = p3.match(line)
            if m:
                show_version_dict['hostname'] = \
                    str(m.groupdict()['hostname'])
                continue

        return show_version_dict

