# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/persist' resources
# =============================================


class GtmPersistSchema(MetaParser):

    schema = {}


class GtmPersist(GtmPersistSchema):
    """ To F5 resource for /mgmt/tm/gtm/persist
    """

    cli_command = "/mgmt/tm/gtm/persist"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
