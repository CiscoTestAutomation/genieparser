# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/pool' resources
# =============================================


class LtmPoolSchema(MetaParser):

    schema = {}


class LtmPool(LtmPoolSchema):
    """ To F5 resource for /mgmt/tm/ltm/pool
    """

    cli_command = "/mgmt/tm/ltm/pool"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
