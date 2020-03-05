# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/sfc' resources
# =============================================


class NetSfcSchema(MetaParser):

    schema = {}


class NetSfc(NetSfcSchema):
    """ To F5 resource for /mgmt/tm/net/sfc
    """

    cli_command = "/mgmt/tm/net/sfc"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
