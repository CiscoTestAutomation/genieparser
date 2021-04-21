"""vimcmd.py

Linux parsers for the following commands:
    * vim-cmd vmsvc/getallvms
    * vim-cmd vmsvc/snapshot.get {vmid}
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =======================================================
# Schema for 'vim-cmd vmsvc/getallvms'
# =======================================================
class VimCmdVmsvcGetAllVmsSchema(MetaParser):
    """Schema for vim-cmd vmsvc/getallvms"""
    
    schema = {
        'vmid': {
            Any(): {
                'vmid': str,
                'name': str,
                'file': str,
                'guest_os': str,
                'version': str,
                Optional('annotation'): str,
            }
        }
    }


# =======================================================
# Parser for 'vim-cmd vmsvc/getallvms'
# =======================================================
class VimCmdVmsvcGetAllVms(VimCmdVmsvcGetAllVmsSchema):
    """Parser for vim-cmd vmsvc/getallvms"""
    
    cli_command = ['vim-cmd vmsvc/getallvms']
    
    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
            
        else:
            out = output

        # Parsed output
        ret_dict = {}
        
        #     Vmid      Name                         File                           Guest OS         Version   Annotation
        #      42     P1-4          [VM_storage] P1-4/P1-4.vmx                 other26xLinuxGuest     vmx-07              
        #      43     PE1-4_old     [VM_storage] PE1-4/PE1-4.vmx               other26xLinuxGuest     vmx-07              
        #      45     N7K-PE1-2     [VM_storage] N7K-PE1-2/N7K-PE1-2.vmx       other24xLinuxGuest     vmx-08              
        #      51     n9kv1_1       [VM_storage] n9kv1_1/n9kv1_1.vmx           otherGuest64           vmx-10              
        #      52     n9kv2_1       [VM_storage] n9kv2_1/n9kv2_1.vmx           otherGuest64           vmx-10              
        #       9     PE1-2         [VM_storage] PE1/PE1.vmx                   other24xLinuxGuest     vmx-08
        p1 = re.compile(r'^(?P<vmid>\S+)\s+(?P<name>\S+)\s+' + 
                        r'(?P<file>\S+\s+\S+)\s+(?P<guest_os>\S+)\s+' + 
                        r'(?P<version>\S+)')
        
        #       9     PE1-2         [VM_storage] PE1/PE1.vmx                   other24xLinuxGuest     vmx-08    - machine 2
        p2 = re.compile(r'^(?P<vmid>\S+)\s+(?P<name>\S+)\s+' + 
                        r'(?P<file>\S+\s+\S+)\s+(?P<guest_os>\S+)\s+' + 
                        r'(?P<version>\S+)\s+(?P<annotation>[\s\S]+)$')
        
        for line in out.splitlines():
            line = line.strip()
            
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                vm_id = groups['vmid']
                ret_dict.setdefault('vmid', {}).setdefault(vm_id, groups)
                continue
            
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                vm_id = groups['vmid']
                ret_dict.setdefault('vmid', {}).setdefault(vm_id, groups)
                continue
        
        #if len(ret_dict) == 0:
        #    ret_dict.setdefault('vmid', {})

        return ret_dict
    

# =======================================================
# Schema for 'vim-cmd vmsvc/snapshot.get {vmid}'
# =======================================================
class VimCmdVmsvcSnapshotGetVmIdSchema(MetaParser):
    """Schema for vim-cmd vmsvc/snapshot.get {vmid}"""
    
    schema = {
        'vmid': {
            Any(): {
                'snapshot': {
                    Any(): {   # snapshot id
                        'name': str,
                        'id': str,
                        Optional('description'): str,
                        'created': str,
                        'state': str
                    }
                }
            }
        }
    }


# =======================================================
# Parser for 'vim-cmd vmsvc/snapshot.get {vmid}'
# =======================================================
class VimCmdVmsvcSnapshotGetVmId(VimCmdVmsvcSnapshotGetVmIdSchema):
    """Parser for vim-cmd vmsvc/snapshot.get {vmid}"""
    
    cli_command = ['vim-cmd vmsvc/snapshot.get {vmid}']
    
    def cli(self, vmid, output=None):
        if output is None:
            cmd = self.cli_command[0].format(vmid=vmid)
            out = self.device.execute(cmd)
        else:
            out = output
            
        # Parsed Output
        ret_dict = {}
        
        # --Snapshot Id        : 8
        # ----Snapshot Id        : 13
        p1 = re.compile(r'^.*Snapshot\s+Id\s+:\s+(?P<id>\S+)$')
        
        # --Snapshot Name        : PE1RebootGoldenSnapshot
        # ----Snapshot Name        : PE1-2NEWGOLDENSNAPSHOT
        p2 = re.compile(r'^.*Snapshot\s+Name\s+:\s+(?P<name>\S+)$')
        
        # --Snapshot Desciption  :
        # ----Snapshot Desciption  :
        p3 = re.compile(r'^.*Snapshot\s+Desciption\s+:\s+(?P<description>\S+)$')
        
        # --Snapshot Created On  : 12/1/2014 14:39:4
        # ----Snapshot Created On  : 10/2/2015 9:13:45
        p4 = re.compile(r'^.*Snapshot\s+Created\s+On\s+:\s+(?P<created>\S+\s+\S+)$')
        
        # --Snapshot State       : powered off
        # ----Snapshot State       : powered off
        p5 = re.compile(r'^.*Snapshot\s+State\s+:\s+(?P<state>\S+\s+\S+)$')
        
        snapshot_name = ''
        for line in out.splitlines():
            line = line.strip()
            
            # --Snapshot Id        : 8
            # ----Snapshot Id        : 13
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                snapshot_id = groups['id']
                
                # We add the snapshot name into the groups dictionary
                # Since the snapshot name pattern will come first than the 
                # snapshot id pattern which we use it as the unique key in
                # our return dictionary
                groups['name'] = snapshot_name
                snapshot_info_dict = ret_dict.setdefault('vmid', {}).\
                    setdefault(vmid, {}).setdefault('snapshot', {}).\
                        setdefault(snapshot_id, groups)
                continue
            
            # --Snapshot Name        : PE1RebootGoldenSnapshot
            # ----Snapshot Name        : PE1-2NEWGOLDENSNAPSHOT
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                snapshot_name = groups['name']
                continue
            
            # --Snapshot Desciption  :
            # ----Snapshot Desciption  :
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                snapshot_info_dict.update(groups)
                continue
            
            # --Snapshot Created On  : 12/1/2014 14:39:4
            # ----Snapshot Created On  : 10/2/2015 9:13:45
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                snapshot_info_dict.update(groups)
                continue
                
            # --Snapshot State       : powered off
            # ----Snapshot State       : powered off
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                snapshot_info_dict.update(groups)
                continue

        return ret_dict

