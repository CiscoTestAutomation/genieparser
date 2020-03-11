# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cloud/ltm/node-addresses' resources
# =============================================


class CloudLtmNodeaddressesSchema(MetaParser):

    schema = {}


class CloudLtmNodeaddresses(CloudLtmNodeaddressesSchema):
    """ To F5 resource for /mgmt/tm/cloud/ltm/node-addresses
    """

    cli_command = "/mgmt/tm/cloud/ltm/node-addresses"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
