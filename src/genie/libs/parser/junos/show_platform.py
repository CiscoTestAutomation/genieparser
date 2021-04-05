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
                    Optional, Use, ListOf


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
        # /root/filename999.cfg
        # /root/filename999: No such file or directory
        # /root/filename999.cfg: No such file or directory
        p3 = re.compile(r'^\/(?P<dir>(\S+))\/(?P<file>([a-zA-Z0-9\-\_\/\.]+))'
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

    # main schema
    schema = {
            "software-information": {
            "host-name": str,
            "junos-version": str,
            "product-model": str,
            "product-name": str,
            "package-information": ListOf({
                "comment": str,
                "name": str,
            })
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
        Optional("@xmlns:junos"): str,
        "directory-list": {
            Optional("@junos:seconds"): str,
            Optional("@junos:style"): str,
            Optional("@root-path"): str,
            "directory": {
                Optional("@name"): str,
                "file-information": ListOf({
                    "file-date": {
                        Optional("#text"): str,
                        Optional("@junos:format"): str
                    },
                    "file-group": str,
                    "file-links": str,
                    "file-name": str,
                    "file-owner": str,
                    "file-permissions": {
                        Optional("#text"): str,
                        Optional("@junos:format"): str
                    },
                    "file-size": str
                }),
                "total-files": str
            }
        }
    }

# ===================================
# Parser for:
#   * 'file list {directory} detail'
# ===================================
class FileListDetail(FileListDetailSchema):

    cli_command = ['file list {root_path} detail']
    def cli(self, root_path, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(
                root_path=root_path))
        else:
            out = output

        ret_dict = {}

        # -rw-r-----  1 root  wheel     525672 May 22 02:40 /var/log/trace-static
        p1 = re.compile(r'^(?P<file_permissions>\S+)\s+(?P<file_links>\d+)\s+'
            r'(?P<file_owner>\S+)\s+(?P<file_group>\S+)\s+(?P<file_size>\d+)\s+'
            r'(?P<file_date>[\S\s]+)\s+(?P<file_name>\S+)$')

        # total files: 2
        p2 = re.compile(r'^total\s+files:\s+(?P<total_files>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            # -rw-r-----  1 root  wheel     525672 May 22 02:40 /var/log/trace-static
            m = p1.match(line)
            if m:
                group = m.groupdict()
                dir_dict = ret_dict.setdefault('directory-list', {}). \
                    setdefault('directory', {})
                file_information_list = dir_dict.setdefault('file-information', [])
                file_dict = {}
                keys = ['file_group', 'file_links', 'file_name', 
                    'file_owner', 'file_size']
                for key in keys:
                    file_dict.update({key.replace('_', '-') : group[key]})
                file_dict.setdefault('file-date', {}). \
                    update({'@junos:format': group['file_date']})
                file_dict.setdefault('file-permissions', {}). \
                    update({'@junos:format': group['file_permissions']})
                file_information_list.append(file_dict)
                continue

            # total files: 2 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dir_dict.update({'total-files': group['total_files']})
                continue
        return ret_dict