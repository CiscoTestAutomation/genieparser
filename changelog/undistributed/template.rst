Templates
=========

.. code-block::

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

1.

.. code-block::

    --------------------------------------------------------------------------------
                                New
    --------------------------------------------------------------------------------
    * NXOS
        * Added ShowRoutingVrfAll:
            * show routing vrf all
            * show routing vrf {vrf}
            * show routing {ip} vrf all
            * show routing {ip} vrf {vrf}
            

2.

.. code-block::

    --------------------------------------------------------------------------------
                                New
    --------------------------------------------------------------------------------
    * IOSXE
        * Modified ShowCryptoPkiCertificates:
            * show crypto pki certificates {trustpoint_name}

3.

.. code-block::

    --------------------------------------------------------------------------------
                                Fix
    --------------------------------------------------------------------------------
    * IOS
        * Modified ShowVersion:
            * Changed <key1>, <key2> from schema to Optional.
            * Updated regex pattern <p1> to accommodate various outputs.
            
        * Modified ShowTrack:
            * Added keys <key3>, <key4> into the schema.

4.

.. code-block::
            
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
            
        * Modified ShowTrack:
            * Added keys <key3>, <key4> into the schema.
