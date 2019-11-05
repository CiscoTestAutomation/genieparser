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
            Any(): {  # '169.0.0.1'
                'type': str,
                'age': int,
                'link_in': int,
                'link_out': int,
                Optional('protocol'): {
                    Any(): {  # 'ospf(0.0.0.1)'
                        'to': {
                            Any(): {  # '169.0.0.1'
                                'local': {
                                    Any(): {  # '169.0.0.1'
                                        'remote': {
                                            Any(): {  # '169.0.0.1'
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
                                                'interface_switching_capability_descriptor': {
                                                    Any(): {  # from Interface Switching Capability Descriptor(1):
                                                        'switching_type': str,
                                                        'encoding_type': str,
                                                        'maximum_lsp_bw': {
                                                            Any(): {  # 1, 2, 3, ...
                                                                'bw': str
                                                            }
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
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        'prefixes': {
                            Any(): {  # prefix
                                'flags': str,
                                'prefix_sid': {
                                    Any(): {  # sid
                                        'flags': str,
                                        'algo': int
                                    }
                                }
                            }
                        },
                        'spring_capabilities': {
                            'srgb_block': {
                                'start': int,
                                'range': int,
                                'flags': str
                            }
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
