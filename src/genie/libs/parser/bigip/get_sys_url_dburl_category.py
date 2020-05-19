# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/url-db/url-category' resources
# =============================================


class SysUrldbUrlcategorySchema(MetaParser):

    schema = {}


class SysUrldbUrlcategory(SysUrldbUrlcategorySchema):
    """ To F5 resource for /mgmt/tm/sys/url-db/url-category
    """

    cli_command = "/mgmt/tm/sys/url-db/url-category"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
