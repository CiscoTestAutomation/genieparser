"""
IOSXE C9300 parsers for the following show commands:
    * show system integrity all compliance nonce <nonce>
    * show system integrity all measurement nonce <nonce>
    * show system integrity all trust_chain nonce <nonce>
"""

# import iosxe/c9500 parser
from genie.libs.parser.iosxe.c9500.show_system import (
    ShowSystemIntegrityAllComplianceNonce as ShowSystemIntegrityAllComplianceNonce_c9500,
    ShowSystemIntegrityAllMeasurementNonce as ShowSystemIntegrityAllMeasurementNonce_c9500,
    ShowSystemIntegrityAllTrustChainNonce as ShowSystemIntegrityAllTrustChainNonce_c9500,
)


class ShowSystemIntegrityAllComplianceNonce(ShowSystemIntegrityAllComplianceNonce_c9500):
    """Parser for show system integrity all compliance nonce <nonce>"""

    pass


class ShowSystemIntegrityAllMeasurementNonce(ShowSystemIntegrityAllMeasurementNonce_c9500):
    """Parser for show system integrity all measurement nonce <nonce>"""

    pass


class ShowSystemIntegrityAllTrustChainNonce(ShowSystemIntegrityAllTrustChainNonce_c9500):
    """Parser for show system integrity all trust_chain nonce <nonce>"""

    pass
