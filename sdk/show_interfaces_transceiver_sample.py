import pprint
from genie.conf.base import Device
dev = Device(name="aName", os="aos)
dev.custom.abstraction = {"order":["os"]}
with open('show_interfaces_transceiver.txt' as f:
   output = f.read()
print(output)
res=dev.parse("show_interfaces_transceiver", output=output)
pprint.pprint(res, width=100)

