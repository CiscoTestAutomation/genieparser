# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/performance/all-stats' resources
# =============================================


class SysPerformanceAllstatsSchema(MetaParser):

    schema = {}


class SysPerformanceAllstats(SysPerformanceAllstatsSchema):
    """ To F5 resource for /mgmt/tm/sys/performance/all-stats
    """

    cli_command = "/mgmt/tm/sys/performance/all-stats"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
