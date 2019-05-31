"""
    interface.py
    DNAC parsers for the following show commands:

    * /dna/intent/api/v1/interface
"""

import os
import logging
import pprint
import re
import unittest
from genie import parsergen
from collections import defaultdict

from ats.log.utils import banner

from genie.metaparser import MetaParser
from genie.metaparser.util import merge_dict, keynames_convert
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use
# import parser utils
from genie.libs.parser.utils.common import Common

logger = logging.getLogger(__name__)


class Interface(MetaParser):
    """schema for /dna/intent/api/v1/interface"""

    schema = {
               Any(): {},
             }


class Interfaces(InterfacesSchema):
    """parser for /dna/intent/api/v1/interface"""

    cli_command = ['/dna/intent/api/v1/interface']

    def cli(self,interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.get(cmd)
        else:
            out = output

        return {}
