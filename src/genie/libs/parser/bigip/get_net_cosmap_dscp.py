# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/cos/map-dscp' resources
# =============================================


class NetCosMapdscpSchema(MetaParser):

    schema = {}


class NetCosMapdscp(NetCosMapdscpSchema):
    """ To F5 resource for /mgmt/tm/net/cos/map-dscp
    """

    cli_command = "/mgmt/tm/net/cos/map-dscp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
