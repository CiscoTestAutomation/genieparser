# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/fix' resources
# =============================================


class LtmProfileFixSchema(MetaParser):

    schema = {}


class LtmProfileFix(LtmProfileFixSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/fix
    """

    cli_command = "/mgmt/tm/ltm/profile/fix"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
