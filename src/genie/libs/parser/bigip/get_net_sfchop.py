# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/sfc/hop' resources
# =============================================


class NetSfcHopSchema(MetaParser):

    schema = {}


class NetSfcHop(NetSfcHopSchema):
    """ To F5 resource for /mgmt/tm/net/sfc/hop
    """

    cli_command = "/mgmt/tm/net/sfc/hop"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
