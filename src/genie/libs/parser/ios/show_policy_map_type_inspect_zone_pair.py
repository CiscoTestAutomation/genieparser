# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.iosxe.show_policy_map_type_inspect_zone_pair import ShowPolicyMapTypeInspectZonePair as ShowPolicyZonePair_iosxe 


class ShowPolicyMapTypeInspectZonePair(ShowPolicyZonePair_iosxe):

    """ Parser for:
      show policy-map type inspect zone-pair
      show policy-map type inspect zone-pair {zone_pair_name} """
    
    pass
