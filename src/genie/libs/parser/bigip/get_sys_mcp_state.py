# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/mcp-state' resources
# =============================================


class SysMcpstateSchema(MetaParser):

    schema = {}


class SysMcpstate(SysMcpstateSchema):
    """ To F5 resource for /mgmt/tm/sys/mcp-state
    """

    cli_command = "/mgmt/tm/sys/mcp-state"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
