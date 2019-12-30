# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/auth/kerberos-delegation' resources
# =============================================


class LtmAuthKerberosdelegationSchema(MetaParser):

    schema = {}


class LtmAuthKerberosdelegation(LtmAuthKerberosdelegationSchema):
    """ To F5 resource for /mgmt/tm/ltm/auth/kerberos-delegation
    """

    cli_command = "/mgmt/tm/ltm/auth/kerberos-delegation"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
