# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/ipother' resources
# =============================================


class LtmProfileIpotherSchema(MetaParser):

    schema = {}


class LtmProfileIpother(LtmProfileIpotherSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/ipother
    """

    cli_command = "/mgmt/tm/ltm/profile/ipother"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
