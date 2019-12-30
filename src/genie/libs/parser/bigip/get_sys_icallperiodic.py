# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/icall/handler/periodic' resources
# =============================================


class SysIcallPeriodicSchema(MetaParser):

    schema = {}


class SysIcallPeriodic(SysIcallPeriodicSchema):
    """ To F5 resource for /mgmt/tm/sys/icall/handler/periodic
    """

    cli_command = "/mgmt/tm/sys/icall/handler/periodic"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
