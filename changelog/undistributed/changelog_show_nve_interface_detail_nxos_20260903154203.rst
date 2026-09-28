--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* NXOS
    * Modified ShowNveInterfaceDetail:
        * Added fabric_convergence_time, fabric_convergence_time_left, and multisite_fabric_advertise_pip_l3 keys to the schema.
        * Added regex patterns p27, p28, and p29 to parse Fabric convergence time, Fabric convergence time left, and Multisite fabric-advertise-pip l3 configured output.
