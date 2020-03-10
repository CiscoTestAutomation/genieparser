# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/self' resources
# =============================================


class NetSelfSchema(MetaParser):

    schema = {}


class NetSelf(NetSelfSchema):
    """ To F5 resource for /mgmt/tm/net/self
    """

    cli_command = "/mgmt/tm/net/self"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
