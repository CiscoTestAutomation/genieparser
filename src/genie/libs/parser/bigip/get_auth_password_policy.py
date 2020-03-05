# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/password-policy' resources
# =============================================


class AuthPasswordpolicySchema(MetaParser):

    schema = {}


class AuthPasswordpolicy(AuthPasswordpolicySchema):
    """ To F5 resource for /mgmt/tm/auth/password-policy
    """

    cli_command = "/mgmt/tm/auth/password-policy"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
