--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* C9400
    * Modified/Revised ShowEnvironmentAll:
        * Changed schema to include "switch" for every switch in the stack.
        * Updated regex pattern to accomodate for "Switch:1" and "Switch: 1" outputs and use those as keys to the power supply and fantray parsing.