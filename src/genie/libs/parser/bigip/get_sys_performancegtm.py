# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/performance/gtm' resources
# =============================================


class SysPerformanceGtmSchema(MetaParser):

    schema = {}


class SysPerformanceGtm(SysPerformanceGtmSchema):
    """ To F5 resource for /mgmt/tm/sys/performance/gtm
    """

    cli_command = "/mgmt/tm/sys/performance/gtm"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
