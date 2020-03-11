# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/mroute' resources
# =============================================


class NetMrouteSchema(MetaParser):

    schema = {}


class NetMroute(NetMrouteSchema):
    """ To F5 resource for /mgmt/tm/net/mroute
    """

    cli_command = "/mgmt/tm/net/mroute"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
