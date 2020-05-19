# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/cipher/group' resources
# =============================================


class LtmCipherGroupSchema(MetaParser):

    schema = {}


class LtmCipherGroup(LtmCipherGroupSchema):
    """ To F5 resource for /mgmt/tm/ltm/cipher/group
    """

    cli_command = "/mgmt/tm/ltm/cipher/group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
