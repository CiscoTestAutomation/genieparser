# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ucs' resources
# =============================================


class SysUcsSchema(MetaParser):

    schema = {}


class SysUcs(SysUcsSchema):
    """ To F5 resource for /mgmt/tm/sys/ucs
    """

    cli_command = "/mgmt/tm/sys/ucs"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
