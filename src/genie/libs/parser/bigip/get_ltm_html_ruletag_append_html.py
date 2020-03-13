# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/html-rule/tag-append-html' resources
# =============================================


class LtmHtmlruleTagappendhtmlSchema(MetaParser):

    schema = {}


class LtmHtmlruleTagappendhtml(LtmHtmlruleTagappendhtmlSchema):
    """ To F5 resource for /mgmt/tm/ltm/html-rule/tag-append-html
    """

    cli_command = "/mgmt/tm/ltm/html-rule/tag-append-html"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
