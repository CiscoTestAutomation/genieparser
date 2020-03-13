# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/auth/tacacs' resources
# =============================================


class LtmAuthTacacsSchema(MetaParser):

    schema = {}


class LtmAuthTacacs(LtmAuthTacacsSchema):
    """ To F5 resource for /mgmt/tm/ltm/auth/tacacs
    """

    cli_command = "/mgmt/tm/ltm/auth/tacacs"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
