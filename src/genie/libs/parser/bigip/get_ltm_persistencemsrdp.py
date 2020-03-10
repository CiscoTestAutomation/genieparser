# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/persistence/msrdp' resources
# =============================================


class LtmPersistenceMsrdpSchema(MetaParser):

    schema = {}


class LtmPersistenceMsrdp(LtmPersistenceMsrdpSchema):
    """ To F5 resource for /mgmt/tm/ltm/persistence/msrdp
    """

    cli_command = "/mgmt/tm/ltm/persistence/msrdp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
