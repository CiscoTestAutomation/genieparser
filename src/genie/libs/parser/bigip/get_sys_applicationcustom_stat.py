# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/application/custom-stat' resources
# =============================================


class SysApplicationCustomstatSchema(MetaParser):

    schema = {}


class SysApplicationCustomstat(SysApplicationCustomstatSchema):
    """ To F5 resource for /mgmt/tm/sys/application/custom-stat
    """

    cli_command = "/mgmt/tm/sys/application/custom-stat"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
