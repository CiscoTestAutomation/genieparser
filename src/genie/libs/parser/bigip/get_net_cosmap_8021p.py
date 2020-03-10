# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/cos/map-8021p' resources
# =============================================


class NetCosMap8021pSchema(MetaParser):

    schema = {}


class NetCosMap8021p(NetCosMap8021pSchema):
    """ To F5 resource for /mgmt/tm/net/cos/map-8021p
    """

    cli_command = "/mgmt/tm/net/cos/map-8021p"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
