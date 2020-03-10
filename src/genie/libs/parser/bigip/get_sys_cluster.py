# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/cluster' resources
# =============================================


class SysClusterSchema(MetaParser):

    schema = {}


class SysCluster(SysClusterSchema):
    """ To F5 resource for /mgmt/tm/sys/cluster
    """

    cli_command = "/mgmt/tm/sys/cluster"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
