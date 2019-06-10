* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                policy-map
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowPolicyMap to parser customer's output
        fixed not parsing lines with kbps
        added wred_type key in schema
    * Fix ShowPolicyMapInterface
        set priority level to default if not exist in output
        moved child-policy under parent-policy

--------------------------------------------------------------------------------
                                platform
--------------------------------------------------------------------------------
* IOSXE
    * Fixed a bug in ShowRedundancy where ParserOutputEmptyException is nor raised
    * Update ShowPlatformHardware to support qlimit/queue depth in bytes and pkts

--------------------------------------------------------------------------------
                                NTP
--------------------------------------------------------------------------------

* IOSXE
    * Update ShowNtpStatus to support refid after adding leap second