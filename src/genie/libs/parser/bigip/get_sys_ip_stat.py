# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ip-stat' resources
# =============================================


class SysIpstatSchema(MetaParser):

    schema = {}


class SysIpstat(SysIpstatSchema):
    """ To F5 resource for /mgmt/tm/sys/ip-stat
    """

    cli_command = "/mgmt/tm/sys/ip-stat"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
