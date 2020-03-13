# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/persistence/source-addr' resources
# =============================================


class LtmPersistenceSourceaddrSchema(MetaParser):

    schema = {}


class LtmPersistenceSourceaddr(LtmPersistenceSourceaddrSchema):
    """ To F5 resource for /mgmt/tm/ltm/persistence/source-addr
    """

    cli_command = "/mgmt/tm/ltm/persistence/source-addr"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
