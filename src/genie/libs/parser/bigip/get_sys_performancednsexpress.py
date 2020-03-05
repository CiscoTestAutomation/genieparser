# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/performance/dnsexpress' resources
# =============================================


class SysPerformanceDnsexpressSchema(MetaParser):

    schema = {}


class SysPerformanceDnsexpress(SysPerformanceDnsexpressSchema):
    """ To F5 resource for /mgmt/tm/sys/performance/dnsexpress
    """

    cli_command = "/mgmt/tm/sys/performance/dnsexpress"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
