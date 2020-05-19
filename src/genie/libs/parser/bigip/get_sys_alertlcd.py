# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/alert/lcd' resources
# =============================================


class SysAlertLcdSchema(MetaParser):

    schema = {}


class SysAlertLcd(SysAlertLcdSchema):
    """ To F5 resource for /mgmt/tm/sys/alert/lcd
    """

    cli_command = "/mgmt/tm/sys/alert/lcd"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
