# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/html-rule/comment-raise-event' resources
# =============================================


class LtmHtmlruleCommentraiseeventSchema(MetaParser):

    schema = {}


class LtmHtmlruleCommentraiseevent(LtmHtmlruleCommentraiseeventSchema):
    """ To F5 resource for /mgmt/tm/ltm/html-rule/comment-raise-event
    """

    cli_command = "/mgmt/tm/ltm/html-rule/comment-raise-event"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
