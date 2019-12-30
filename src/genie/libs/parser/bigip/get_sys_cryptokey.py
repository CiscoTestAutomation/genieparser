# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/key' resources
# =============================================


class SysCryptoKeySchema(MetaParser):

    schema = {}


class SysCryptoKey(SysCryptoKeySchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/key
    """

    cli_command = "/mgmt/tm/sys/crypto/key"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
