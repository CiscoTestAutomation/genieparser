# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/tacacs' resources
# =============================================


class AuthTacacsSchema(MetaParser):

    schema = {}


class AuthTacacs(AuthTacacsSchema):
    """ To F5 resource for /mgmt/tm/auth/tacacs
    """

    cli_command = "/mgmt/tm/auth/tacacs"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
