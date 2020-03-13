# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cm/traffic-group' resources
# =============================================


class CmTrafficgroupSchema(MetaParser):

    schema = {}


class CmTrafficgroup(CmTrafficgroupSchema):
    """ To F5 resource for /mgmt/tm/cm/traffic-group
    """

    cli_command = "/mgmt/tm/cm/traffic-group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
