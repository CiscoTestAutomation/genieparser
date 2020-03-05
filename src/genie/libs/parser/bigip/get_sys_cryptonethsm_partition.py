# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/crypto/fips/nethsm-partition' resources
# =============================================


class SysCryptoNethsmpartitionSchema(MetaParser):

    schema = {}


class SysCryptoNethsmpartition(SysCryptoNethsmpartitionSchema):
    """ To F5 resource for /mgmt/tm/sys/crypto/fips/nethsm-partition
    """

    cli_command = "/mgmt/tm/sys/crypto/fips/nethsm-partition"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
