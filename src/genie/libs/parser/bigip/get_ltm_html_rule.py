# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/html-rule' resources
# =============================================


class LtmHtmlruleSchema(MetaParser):

    schema = {}


class LtmHtmlrule(LtmHtmlruleSchema):
    """ To F5 resource for /mgmt/tm/ltm/html-rule
    """

    cli_command = "/mgmt/tm/ltm/html-rule"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
