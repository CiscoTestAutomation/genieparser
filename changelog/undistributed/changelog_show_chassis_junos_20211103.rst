--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* JUNOS
  * Modified ShowChassisHardwareSchema:
    * Modified fields for chassis-module
    * Modified chassis-sub-sub-module to list of dictionaries
  * Modified ShowChassisHardware:
    * Modified RegEx for p_chassis, p_module0, p_module1, p_sub_module, p_sub_sub_module, p_sub_sub_sub_module to capture:
        * Correct empty version
        * Multiple formats for part_number
        * Multiple formats for serial number
        * Capture description to end of line instead of end of all output
    * Added relevant example output to test against