# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/data-group/external' resources
# =============================================


class LtmDatagroupExternalSchema(MetaParser):

    schema = {}


class LtmDatagroupExternal(LtmDatagroupExternalSchema):
    """ To F5 resource for /mgmt/tm/ltm/data-group/external
    """

    cli_command = "/mgmt/tm/ltm/data-group/external"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
