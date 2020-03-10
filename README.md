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

Installation guide can be found on [our website].

[our website]: https://developer.cisco.com/site/pyats/

```
$ pip install genie.metaparser
```

# ChangeLog

Change logs can be found [here](changelog/CHANGELOG.md).



# To contributors:

[Guide] 

[Guide]: https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/writeparser/writeparser.html#


Once you create a new parser, don't forget to check 1, 2, and 3;
if you only update the parser class without modifying/creating the schema, please check 2 and 3. 
- [ ] 1. `make json`
- [ ] 2. cd tests; and execute `python -m unittest -v`
- [ ] 3. update [changelog] by following the existing format

[changelog]: https://github.com/CiscoTestAutomation/genieparser/blob/master/changelog/undistributed.rst



> Copyright (c) 2018 Cisco Systems, Inc. and/or its affiliates
