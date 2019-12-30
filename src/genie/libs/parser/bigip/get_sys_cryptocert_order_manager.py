# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/cert-order-manager' resources
# =============================================


class SysCryptoCertordermanagerSchema(MetaParser):

    schema = {}


class SysCryptoCertordermanager(SysCryptoCertordermanagerSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/cert-order-manager
    """

    cli_command = "/mgmt/tm/sys/crypto/cert-order-manager"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
