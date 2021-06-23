''' ShowDeviceTrackingFeatures.py

IOSXE parsers for the following show commands:

    * show device-tracking-features

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ====================================================
# Schema for 'show device-tracking features
# ====================================================
class ShowDeviceTrackingFeaturesSchema(MetaParser):
    """ Schema for show device-tracking features """

    schema = {
        'features': 
        {Any(): 
            {'feature': str,
            'priority': int,
            'state': str
            }
        },
    }

# =============================================
# Parser for 'show device-tracking features'
# =============================================
class ShowDeviceTrackingFeatures(ShowDeviceTrackingFeaturesSchema):
    """ show device-tracking features """

    cli_command = 'show device-tracking features'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output


        p1 = re.compile(r'^(?P<feature>\S+.+\S+)\s+(?P<priority>\d+)\s+(?P<state>\w+)')

        parser_dict = {}

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                temp_dict = {}
                if 'features' not in parser_dict:
                    parser_dict.setdefault('features', {})
                g = m.groupdict()
                temp_dict['feature'] = g['feature']
                temp_dict['priority'] = int(g['priority'])
                temp_dict['state'] = g['state']

                parser_dict['features'][g['feature']] = temp_dict 
      
        return parser_dict
