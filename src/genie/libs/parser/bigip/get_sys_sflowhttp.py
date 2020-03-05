# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/sflow/data-source/http' resources
# =============================================


class SysSflowHttpSchema(MetaParser):

    schema = {}


class SysSflowHttp(SysSflowHttpSchema):
    """ To F5 resource for /mgmt/tm/sys/sflow/data-source/http
    """

    cli_command = "/mgmt/tm/sys/sflow/data-source/http"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
