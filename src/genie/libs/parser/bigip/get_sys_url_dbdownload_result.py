# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/url-db/download-result' resources
# =============================================


class SysUrldbDownloadresultSchema(MetaParser):

    schema = {}


class SysUrldbDownloadresult(SysUrldbDownloadresultSchema):
    """ To F5 resource for /mgmt/tm/sys/url-db/download-result
    """

    cli_command = "/mgmt/tm/sys/url-db/download-result"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
