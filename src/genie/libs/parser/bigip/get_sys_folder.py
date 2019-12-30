# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/folder' resources
# =============================================


class SysFolderSchema(MetaParser):

    schema = {}


class SysFolder(SysFolderSchema):
    """ To F5 resource for /mgmt/tm/sys/folder
    """

    cli_command = "/mgmt/tm/sys/folder"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
