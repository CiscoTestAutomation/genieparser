''' show_smnp.py

JUNOS parsers for the following commands:
    * show snmp mib walk system
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)


class ShowSnmpMibWalkSystemSchema(MetaParser):
    """ Schema for:
            * show snmp mib walk system
    """

    # Sub Schema snmp-object
    def validate_snmp_object_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('snmp-object is not a list')
        snmp_object_schema = Schema({
                    "name": str,
                    "object-value": str,
                    Optional("object-value-type"): str,
                    Optional("oid"): str
                })
        # Validate each dictionary in list
        for item in value:
            snmp_object_schema.validate(item)
        return value

    schema = {
        "snmp-object-information": {
            "snmp-object": Use(validate_snmp_object_list),
        }
    }


class ShowSnmpMibWalkSystem(ShowSnmpMibWalkSystemSchema):
    """ Parser for:
            * show snmp mib walk system
    """
    cli_command = 'show snmp mib walk system'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # sysContact.0  = KHK
        p1 = re.compile(r'^(?P<name>\S+) += +(?P<object_value>.+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()

                snmp_object_list = ret_dict.setdefault("snmp-object-information", {})\
                    .setdefault("snmp-object",[])

                entry = {}
                entry['name'] = group['name']
                entry['object-value'] = group["object_value"]

                snmp_object_list.append(entry)

        return ret_dict
