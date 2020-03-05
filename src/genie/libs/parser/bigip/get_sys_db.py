# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/db' resources
# =============================================


class SysDbSchema(MetaParser):

    schema = {}


class SysDb(SysDbSchema):
    """ To F5 resource for /mgmt/tm/sys/db
    """

    cli_command = "/mgmt/tm/sys/db"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
