# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/autoscale-group' resources
# =============================================


class SysAutoscalegroupSchema(MetaParser):

    schema = {}


class SysAutoscalegroup(SysAutoscalegroupSchema):
    """ To F5 resource for /mgmt/tm/sys/autoscale-group
    """

    cli_command = "/mgmt/tm/sys/autoscale-group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
