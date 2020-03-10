# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/global-settings/rule' resources
# =============================================


class LtmGlobalsettingsRuleSchema(MetaParser):

    schema = {}


class LtmGlobalsettingsRule(LtmGlobalsettingsRuleSchema):
    """ To F5 resource for /mgmt/tm/ltm/global-settings/rule
    """

    cli_command = "/mgmt/tm/ltm/global-settings/rule"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
