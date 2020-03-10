# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/rule' resources
# =============================================


class GtmRuleSchema(MetaParser):

    schema = {}


class GtmRule(GtmRuleSchema):
    """ To F5 resource for /mgmt/tm/gtm/rule
    """

    cli_command = "/mgmt/tm/gtm/rule"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
