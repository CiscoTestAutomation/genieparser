# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/ipsec/traffic-selector' resources
# =============================================


class NetIpsecTrafficselectorSchema(MetaParser):

    schema = {}


class NetIpsecTrafficselector(NetIpsecTrafficselectorSchema):
    """ To F5 resource for /mgmt/tm/net/ipsec/traffic-selector
    """

    cli_command = "/mgmt/tm/net/ipsec/traffic-selector"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
