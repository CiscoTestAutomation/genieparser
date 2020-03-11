# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/ca-bundle-manager' resources
# =============================================


class SysCryptoCabundlemanagerSchema(MetaParser):

    schema = {}


class SysCryptoCabundlemanager(SysCryptoCabundlemanagerSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/ca-bundle-manager
    """

    cli_command = "/mgmt/tm/sys/crypto/ca-bundle-manager"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
