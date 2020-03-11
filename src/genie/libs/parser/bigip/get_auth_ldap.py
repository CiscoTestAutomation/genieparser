# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/ldap' resources
# =============================================


class AuthLdapSchema(MetaParser):

    schema = {}


class AuthLdap(AuthLdapSchema):
    """ To F5 resource for /mgmt/tm/auth/ldap
    """

    cli_command = "/mgmt/tm/auth/ldap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
