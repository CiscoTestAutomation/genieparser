--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Fix ISIS Learn on IOS-XE:
      * Modified ShowClnsTraffic:
        * Set level-1 as optional in schema (allowing level-2 only nodes)
      * Modified ShowIsisDatabaseDetail:
        * Add a new field in the schema "ipv4_interarea_reachability"
        * Change the correspondant parser to handle this field
      * Update CLNS & ISIS Mock tests to follow new schema

* VIPTELA
    * Fix duplicated lines in Show CloudExpress Applications

