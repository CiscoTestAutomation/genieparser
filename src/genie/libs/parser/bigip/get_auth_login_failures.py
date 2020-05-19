# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/login-failures' resources
# =============================================


class AuthLoginfailuresSchema(MetaParser):

    schema = {}


class AuthLoginfailures(AuthLoginfailuresSchema):
    """ To F5 resource for /mgmt/tm/auth/login-failures
    """

    cli_command = "/mgmt/tm/auth/login-failures"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
