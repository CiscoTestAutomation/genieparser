"""show_lag.py
   supported commands:
     *  show lacp sys-id
     *  show lacp counters
     *  show lacp <channel_group> counters
     *  show lacp internal
     *  show lacp <channel_group> internal
     *  show lacp neighbor
     *  show lacp <channel_group> neighbor
     *  show pagp counters
     *  show pagp <channel_group> counters
     *  show pagp neighbor
     *  show pagp <channel_group> neighbor
     *  show pagp internal
     *  show pagp <channel_group> internal
     *  show etherchannel summary
     *  show etherchannel load-balancing
     *  show lacp neighbor detail
"""
# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# import iosxe parser
from genie.libs.parser.iosxe.show_lag import ShowLacpSysId as ShowLacpSysId_iosxe,\
                    ShowEtherchannelSummary as ShowEtherchannelSummary_iosxe,\
                    ShowLacpCounters as ShowLacpCounters_iosxe,\
                    ShowLacpInternal as ShowLacpInternal_iosxe,\
                    ShowLacpNeighbor as ShowLacpNeighbor_iosxe,\
                    ShowPagpCounters as ShowPagpCounters_iosxe,\
                    ShowPagpNeighbor as ShowPagpNeighbor_iosxe,\
                    ShowPagpInternal as ShowPagpInternal_iosxe,\
                    ShowEtherChannelLoadBalancing as ShowEtherChannelLoadBalancing_iosxe,\
                    ShowLacpNeighborDetail as ShowLacpNeighborDetail_iosxe

# ====================================================
#  parser for show lacp sys-id
# ====================================================
class ShowLacpSysId(ShowLacpSysId_iosxe):
    """Parser for :
       show lacp sys-id"""
    pass


# ====================================================
#  parser for show lacp counters
# ====================================================
class ShowLacpCounters(ShowLacpCounters_iosxe):
    """Parser for :
      show lacp counters"""
    pass


# ====================================================
#  parser for show lacp internal
# ====================================================
class ShowLacpInternal(ShowLacpInternal_iosxe):
    """Parser for :
      show lacp internal"""
    pass


# ====================================================
#  parser for show lacp neighbor
# ====================================================
class ShowLacpNeighbor(ShowLacpNeighbor_iosxe):
    """Parser for :
      show lacp neighbor"""
    pass


# ====================================================
#  parser for show pagp counters
# ====================================================
class ShowPagpCounters(ShowPagpCounters_iosxe):
    """Parser for :
      show pagp counters"""
    pass


# ====================================================
#  parser for show pagp neighbor
# ====================================================
class ShowPagpNeighbor(ShowPagpNeighbor_iosxe):
    """Parser for :
      show pagp neighbor"""
    pass


# ====================================================
#  parser for show pagp internal
# ====================================================
class ShowPagpInternal(ShowPagpInternal_iosxe):
    """Parser for :
      show pagp internal
      show pagp <channel_group> internal"""
    pass


# ====================================================
#  parser for show etherchannel summary
# ====================================================
class ShowEtherchannelSummary(ShowEtherchannelSummary_iosxe):
    """Parser for :
      show etherchannel summary"""
    pass


# ====================================================
#  parser for show etherchannel load-balancing
# ====================================================
class ShowEtherChannelLoadBalancing(ShowEtherChannelLoadBalancing_iosxe):
    """Parser for :
      show etherchannel load-balancing"""
    pass


# ====================================================
#  parser for show lacp neighbor detail
# ====================================================
class ShowLacpNeighborDetail(ShowLacpNeighborDetail_iosxe):
    """Parser for :
        show lacp neighbor detail"""
    pass