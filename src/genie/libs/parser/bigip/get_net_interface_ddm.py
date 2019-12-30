# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/interface-ddm' resources
# =============================================


class NetInterfaceddmSchema(MetaParser):

    schema = {}


class NetInterfaceddm(NetInterfaceddmSchema):
    """ To F5 resource for /mgmt/tm/net/interface-ddm
    """

    cli_command = "/mgmt/tm/net/interface-ddm"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
