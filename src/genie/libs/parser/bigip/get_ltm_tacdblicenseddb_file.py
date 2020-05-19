# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/tacdb/licenseddb-file' resources
# =============================================


class LtmTacdbLicenseddbfileSchema(MetaParser):

    schema = {}


class LtmTacdbLicenseddbfile(LtmTacdbLicenseddbfileSchema):
    """ To F5 resource for /mgmt/tm/ltm/tacdb/licenseddb-file
    """

    cli_command = "/mgmt/tm/ltm/tacdb/licenseddb-file"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
