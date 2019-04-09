"""show_crypto.py

IOS parsers for the following show commands:
   * show crypto pki certificates <WORD>
"""
from genie.libs.parser.iosxe.show_crypto import ShowCryptoPkiCertificates as ShowCryptoPkiCertificates_iosxe


# =================================================
#  Parser for 'show crypto pki certificates <WORD>'
# =================================================
class ShowCryptoPkiCertificates(ShowCryptoPkiCertificates_iosxe):
    """Parser for show crypto pki certificates <WORD>"""
    pass