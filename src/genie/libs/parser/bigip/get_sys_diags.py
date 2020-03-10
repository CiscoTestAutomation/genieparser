# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/diags' resources
# =============================================


class SysDiagsSchema(MetaParser):

    schema = {}


class SysDiags(SysDiagsSchema):
    """ To F5 resource for /mgmt/tm/sys/diags
    """

    cli_command = "/mgmt/tm/sys/diags"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
