# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/fix-connection' resources
# =============================================


class SysFixconnectionSchema(MetaParser):

    schema = {}


class SysFixconnection(SysFixconnectionSchema):
    """ To F5 resource for /mgmt/tm/sys/fix-connection
    """

    cli_command = "/mgmt/tm/sys/fix-connection"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
