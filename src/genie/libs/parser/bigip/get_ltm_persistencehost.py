# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/persistence/host' resources
# =============================================


class LtmPersistenceHostSchema(MetaParser):

    schema = {}


class LtmPersistenceHost(LtmPersistenceHostSchema):
    """ To F5 resource for /mgmt/tm/ltm/persistence/host
    """

    cli_command = "/mgmt/tm/ltm/persistence/host"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
