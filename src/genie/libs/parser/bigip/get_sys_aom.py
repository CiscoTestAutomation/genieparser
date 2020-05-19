# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/aom' resources
# =============================================


class SysAomSchema(MetaParser):

    schema = {}


class SysAom(SysAomSchema):
    """ To F5 resource for /mgmt/tm/sys/aom
    """

    cli_command = "/mgmt/tm/sys/aom"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
