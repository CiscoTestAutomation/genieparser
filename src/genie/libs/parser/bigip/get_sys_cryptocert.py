# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/cert' resources
# =============================================


class SysCryptoCertSchema(MetaParser):

    schema = {}


class SysCryptoCert(SysCryptoCertSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/cert
    """

    cli_command = "/mgmt/tm/sys/crypto/cert"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
