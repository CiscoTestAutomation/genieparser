# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
 
# ==============================
# Schema for 'show ip alias'
# ==============================
class ShowIPAliasSchema(MetaParser):
 
    ''' Schema for "show ip alias" '''
    schema = {
        'ip_alias': 
            { Any():
                'address_type': str, 
                'ip_address': str, 
                Optional('port'): int
            }
        },
    }
