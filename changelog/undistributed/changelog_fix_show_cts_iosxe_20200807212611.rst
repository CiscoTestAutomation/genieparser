--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowCtsInterfaceSchema:
        * Changed global_dot1x_feature from schema to Optional (not present on port-channel interfaces)
        * Changed cts mode value from schema to Optional to (not present when cts status is disabled)
    * Modified ShowCtsInterface:
        * Updated regex pattern p2 to also match Port-channel interfaces
        * Updated regex pattern p3 to also match CTS disabled status
        * Added conditional to cts_dict so mode key is not generated if cts is disabled
    * Modified golden_output2_expected test data
        * Added expected output for Port-channel interfaces
    * Added golden_output4 test data & expected results