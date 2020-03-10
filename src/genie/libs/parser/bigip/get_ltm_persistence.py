# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/persistence' resources
# =============================================


class LtmPersistenceSchema(MetaParser):

    schema = {}


class LtmPersistence(LtmPersistenceSchema):
    """ To F5 resource for /mgmt/tm/ltm/persistence
    """

    cli_command = "/mgmt/tm/ltm/persistence"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
