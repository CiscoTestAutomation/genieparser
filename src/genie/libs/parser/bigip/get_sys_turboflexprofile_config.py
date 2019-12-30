# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/turboflex/profile-config' resources
# =============================================


class SysTurboflexProfileconfigSchema(MetaParser):

    schema = {}


class SysTurboflexProfileconfig(SysTurboflexProfileconfigSchema):
    """ To F5 resource for /mgmt/tm/sys/turboflex/profile-config
    """

    cli_command = "/mgmt/tm/sys/turboflex/profile-config"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
