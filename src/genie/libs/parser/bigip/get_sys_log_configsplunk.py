# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/log-config/destination/splunk' resources
# =============================================


class SysLogconfigSplunkSchema(MetaParser):

    schema = {}


class SysLogconfigSplunk(SysLogconfigSplunkSchema):
    """ To F5 resource for /mgmt/tm/sys/log-config/destination/splunk
    """

    cli_command = "/mgmt/tm/sys/log-config/destination/splunk"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
