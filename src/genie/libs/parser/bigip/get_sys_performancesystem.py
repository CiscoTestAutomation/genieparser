# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/performance/system' resources
# =============================================


class SysPerformanceSystemSchema(MetaParser):

    schema = {}


class SysPerformanceSystem(SysPerformanceSystemSchema):
    """ To F5 resource for /mgmt/tm/sys/performance/system
    """

    cli_command = "/mgmt/tm/sys/performance/system"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
