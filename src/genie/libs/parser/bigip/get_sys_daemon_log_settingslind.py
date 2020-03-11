# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/daemon-log-settings/lind' resources
# =============================================


class SysDaemonlogsettingsLindSchema(MetaParser):

    schema = {}


class SysDaemonlogsettingsLind(SysDaemonlogsettingsLindSchema):
    """ To F5 resource for /mgmt/tm/sys/daemon-log-settings/lind
    """

    cli_command = "/mgmt/tm/sys/daemon-log-settings/lind"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
