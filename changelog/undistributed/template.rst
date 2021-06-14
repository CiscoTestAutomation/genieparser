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

.. code-block::

    --------------------------------------------------------------------------------
                                New
    --------------------------------------------------------------------------------
    * IOSXE
        * Added ShowIpArp:
            * show ip arp
            * show ip arp vrf {vrf}


    --------------------------------------------------------------------------------
                                Fix
    --------------------------------------------------------------------------------
    * IOS
        * Modified ShowVersion:
            * Changed <key1>, <key2> from schema to Optional.
            * Updated regex pattern <p1> to accommodate various outputs.
            
        * Modified ShowTrack:
            * Added keys <key3>, <key4> into the schema.
