# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/distributed-app' resources
# =============================================


class GtmDistributedappSchema(MetaParser):

    schema = {}


class GtmDistributedapp(GtmDistributedappSchema):
    """ To F5 resource for /mgmt/tm/gtm/distributed-app
    """

    cli_command = "/mgmt/tm/gtm/distributed-app"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
