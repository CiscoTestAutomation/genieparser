# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cloud/ltm/pool-members' resources
# =============================================


class CloudLtmPoolmembersSchema(MetaParser):

    schema = {}


class CloudLtmPoolmembers(CloudLtmPoolmembersSchema):
    """ To F5 resource for /mgmt/tm/cloud/ltm/pool-members
    """

    cli_command = "/mgmt/tm/cloud/ltm/pool-members"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
