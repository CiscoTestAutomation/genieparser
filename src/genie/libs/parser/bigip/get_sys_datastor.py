# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/datastor' resources
# =============================================


class SysDatastorSchema(MetaParser):

    schema = {}


class SysDatastor(SysDatastorSchema):
    """ To F5 resource for /mgmt/tm/sys/datastor
    """

    cli_command = "/mgmt/tm/sys/datastor"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
