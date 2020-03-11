# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ready' resources
# =============================================


class SysReadySchema(MetaParser):

    schema = {}


class SysReady(SysReadySchema):
    """ To F5 resource for /mgmt/tm/sys/ready
    """

    cli_command = "/mgmt/tm/sys/ready"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
