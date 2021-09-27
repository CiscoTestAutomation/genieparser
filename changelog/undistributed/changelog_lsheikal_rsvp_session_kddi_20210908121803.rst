--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOSXR
    * Added ShowRSVPGracefulRestartNeighborsDetail:
        * Added 'show rsvp graceful-restart neighbors detail'

    * Added ShowRSVPSessionDetail:
        * Added 'show rsvp session detail'
        * Added 'show rsvp session destination {ip_address} detail dst-port {tunnel_id}'

--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowRSVPSession:
        * Modified schema and changed respective parser logic

    * Modified ShowRSVPNeighbor:
        * Replaced '-' with '_' in schema

    * Modified ShowRSVPGracefulRestartNeighbors:
        * Replaced '-' with '_' in schema

