# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/sync-status' resources
# =============================================


class GtmSyncstatusSchema(MetaParser):

    schema = {}


class GtmSyncstatus(GtmSyncstatusSchema):
    """ To F5 resource for /mgmt/tm/gtm/sync-status
    """

    cli_command = "/mgmt/tm/gtm/sync-status"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
