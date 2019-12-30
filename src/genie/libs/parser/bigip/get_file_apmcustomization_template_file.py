# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/file/apm/policy/customization-template-file' resources
# =============================================


class FileApmCustomizationtemplatefileSchema(MetaParser):

    schema = {}


class FileApmCustomizationtemplatefile(FileApmCustomizationtemplatefileSchema):
    """ To F5 resource for /mgmt/tm/file/apm/policy/customization-template-file
    """

    cli_command = "/mgmt/tm/file/apm/policy/customization-template-file"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
