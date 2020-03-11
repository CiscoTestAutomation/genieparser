# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/ifile' resources
# =============================================


class LtmIfileSchema(MetaParser):

    schema = {}


class LtmIfile(LtmIfileSchema):
    """ To F5 resource for /mgmt/tm/ltm/ifile
    """

    cli_command = "/mgmt/tm/ltm/ifile"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
