# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/state-mirroring' resources
# =============================================


class SysStatemirroringSchema(MetaParser):

    schema = {}


class SysStatemirroring(SysStatemirroringSchema):
    """ To F5 resource for /mgmt/tm/sys/state-mirroring
    """

    cli_command = "/mgmt/tm/sys/state-mirroring"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
