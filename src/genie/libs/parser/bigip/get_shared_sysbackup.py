# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/shared/sys/backup' resources
# =============================================


class SharedSysBackupSchema(MetaParser):

    schema = {}


class SharedSysBackup(SharedSysBackupSchema):
    """ To F5 resource for /mgmt/tm/shared/sys/backup
    """

    cli_command = "/mgmt/tm/shared/sys/backup"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
