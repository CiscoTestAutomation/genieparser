# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/client' resources
# =============================================


class SysCryptoClientSchema(MetaParser):

    schema = {}


class SysCryptoClient(SysCryptoClientSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/client
    """

    cli_command = "/mgmt/tm/sys/crypto/client"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
