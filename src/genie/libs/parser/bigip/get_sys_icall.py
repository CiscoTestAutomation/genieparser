# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/icall' resources
# =============================================


class SysIcallSchema(MetaParser):

    schema = {}


class SysIcall(SysIcallSchema):
    """ To F5 resource for /mgmt/tm/sys/icall
    """

    cli_command = "/mgmt/tm/sys/icall"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
