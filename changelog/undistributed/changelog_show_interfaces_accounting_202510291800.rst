----------------------
         Fix
----------------------
* iosxe
    * Modified class ShowInterfacesAccounting
        * Modified regex pattern to support interface descriptions with multiple spaces
        * Only right-strip whitespace from lines and modify regex for lines containing counters to add explicit leading
          whitespace