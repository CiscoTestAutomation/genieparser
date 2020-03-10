# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/performance' resources
# =============================================


class SysPerformanceSchema(MetaParser):

    schema = {}


class SysPerformance(SysPerformanceSchema):
    """ To F5 resource for /mgmt/tm/sys/performance
    """

    cli_command = "/mgmt/tm/sys/performance"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
