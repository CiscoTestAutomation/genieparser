# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/radius-server' resources
# =============================================


class AuthRadiusserverSchema(MetaParser):

    schema = {}


class AuthRadiusserver(AuthRadiusserverSchema):
    """ To F5 resource for /mgmt/tm/auth/radius-server
    """

    cli_command = "/mgmt/tm/auth/radius-server"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
