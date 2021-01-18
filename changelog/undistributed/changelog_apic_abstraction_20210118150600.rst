--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* NXOS
    * ACI
        * Removed AcidiagFnvread (moved to os=apic):
            * acidiag fnvread
        * Removed ShowFirmwareUpgradeStatus (moved to os=apic):
            * show firmware upgrade status
            * show firmware upgrade status switch-group {switch_group}
        * Removed ShowFirmwareUpgradeStatusControllerGroup (moved to os=apic):
            * show firmware upgrade status controller-group
        * Removed ShowFirmwareRepository (moved to os=apic):
            * show firmware repository

* APIC
    * Added AcidiagFnvread (from os=nxos, platform=aci):
        * acidiag fnvread
    * Added ShowFirmwareUpgradeStatus (from os=nxos, platform=aci):
        * show firmware upgrade status
        * show firmware upgrade status switch-group {switch_group}
    * Added ShowFirmwareUpgradeStatusControllerGroup (from os=nxos, platform=aci):
        * show firmware upgrade status controller-group
    * Added ShowFirmwareRepository (from os=nxos, platform=aci):
        * show firmware repository
