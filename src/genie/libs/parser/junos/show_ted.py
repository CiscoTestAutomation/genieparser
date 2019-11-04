"""show_ted.py

JunOS parsers for the following show commands:

"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common


# =======================================================
# Schema for 'show interfaces terse [| match <interface>]
# =======================================================
class ShowTedDatabaseExtensiveSchema(MetaParser):
    """Schema for show interfaces terse [| match <interface>]"""

    schema = {
        'isis_nodes': int,
        'inet_nodes': int,
        'node': {
            Any(): {
                'type': str,
                'age': int,
                'link_in': int,
                'link_out': int,
                Optional('protocol'): {
                    Any(): {  # ospf
                        Any(): {  # to_local_remote
                            'to': str,
                            'local': str,
                            'remote': str,
                            'local_interface_index': int,
                            'remote_interface_index': int,
                            Optional('color'): str,
                            'metric': int,
                            Optional('static_bw'): str,
                            Optional('reservable_bw'): str,
                            Optional('available_bw'): {
                                Any(): {  # priority
                                    'bw': str
                                }
                            },
                            'interface_switching': {
                                'switching_type': str,
                                'encoding_type': str,
                                'maximum_lsp_bw': {
                                    Any(): {
                                        'bw': str
                                    }
                                }
                            },
                            'p2p_adj_sid': {
                                'sid': {
                                    Any(): {
                                        'address_family': str,
                                        'flags': str,
                                        'weight': int
                                    }
                                }
                            },
                        },
                        'prefixes': {
                            Any(): {  # prefix
                                'flags': str,
                                'prefix_sid': {
                                    'sid': int,
                                    'flags': str,
                                    'algo': int
                                }
                            }
                        },
                        'spring_capabilities': {
                            'srgb_start': int,
                            'srgb_range': int,
                            'srgb_flags': str
                        },
                        'spring_algorithms': list
                    }
                }
            }
        }
    }


# =======================================================
# Parser for 'show interfaces terse [| match <interface>]
# =======================================================
class ShowTedDatabaseExtensive(ShowTedDatabaseExtensiveSchema):
    """Parser for """

    cli_command = ['']

    def cli(self, interface=None, output=None):
        # execute the command
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output
