# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/adc/fileobject/ssl-key' resources
# =============================================


class AdcFileobjectSslkeySchema(MetaParser):

    schema = {}


class AdcFileobjectSslkey(AdcFileobjectSslkeySchema):
    """ To F5 resource for /mgmt/tm/adc/fileobject/ssl-key
    """

    cli_command = "/mgmt/tm/adc/fileobject/ssl-key"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
