# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto' resources
# =============================================


class SysCryptoSchema(MetaParser):

    schema = {}


class SysCrypto(SysCryptoSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto
    """

    cli_command = "/mgmt/tm/sys/crypto"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
