# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/auth/ldap' resources
# =============================================


class LtmAuthLdapSchema(MetaParser):

    schema = {}


class LtmAuthLdap(LtmAuthLdapSchema):
    """ To F5 resource for /mgmt/tm/ltm/auth/ldap
    """

    cli_command = "/mgmt/tm/ltm/auth/ldap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
