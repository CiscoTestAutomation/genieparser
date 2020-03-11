# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/tacdb/customdb' resources
# =============================================


class LtmTacdbCustomdbSchema(MetaParser):

    schema = {}


class LtmTacdbCustomdb(LtmTacdbCustomdbSchema):
    """ To F5 resource for /mgmt/tm/ltm/tacdb/customdb
    """

    cli_command = "/mgmt/tm/ltm/tacdb/customdb"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
