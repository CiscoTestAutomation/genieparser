# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/remote-user' resources
# =============================================


class AuthRemoteuserSchema(MetaParser):

    schema = {}


class AuthRemoteuser(AuthRemoteuserSchema):
    """ To F5 resource for /mgmt/tm/auth/remote-user
    """

    cli_command = "/mgmt/tm/auth/remote-user"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
