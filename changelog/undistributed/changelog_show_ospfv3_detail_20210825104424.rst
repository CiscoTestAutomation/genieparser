--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowOspfv3VrfAllInclusiveNeighborDetailSchema:
        * Changed 'bfd_enable' key in schema to str type from bool.
        
    * Modified ShowOspfv3VrfAllInclusiveNeighborDetail:
        * Added support for 'bfd_enable' and 'bfd_mode'