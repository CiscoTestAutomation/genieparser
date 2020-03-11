# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/diags/ihealth-result' resources
# =============================================


class SysDiagsIhealthresultSchema(MetaParser):

    schema = {}


class SysDiagsIhealthresult(SysDiagsIhealthresultSchema):
    """ To F5 resource for /mgmt/tm/sys/diags/ihealth-result
    """

    cli_command = "/mgmt/tm/sys/diags/ihealth-result"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
