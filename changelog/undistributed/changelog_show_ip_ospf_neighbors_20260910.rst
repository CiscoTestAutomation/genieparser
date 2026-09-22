--------------------------------------------------------------------------------
                            New
--------------------------------------------------------------------------------
* NXOS
    * Added ShowIpOspfNeighbors:
        * Added parser and schema for show ip ospf neighbors.
        * Extracts process, VRF, neighbor count, interface, router ID, priority,
          adjacency state, neighbor role, uptime, and neighbor address.
        * Preserves identical router IDs on different interfaces and reports
          explicit zero-neighbor summaries as structured data.
        * Rejects incomplete tables whose parsed row count differs from the
          reported count.
        * Adds lab-derived and synthetic fixtures and malformed-input tests.
