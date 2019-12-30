# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/tacdb/customdb-file' resources
# =============================================


class LtmTacdbCustomdbfileSchema(MetaParser):

    schema = {}


class LtmTacdbCustomdbfile(LtmTacdbCustomdbfileSchema):
    """ To F5 resource for /mgmt/tm/ltm/tacdb/customdb-file
    """

    cli_command = "/mgmt/tm/ltm/tacdb/customdb-file"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
