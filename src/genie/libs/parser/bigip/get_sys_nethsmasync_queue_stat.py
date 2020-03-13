# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/nethsm/async-queue-stat' resources
# =============================================


class SysNethsmAsyncqueuestatSchema(MetaParser):

    schema = {}


class SysNethsmAsyncqueuestat(SysNethsmAsyncqueuestatSchema):
    """ To F5 resource for /mgmt/tm/sys/nethsm/async-queue-stat
    """

    cli_command = "/mgmt/tm/sys/nethsm/async-queue-stat"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
