# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/file/apm/policy/customization-group' resources
# =============================================


class FileApmCustomizationgroupSchema(MetaParser):

    schema = {}


class FileApmCustomizationgroup(FileApmCustomizationgroupSchema):
    """ To F5 resource for /mgmt/tm/file/apm/policy/customization-group
    """

    cli_command = "/mgmt/tm/file/apm/policy/customization-group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
