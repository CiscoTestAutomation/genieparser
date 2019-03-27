

#Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

class ShowCdpSchema(MetaParser):
    
    schema = {
        'cdp':
            {'devices': 
    		  {Any():
    			{'id': str,
    			'local_interface': str,
    			'hold_time': int,
    			Optional('capability'): str,
    			'platform': str,
    			'port_id': str,
    			},
    		},
        },
    }