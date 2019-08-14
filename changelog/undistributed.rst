* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXE
    * Fix ShowRedundancyStates
        changed 'maintenance_mode' key to optional to support more output

--------------------------------------------------------------------------------
                                Lag
--------------------------------------------------------------------------------
* IOSXR
    * Update ShowBundle
        to support 'show bundle {interface}'

--------------------------------------------------------------------------------
                                Authentication Sessions
--------------------------------------------------------------------------------
* IOSXE
   * ShowAuthenticationSessions for: 
        * 'show authentication sessions'
        * 'show authentication sessions interface {interface}'
   * ShowAuthenticationSessionsInterfaceDetails for:
        * 'show authentication sessions interface {interface} details'
