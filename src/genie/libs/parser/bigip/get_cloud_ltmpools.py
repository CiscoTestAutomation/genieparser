# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cloud/ltm/pools' resources
# =============================================


class CloudLtmPoolsSchema(MetaParser):

    schema = {}


class CloudLtmPools(CloudLtmPoolsSchema):
    """ To F5 resource for /mgmt/tm/cloud/ltm/pools
    """

    cli_command = "/mgmt/tm/cloud/ltm/pools"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
