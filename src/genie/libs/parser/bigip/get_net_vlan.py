# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/vlan' resources
# =============================================


class NetVlanSchema(MetaParser):

    schema = {}


class NetVlan(NetVlanSchema):
    """ To F5 resource for /mgmt/tm/net/vlan
    """

    cli_command = "/mgmt/tm/net/vlan"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
