# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/tmm-info' resources
# =============================================


class SysTmminfoSchema(MetaParser):

    schema = {}


class SysTmminfo(SysTmminfoSchema):
    """ To F5 resource for /mgmt/tm/sys/tmm-info
    """

    cli_command = "/mgmt/tm/sys/tmm-info"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
