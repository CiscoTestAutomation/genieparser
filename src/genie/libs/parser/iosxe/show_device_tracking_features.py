''' ShowDeviceTrackingFeatures.py

IOSXE parsers for the following show commands:

    * show device-tracking features

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
        'features': {
            str: {
                'feature': str,
                'priority': int,
                'state': str
            }
        }
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

        #feature, priority and state
        p1 = re.compile(r'^(?P<feature>\S+.+\S+)\s+(?P<priority>\d+)\s+(?P<state>\w+)')

        parser_dict = {}

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            
            if m:
                features = parser_dict.setdefault('features', {})
                feature = features.setdefault(m.groupdict()['feature'], {})
                feature.update({'feature':  m.groupdict()['feature']})
                feature.update({'priority': int(m.groupdict()['priority'])})
                feature.update({'state':  m.groupdict()['state']})

        return parser_dict
