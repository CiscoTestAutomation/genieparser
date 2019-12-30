# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/rst-cause' resources
# =============================================


class NetRstcauseSchema(MetaParser):

    schema = {}


class NetRstcause(NetRstcauseSchema):
    """ To F5 resource for /mgmt/tm/net/rst-cause
    """

    cli_command = "/mgmt/tm/net/rst-cause"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
