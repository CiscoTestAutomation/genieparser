# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/bwc' resources
# =============================================


class NetBwcSchema(MetaParser):

    schema = {}


class NetBwc(NetBwcSchema):
    """ To F5 resource for /mgmt/tm/net/bwc
    """

    cli_command = "/mgmt/tm/net/bwc"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
