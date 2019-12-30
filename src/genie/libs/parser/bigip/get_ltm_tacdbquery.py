# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/tacdb/query' resources
# =============================================


class LtmTacdbQuerySchema(MetaParser):

    schema = {}


class LtmTacdbQuery(LtmTacdbQuerySchema):
    """ To F5 resource for /mgmt/tm/ltm/tacdb/query
    """

    cli_command = "/mgmt/tm/ltm/tacdb/query"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
