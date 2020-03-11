# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/clock' resources
# =============================================


class SysClockSchema(MetaParser):

    schema = {}


class SysClock(SysClockSchema):
    """ To F5 resource for /mgmt/tm/sys/clock
    """

    cli_command = "/mgmt/tm/sys/clock"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
