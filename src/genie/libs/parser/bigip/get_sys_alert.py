# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/alert' resources
# =============================================


class SysAlertSchema(MetaParser):

    schema = {}


class SysAlert(SysAlertSchema):
    """ To F5 resource for /mgmt/tm/sys/alert
    """

    cli_command = "/mgmt/tm/sys/alert"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
