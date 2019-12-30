# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/smtps' resources
# =============================================


class LtmProfileSmtpsSchema(MetaParser):

    schema = {}


class LtmProfileSmtps(LtmProfileSmtpsSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/smtps
    """

    cli_command = "/mgmt/tm/ltm/profile/smtps"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
