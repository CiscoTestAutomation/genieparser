# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/connection' resources
# =============================================


class SysConnectionSchema(MetaParser):

    schema = {}


class SysConnection(SysConnectionSchema):
    """ To F5 resource for /mgmt/tm/sys/connection
    """

    cli_command = "/mgmt/tm/sys/connection"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
