* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpv6Neighbors
        * Add command 'show ipv6 neighbors {interface}'
        * Add command 'show ipv6 neighbors vrf {vrf} {interface}'
    * Update ShowIpv6Interface
        * Add 'suppress' key to schema
