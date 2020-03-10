# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/application/apl-script' resources
# =============================================


class SysApplicationAplscriptSchema(MetaParser):

    schema = {}


class SysApplicationAplscript(SysApplicationAplscriptSchema):
    """ To F5 resource for /mgmt/tm/sys/application/apl-script
    """

    cli_command = "/mgmt/tm/sys/application/apl-script"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
