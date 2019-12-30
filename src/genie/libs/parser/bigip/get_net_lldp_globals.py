# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/lldp-globals' resources
# =============================================


class NetLldpglobalsSchema(MetaParser):

    schema = {}


class NetLldpglobals(NetLldpglobalsSchema):
    """ To F5 resource for /mgmt/tm/net/lldp-globals
    """

    cli_command = "/mgmt/tm/net/lldp-globals"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
