# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ipfix' resources
# =============================================


class SysIpfixSchema(MetaParser):

    schema = {}


class SysIpfix(SysIpfixSchema):
    """ To F5 resource for /mgmt/tm/sys/ipfix
    """

    cli_command = "/mgmt/tm/sys/ipfix"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
