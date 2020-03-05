# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/source' resources
# =============================================


class AuthSourceSchema(MetaParser):

    schema = {}


class AuthSource(AuthSourceSchema):
    """ To F5 resource for /mgmt/tm/auth/source
    """

    cli_command = "/mgmt/tm/auth/source"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
