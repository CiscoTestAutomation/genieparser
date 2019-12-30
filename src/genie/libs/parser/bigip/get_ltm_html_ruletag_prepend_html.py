# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/html-rule/tag-prepend-html' resources
# =============================================


class LtmHtmlruleTagprependhtmlSchema(MetaParser):

    schema = {}


class LtmHtmlruleTagprependhtml(LtmHtmlruleTagprependhtmlSchema):
    """ To F5 resource for /mgmt/tm/ltm/html-rule/tag-prepend-html
    """

    cli_command = "/mgmt/tm/ltm/html-rule/tag-prepend-html"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
