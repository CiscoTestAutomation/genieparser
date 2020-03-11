# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/node' resources
# =============================================


class LtmNodeSchema(MetaParser):

    schema = {}


class LtmNode(LtmNodeSchema):
    """ To F5 resource for /mgmt/tm/ltm/node
    """

    cli_command = "/mgmt/tm/ltm/node"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
