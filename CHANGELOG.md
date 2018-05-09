# May 2018

## May 8th

* Normalized all the ats.tcl imports in the package.
* New parsers added and their corresponding unittests.
***18 files changed, 3104 insertions(+), 17 deletions(-)***

| File                                                          | Changes                                     |
| ------------------------------------------------------------- |:-------------------------------------------:|
| src/genie/libs/parser/base.py                                 |   2 +-                                      |
| src/genie/libs/parser/iosxe/show_access_session.py            | 101 +++++                                   |
| src/genie/libs/parser/iosxe/show_acl.py                       |   2 +-                                      |
| src/genie/libs/parser/iosxe/show_dot1x.py                     | 479 +++++++++++++++++++++++                 |
| src/genie/libs/parser/iosxe/show_fdb.py                       | 205 ++++++++++                              |
| src/genie/libs/parser/iosxe/show_interface.py                 |   6 +-                                      |
| src/genie/libs/parser/iosxe/show_lag.py                       | 706 +++++++++++++++++++++++++++++++++       |
| src/genie/libs/parser/iosxe/tests/test_show_access_session.py |  62 +++                                     |
| src/genie/libs/parser/iosxe/tests/test_show_dot1x.py          | 382 ++++++++++++++++++                      |
| src/genie/libs/parser/iosxe/tests/test_show_fdb.py            | 263 +++++++++++++                           |
| src/genie/libs/parser/iosxe/tests/test_show_lag.py            | 844 ++++++++++++++++++++++++++++++++++++++++|
| src/genie/libs/parser/iosxr/base.py                           |   2 +-                                      |
| src/genie/libs/parser/iosxr/show_interface.py                 |  56 ++-                                     |
| src/genie/libs/parser/iosxr/show_vrf.py                       |   1 +                                       |
| src/genie/libs/parser/nxos/show_bgp.py                        |   3 +-                                      |
| src/genie/libs/parser/nxos/show_platform.py                   |   2 +-                                      |
| src/genie/libs/parser/nxos/show_rip.py                        |   2 +-                                      |
| src/genie/libs/parser/utils/common.py                         |   3 +-                                      |
