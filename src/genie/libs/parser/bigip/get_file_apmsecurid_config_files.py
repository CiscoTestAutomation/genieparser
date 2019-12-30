# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/file/apm/aaa/securid-config-files' resources
# =============================================


class FileApmSecuridconfigfilesSchema(MetaParser):

    schema = {}


class FileApmSecuridconfigfiles(FileApmSecuridconfigfilesSchema):
    """ To F5 resource for /mgmt/tm/file/apm/aaa/securid-config-files
    """

    cli_command = "/mgmt/tm/file/apm/aaa/securid-config-files"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
