-------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowVrrp:
        * Changed master_router_priority,master_advertisement_interval_secs and master_advertisement_interval_secs from schema to be int or string
        * Updated regex pattern <p2>, <p3> to accommodate various outputs
        * Added regex pattern <p17_2> to accomdate unknown values for negative cases 
