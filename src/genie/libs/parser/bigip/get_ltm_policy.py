# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/policy' resources
# =============================================


class LtmPolicySchema(MetaParser):

    schema = {}


class LtmPolicy(LtmPolicySchema):
    """ To F5 resource for /mgmt/tm/ltm/policy
    """

    cli_command = "/mgmt/tm/ltm/policy"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
