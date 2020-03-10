# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/remote-role' resources
# =============================================


class AuthRemoteroleSchema(MetaParser):

    schema = {}


class AuthRemoterole(AuthRemoteroleSchema):
    """ To F5 resource for /mgmt/tm/auth/remote-role
    """

    cli_command = "/mgmt/tm/auth/remote-role"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
