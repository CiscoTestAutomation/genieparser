# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/trunk' resources
# =============================================


class NetTrunkSchema(MetaParser):

    schema = {}


class NetTrunk(NetTrunkSchema):
    """ To F5 resource for /mgmt/tm/net/trunk
    """

    cli_command = "/mgmt/tm/net/trunk"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
