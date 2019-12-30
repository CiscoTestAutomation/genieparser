# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/tacdb/licenseddb' resources
# =============================================


class LtmTacdbLicenseddbSchema(MetaParser):

    schema = {}


class LtmTacdbLicenseddb(LtmTacdbLicenseddbSchema):
    """ To F5 resource for /mgmt/tm/ltm/tacdb/licenseddb
    """

    cli_command = "/mgmt/tm/ltm/tacdb/licenseddb"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
