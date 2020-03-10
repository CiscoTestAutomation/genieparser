# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/tunnels/etherip' resources
# =============================================


class NetTunnelsEtheripSchema(MetaParser):

    schema = {}


class NetTunnelsEtherip(NetTunnelsEtheripSchema):
    """ To F5 resource for /mgmt/tm/net/tunnels/etherip
    """

    cli_command = "/mgmt/tm/net/tunnels/etherip"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
