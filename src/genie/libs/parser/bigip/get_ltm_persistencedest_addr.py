# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/persistence/dest-addr' resources
# =============================================


class LtmPersistenceDestaddrSchema(MetaParser):

    schema = {}


class LtmPersistenceDestaddr(LtmPersistenceDestaddrSchema):
    """ To F5 resource for /mgmt/tm/ltm/persistence/dest-addr
    """

    cli_command = "/mgmt/tm/ltm/persistence/dest-addr"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
