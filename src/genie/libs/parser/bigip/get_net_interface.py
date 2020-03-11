# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/interface' resources
# =============================================


class NetInterfaceSchema(MetaParser):

    schema = {}


class NetInterface(NetInterfaceSchema):
    """ To F5 resource for /mgmt/tm/net/interface
    """

    cli_command = "/mgmt/tm/net/interface"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
