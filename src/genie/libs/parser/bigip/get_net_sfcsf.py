# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/sfc/sf' resources
# =============================================


class NetSfcSfSchema(MetaParser):

    schema = {}


class NetSfcSf(NetSfcSfSchema):
    """ To F5 resource for /mgmt/tm/net/sfc/sf
    """

    cli_command = "/mgmt/tm/net/sfc/sf"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
