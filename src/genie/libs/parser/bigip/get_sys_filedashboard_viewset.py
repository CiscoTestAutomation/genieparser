# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/file/dashboard-viewset' resources
# =============================================


class SysFileDashboardviewsetSchema(MetaParser):

    schema = {}


class SysFileDashboardviewset(SysFileDashboardviewsetSchema):
    """ To F5 resource for /mgmt/tm/sys/file/dashboard-viewset
    """

    cli_command = "/mgmt/tm/sys/file/dashboard-viewset"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
