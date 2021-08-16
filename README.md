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

# How to write 'changelog':
1. A few examples are added into changelog/undistributed/template.rst:
```
* IOS
* Modified ShowVersion:
    * Changed <key1>, <key2> from schema to Optional.
        * Updated regex pattern <p1> to accommodate various outputs.
        * Added keys <key3>, <key4> into the schema.
```
Please take it as a reference, and avoid to create vague logs, such as 'Updated regex.' 

2. How to generate an unique number for file name:
```
>>>from datetime import datetime
>>>datetime.utcnow().strftime('%Y%m%d%H%M%S')
'20200807212611'
```

> Copyright (c) 2020 Cisco Systems, Inc. and/or its affiliates
