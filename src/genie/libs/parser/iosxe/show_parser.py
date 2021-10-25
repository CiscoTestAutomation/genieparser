"""show_parser.py
   supported commands:
     * show parser encrypt file status
     
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional



# =============================================
# Parser for 'show parser encrypt file status'
# =============================================

class ShowParserEncryptFileStatusSchema(MetaParser):
    """
    Schema for show parser encrypt file status
    """

    schema = {
        'feature': bool,
        'file_format': str,
        'encryption_version':str,  
    }  

class ShowParserEncryptFileStatus(ShowParserEncryptFileStatusSchema):
    """ Parser for show parser encrypt file status"""

    # Parser for 'show parser encrypt file status'
    cli_command = 'show parser encrypt file status'

    def cli(self,output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)
        # initial variables
        ret_dict = {}
        
        #Feature:            Enabled
        p1=re.compile('^Feature\:\s+(?P<feature>Enabled|Disabled)$')
        
        #File Format:        Cipher text
        p2=re.compile('^File Format:\s+(?P<format>(Plain|Cipher) text)$')
        
        #Encryption Version: ver1 
        p3= re.compile('^Encryption Version:\s+(?P<encrypt_ver>\S+)$')
        
        for line in output.splitlines():
            line = line.strip() 
            
            #Feature:            Enabled
            m = p1.match(line)
            if m:
                group=m.groupdict()
                ret_dict['feature'] = True if \
                    group['feature'] == 'Enabled' else\
                    False
                continue
                
            #File Format:        Cipher text
            m=p2.match(line)
            if m:
                group=m.groupdict()
                ret_dict['file_format'] =group['format']
                continue
            
            #Encryption Version: ver1 
            m=p3.match(line) 
            if m:
                group=m.groupdict()
                ret_dict['encryption_version']=group['encrypt_ver']
                continue
                
        return ret_dict