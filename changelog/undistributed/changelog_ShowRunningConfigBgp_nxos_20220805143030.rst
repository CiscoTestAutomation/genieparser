--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* NXOS
    * Modified ShowRunningConfigBgp:
        * Updated regex pattern <p45> to accommodate more than just letters and numbers in BGP neighbor description.  E.g.  []-"_' '
