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
from genie.metaparser.util.schemaengine import Schema, Any, \
                    Optional, Use, SchemaTypeError


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
# Schema for show version
# ===========================
class ShowVersionSchema(MetaParser):
    """
    schema = {
        "software-information": {
            "host-name": str,
            "junos-version": str,
            "product-model": str,
            "product-name": str,
            "package-information":
                   [
                        {
                            "comment": str,
                            "name": str,
                        }
                    ]
            }
    """

    def validate_package_info_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('package infomation is not a list')
        package_info_schema = Schema(
            {
                "comment": str,
                "name": str,
            }
        )

        for item in value:
            package_info_schema.validate(item)
        return value

    # main schema
    schema = {
            "software-information": {
            "host-name": str,
            "junos-version": str,
            "product-model": str,
            "product-name": str,
            "package-information": Use(validate_package_info_list)
        }
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

        # -----------------------------------------------------------
        #  Regex patterns
        # -----------------------------------------------------------

        # Junos: 15.1R1-S1
        p1 = re.compile(r'^Junos: +(?P<junosversion>\S+)$')

        # Model: ex4300-24p
        p2 = re.compile(r'^Model: +(?P<productmodel>\S+)$')

        # Hostname: myJunosDevice
        p3 = re.compile(r'^Hostname: +(?P<hostname>\S+)$')

        # JUNOS EX  Software Suite [18.2R2-S1]
        p4 = re.compile(r'^JUNOS +(?P<package>.*)$')

        show_version_dict["software-information"] = {}
        show_version_dict["software-information"]["package-information"] = []

        # -----------------------------------------------------------
        #  Build parsed output
        # -----------------------------------------------------------
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                show_version_dict["software-information"]['junos-version'] = \
                    m.groupdict()['junosversion']
                continue

            m = p2.match(line)
            if m:
                show_version_dict["software-information"]['product-model'] = \
                    m.groupdict()['productmodel']
                show_version_dict["software-information"]['product-name'] = \
                    m.groupdict()['productmodel']
                continue

            m = p3.match(line)
            if m:
                show_version_dict["software-information"]['host-name'] = \
                    m.groupdict()['hostname']
                continue

            m = p4.match(line)
            if m:
                # Cleaning name to remove multiple white spaces, lower case string,
                # remove JUNOS word, version between brakes (if present)
                # and replacing spaces for dashes

                name = re.sub(' +', ' ', m.groupdict()['package'].replace("JUNOS", ""))

                if "[" in name:
                    name = name.split("[")[0].strip().lower().replace(" ", "-")
                else:
                    name = name.strip().lower().replace("  ", "-").replace(" ", "-")

                show_version_dict["software-information"]['package-information'].append(
                    {
                        "comment": m.groupdict()['package'],
                        "name": name
                    }
                )
                continue

        # Check for empty input
        if 'junos-version' not in show_version_dict["software-information"].keys():
            return {}

        return show_version_dict

# ===================================
# Schema for:
#   * 'file list {directory} detail'
# ===================================
class FileListDetailSchema(MetaParser):

    schema = {
        'dir': {
            Any(): {
                Optional('files'): {
                    Any(): {
                        'permission': str,
                        'number': str,
                        'user': str,
                        'group': str,
                        'file_size': str,
                        'date_time': str,
                        'file_name': str,
                    },
                },
                Optional('total_files'): int,
            },
        },
    }

# ===================================
# Parser for:
#   * 'file list {directory} detail'
# ===================================
class FileListDetail(FileListDetailSchema):

    cli_command = ['file list {directory} detail']
    def cli(self, directory, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(
                directory=directory))
        else:
            out = output
        
        ret_dict = {}

        # -rw-r-----  1 root  wheel     525672 May 22 02:40 /var/log/trace-static
        p1 = re.compile(r'^(?P<permission>\S+)\s+(?P<number>\d+)\s+'
            r'(?P<user>\S+)\s+(?P<group>\S+)\s+(?P<file_size>\d+)\s+'
            r'(?P<date_time>[\S\s]+)\s+(?P<file_name>\S+)$')
        
        # total files: 2
        p2 = re.compile(r'^total\s+files:\s+(?P<total_files>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            # -rw-r-----  1 root  wheel     525672 May 22 02:40 /var/log/trace-static
            m = p1.match(line)
            if m:
                group = m.groupdict()
                dir_dict = ret_dict.setdefault('dir', {}). \
                    setdefault(directory, {})
                file_dict = dir_dict.setdefault('files', {}). \
                    setdefault(group['file_name'], {})
                file_dict.update({k:
                    v for k, v in group.items() if v is not None})
                continue

            # total files: 2 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dir_dict.update({'total_files': int(group['total_files'])})
                continue

        return ret_dict
