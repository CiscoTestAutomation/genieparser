# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/software/hotfix' resources
# =============================================


class SysSoftwareHotfixSchema(MetaParser):

    schema = {}


class SysSoftwareHotfix(SysSoftwareHotfixSchema):
    """ To F5 resource for /mgmt/tm/sys/software/hotfix
    """

    cli_command = "/mgmt/tm/sys/software/hotfix"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
