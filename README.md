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

> Copyright (c) 2020 Cisco Systems, Inc. and/or its affiliates

# Common Regex Patterns

This is a list of common patterns that are useful to use when writing a parser. This list is by no means exhaustive, and the patterns strike a balance between size and specificity.
Remember to check this section for updates as we add new patterns.

### general patterns

| pattern name | description | pattern |
| :---: | :--- | :---: |
| ipv4 | ipv4 address, this will match patterns like 999.999.999, it is not a validator | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}` |
| ipv4 subnet | ipv4 address with a subnet at the end  | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}` |
| ipv6 | simple ipv6 pattern, exhaustive ipv6 patterns are very long and unnecessary most of the time | `[\w\:]+` |
| ipv6 subnet | ipv6 with subnet at the end | `[\w\:]+\/\d{1,3}` |
| cisco mac | cisco format mac addresses (ex. aaaa.bbbb.cccc) | `([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}` |
| general mac | general mac address (ex. AA:BB:CC:DD:EE:FF) | `(([a-fA-F\d]{2}:){5}[a-fA-F\d]{2})` |
| unit measurement | matches floats that represent a unit, like the current temperature or power, these options can usually also be N/A (ex. -5.00 C, 2.97 V, -2.30 dBm) | `[\dNAna\/-\.]+` |
| interface name | matches the characters that can compose an interface name | `[\w\/\.-]+ `|
| time stamp | basic hh:mm timestamp regex, can be extended to more complex timestamps easily | `\d{1,2}:\d{1,2}` |

### General Option List Patterns

| pattern name | description | pattern |
| :---: | :--- | :---: |
| link state | whether a link is up or down, this list can be used as a base when something has a similar but expanded set of states, consider using with the case insensitive flag | <code>up&#124;down&#124;administratively up&#124;administratively down</code> |
| enabled status | for all situations that use enable and disable, also useful as base when there are further options  | <code>\[e&#124;E\]nabled&#124;\[d&#124;D\]isabled</code> |
| duplex state | used to match the state of the duplex, may need to be adjusted for different show commands that output duplex differently | <code>(auto&#124;full&#124;half)?\[-\s\]?(\[d&#124;D\]uplex&#124;unknown)</code> |

### ACL Patterns

| pattern name | description | pattern |
| :---: | :--- | :---: |
| acl name | all the characters that can compose an acl name | `[\w-\.#]+` |
| acl target | can be any, or host and then an ip or mac address | <code>any&#124;(host \d{1,3}\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}&#124;(\[a-fA-F\d\]{4}\\.){2}\[a-fA-F\d\]{4})</code> |
| acl operator | the match action of the acl in a convenient list | <code>eq&#124;gt&#124;lt&#124;neq&#124;range</code> |
| acl action | whether the acl results in allowing or stopping the flow | <code>permit&#124;deny</code> |
| acl message type | the possible message types acls can match in a convenient list | <code>ttl-exceeded&#124;unreachable&#124;packet-too-big&#124;echo-reply&#124;echo&#124;router-advertisement&#124;mld-query+</code> |
| acl protocols  | the possible protocols acls can match in a convenient list | <code>ip&#124;ipv6&#124;tcp&#124;udp&#124;ahp&#124;esp&#124;hbh&#124;icmp&#124;pcp&#124;sctp</code> |

### Access Point and Wireless Patterns

| pattern name | description | pattern |
| :---: | :--- | :---: |
| ap power | the current radio power of the access point in dBm | `\*\d\/\d.*dBm\)` |
| ap band | The current band of the access point in GHz| `[\d\.]+\s+GHz` |
| ap setting status | whether a feature or setting on the access point is enabled or disabled, or not configured at all | <code>([e&#124;E]nabled)&#124;([d&#124;D]isabled)&#124;(Not Configured)</code> |

### BGP Patterns

| pattern name | description | pattern |
| :---: | :--- | :---: |
| bgp as path | the autonomous system path of the bgp route| `[\d\s\{\}]+` |
| bgp next hop | the next hop of the bgp route | `[\w\.\:\/\[\]\,]+` |
| bgp path type | possible bgp path types in a convenient list | <code>i&#124;e&#124;c&#124;l&#124;a&#124;r&#124;I</code> |
| bgp origin code | possible bgp origin codes in a convenient list | <code>i&#124;e&#124;\?&#124;\\&#124;</code> |

### MPLS Patterns

| pattern name | description | pattern |
| :---: | :--- | :---: |
| ldp id | ldp id is just an ipv4 address with a colon and numbers at the end | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+` |
| mpls active state | possible mpls states are active, passive, and active/passive, which can be unclear| <code>active&#124;passive&#124;active\\/passive</code> |

#### OSPF Patterns

| pattern name | description | pattern |
| :---: | :--- | :---: |
| ospf advertising state | whether a route is being advertised or not | <code>Advertise&#124;DoNotAdvertise</code> |
| ospf packet type | possible ospf packet types in a convenient list | <code>Invalid&#124;Hello&#124;DB des&#124;LS req&#124;LS upd&#124;LS ack</code> |

### VLAN Patterns

| pattern name | description | pattern |
| :---: | :--- | :---: |
| vlan status | possible vlan statuses in a convenient list | <code>active&#124;suspended&#124;(.\*)lshut&#124;(.\*)unsup</code> |
| vlan list | matches vlan lists, such as 1,2,3-5 | `[\d\-\,]+` |
| port channel state | possible port channel states in a convenient list | <code>passive&#124;active&#124;on&#124;off</code> |
















