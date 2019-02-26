'''
IOS Parsers

'''
# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, Optional

from genie.libs.parser.iosxe.show_standby import ShowStandbyDelay as ShowStandbyDelay_iosxe, \
                                                 ShowStandbyAll as ShowStandbyAll_iosxe,\
                                                 ShowStandbyInternal as ShowStandbyInternal_iosxe


class ShowStandbyInternalIosSchema(MetaParser):
    """Schema for show standby internal"""
    schema = \
            {
                'hsrp_common_process_state': str,
                Optional('msgQ_size'): int,
                Optional('msgQ_max_size'): int,
                'hsrp_ipv4_process_state': str,
                'hsrp_ipv6_process_state': str,
                'hsrp_timer_wheel_state': str,
                Optional('hsrp_ha_state'): str,
                Optional('v3_to_v4_transform'): str,
                Optional('virtual_ip_hash_table'): {
                    Any(): {
                        Any(): {
                            'ip': str,
                            'interface': str,
                            'group': int,
                        }
                    }
                },
                Optional('mac_address_table'): {
                    Any(): {
                        'interface': str,
                        'mac_address': str,
                        'group': int,
                    }
                }
            }

class ShowStandbyInternal(ShowStandbyInternalIosSchema, ShowStandbyInternal_iosxe):
    """Parser for show standby internal"""
    pass

class ShowStandbyAll(ShowStandbyAll_iosxe):
    """Parser for show standby all"""
    pass

class ShowStandbyDelay(ShowStandbyDelay_iosxe):
    """Parser for show standby delay"""
    pass
