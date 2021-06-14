--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowLogging:
      * Fixed patterns to support show logging parser when monitor logging is disabled
      * Fixed pattern p11 to recognize vrf information

    * Modified ShowLoggingSchema:
      * Made monitoring keys (level, message_logged, xml and filtering) optional 
