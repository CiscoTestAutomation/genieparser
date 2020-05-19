# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/sync-sys-files' resources
# =============================================


class SysSyncsysfilesSchema(MetaParser):

    schema = {}


class SysSyncsysfiles(SysSyncsysfilesSchema):
    """ To F5 resource for /mgmt/tm/sys/sync-sys-files
    """

    cli_command = "/mgmt/tm/sys/sync-sys-files"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
