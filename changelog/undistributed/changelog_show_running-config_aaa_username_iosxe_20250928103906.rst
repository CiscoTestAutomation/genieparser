--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunningConfigAAAUsernameSchema(MetaParser):
        * added: optional 'autocommand'
        * added: optional 'nopassword'

--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowRunningConfigAAAUsername(ShowRunningConfigAAAUsernameSchema)
        * Changed how the cli() function parses arguments and parameters.
        * Added support for 'autocommand'
        * Added support for 'nopassword'
        * Added support for multiline usernames
        * Added logging (warning) for unsupported options
