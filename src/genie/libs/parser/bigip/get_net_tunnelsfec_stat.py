# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/tunnels/fec-stat' resources
# =============================================


class NetTunnelsFecstatSchema(MetaParser):

    schema = {}


class NetTunnelsFecstat(NetTunnelsFecstatSchema):
    """ To F5 resource for /mgmt/tm/net/tunnels/fec-stat
    """

    cli_command = "/mgmt/tm/net/tunnels/fec-stat"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
