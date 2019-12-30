# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/eviction-policy' resources
# =============================================


class LtmEvictionpolicySchema(MetaParser):

    schema = {}


class LtmEvictionpolicy(LtmEvictionpolicySchema):
    """ To F5 resource for /mgmt/tm/ltm/eviction-policy
    """

    cli_command = "/mgmt/tm/ltm/eviction-policy"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
