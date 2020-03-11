# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/allow-key-export' resources
# =============================================


class SysCryptoAllowkeyexportSchema(MetaParser):

    schema = {}


class SysCryptoAllowkeyexport(SysCryptoAllowkeyexportSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/allow-key-export
    """

    cli_command = "/mgmt/tm/sys/crypto/allow-key-export"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
