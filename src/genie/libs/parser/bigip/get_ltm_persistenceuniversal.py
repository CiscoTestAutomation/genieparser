# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/persistence/universal' resources
# =============================================


class LtmPersistenceUniversalSchema(MetaParser):

    schema = {}


class LtmPersistenceUniversal(LtmPersistenceUniversalSchema):
    """ To F5 resource for /mgmt/tm/ltm/persistence/universal
    """

    cli_command = "/mgmt/tm/ltm/persistence/universal"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
