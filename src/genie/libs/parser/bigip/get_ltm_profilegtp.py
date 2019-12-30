# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/gtp' resources
# =============================================


class LtmProfileGtpSchema(MetaParser):

    schema = {}


class LtmProfileGtp(LtmProfileGtpSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/gtp
    """

    cli_command = "/mgmt/tm/ltm/profile/gtp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
