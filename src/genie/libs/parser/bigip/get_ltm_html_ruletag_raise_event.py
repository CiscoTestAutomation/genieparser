# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/html-rule/tag-raise-event' resources
# =============================================


class LtmHtmlruleTagraiseeventSchema(MetaParser):

    schema = {}


class LtmHtmlruleTagraiseevent(LtmHtmlruleTagraiseeventSchema):
    """ To F5 resource for /mgmt/tm/ltm/html-rule/tag-raise-event
    """

    cli_command = "/mgmt/tm/ltm/html-rule/tag-raise-event"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
