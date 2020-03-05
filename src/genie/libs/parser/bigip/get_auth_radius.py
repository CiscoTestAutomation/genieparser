# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/radius' resources
# =============================================


class AuthRadiusSchema(MetaParser):

    schema = {}


class AuthRadius(AuthRadiusSchema):
    """ To F5 resource for /mgmt/tm/auth/radius
    """

    cli_command = "/mgmt/tm/auth/radius"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
