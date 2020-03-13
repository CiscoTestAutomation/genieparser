# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/cert-ldap' resources
# =============================================


class AuthCertldapSchema(MetaParser):

    schema = {}


class AuthCertldap(AuthCertldapSchema):
    """ To F5 resource for /mgmt/tm/auth/cert-ldap
    """

    cli_command = "/mgmt/tm/auth/cert-ldap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
