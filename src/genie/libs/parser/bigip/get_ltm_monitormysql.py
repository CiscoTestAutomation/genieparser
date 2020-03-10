# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/mysql' resources
# =============================================


class LtmMonitorMysqlSchema(MetaParser):

    schema = {}


class LtmMonitorMysql(LtmMonitorMysqlSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/mysql
    """

    cli_command = "/mgmt/tm/ltm/monitor/mysql"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
