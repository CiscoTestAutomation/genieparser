# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ha-group' resources
# =============================================


class SysHagroupSchema(MetaParser):

    schema = {}


class SysHagroup(SysHagroupSchema):
    """ To F5 resource for /mgmt/tm/sys/ha-group
    """

    cli_command = "/mgmt/tm/sys/ha-group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
