# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/rtsp' resources
# =============================================


class LtmProfileRtspSchema(MetaParser):

    schema = {}


class LtmProfileRtsp(LtmProfileRtspSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/rtsp
    """

    cli_command = "/mgmt/tm/ltm/profile/rtsp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
