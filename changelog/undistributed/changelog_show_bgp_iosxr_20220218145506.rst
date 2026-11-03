--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOS-XR
    * Modified ShowBgpInstanceNeighborsReceivedRoutes:
        * Updated regex pattern <p13> and <p13_1> to accommodate for BGP confederations in AS_PATH.
        * Updated regex pattern <p13.m1> , <p13.m2> and <p13.m3> to accommodate for BGP confederations in AS_PATH.
    * Modified ShowBgpInstanceNeighborsAdvertisedRoutes:
        * Updated regex pattern <p4> and <p5_1> to accommodate for BGP confederations in AS_PATH.
    * Modified ShowBgpInstanceAllAll:
        * Updated regex pattern <p16_2> , <p16> and <p17> to accommodate for BGP confederations in AS_PATH.
        * Updated regex pattern <p16.m1> , <p16.m2> and <p16.m3> to accommodate for BGP confederations in AS_PATH.

