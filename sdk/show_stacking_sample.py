import pprint
from genie.conf.base import Device
dev = Device(name="aName", os="aos)
dev.custom.abstraction = {"order":["os"]}
with open('show_stacking.txt' as f:
   output = f.read()
print(output)
res=dev.parse("show_stacking", output=output)
pprint.pprint(res, width=100)

