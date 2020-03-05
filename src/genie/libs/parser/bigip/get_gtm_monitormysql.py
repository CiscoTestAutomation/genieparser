# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/mysql' resources
# =============================================


class GtmMonitorMysqlSchema(MetaParser):

    schema = {}


class GtmMonitorMysql(GtmMonitorMysqlSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/mysql
    """

    cli_command = "/mgmt/tm/gtm/monitor/mysql"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
