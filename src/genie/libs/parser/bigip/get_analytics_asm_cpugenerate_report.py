# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/asm-cpu/generate-report' resources
# =============================================


class AnalyticsAsmcpuGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsAsmcpuGeneratereport(AnalyticsAsmcpuGeneratereportSchema):
    """ To F5 resource for /mgmt/tm/analytics/asm-cpu/generate-report
    """

    cli_command = "/mgmt/tm/analytics/asm-cpu/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
