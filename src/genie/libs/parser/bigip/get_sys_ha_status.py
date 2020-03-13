# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ha-status' resources
# =============================================


class SysHastatusSchema(MetaParser):

    schema = {}


class SysHastatus(SysHastatusSchema):
    """ To F5 resource for /mgmt/tm/sys/ha-status
    """

    cli_command = "/mgmt/tm/sys/ha-status"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
