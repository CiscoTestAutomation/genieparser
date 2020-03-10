# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/fastl4' resources
# =============================================


class LtmProfileFastl4Schema(MetaParser):

    schema = {}


class LtmProfileFastl4(LtmProfileFastl4Schema):
    """ To F5 resource for /mgmt/tm/ltm/profile/fastl4
    """

    cli_command = "/mgmt/tm/ltm/profile/fastl4"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
