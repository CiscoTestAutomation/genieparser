# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/auth/partition' resources
# =============================================


class AuthPartitionSchema(MetaParser):

    schema = {}


class AuthPartition(AuthPartitionSchema):
    """ To F5 resource for /mgmt/tm/auth/partition
    """

    cli_command = "/mgmt/tm/auth/partition"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
