--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowPowerInline:
        * Re-named regex pattern p1 to p1a and changed the pattern for <power> & <max> to always include ´.´,
          to avoid falsely matching of Cat45xxR outputs.
        * Added regex pattern p1b to cover 'show power inline' output from Cat45xxR.
        