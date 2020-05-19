# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/icall/handler/perpetual' resources
# =============================================


class SysIcallPerpetualSchema(MetaParser):

    schema = {}


class SysIcallPerpetual(SysIcallPerpetualSchema):
    """ To F5 resource for /mgmt/tm/sys/icall/handler/perpetual
    """

    cli_command = "/mgmt/tm/sys/icall/handler/perpetual"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
