# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/version' resources
# =============================================


class SysVersionSchema(MetaParser):

    schema = {}


class SysVersion(SysVersionSchema):
    """ To F5 resource for /mgmt/tm/sys/version
    """

    cli_command = "/mgmt/tm/sys/version"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
