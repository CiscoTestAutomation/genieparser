""" show_log.py

JunOs parsers for the following show commands:
    * show log {filename}
    * show log {filename} | match {match}
    * show log {filename} | except {except_show_log} | match {match}
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema)


class ShowLogFilenameSchema(MetaParser):
    """ Schema for:
            * show log {filename}
    """

    schema = {
        "file-content": list
    }

class ShowLogFilename(ShowLogFilenameSchema):
    """ Parser for:
            * show log {filename}
            * show log {filename} | match {match}
            * show log {filename} | except {except_} | match {match}
    """
    cli_command = ['show log {filename}',
        'show log {filename} | match {match}',
        'show log {filename} | except {except_} | match {match}']

    def cli(self, filename, output=None, except_=None, match=None):
        if not output:
            if match and except_:
                out = self.device.execute(self.cli_command[2].format(
                    filename=filename,
                    except_=except_,
                    match=match))
            elif match:
                out = self.device.execute(self.cli_command[1].format(
                    filename=filename,
                    match=match))
            else:
                out = self.device.execute(self.cli_command[0].format(filename=filename))
        else:
            out = output

        ret_dict = {}
        lines = out.splitlines()
        if len(lines) > 1:
            ret_dict['file-content'] = []
        p = re.compile(r"^(?!{).*")

        for line in lines:
            line = line.strip()
            m = p.match(line)
            if m:
                ret_dict['file-content'].append(line)

        return ret_dict

class ShowLogFilenameMatchExcept(ShowLogFilenameSchema):
    """ Parser for:
            * show log {filename} | match {match} | except {except}
    """
    cli_command = ['show log {filename} | match {match} | except {except_}']

    def cli(self, filename, except_, match, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0].format(
                filename=filename,
                except_=except_,
                match=match))
        else:
            out = output

        ret_dict = {}
        lines = out.splitlines()
        if len(lines) > 1:
            ret_dict['file-content'] = []
        p = re.compile(r"^(?!{).*")

        for line in lines:
            line = line.strip()
            m = p.match(line)
            if m:
                ret_dict['file-content'].append(line)

        return ret_dict

class ShowLogFilenameMatchExcept(ShowLogFilenameSchema):
    """ Parser for:
            * show log {filename} | match {match} | except {except}
    """
    cli_command = ['show log {filename} | match {match} | except {except_}']

    def cli(self, filename, except_, match, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0].format(
                filename=filename,
                except_=except_,
                match=match))
        else:
            out = output

        ret_dict = {}

        lines = out.splitlines()
        if len(lines) > 1:
            ret_dict['file-content'] = out.splitlines()[1:]

        return ret_dict