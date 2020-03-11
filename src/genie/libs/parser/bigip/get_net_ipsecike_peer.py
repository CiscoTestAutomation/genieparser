# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/ipsec/ike-peer' resources
# =============================================


class NetIpsecIkepeerSchema(MetaParser):

    schema = {}


class NetIpsecIkepeer(NetIpsecIkepeerSchema):
    """ To F5 resource for /mgmt/tm/net/ipsec/ike-peer
    """

    cli_command = "/mgmt/tm/net/ipsec/ike-peer"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
