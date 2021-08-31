--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowCtsRoleBasedPermissionsSchema:
        * Modified int to be Optional inside 'indexes' key
    * Modified ShowCtsRoleBasedPermissions:
        * Initialized 'indexes' key by default so that there is no runtime error if collection is empty



