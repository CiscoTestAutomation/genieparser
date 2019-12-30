# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/cert-validator/ocsp' resources
# =============================================


class SysCryptoOcspSchema(MetaParser):

    schema = {}


class SysCryptoOcsp(SysCryptoOcspSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/cert-validator/ocsp
    """

    cli_command = "/mgmt/tm/sys/crypto/cert-validator/ocsp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
