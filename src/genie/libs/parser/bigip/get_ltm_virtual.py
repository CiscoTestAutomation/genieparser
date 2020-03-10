# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/virtual' resources
# =============================================


class LtmVirtualSchema(MetaParser):

    schema = {}


class LtmVirtual(LtmVirtualSchema):
    """ To F5 resource for /mgmt/tm/ltm/virtual
    """

    cli_command = "/mgmt/tm/ltm/virtual"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
