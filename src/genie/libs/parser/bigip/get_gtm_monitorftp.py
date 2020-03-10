# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/ftp' resources
# =============================================


class GtmMonitorFtpSchema(MetaParser):

    schema = {}


class GtmMonitorFtp(GtmMonitorFtpSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/ftp
    """

    cli_command = "/mgmt/tm/gtm/monitor/ftp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
