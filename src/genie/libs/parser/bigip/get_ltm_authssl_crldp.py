# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/auth/ssl-crldp' resources
# =============================================


class LtmAuthSslcrldpSchema(MetaParser):

    schema = {}


class LtmAuthSslcrldp(LtmAuthSslcrldpSchema):
    """ To F5 resource for /mgmt/tm/ltm/auth/ssl-crldp
    """

    cli_command = "/mgmt/tm/ltm/auth/ssl-crldp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
