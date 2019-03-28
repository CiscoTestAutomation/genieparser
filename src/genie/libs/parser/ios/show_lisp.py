''' show_lisp.py

IOS parsers for the following show commands:
    * show lisp session
    * show lisp platform
    * show lisp all extranet <extranet> instance-id <instance_id>
    * show lisp all instance-id <instance_id> dynamic-eid detail
    * show lisp all service ipv4
    * show lisp all service ipv6
    * show lisp all service ethernet
    * show lisp all instance-id <instance_id> ipv4
    * show lisp all instance-id <instance_id> ipv6
    * show lisp all instance-id <instance_id> ethernet
    * show lisp all instance-id <instance_id> ipv4 map-cache
    * show lisp all instance-id <instance_id> ipv6 map-cache
    * show lisp all instance-id <instance_id> ethernet map-cache
    * show lisp all instance-id <instance_id> ipv4 server rloc members
    * show lisp all instance-id <instance_id> ipv6 server rloc members
    * show lisp all instance-id <instance_id> ethernet server rloc members
    * show lisp all instance-id <instance_id> ipv4 smr
    * show lisp all instance-id <instance_id> ipv6 smr
    * show lisp all instance-id <instance_id> ethernet smr
    * show lisp all service ipv4 summary
    * show lisp all service ipv6 summary
    * show lisp all service ethernet summary
    * show lisp all instance-id <instance_id> ipv4 database
    * show lisp all instance-id <instance_id> ipv6 database
    * show lisp all instance-id <instance_id> ethernet database
    * show lisp all instance-id <instance_id> ipv4 server summary
    * show lisp all instance-id <instance_id> ipv6 server summary
    * show lisp all instance-id <instance_id> ethernet server summary
    * show lisp all instance-id <instance_id> ipv4 server detail internal
    * show lisp all instance-id <instance_id> ipv6 server detail internal
    * show lisp all instance-id <instance_id> ethernet server detail internal
    * show lisp all instance-id <instance_id> ipv4 statistics
    * show lisp all instance-id <instance_id> ipv6 statistics
    * show lisp all instance-id <instance_id> ethernet statistics
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common

# import iosxe parser
from genie.libs.parser.iosxe.show_lisp import ShowLispSession as ShowLispSession_iosxe,\
                                              ShowLispPlatform as ShowLispPlatform_iosxe,\
                                              ShowLispExtranet as ShowLispExtranet_iosxe,\
                                              ShowLispDynamicEidDetail as ShowLispDynamicEidDetail_iosxe,\
                                              ShowLispService as ShowLispService_iosxe,\
                                              ShowLispServiceMapCache as ShowLispServiceMapCache_iosxe,\
                                              ShowLispServiceRlocMembers as ShowLispServiceRlocMembers_iosxe,\
                                              ShowLispServiceSmr as ShowLispServiceSmr_iosxe,\
                                              ShowLispServiceSummary as ShowLispServiceSummary_iosxe,\
                                              ShowLispServiceDatabase as ShowLispServiceDatabase_iosxe,\
                                              ShowLispServiceServerSummary as ShowLispServiceServerSummary_iosxe,\
                                              ShowLispServiceServerDetailInternal as ShowLispServiceServerDetailInternal_iosxe,\
                                              ShowLispServiceStatistics as ShowLispServiceStatistics_iosxe

# ==============================
# Parser for 'show lisp session'
# ==============================
class ShowLispSession(ShowLispSession_iosxe):
    ''' Parser for show lisp session'''
    pass


# ==============================
# Parser for 'show lisp platform'
# ==============================
class ShowLispPlatform(ShowLispPlatform_iosxe):
    ''' Parser for "show lisp platform" '''
    pass


# ========================================================================
# Parser for 'show lisp all extranet <extranet> instance-id <instance_id>'
# ========================================================================
class ShowLispExtranet(ShowLispExtranet_iosxe):
    ''' Parser for "show lisp all extranet <extranet> instance-id <instance_id>"'''
    pass


# =======================================================================
# Parser for 'show lisp all instance-id <instance_id> dynamic-eid detail'
# =======================================================================
class ShowLispDynamicEidDetail(ShowLispDynamicEidDetail_iosxe):
    ''' Parser for "show lisp all instance-id <instance_id> dynamic-eid detail"'''
    pass


# ==============================================================
# Parser for 'show lisp all instance-id <instance_id> <service>'
# ==============================================================
class ShowLispService(ShowLispService_iosxe):
    '''Parser for "show lisp all instance-id <instance_id> <service>"'''
    pass


# ========================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> map-cache'
# ========================================================================
class ShowLispServiceMapCache(ShowLispServiceMapCache_iosxe):
    '''Parser for "show lisp all instance-id <instance_id> <service> map-cache"'''
    pass


# ===========================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> rloc members'
# ===========================================================================
class ShowLispServiceRlocMembers(ShowLispServiceRlocMembers_iosxe):
    '''Parser for "show lisp all instance-id <instance_id> <service> rloc members"'''
    pass


# ==================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> smr'
# ==================================================================
class ShowLispServiceSmr(ShowLispServiceSmr_iosxe):
    '''Parser for "show lisp all instance-id <instance_id> <service> smr"'''
    pass


# ====================================================
# Parser for 'show lisp all service <service> summary'
# ====================================================
class ShowLispServiceSummary(ShowLispServiceSummary_iosxe):
    '''Parser for "show lisp all service <service> summary"'''
    pass


# =======================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> dabatase'
# =======================================================================
class ShowLispServiceDatabase(ShowLispServiceDatabase_iosxe):
    '''Parser for "show lisp all instance-id <instance_id> <service> dabatase"'''
    pass


# =============================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> server summary'
# =============================================================================
class ShowLispServiceServerSummary(ShowLispServiceServerSummary_iosxe):
    '''Parser for "show lisp all instance-id <instance_id> <service> server summary"'''
    pass


# =====================================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> server detail internal'
# =====================================================================================
class ShowLispServiceServerDetailInternal(ShowLispServiceServerDetailInternal_iosxe):
    '''Parser for "show lisp all instance-id <instance_id> <service> server detail internal"'''
    pass


# =========================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> statistics'
# =========================================================================
class ShowLispServiceStatistics(ShowLispServiceStatistics_iosxe):
    '''Parser for "show lisp all instance-id <instance_id> <service> statistics"'''
    pass
