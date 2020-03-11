# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/cert-validator/crl' resources
# =============================================


class SysCryptoCrlSchema(MetaParser):

    schema = {}


class SysCryptoCrl(SysCryptoCrlSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/cert-validator/crl
    """

    cli_command = "/mgmt/tm/sys/crypto/cert-validator/crl"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
