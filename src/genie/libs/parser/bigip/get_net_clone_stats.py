# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/clone-stats' resources
# =============================================


class NetClonestatsSchema(MetaParser):

    schema = {}


class NetClonestats(NetClonestatsSchema):
    """ To F5 resource for /mgmt/tm/net/clone-stats
    """

    cli_command = "/mgmt/tm/net/clone-stats"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
