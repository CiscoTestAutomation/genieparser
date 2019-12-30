# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/icall/handler' resources
# =============================================


class SysIcallHandlerSchema(MetaParser):

    schema = {}


class SysIcallHandler(SysIcallHandlerSchema):
    """ To F5 resource for /mgmt/tm/sys/icall/handler
    """

    cli_command = "/mgmt/tm/sys/icall/handler"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
