# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/hypervisor-info' resources
# =============================================


class SysHypervisorinfoSchema(MetaParser):

    schema = {}


class SysHypervisorinfo(SysHypervisorinfoSchema):
    """ To F5 resource for /mgmt/tm/sys/hypervisor-info
    """

    cli_command = "/mgmt/tm/sys/hypervisor-info"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
