# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/ipsec' resources
# =============================================


class NetIpsecSchema(MetaParser):

    schema = {}


class NetIpsec(NetIpsecSchema):
    """ To F5 resource for /mgmt/tm/net/ipsec
    """

    cli_command = "/mgmt/tm/net/ipsec"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
