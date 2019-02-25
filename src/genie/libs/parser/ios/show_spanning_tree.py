"""show_spanning_tree.py
   supported commands:
     *  show spanning-tree detail
     *  show spanning-tree mst detail
     *  show spanning-tree summary
     *  show errdisable recovery
     *  show spanning-tree
     *  show spanning-tree mst <WORD>
     *  show spanning-tree vlan <WORD>
     *  show spanning-tree mst configuration

"""
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional

from genie.libs.parser.iosxe.show_spanning_tree import ShowSpanningTreeSummary as ShowSpanningTreeSummary_iosxe,\
                                                       ShowSpanningTreeDetail as ShowSpanningTreeDetail_iosxe,\
                                                       ShowSpanningTree as ShowSpanningTree_iosxe,\
                                                       ShowSpanningTreeMstDetail as ShowSpanningTreeMstDetail_iosxe,\
                                                       ShowErrdisableRecovery as ShowErrdisableRecovery_iosxe,\
                                                       ShowSpanningTreeMstConfiguration as ShowSpanningTreeMstConfiguration_iosxe

class ShowSpanningTreeSummarySchema(MetaParser):
    """Schema for show spanning-tree summary"""
    schema = {
        Optional('etherchannel_misconfig_guard'): bool,
        Optional('extended_system_id'): bool,
        Optional('portfast_default'): bool,
        'bpdu_guard': bool,
        Optional('bpdu_filter'): bool,
        Optional('bridge_assurance'): bool,
        Optional('loop_guard'): bool,
        'uplink_fast': bool,
        'backbone_fast': bool,
        Optional('root_bridge_for'): str,
        Optional('pvst_simulation'): bool,
        Optional("configured_pathcost"): {
            'method': str,
            Optional('operational_value'): str,
        },
        Optional('mode'): {
            Any(): {  # mstp, pvst, rapid_pvst
                Any(): {   # <mst_domain>,  <pvst_id>
                    'blocking': int,
                    'listening': int,
                    'learning': int,
                    'forwarding': int,
                    'stp_active': int,
                }
            }
        },
        'total_statistics': {
            'blockings': int,
            'listenings': int,
            'learnings': int,
            'forwardings': int,
            'stp_actives': int,
            Optional('num_of_msts'): int,
            Optional('num_of_vlans'): int,
        }
    }

class ShowSpanningTreeSummary(ShowSpanningTreeSummarySchema,ShowSpanningTreeSummary_iosxe):
    """Parser for show show spanning-tree summary"""
    pass

class ShowSpanningTreeDetail(ShowSpanningTreeDetail_iosxe):
    """Parser for show spanning-tree detail"""
    pass

class ShowSpanningTree(ShowSpanningTree_iosxe):
    """Parser for show spanning-tree [mst|vlan <WORD>]"""
    pass


class ShowSpanningTreeMstDetail(ShowSpanningTreeMstDetail_iosxe):
    pass


class ShowErrdisableRecovery(ShowErrdisableRecovery_iosxe):
    """Parser for show errdisable recovery"""
    pass


class ShowSpanningTreeMstConfiguration(ShowSpanningTreeMstConfiguration_iosxe):
    "Parser for show spanning-tree mst configuration "
    pass