# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/auth' resources
# =============================================


class LtmAuthSchema(MetaParser):

    schema = {}


class LtmAuth(LtmAuthSchema):
    """ To F5 resource for /mgmt/tm/ltm/auth
    """

    cli_command = "/mgmt/tm/ltm/auth"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
