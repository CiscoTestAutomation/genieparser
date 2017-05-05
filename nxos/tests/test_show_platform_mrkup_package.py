import parsergen as pg 
from parsergen import extend_markup
from textwrap import dedent

marked_up_show_platform = '''\
OS: nxos

CMD: show_version

SHOWCMD: show version

PREFIX: show.version

ACTUAL:
Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
Copyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.
The copyrights to certain works contained in this software are
owned by other third parties and used and distributed under
license. Certain components of this software are licensed under
the GNU General Public License (GPL) version 2.0 or the GNU
Lesser General Public License (LGPL) Version 2.1. A copy of each
such license is available at
http://www.opensource.org/licenses/gpl-2.0.php and
http://www.opensource.org/licenses/lgpl-2.1.php

Software
  BIOS:      version 2.12.0
  kickstart: version 8.1(1) [build 8.1(0.129)] [gdb]
  system:    version 8.1(1) [build 8.1(0.129)] [gdb]
  BIOS compile time:       05/29/2013
  kickstart image file is: slot0:///n7000-s2-kickstart.8.1.0.129.gbin
  kickstart compile time:  4/30/2017 23:00:00 [04/15/2017 04:34:05]
  system image file is:    slot0:///n7000-s2-dk9.8.1.0.129.gbin
  system compile time:     4/30/2017 23:00:00 [04/15/2017 06:43:41]


Hardware
  cisco Nexus7000 C7009 (9 Slot) Chassis ("Supervisor Module-2")
  Intel(R) Xeon(R) CPU         with 32938744 kB of memory.
  Processor Board ID JAF1708AAKL

  Device name: PE1
  bootflash:    2007040 kB
  slot0:        7989768 kB (expansion flash)

Kernel uptime is 0 day(s), 0 hour(s), 53 minute(s), 5 second(s)

Last reset at 885982 usecs after  Wed Apr 19 10:23:31 2017

  Reason: Reset Requested by CLI command reload
  System version: 6.2(6)
  Service: 

plugin
  Core Plugin, Ethernet Plugin

Active Package(s)

MARKUP:
Cisco XW<platform>XNexus Operating System (XXX<[A-Z\-]+><os>XXXNX-OS) Software
TAC support: http://www.cisco.com/tac
Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
Copyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.
The copyrights to certain works contained in this software are
owned by other third parties and used and distributed under
license. Certain components of this software are licensed under
the GNU General Public License (GPL) version 2.0 or the GNU
Lesser General Public License (LGPL) Version 2.1. A copy of each
such license is available at
http://www.opensource.org/licenses/gpl-2.0.php and
http://www.opensource.org/licenses/lgpl-2.1.php

Software
  BIOS:      XR<bios>Xversion 2.12.0
  kickstart: XR<kickstart>Xversion 8.1(1) [build 8.1(0.129)] [gdb]
  system:    XR<system>Xversion 8.1(1) [build 8.1(0.129)] [gdb]
  BIOS compile time:       XR<bios_compile_time>X05/29/2013
  kickstart image file is: XR<kickstart_image_file>Xslot0:///n7000-s2-kickstart.8.1.0.129.gbin
  kickstart compile time:  XR<kickstart_compile_time>X4/30/2017 23:00:00 [04/15/2017 04:34:05]
  system image file is:    XR<system_image_file>Xslot0:///n7000-s2-dk9.8.1.0.129.gbin
  system compile time:     XR<system_compile_time>X4/30/2017 23:00:00 [04/15/2017 06:43:41]


Hardware
  cisco XXX<[a-zA-Z0-9]+ +[a-zA-Z0-9]+><model>XXXNexus7000 C7009 (XN<slots>X9 Slot) Chassis XR<chassis>X("Supervisor Module-2")
  XXX<[a-zA-Z0-9\(\)]+ +[a-zA-Z0-9\(\)]+><cpu>XXXIntel(R) Xeon(R) CPU         with XN<memory>X32938744 kB of memory.
  Processor Board ID XW<processor_board_id>XJAF1708AAKL

  Device name: XR<device_name>XPE1
  bootflash:    XN<bootflash>X2007040 kB
  slot0:        7989768 kB (expansion flash)

Kernel uptime is XN<days>X0 day(s), XN<hours>X0 hour(s), XN<minutes>X53 minute(s), XN<seconds>X5 second(s)


Last reset at 885982 usecs after  Wed Apr 19 10:23:31 2017

  Reason: XR<reason>XReset Requested by CLI command reload
  System version: XR<system_version>X6.2(6)
  Service: 

plugin
  Core Plugin, Ethernet Plugin

Active Package(s)
        '''

pg.extend_markup(dedent(marked_up_show_platform))
