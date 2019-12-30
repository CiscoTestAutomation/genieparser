# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/daemon-log-settings/mcpd' resources
# =============================================


class SysDaemonlogsettingsMcpdSchema(MetaParser):

    schema = {}


class SysDaemonlogsettingsMcpd(SysDaemonlogsettingsMcpdSchema):
    """ To F5 resource for /mgmt/tm/sys/daemon-log-settings/mcpd
    """

    cli_command = "/mgmt/tm/sys/daemon-log-settings/mcpd"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
