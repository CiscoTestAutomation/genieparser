# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/daemon-log-settings/tmm' resources
# =============================================


class SysDaemonlogsettingsTmmSchema(MetaParser):

    schema = {}


class SysDaemonlogsettingsTmm(SysDaemonlogsettingsTmmSchema):
    """ To F5 resource for /mgmt/tm/sys/daemon-log-settings/tmm
    """

    cli_command = "/mgmt/tm/sys/daemon-log-settings/tmm"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
