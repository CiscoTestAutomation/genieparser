# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/icall/script' resources
# =============================================


class SysIcallScriptSchema(MetaParser):

    schema = {}


class SysIcallScript(SysIcallScriptSchema):
    """ To F5 resource for /mgmt/tm/sys/icall/script
    """

    cli_command = "/mgmt/tm/sys/icall/script"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
