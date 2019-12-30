# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/html-rule/comment-remove' resources
# =============================================


class LtmHtmlruleCommentremoveSchema(MetaParser):

    schema = {}


class LtmHtmlruleCommentremove(LtmHtmlruleCommentremoveSchema):
    """ To F5 resource for /mgmt/tm/ltm/html-rule/comment-remove
    """

    cli_command = "/mgmt/tm/ltm/html-rule/comment-remove"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
