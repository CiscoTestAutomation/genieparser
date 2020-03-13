# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/tunnels/ipip' resources
# =============================================


class NetTunnelsIpipSchema(MetaParser):

    schema = {}


class NetTunnelsIpip(NetTunnelsIpipSchema):
    """ To F5 resource for /mgmt/tm/net/tunnels/ipip
    """

    cli_command = "/mgmt/tm/net/tunnels/ipip"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
