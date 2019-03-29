from genie import parsergen as pg 
from genie.libs.parsergen import extend_markup
from textwrap import dedent

marked_up_show_bgp_all_all_all_instance = '''\
OS: iosxr

CMD: show_bgp_instance_all_all_all_<WORD>

SHOWCMD: show bgp instance all all all {address_family}

PREFIX: show.bgp.instance.all.all.all

ACTUAL:
Wed Jul 12 15:23:42.143 EDT

BGP instance 0: 'default'
=========================

Address Family: IPv4 Unicast
----------------------------

BGP routing table entry for 10.3.4.0/34
Versions:
  Process           bRIB/RIB  SendTblVer
  Speaker                  4           4
Last Modified: Jul  9 08:46:14.166 for 3d06h
Paths: (1 available, best #1)
  Not advertised to any peer
  Path #1: Received by speaker 0
  Not advertised to any peer
  Local
    0.0.0.0 from 0.0.0.0 (10.64.4.4)
      Origin incomplete, metric 0, localpref 100, weight 32768, valid, redistributed, best, group-best
      Received Path ID 0, Local Path ID 0, version 4

MARKUP:
XW<date>XWed Jul 12 15:23:42.143 EDT

BGP instance 0: 'default'
=========================

Address Family: XXX<[a-zA-Z0-9\s]+><address_family>XXXIPv4 Unicast
----------------------------

BGP routing table entry for XA<ip_address>X10.3.4.0/34
Versions:
  Process           bRIB/RIB  SendTblVer
  Speaker                  4           4
Last Modified: Jul  9 08:46:14.166 for 3d06h
Paths: (1 available, best #1)
  Not advertised to any peer
  Path #1: Received by speaker 0
  Not advertised to any peer
  Local
    0.0.0.0 from 0.0.0.0 (10.64.4.4)
      Origin incomplete, metric 0, localpref XN<localpref_number>X100, weight 32768, valid, redistributed, best, group-best
      Received Path ID 0, Local Path ID 0, version 4

        '''

pg.extend_markup(dedent(marked_up_show_bgp_all_all_all_instance))
