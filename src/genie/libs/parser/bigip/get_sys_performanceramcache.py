# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/performance/ramcache' resources
# =============================================


class SysPerformanceRamcacheSchema(MetaParser):

    schema = {}


class SysPerformanceRamcache(SysPerformanceRamcacheSchema):
    """ To F5 resource for /mgmt/tm/sys/performance/ramcache
    """

    cli_command = "/mgmt/tm/sys/performance/ramcache"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
