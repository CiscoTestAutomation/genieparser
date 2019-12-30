# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/turboflex/warning' resources
# =============================================


class SysTurboflexWarningSchema(MetaParser):

    schema = {}


class SysTurboflexWarning(SysTurboflexWarningSchema):
    """ To F5 resource for /mgmt/tm/sys/turboflex/warning
    """

    cli_command = "/mgmt/tm/sys/turboflex/warning"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
