1. An existing parser class that has new/additional configuration lines to parse:

--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunInterfaceSchema to parse the following configuration lines for an interface:
        * dot1x_timeout_supp_timeout : str
        * dot1x_timeout_ratelimit_period : str
        * dot1x_source_template : str
        * ipv6_nd_raguard : bool
        * spanning_tree_guard : str
        * switchport_voice_vlan : str