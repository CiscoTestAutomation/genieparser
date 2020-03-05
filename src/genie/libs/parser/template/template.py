#*******************************************************************************
#*                           Parser Template
#* ----------------------------------------------------------------------------
#* ABOUT THIS TEMPLATE - Please read
#*
#* - Any comments with "#*" in front of them (like this entire comment box) are
#*   for template clarifications only and should be removed from the final
#*   product.
#*
#* - Anything enclosed in <> must be replaced by the appropriate text for your
#*   application
#*
#* Author:
#*    Ke Liu, Automation Strategy - Core Software Group (CSG)
#*
#* Support:
#*    asg-genie-support@cisco.com
#*
#* Description:
#*   This template file describes how to write a specific parser class by
#*   inheriting the MataParser object.
#*
#* Read More:
#*   For the complete and up-to-date user guide on parser template, visit:
#*   URL= http://wwwin-pyats.cisco.com/documentation/html/parser/index.html
#*
#*******************************************************************************

#*******************************************************************************
#* DOCSTRINGS
#*
#*   All test scripts should use the built-in Python docstrings functionality 
#*   to define script/class/method headers.
#*
#* Format:
#*   Docstring format should follow:
#*   URL= http://sphinxcontrib-napoleon.readthedocs.org/en/latest/index.html
#*
#* Read More:
#*   Python Docstrings, PEP 257: 
#*   URL= http://legacy.python.org/dev/peps/pep-0257/
#*******************************************************************************
'''template.py

< describe your parser >

Arguments:
    <name> (<type>): <description of your parser argument>

Examples:
    < provide examples on how to use this parser: init and call. >

References:
    < provide references here. >

Notes:
    < provide notes if needed >

'''

#*******************************************************************************
#* OPTIONAL AUTHOR INFORMATION
#*
#*   format:
#*      __author__ = '<first> <last> <email>'
#*      __copyright__ = 'Copyright 2016, Cisco Systems'
#*      __credits__ = ['<list>', '<of>', '<names>']
#*      __maintainer__ = '<team owning/maintaining this script>'
#*      __email__ = '<email of owners>''
#*      __date__= '<last modified date>'
#*      __version__ = <decimal version string>
#*
#*******************************************************************************

# optional author information
__author__ = 'Ke Liu <kel2@cisco.com>'
__copyright__ = 'Copyright 2016, Cisco Systems'
__credits__ = ["Sedy Yadollahi", 
               "Siming Yuan", 
               "Jean-Benoit Aubin"]
__maintainer__ = 'ASG/ATS team'
__email__ = 'asg-genie-support@cisco.com'
__date__= 'May 01, 2016'
__version__ = 1.0


#*******************************************************************************
#* IMPORTS
#*
#*   import all modules that are needed in your test script here. Use some 
#*   form of sorting to make it easy to read. 
#*
#* Convention:
#*   - one module per import for clarity
#*   - sort imports either alphabetically or per length to give ease of reading,
#*     also try to differentiate by functionality/distributor
#*
#* Example:
#*   import os
#*   import sys
#*   import xmltodict
#*   from pyats import tcl
#*   from genie.metaparser import MetaParser
#*
#* Read More:
#*   Python Import System
#*   URL= https://docs.python.org/3/reference/import.html
#*******************************************************************************

#
# imports statements
#
from genie.metaparser.util.schemaengine import Any
from genie.metaparser import MetaParser

#*******************************************************************************
#* ShowParser: parser class
#*
#* Each module contains at least one parser class which provides the 
# implementation details of all supported parsing mechanisms (cli(), xml(), 
#* yang()). Each parser class must inherit from `MetaParser`.
#*
#* Class name should be the first 2 words of the 
#* corresponding cli command or equivalent. For example: class 'ShowVersion' 
#* to represent 'show version'.
#*
#* If the first 2 words contain strong ambiguity (e.g.: show ip),
#* extend the next word (e.g.: show ip ospf) to clarify the parser purpose.
#*
#* For variable phrases within the parser name (e.g.: show interface Eth3/4),
#* use _WORD_ to present the phrase (e.g.: ShowInterface_WORD_).
#*

