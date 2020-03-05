# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/cert-validator' resources
# =============================================


class SysCryptoCertvalidatorSchema(MetaParser):

    schema = {}


class SysCryptoCertvalidator(SysCryptoCertvalidatorSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/cert-validator
    """

    cli_command = "/mgmt/tm/sys/crypto/cert-validator"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
