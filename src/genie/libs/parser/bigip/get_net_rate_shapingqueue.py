# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/rate-shaping/queue' resources
# =============================================


class NetRateshapingQueueSchema(MetaParser):

    schema = {}


class NetRateshapingQueue(NetRateshapingQueueSchema):
    """ To F5 resource for /mgmt/tm/net/rate-shaping/queue
    """

    cli_command = "/mgmt/tm/net/rate-shaping/queue"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