class ShowParser(MetaParser):

    '''class ShowParser

    parser class - implement detailed parsing mechanisms for cli, xml, and 
    yang output.

    Arguments:
        <name> (<type>): <description of your parser argument>
    
    Examples:
        < provide examples on how to initialize this parser. >
    '''

    #*************************
    #* class constructor (optional) __init__():
    #* 
    #* In case of redefining __init__ in parser class to overwrite the super
    #* class MetaParser __init__() to support extra attributes, here is an 
    #* example:
    #*     def __init__(self, name, **kwargs):
    #*         super().__init__(name=name, **kwargs)
    
    # <define your own __init__ here, or skip it by using superclass definition>

    #*************************
    #* schema - class variable
    #*
    #* schema defines the common data structure among all types of device output 
    #* (cli, xml, yang) the current parser supports. Typical scenario is:
    #* the first user who defines the first parsing mechanism (e.g.: cli ()) in 
    #* parser class will also define the schema for the output structure.
    #* At the end of the parsing process, parser engine (MetaParser) will do
    #* schema checking to make sure the parser always returns the output 
    #* (nested dict) that has the same data structure across all supported 
    #* parsing mechanisms (cli(), yang(), xml()).
    #* 
    #* Example of schema (show version) - nested dict
    #*    schema = {'cmp': {
    #*                    'module': {
    #*                             Any(): {
    #*                                     'bios_compile_time': str,
    #*                                     'bios_version': str,
    #*                                     'image_compile_time': str,
    #*                                     'image_version': str,
    #*                                     'status': str},}},
    #*              'hardware': {
    #*                    'bootflash': str,
    #*                    'chassis': str,
    #*                    'cpu': str,
    #*                    'device_name': str,
    #*                    'memory': str,
    #*                    'model': str,
    #*                    'processor_board_id': str,
    #*                    'slots': str,
    #*                    Any(): Any(),},}
    #*
    #* Here Any() in schema acting like a wildcard character, usually used to 
    #* presenting the variable keys within the dictionary.
    #* For more info on how to use scheme: please read schemaengine API doc.
    #*

    # schema = <dict>

    #******************************
    #* parsing mechanism: cli
    #* Function cli() defines the cli type output parsing mechanism which
    #* typically contains 3 steps: executing, transforming, returning
    #*
    #* Step1 - executing
    #* User has choices of calling the existing cli parsers from known 
    #* libraries, or implementing new parsing mechanism here 
    #* (eg.: regular expression).
    #*
    #* Example 1 - calling existing cli parser lib: CAAS
    #*     from pyats import tcl
    #*     output = tcl.q.caas.abstract(device=self.device.handle, 
    #*                                  exec='show version')
    #*     parsed_output = tcl.cast_any(output[1])
    #
    #* Example 2 - calling existing cli parser lib: ROUTER_SHOW
    #*     from pyats import tcl
    #*     parsed_output = tcl.q.router_show(device=device.handle, 
    #*                                       cmd=show version)
    #*
    #* Example 3 - calling existing cli parser lib: PYPARSE
    #*     from autoparser import pyparse
    #*     parsed_output = pyparse(device=device, 
    #*                             cmd = cli, 
    #*                             path_to_lib=path_to_lib,
    #*                             keys=keys)
    #*
    #* Example 4 - user implementing parsing mechanism
    #*    parsed_output = {}
    #*    output = self.device.execute("show version | inc 'cisco '")
    #*    m = re.match(r"cisco ([a-zA-Z0-9 ]+)", output.strip(' \t\n\r'))
    #*    if m:
    #*        parsed_output['model'] = m.group(0).strip()
    #* 
    #* Step2 - transforming
    #* This step might be optional for the first parser mechanism writer.
    #* The purpose of this step is to enforce the final output structure from
    #* all different parsing mechanisms (cli(), xml(), yang())to be same.
    #* User can greatly leverage all the functionalities provided in 
    #* metaparser.util class.
    #*
    #* Useful tools to do the transformation:
    #* dict.update()  --> adding missing key-value pairs
    #* metaparser.util.keynames_convert()  --> nested key names converting
    #*
    #* Step3: - returning
    #* return the final result - the structure of the result has to be 
    #* (nested)dictionary

    def cli(self, **kwargs):
        # executing parser
        # <step1 executing: get parsing resullt by calling existing parser \
        #        function or write user own parsing code here>
        
        # converting the result to compliance with schema
        # <step2: transform the datastructure to be compliance with the schema \
        #         defined on top of the class>
        
        # <step3: return the final parsing result>
        return

    #******************************
    #* parsing mechanism: xml
    #* Function xml() defines the xml type output parsing mechanism which
    #* typically contains 3 steps: executing, transforming, returning
    #*
    #* Step1 - executing
    #* User has choices of calling the existing xml parsers from known 
    #* libraries, or implementing new parsing mechanism here.
    #*
    #* Example - calling existing xml parser lib: CAAS
    #*     from pyats import tcl
    #*     output = tcl.q.caas.abstract(device=self.device.handle, 
    #*                                  exec='show version | xml')
    #*     parsed_output = tcl.cast_any(output[1])
    #
    #* 
    #* Step2 - transforming
    #* This step might be optional for the first parser mechanism writer.
    #* The purpose of this step is to enforce the final output structure from
    #* all different parsing mechanisms (cli(), xml(), yang())to be same.
    #* User can greatly leverage all the functionalities provided in 
    #* metaparser.util class.
    #*
    #* Useful tools to do the transformation:
    #* dict.update()  --> adding missing key-value pairs
    #* metaparser.util.keynames_convert()  --> nested key names converting
    #*
    #* Step3: - returning
    #* return the final result - the structure of the result has to be 
    #* (nested)dictionary

    def xml(self, **kwargs):
        # executing parser
        # <step1 executing: get parsing resullt by calling existing parser \
        #        function or write user own parsing code here>
        
        # converting the result to compliance with schema
        # <step2: transform the datastructure to be compliance with the schema \
        #         defined on top of the class>

        # <step3: return the final parsing result>
        return

    #******************************
    #* parsing mechanism: yang
    #* Function yang() defines the yang type output parsing mechanism which
    #* typically contains 3 steps: executing, transforming, returning
    #*
    #* Step1 - executing
    #* User has choices of calling the existing yang parsers from known 
    #* libraries, or implementing new parsing mechanism here.
    #*
    #* Example - yang parsing mechnism implementation
    #*       import xmltodict
    #*       from cnetconf import testmodel
    #*
    #*       # create netconf client obj
    #*       base = testmodel.BaseTest()
    #*
    #*       # connect to netconf server
    #        base.connect_netconf()
    #*      
    #*       # prepare the rpc request
    #*       netconf_request = """
    #*   <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    #*           <get>
    #*             <filter>
    #*               <native xmlns="">
    #*                   <version>
    #*                   </version>
    #*               </native>
    #*             </filter>
    #*           </get>
    #*         </rpc>
    #*       """
    #*
    #*       # sending request to get response
    #*       ncout = base.netconf.send_config(netconf_request)
    #*
    #*       # filter out the 'data' from the raw response
    #*       filtered_result = xmltodict.parse(ncout, 
    #*                                         process_namespaces=True,
    #*                                         namespaces={
    #*                          'urn:ietf:params:xml:ns:netconf:base:1.0':None,
    #*                          'urn:ios':None,})
    #*
    #*       # nested dict contains only interested data
    #*       parsed_output =  filtered_result['rpc-reply']['data'].get('native')
    #* 
    #* Step2 - transforming
    #* This step might be optional for the first parser mechanism writer.
    #* The purpose of this step is to enforce the final output structure from
    #* all different parsing mechanisms (cli(), xml(), yang())to be same.
    #* User can greatly leverage all the functionalities provided in 
    #* metaparser.util class.
    #*
    #* Useful tools to do the transformation:
    #* dict.update()  --> adding missing key-value pairs
    #* metaparser.util.keynames_convert()  --> nested key names converting
    #*
    #* Step3: - returning
    #* return the final result - the structure of the result has to be 
    #* (nested)dictionary

    def yang(self, **kwargs):
        # executing parser
        # <step1 executing: get parsing resullt by calling existing parser \
        #        function or write user own parsing code here>
        
        # converting the result to compliance with schema
        # <step2: transform the datastructure to be compliance with the schema \
        #         defined on top of the class>

        # <step3: return the final parsing result>
        return
