# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/nethsm' resources
# =============================================


class SysNethsmSchema(MetaParser):

    schema = {}


class SysNethsm(SysNethsmSchema):
    """ To F5 resource for /mgmt/tm/sys/nethsm
    """

    cli_command = "/mgmt/tm/sys/nethsm"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
