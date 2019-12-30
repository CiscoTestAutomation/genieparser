# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/data-group' resources
# =============================================


class LtmDatagroupSchema(MetaParser):

    schema = {}


class LtmDatagroup(LtmDatagroupSchema):
    """ To F5 resource for /mgmt/tm/ltm/data-group
    """

    cli_command = "/mgmt/tm/ltm/data-group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
