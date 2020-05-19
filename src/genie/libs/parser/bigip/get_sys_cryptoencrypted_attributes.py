# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/encrypted-attributes' resources
# =============================================


class SysCryptoEncryptedattributesSchema(MetaParser):

    schema = {}


class SysCryptoEncryptedattributes(SysCryptoEncryptedattributesSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/encrypted-attributes
    """

    cli_command = "/mgmt/tm/sys/crypto/encrypted-attributes"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
