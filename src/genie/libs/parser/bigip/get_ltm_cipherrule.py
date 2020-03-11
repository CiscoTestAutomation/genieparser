# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/cipher/rule' resources
# =============================================


class LtmCipherRuleSchema(MetaParser):

    schema = {}


class LtmCipherRule(LtmCipherRuleSchema):
    """ To F5 resource for /mgmt/tm/ltm/cipher/rule
    """

    cli_command = "/mgmt/tm/ltm/cipher/rule"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
