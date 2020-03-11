# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/splitsessionclient' resources
# =============================================


class LtmProfileSplitsessionclientSchema(MetaParser):

    schema = {}


class LtmProfileSplitsessionclient(LtmProfileSplitsessionclientSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/splitsessionclient
    """

    cli_command = "/mgmt/tm/ltm/profile/splitsessionclient"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
