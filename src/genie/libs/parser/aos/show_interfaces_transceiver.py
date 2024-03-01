"""show_interfaces_transceiver.py

"""
import re
import logging

from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Any, Optional


logger = logging.getLogger(__name__)


def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value, expression))
    return match

# ====================================================
#  schema for show interfacces transceiver
# ====================================================
class ShowInterfacesTransceiverSchema(MetaParser):
    """Schema for show interfaces transciever"""
    schema = {
        'port':{
            Any():{
                Optional('port'): str,
                Optional('type'): str,
                Optional('productNumber'): str,
                Optional('serialNumber'): str,
                Optional('partNumber'): str,
                Optional('port1'): str,
                Optional('type1'): str,
                Optional('productNumber1'): str,
                Optional('serialNumber1'): str,
                Optional('partNumber1'): str,
                                    }
                },
            }

# ====================================================
#  parser for show interfaces transceiver
# ====================================================
class ShowInterfacesTransceiver(ShowInterfacesTransceiverSchema):
    """Parser for show interfaces transceiver"""
    cli_command = 'show interfaces transceiver'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


#                      Product      Serial             Part
#  Port    Type        Number       Number             Number
#  ------- ----------- ------------ ------------------ ----------
#  A1      SFP+SR      J9150A       N012218DB123       1990-4065
#  A2      SFP+SR      J9150A       N012218DB123       1990-4065

# Transceiver Technical Information:

#                      Product      Serial             Part
#  Port    Type        Number       Number             Number
#  ------- ----------- ------------ ------------------ ----------

        try:
            p0 = re.compile(r'\s+?(?P<port>([A-Z0-9]+?\/?[A-Z0-9]+?|\-+?))\s+?(?P<type>((([0-9A-Z]+\+?[0-9A-Z]+))|(\*?)|\-+))\s+?(?P<productNumber>(([A-Z0-9\+]+?)|\-+))\s+?(?P<serialNumber>([A-Z0-9]+)|\-+||(\?\??)?)\s+(?P<partNumber>(([a-z0-9]+\-?[a-z0-9]+?)|\-+))?$')
        except:
            p0 = re.compile(r'\s+?(?P<port>(No))\s(?P<type>(trans))(?P<productNumber>(ceiver))?\s?(?P<serialNumber>(pres))(?P<partNumber>(ent))?$')
        id_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue


#                      Product      Serial             Part
#  Port    Type        Number       Number             Number
#  ------- ----------- ------------ ------------------ ----------
#  A1      SFP+SR      J9150A       N012218DB123       1990-4065
#  A2      SFP+SR      J9150A       N012218DB123       1990-4065

# Transceiver Technical Information:

#                      Product      Serial             Part
#  Port    Type        Number       Number             Number
#  ------- ----------- ------------ ------------------ ----------


            m = p0.match(line)
            if m:
                id = m.groupdict()['port']
                if 'port' not in id_dict:
                    id_dict['port'] = {}

                if id not in id_dict:
                    id_dict['port'][id] = {}

                id_dict['port'][id]['port'] = id
                id_dict['port'][id]['type'] = m.groupdict()['type']
                id_dict['port'][id]['productNumber'] = m.groupdict()['productNumber']
                id_dict['port'][id]['serialNumber'] = m.groupdict()['serialNumber']
                id_dict['port'][id]['partNumber'] = m.groupdict()['partNumber']

        return id_dict
