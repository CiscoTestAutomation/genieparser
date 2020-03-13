# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/log-config/destination/alertd' resources
# =============================================


class SysLogconfigAlertdSchema(MetaParser):

    schema = {}


class SysLogconfigAlertd(SysLogconfigAlertdSchema):
    """ To F5 resource for /mgmt/tm/sys/log-config/destination/alertd
    """

    cli_command = "/mgmt/tm/sys/log-config/destination/alertd"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
