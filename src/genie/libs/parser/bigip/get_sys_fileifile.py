# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/file/ifile' resources
# =============================================


class SysFileIfileSchema(MetaParser):

    schema = {}


class SysFileIfile(SysFileIfileSchema):
    """ To F5 resource for /mgmt/tm/sys/file/ifile
    """

    cli_command = "/mgmt/tm/sys/file/ifile"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
