
# Python
import re
import logging
from collections import OrderedDict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

class ShowPlatformIntegritySchema(MetaParser):
    schema = {}

class ShowPlatformIntegrity(ShowPlatformIntegritySchema):
    cli_command = 'show platform integrity'
    def cli(output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        p1 = re.compile(r'^Platform: +(?P<platform>\S+)$')
        p2 = re.compile(r'^Boot +(?P<boot>\d+) +Version: +(?P<version>\S+)$')
        p3 = re.compile(r'^Boot +(?P<boot>\d+) +Hash: +(?P<hash>\S+)$')
        p4 = re.compile(r'^Boot +Loader +Version: +(?P<boot_loader_version>[\S ]+)$')
        p5 = re.compile(r'^Boot +Loader +Hash:$')
        p6 = re.compile(r'^(?P<hash>\S+)$')
        p7 = re.compile(r'^OS +Version: +(?P<os_version>\S+)$')
        p8 = re.compile(r'^OS +Hashes:$')
        p9 = re.compile(r'^\S+:$')