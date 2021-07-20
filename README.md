[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/CiscoTestAutomation/genieparser)

# Genie Parser

Genie is both a library framework and a test harness that facilitates rapid
development, encourages re-usability, and simplifies writing test automation. Genie
bundled with the modular architecture of pyATS framework accelerates and
simplifies test automation leveraging all the perks of the Python programming
language in an object-orienting fashion.

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers to start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites.

Genie was initially developed internally in Cisco, and is now available to the
general public starting early 2018 through [Cisco DevNet].

[Cisco DevNet]: https://developer.cisco.com/

This is a sub-component of Genie that parses the device output into structured
datastructure.

# Installation

The package is automatically installed when pyATS gets installed

```
$ pip install 'pyats[full]'
```

Detailed installation guide can be found on [our website].
[our website]: https://developer.cisco.com/site/pyats/

# Development

To develop this package, assuming you have Genie already installed in your
environment, follow the commands below:

```bash
# clone this repo
bash$ git clone https://github.com/CiscoTestAutomation/genieparser.git

# source pyats environment
bash$ source /path/to/pyats_workspace/env.sh (or env.csh)

# put all packages in dev mode
bash$ cd genieparser
bash$ make develop
```

Now you should be able to develop the files and see it reflected in your runs.

# ChangeLog

Change logs can be found [here](changelog/CHANGELOG.md).



# To contributors:

[Guide] 

[Guide]: https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/writeparser/writeparser.html#


YouTube Video: <How to write a Genie parser for Cisco!> https://youtube.com/watch?v=ibLNilSfdTc (Thank you! @Jmahaja1)


Once you create a new parser, don't forget to check 1, 2, and 3;
if you only update the parser class without modifying/creating the schema, please check 2 and 3. 
- [ ] 1. `make json`
- [ ] 2. create changelog for your pull request.
- [ ] 3. make sure GitHub Actions checks passed.

# How to write a 'changelog' for your contribution:
1. Become familiarized with the examples at [changelog/undistributed/template.rst](https://github.com/CiscoTestAutomation/genieparser/blob/master/changelog/undistributed/template.rst). Changelogs must be written in the same style as the examples found there:
```
--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* NXOS
    * Modified ShowVersion:
        * Changed <key1>, <key2> from schema to Optional.
        * Updated regex pattern <p1> to accommodate various outputs.
```

When writing about what was changed, avoid using vague statements such as 'Updated regex' or 'Fixed bug'. 
If modifying an existing parser, then specify the schema keys and regex patterns that have been changed. 

2. The changelog (singular) that accompanies a contribution must have a unique file name and be in `genieparser/changelog/undistributed/`. If you need help generating a unique file name, then enter the following bash/terminal command to generate a sufficiently unique number (linux and mac only):
```
$ date "+%Y%m%d%H%M%S"
```
Put a short description in the name of the changelog file and then appended this number at the end of the file. 
For example, `genieparser/changelog/undistributed/changelog_show_interface_iosxe_20200807212611.rst` 


# Common Regex Patterns

This is a list of common patterns that are useful to use when writing a parser. This list is by no means exhaustive, and the patterns strike a balance between size and specificity.
Remember to check this section for updates as we add new patterns.

You can help improve this list by expanding it. Everyone is welcome to contribute and extend the list with knew helpful patterns and ideas.

### general patterns

| pattern name | description | pattern | examples |
| :---: | :--- | :---: | :--- |
| ipv4 | ipv4 address, this will match any pattern of three groups of 1-3 numbers separated by dots  | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}` | `0.0.0.0` <br /> `192.168.0.1` <br /> `255.255.255` <br /> please note: it will also match invalid addresses like `999.999.999` |
| ipv4 with subnet | ipv4 address with a subnet at the end  | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}` | `10.0.0.0/8` <br /> `192.168.0.1/16` <br /> `255.255.255/32` <br /> please note: it will also match invalid addresses like `999.999.999/64` |
| ipv6 | simple ipv6 pattern, exhaustive ipv6 patterns are very long and unnecessary most of the time | `[a-fA-F\d\:]+` | `fe80::1` <br /> `::2` <br /> `2001:0db8:85a3:0000:0000:8a2e:0370:7334` <br /> please note: it will also match invalid addresses like `::::0` <br /> `a::02345678::0::0` |
| ipv6 with subnet | ipv6 with a subnet at the end | `[a-fA-F\d\:]+\/\d{1,3}` | `::2/128` <br /> `2001:0db8:85a3:0000:0000:8a2e:0370:7334/64` <br /> please note: it will also match invalid addresses like `::2/256` <br /> `::::0/999` <br /> `a::02345678::0::0/001` |
| mac (1) | mac addresses with dot delimiter | `([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}` | `aaaa.bbbb.cccc` <br /> `AAAA.BBBB.CCCC` <br /> `1a2b.3c4d.5e6f` |
| mac (2) | mac addresses with colon delimiter | `(([a-fA-F\d]{2}:){5}[a-fA-F\d]{2})` | `aa:bb:cc:dd:ee:ff` <br /> `AA:BB:CC:DD:EE:FF` <br /> `a1:b2:c3:d4:e5:f6` |
| unit measurement | matches floats that represent a unit, like the current temperature or power, these options can usually also be N/A | `[\dNAna\/-\.]+` | `-5.00 C` <br /> `2.97 V` <br /> `-2.30 dBm` <br /> please note: the pattern will only match the number part and not the unit  |
| interface name | matches the characters that can compose an interface name | `[\w\/\.\-\:]+` | `Port-channel10` <br /> `HundredGigE1/0/35.12` <br /> `Serial1/0/2:0` <br /> `ucse1/0/0` <br /> `FastEthernet1` |
| time stamp | basic hh:mm timestamp regex, can be extended to more complex timestamps easily | `\d{1,2}:\d{2}` | `1:30` <br /> `02:45` <br /> `12:30` <br /> please note: it will also match invalid examples like `99:99` <br />`10:80` |

