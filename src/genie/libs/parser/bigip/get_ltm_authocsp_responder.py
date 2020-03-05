# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/auth/ocsp-responder' resources
# =============================================


class LtmAuthOcspresponderSchema(MetaParser):

    schema = {}


class LtmAuthOcspresponder(LtmAuthOcspresponderSchema):
    """ To F5 resource for /mgmt/tm/ltm/auth/ocsp-responder
    """

    cli_command = "/mgmt/tm/ltm/auth/ocsp-responder"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
