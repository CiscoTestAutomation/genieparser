# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/failover' resources
# =============================================


class SysFailoverSchema(MetaParser):

    schema = {}


class SysFailover(SysFailoverSchema):
    """ To F5 resource for /mgmt/tm/sys/failover
    """

    cli_command = "/mgmt/tm/sys/failover"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
