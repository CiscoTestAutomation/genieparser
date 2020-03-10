# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/diags/ihealth-request' resources
# =============================================


class SysDiagsIhealthrequestSchema(MetaParser):

    schema = {}


class SysDiagsIhealthrequest(SysDiagsIhealthrequestSchema):
    """ To F5 resource for /mgmt/tm/sys/diags/ihealth-request
    """

    cli_command = "/mgmt/tm/sys/diags/ihealth-request"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
