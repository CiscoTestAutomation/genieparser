# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/cos' resources
# =============================================


class NetCosSchema(MetaParser):

    schema = {}


class NetCos(NetCosSchema):
    """ To F5 resource for /mgmt/tm/net/cos
    """

    cli_command = "/mgmt/tm/net/cos"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
