""" show_redundancy.py

AireOS parser for the following command:
    * 'show redundancy'

"""

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

log = logging.getLogger(__name__)

class ShowRedundancySummarySchema(MetaParser):
    """ Schema for show boot """

    schema = {
        'redundancy_mode': str,
        'local_state': str,
        'peer_state': str,
        'unit': str,
        'unit_id': str,
        'redundancy_state': str,
        'mobility_mac': str,
        'redundancy_port':str,
    }

class ShowRedundancySummary(ShowRedundancySummarySchema):
    """ Parser for show redundancy summary"""

    cli_command = 'show redundancy summary'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        parsed_dict = {}

        #Redundancy Mode = SSO ENABLED 
        #Local State = ACTIVE 
        #Peer State = STANDBY HOT 
        #Unit = Primary
        #Unit ID = 70:EA:1A:AE:01:4D
        #Redundancy State = SSO
        #Mobility MAC = 70:EA:1A:AE:01:4D
        #Redundancy Port  = UP
    
        p_redundancy_mode = re.compile(r"^Redundancy +Mode = (?P<redundancy_mode>.+)$")
        p_local_state = re.compile(r"^Local +State = (?P<local_state>.+)$")
        p_peer_state = re.compile(r"^Peer +State = (?P<peer_state>.+)$")
        p_unit = re.compile(r"^Unit = (?P<unit>.+)$")
        p_unit_id = re.compile(r"^Unit ID = (?P<unit_id>.+)$")
        p_redundancy_state = re.compile(r"^Redundancy State = (?P<redundancy_state>.+)$")
        p_mobility_mac = re.compile(r"^Mobility MAC = (?P<mobility_mac>.+)$")
        p_redundancy_port = re.compile(r"^Redundancy Port  = (?P<redundancy_port>.+)$")


        for line in out.splitlines():
            line = line.strip()


            if p_redundancy_mode.match(line):
             match = p_redundancy_mode.match(line)
             parsed_dict.update({ "redundancy_mode": match.group("redundancy_mode") })
             continue
            elif p_local_state.match(line):
             match = p_local_state.match(line)
             parsed_dict.update({ "local_state": match.group("local_state") })
             continue
            elif p_peer_state.match(line):
             match = p_peer_state.match(line)
             parsed_dict.update({ "peer_state": match.group("peer_state") })
             continue
            elif p_unit.match(line):
             match = p_unit.match(line)
             parsed_dict.update({ "unit": match.group("unit") })
             continue
            elif p_unit_id.match(line):
             match = p_unit_id.match(line)
             parsed_dict.update({ "unit_id": match.group("unit_id") })
             continue
            elif p_redundancy_state.match(line):
             match = p_redundancy_state.match(line)
             parsed_dict.update({ "redundancy_state": match.group("redundancy_state") })
             continue
            elif p_mobility_mac.match(line):
             match = p_mobility_mac.match(line)
             parsed_dict.update({ "mobility_mac": match.group("mobility_mac") })
             continue
            elif p_redundancy_port.match(line):
             match = p_redundancy_port.match(line)
             parsed_dict.update({ "redundancy_port": match.group("redundancy_port") })
          
        return parsed_dict
