# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/http-compression' resources
# =============================================


class LtmProfileHttpcompressionSchema(MetaParser):

    schema = {}


class LtmProfileHttpcompression(LtmProfileHttpcompressionSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/http-compression
    """

    cli_command = "/mgmt/tm/ltm/profile/http-compression"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
