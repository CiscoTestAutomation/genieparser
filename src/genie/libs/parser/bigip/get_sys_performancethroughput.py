# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/performance/throughput' resources
# =============================================


class SysPerformanceThroughputSchema(MetaParser):

    schema = {}


class SysPerformanceThroughput(SysPerformanceThroughputSchema):
    """ To F5 resource for /mgmt/tm/sys/performance/throughput
    """

    cli_command = "/mgmt/tm/sys/performance/throughput"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
