
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

class ShowInterfacesSchema(MetaParser):
    schema = {'interfaces': list}