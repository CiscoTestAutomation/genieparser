# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/file/system-ssl-key' resources
# =============================================


class SysFileSystemsslkeySchema(MetaParser):

    schema = {}


class SysFileSystemsslkey(SysFileSystemsslkeySchema):
    """ To F5 resource for /mgmt/tm/sys/file/system-ssl-key
    """

    cli_command = "/mgmt/tm/sys/file/system-ssl-key"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
