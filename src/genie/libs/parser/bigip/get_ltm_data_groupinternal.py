# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/data-group/internal' resources
# =============================================


class LtmDatagroupInternalSchema(MetaParser):

    schema = {}


class LtmDatagroupInternal(LtmDatagroupInternalSchema):
    """ To F5 resource for /mgmt/tm/ltm/data-group/internal
    """

    cli_command = "/mgmt/tm/ltm/data-group/internal"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
