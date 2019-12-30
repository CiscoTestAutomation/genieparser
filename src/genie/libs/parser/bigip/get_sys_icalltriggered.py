# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/icall/handler/triggered' resources
# =============================================


class SysIcallTriggeredSchema(MetaParser):

    schema = {}


class SysIcallTriggered(SysIcallTriggeredSchema):
    """ To F5 resource for /mgmt/tm/sys/icall/handler/triggered
    """

    cli_command = "/mgmt/tm/sys/icall/handler/triggered"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
