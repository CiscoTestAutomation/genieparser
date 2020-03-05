# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cm/failover-status' resources
# =============================================


class CmFailoverstatusSchema(MetaParser):

    schema = {}


class CmFailoverstatus(CmFailoverstatusSchema):
    """ To F5 resource for /mgmt/tm/cm/failover-status
    """

    cli_command = "/mgmt/tm/cm/failover-status"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
