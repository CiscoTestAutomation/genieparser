# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/console' resources
# =============================================


class SysConsoleSchema(MetaParser):

    schema = {}


class SysConsole(SysConsoleSchema):
    """ To F5 resource for /mgmt/tm/sys/console
    """

    cli_command = "/mgmt/tm/sys/console"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
