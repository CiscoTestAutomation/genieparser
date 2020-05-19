# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/pop3' resources
# =============================================


class LtmProfilePop3Schema(MetaParser):

    schema = {}


class LtmProfilePop3(LtmProfilePop3Schema):
    """ To F5 resource for /mgmt/tm/ltm/profile/pop3
    """

    cli_command = "/mgmt/tm/ltm/profile/pop3"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