### General Option List Patterns

| pattern name | description | pattern | examples |
| :---: | :--- | :---: | :--- |
| link state | whether a link is up or down, this list can be used as a base when something has a similar but expanded set of states, consider using with the case insensitive flag | <code>up&#124;down&#124;administratively up&#124;administratively down</code> | `up` <br /> `down` <br /> `administratively up` <br /> `administratively down` |
| enabled status | for all situations that use enable and disable, also useful as base when there are further options  | <code>\[e&#124;E\]nabled&#124;\[d&#124;D\]isabled</code> | `enabled` <br /> `Enabled` <br /> `disabled` <br /> `Disabled` |
| duplex state | used to match the state of the duplex, may need to be adjusted for different show commands that output duplex differently | <code>(auto&#124;full&#124;half)?\[-\s\]?(\[d&#124;D\]uplex&#124;unknown)</code> | `half-duplex` <br /> `full Duplex` <br /> `auto duplex` <br /> `full-Duplex` |

### ACL Patterns

| pattern name | description | pattern | examples |
| :---: | :--- | :---: | :--- |
| acl name | all the characters that can compose an acl name | `[\w-\.#]+` | `ipv4_acl` <br /> `mac_acl` <br /> `#1` |
| acl target | can be any, or host and then an ip or mac address | <code>any&#124;(host (\d{1,3}\\.\d{1,3}\\.\d{1,3}\\.\d{1,3})&#124;(\[a-fA-F\d\]{4}\\.){2}\[a-fA-F\d\]{4})</code> | `any` <br /> `host 192.168.0.1` <br /> `host aaaa.bbbb.cccc` |
| acl operator | the match action of the acl in a convenient list | <code>eq&#124;gt&#124;lt&#124;neq&#124;range</code> | `eq` <br /> `lt` <br /> `range` |
| acl action | whether the acl results in allowing or stopping the flow of traffic | <code>permit&#124;deny</code> | `permit` <br /> `deny` |
| acl message type | the possible message types acls can match in a convenient list | <code>ttl-exceeded&#124;unreachable&#124;packet-too-big&#124;echo-reply&#124;echo&#124;router-advertisement&#124;mld-query+</code> | `unreachable` <br /> `router-advertisement` <br /> `echo` |
| acl protocols  | the possible protocols acls can match in a convenient list | <code>ip&#124;ipv6&#124;tcp&#124;udp&#124;ahp&#124;esp&#124;hbh&#124;icmp&#124;pcp&#124;sctp</code> | `ip` <br /> `tcp` <br /> `icmp` |

### Access Point and Wireless Patterns

| pattern name | description | pattern | examples |
| :---: | :--- | :---: | :--- |
| ap power | the current radio power of the access point in dBm | `[-\d+]+\s+dBm` | `1 dBm` <br /> `-80 dBm` |
| ap band | The current band of the access point in GHz| `[\d\.]+\s+GHz` | `2.4 GHz` <br /> `5 GHz` |
| ap setting status | whether a feature or setting on the access point is enabled or disabled, or not configured at all | <code>([e&#124;E]nabled)&#124;([d&#124;D]isabled)&#124;(Not Configured)</code> | `enabled` <br /> `Disabled` <br /> `Not Configured` |

### BGP Patterns

| pattern name | description | pattern | examples |
| :---: | :--- | :---: | :--- |
| bgp as path | the autonomous system path of the bgp route| `[\d\s\{\}]+` |  `0 200 33299 51178 47751 {27016}` <br /> `0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135}` |
| bgp next hop | the next hop of the bgp route, it normally matches ipv4 and ipv6 addresses, but it can also handle bgp path prefixes | `[\w\.\:\/\[\]\,]+` | `10.4.1.1` <br /> `:FFFF:10.4.1.1` |
| bgp path type | possible bgp path types in a convenient list | <code>i&#124;e&#124;c&#124;l&#124;a&#124;r&#124;I</code> | `e` <br /> `l` <br /> `I` |
| bgp origin code | possible bgp origin codes in a convenient list | <code>i&#124;e&#124;\?&#124;\\&#124;</code> | `e` <br />  `?` <br /> <code> &#124;</code>  |

### MPLS Patterns

| pattern name | description | pattern | examples |
| :---: | :--- | :---: | :--- |
| ldp id | ldp id is just an ipv4 address with a colon and numbers at the end | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+` | `10.169.197.252:0` <br /> please note: it will also match invalid addresses like `999.999.999:0001` |
| mpls active state | possible mpls states are active, passive, and active/passive | <code>active&#124;passive&#124;active\\/passive</code> | `active` <br /> `passive` <br /> `active/passive` |

### OSPF Patterns

| pattern name | description | pattern | examples |
| :---: | :--- | :---: | :--- |
| ospf advertising state | whether a route is being advertised or not | <code>Advertise&#124;DoNotAdvertise</code> | `Advertise` <br /> `DoNotAdvertise` |
| ospf packet type | possible ospf packet types in a convenient list | <code>Invalid&#124;Hello&#124;DB des&#124;LS req&#124;LS upd&#124;LS ack</code> | `Hello` <br /> `LS upd` <br /> `Invalid` |

### VLAN Patterns

| pattern name | description | pattern | examples |
| :---: | :--- | :---: | :--- |
| vlan status | possible vlan statuses in a convenient list | <code>active&#124;suspended&#124;(.\*)lshut&#124;(.\*)unsup</code> | `active` <br /> `suspended` <br /> `act/unsup` <br /> `act/lshut` |
| vlan list | matches vlan lists | `[\d\-\,]+` | `1,2,3,4,5` <br /> `1-5` <br /> `1,2,3-5,6,7,8-10` |
| port channel state | possible port channel states in a convenient list | <code>passive&#124;active&#124;on&#124;off</code> | `passive` <br /> `active` <br /> `off` |


> Copyright (c) 2021 Cisco Systems, Inc. and/or its affiliates
