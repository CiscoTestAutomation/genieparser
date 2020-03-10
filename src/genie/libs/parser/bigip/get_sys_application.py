# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/application' resources
# =============================================


class SysApplicationSchema(MetaParser):

    schema = {}


class SysApplication(SysApplicationSchema):
    """ To F5 resource for /mgmt/tm/sys/application
    """

    cli_command = "/mgmt/tm/sys/application"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
