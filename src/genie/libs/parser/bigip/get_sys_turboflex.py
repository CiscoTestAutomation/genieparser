# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/turboflex' resources
# =============================================


class SysTurboflexSchema(MetaParser):

    schema = {}


class SysTurboflex(SysTurboflexSchema):
    """ To F5 resource for /mgmt/tm/sys/turboflex
    """

    cli_command = "/mgmt/tm/sys/turboflex"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
