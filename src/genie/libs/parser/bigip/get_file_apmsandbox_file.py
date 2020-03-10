# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/file/apm/resource/sandbox-file' resources
# =============================================


class FileApmSandboxfileSchema(MetaParser):

    schema = {}


class FileApmSandboxfile(FileApmSandboxfileSchema):
    """ To F5 resource for /mgmt/tm/file/apm/resource/sandbox-file
    """

    cli_command = "/mgmt/tm/file/apm/resource/sandbox-file"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
