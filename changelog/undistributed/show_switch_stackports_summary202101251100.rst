--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified: ShowSwitchStackPortsSummary
        * 'show switch stack-ports summary'

# Examples
* IOSXE
        * Modified ShowSwitchStackPortsSummary:
        * Changed neighbor, link_changes_count from schema to int (was string).
        * added cli/empty/empty_output_ouput.txt
        * updated cli/equal/golden_output1_output.* for integer change above

