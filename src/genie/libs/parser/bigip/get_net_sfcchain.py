# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/sfc/chain' resources
# =============================================


class NetSfcChainSchema(MetaParser):

    schema = {}


class NetSfcChain(NetSfcChainSchema):
    """ To F5 resource for /mgmt/tm/net/sfc/chain
    """

    cli_command = "/mgmt/tm/net/sfc/chain"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
