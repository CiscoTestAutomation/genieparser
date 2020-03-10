# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/address-list' resources
# =============================================


class NetAddresslistSchema(MetaParser):

    schema = {}


class NetAddresslist(NetAddresslistSchema):
    """ To F5 resource for /mgmt/tm/net/address-list
    """

    cli_command = "/mgmt/tm/net/address-list"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
