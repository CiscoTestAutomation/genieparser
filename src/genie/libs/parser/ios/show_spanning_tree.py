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

class ShowSpanningTreeSummary(ShowSpanningTreeSummary_iosxe):
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