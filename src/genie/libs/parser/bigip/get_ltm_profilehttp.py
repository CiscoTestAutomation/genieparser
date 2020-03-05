# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/http' resources
# =============================================


class LtmProfileHttpSchema(MetaParser):

    schema = {}


class LtmProfileHttp(LtmProfileHttpSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/http
    """

    cli_command = "/mgmt/tm/ltm/profile/http"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
