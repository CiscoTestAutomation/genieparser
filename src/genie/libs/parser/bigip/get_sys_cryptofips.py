# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/fips' resources
# =============================================


class SysCryptoFipsSchema(MetaParser):

    schema = {}


class SysCryptoFips(SysCryptoFipsSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/fips
    """

    cli_command = "/mgmt/tm/sys/crypto/fips"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
