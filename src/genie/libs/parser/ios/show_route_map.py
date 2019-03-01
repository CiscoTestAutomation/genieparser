''' show_route_map.py

IOS parsers for the following show commands:
    * show route-map all
'''

from genie.libs.parser.iosxe.show_route_map import ShowRouteMapAll as ShowRouteMapAll_iosxe

    
class ShowRouteMapAll(ShowRouteMapAll_iosxe):
    """Parser for show route-map all"""
    pass