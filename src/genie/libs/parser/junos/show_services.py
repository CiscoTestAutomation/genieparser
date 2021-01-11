''' show_services.py

JUNOS parsers for the following commands:
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema)


class ShowServicesAccountingAggregationTemplateSchema(MetaParser):
    """ Schema for:
            * show services accounting aggregation template template-name {name} extensive
    """

    schema = {
                "services-accounting-information": {
                    "flow-aggregate-template-detail": {
                        "flow-aggregate-template-detail-ipv4": {
                            "detail-entry": {
                                "source-address": str,
                                "destination-address": str,
                                "source-port": str,
                                "destination-port": str,
                                "protocol": {
                                    "@junos:format": str, 
                                    "#text": str},
                                "tos": str,
                                "tcp-flags": str,
                                "source-mask": str,
                                "destination-mask": str,
                                "input-snmp-interface-index": str,
                                "output-snmp-interface-index": str,
                                "start-time": str,
                                "end-time": str,
                                "packet-count": str,
                                "byte-count": str,
                            },
                        }
                    },
                }
            }

class ShowServicesAccountingAggregationTemplate(ShowServicesAccountingAggregationTemplateSchema):
    """ Parser for:
            * show services accounting aggregation template template-name {name} extensive
    """

    pass

class ShowServicesAccountingUsageSchema(MetaParser):
    """ Schema for:
            * show services accounting usage
    """

    def validate_usage_information(value):
        if not isinstance(value, list):
            raise SchemaTypeError('Usage information is not a list')
    
        usage_information = Schema({
                        "interface-name": str,
                        "uptime": str,
                        "inttime": str,
                        "five-second-load": str,
                        "one-minute-load": str,
                    })
    
        for item in value:
            usage_information.validate(item)
        return value

    schema = {
                "services-accounting-information": {
                    "usage-information": Use(validate_usage_information),
                }
            }


class ShowServicesAccountingUsage(ShowServicesAccountingUsageSchema):
    """ Parser for:
            * show services accounting usage
    """

    cli_command = "show services accounting usage"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # CPU utilization
        p1 = re.compile(r'^CPU +utilization$')

        # ms-9/0/0
        p2 = re.compile(r'^(?P<interface_name>\S+)$')

        # Uptime: 79203479 milliseconds, Interrupt time: 0 microseconds
        p3 = re.compile(r'^Uptime: (?P<uptime>\d+) +milliseconds, '
                        r'+Interrupt +time: +(?P<inttime>\d+) +microseconds$')

        # Load (5 second): 1%, Load (1 minute): 1%
        p4 = re.compile(r'^Load +\(5 +second\): +(?P<five_second_load>\d+)%, '
                        r'+Load +\(1 +minute\): +(?P<one_minute_load>\d+)%$')

        for line in out.splitlines():
            line = line.strip()

            # CPU utilization
            m = p1.match(line)
            if m:
                group = m.groupdict()
                continue

            # ms-9/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                usage_information_list = ret_dict.setdefault(
                    'services-accounting-information', {}
                    ).setdefault('usage-information', [])
                usage_information_dict = {"interface-name": group['interface_name']}
                usage_information_list.append(usage_information_dict)
                continue

            # Uptime: 79203479 milliseconds, Interrupt time: 0 microseconds
            m = p3.match(line)
            if m:
                group = m.groupdict()
                usage_information_dict.update({
                    "uptime": group["uptime"],
                    "inttime": group["inttime"],
                })
                continue

            # Load (5 second): 1%, Load (1 minute): 1%
            m = p4.match(line)
            if m:
                group = m.groupdict()
                usage_information_dict.update({
                    "five-second-load": group["five_second_load"],
                    "one-minute-load": group["one_minute_load"],
                })
                continue

        return ret_dict