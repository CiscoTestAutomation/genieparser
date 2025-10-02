--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunningConfigAAAUsernameSchema(MetaParser):
        * added: optional 'autocommand'
        * added: optional 'nopassword'

* IOSXE
    * Modified ShowRunningConfigAAAUsername(ShowRunningConfigAAAUsernameSchema)
        * Added support for 'autocommand'
        * Added support for 'nopassword'
        * Added support for multiline usernames
        * Added logging (warning) for unsupported options

--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunningConfigAAAUsername(ShowRunningConfigAAAUsernameSchema)
        * Changed how the cli() function parses arguments and parameters.

