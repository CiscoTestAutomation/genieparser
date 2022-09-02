Only one changelog file per pull request. Combine these two templates where applicable.

Templates
=========

--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* <OS>
    * <Added|Modified> <Class>:
        * <New Show Command|Command>

--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* <OS>
    * <Added|Modified|Removed> <Class>:
        * Changes made


Examples
========

1. A new parser class that has 4 associated show commands:

--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* NXOS
    * Added ShowRoutingVrfAll:
        * show routing vrf all
        * show routing vrf {vrf}
        * show routing {ip} vrf all
        * show routing {ip} vrf {vrf}
            
2. An existing parser that has had a new show command added to it: 

--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowCryptoPkiCertificates:
        * show crypto pki certificates {trustpoint_name}


3. Two existing parsers that have been fixed/modified. Combine templates as necessary. 

--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOS
    * Modified ShowVersion:
        * Changed <key1>, <key2> from schema to Optional.
        * Updated regex pattern <p1> to accommodate various outputs.
        
    * Modified ShowTrack:
        * Added keys <key3>, <key4> into the schema.


4. A new parser with 1 associated show command and an existing parser that has been fixed/modified

--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowCryptoPkiCertificates:
        * show crypto pki certificates {trustpoint_name}

--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* NXOS
    * Modified ShowVersion:
        * Changed <key1>, <key2> from schema to Optional.
        * Updated regex pattern <p1> to accommodate various outputs.
