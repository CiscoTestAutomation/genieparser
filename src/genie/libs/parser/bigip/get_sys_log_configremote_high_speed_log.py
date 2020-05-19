# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/log-config/destination/remote-high-speed-log' resources
# =============================================


class SysLogconfigRemotehighspeedlogSchema(MetaParser):

    schema = {}


class SysLogconfigRemotehighspeedlog(SysLogconfigRemotehighspeedlogSchema):
    """ To F5 resource for /mgmt/tm/sys/log-config/destination/remote-high-speed-log
    """

    cli_command = "/mgmt/tm/sys/log-config/destination/remote-high-speed-log"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
