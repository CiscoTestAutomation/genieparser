# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/nat' resources
# =============================================


class LtmNatSchema(MetaParser):

    schema = {}


class LtmNat(LtmNatSchema):
    """ To F5 resource for /mgmt/tm/ltm/nat
    """

    cli_command = "/mgmt/tm/ltm/nat"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
