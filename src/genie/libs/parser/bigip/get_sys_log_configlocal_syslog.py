# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/log-config/destination/local-syslog' resources
# =============================================


class SysLogconfigLocalsyslogSchema(MetaParser):

    schema = {}


class SysLogconfigLocalsyslog(SysLogconfigLocalsyslogSchema):
    """ To F5 resource for /mgmt/tm/sys/log-config/destination/local-syslog
    """

    cli_command = "/mgmt/tm/sys/log-config/destination/local-syslog"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
