# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/scriptd' resources
# =============================================


class SysScriptdSchema(MetaParser):

    schema = {}


class SysScriptd(SysScriptdSchema):
    """ To F5 resource for /mgmt/tm/sys/scriptd
    """

    cli_command = "/mgmt/tm/sys/scriptd"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
