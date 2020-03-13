# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/icall/istats-trigger' resources
# =============================================


class SysIcallIstatstriggerSchema(MetaParser):

    schema = {}


class SysIcallIstatstrigger(SysIcallIstatstriggerSchema):
    """ To F5 resource for /mgmt/tm/sys/icall/istats-trigger
    """

    cli_command = "/mgmt/tm/sys/icall/istats-trigger"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
