# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/user' resources
# =============================================


class AuthUserSchema(MetaParser):

    schema = {}


class AuthUser(AuthUserSchema):
    """ To F5 resource for /mgmt/tm/auth/user
    """

    cli_command = "/mgmt/tm/auth/user"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
