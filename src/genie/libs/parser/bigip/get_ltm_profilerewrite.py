# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/rewrite' resources
# =============================================


class LtmProfileRewriteSchema(MetaParser):

    schema = {}


class LtmProfileRewrite(LtmProfileRewriteSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/rewrite
    """

    cli_command = "/mgmt/tm/ltm/profile/rewrite"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
