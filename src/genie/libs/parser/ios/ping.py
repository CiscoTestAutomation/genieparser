"""ping.py

IOS parsers for the following show commands:
    * ping {addr}
    * ping {addr} source {source} repeat {count}
"""
# import iosxe parser
from genie.libs.parser.iosxe.ping import Ping as Ping_iosxe

class Ping(Ping_iosxe):
    """ parser for
        * ping {addr}
        * ping {addr} source {source} repeat {count}
    """
    pass
