'''Common functions to be used in parsers'''

# python
import re
import warnings

class Common():
    '''Common functions to be used in parsers.'''

    @classmethod
    def regexp(self, expression):
        def match(value):
            if re.match(expression, value):
                return value
            else:
                raise TypeError("Value '%s' doesnt match regex '%s'"
                                % (value, expression))
        return match

    @classmethod
    def convert_intf_name(self, intf):
        '''return the full interface name

            Args:
                intf (`str`): Short version of the interface name

            Returns:
                Full interface name fit the standard

            Raises:
                None

            example:

                >>> convert_intf_name(intf='Eth2/1')
        '''

        # Please add more when face other type of interface
        convert = {'Eth': 'Ethernet',
                   'Lo': 'Loopback',
                   'Fa': 'FastEthernet',
                   'Po': 'Port-channel',
                   'Null': 'Null',
                   'Gi': 'GigabitEthernet',
                   'Te': 'TenGigabitEthernet',
                   'mgmt': 'mgmt'}
        int_type = re.search('([a-zA-Z]+)', intf).group(0)
        int_port = re.search('([\d\/\.]+)', intf).group(0)
        if int_type in convert.keys():
            return(convert[int_type] + int_port)
        else:
            return(intf)


    @classmethod
    def retrieve_xml_child(self, root, key):
        '''return the root which contains the key from xml

            Args:

                root (`obj`): ElementTree Object, point to top of the tree
                key (`str`): Expceted tag name. ( without namespace)

            Returns:
                Element object of the given tag

            Raises:
                None

            example:

                >>> retrieve_xml_child(
                        root=<Element '{urn:ietf:params:xml:ns:netconf:base:1.0}rpc-reply' at 0xf760434c>,
                        key='TABLE_vrf')
        '''
        for item in root:
            if key in item.tag:
                return item
            else:
                root = item
                return self.retrieve_xml_child(root, key)


    @classmethod
    def compose_compare_command(self, root, namespace, expect_command):
        '''compose commmand from the xml Element object from the root,
           then compare with the command with the expect_command.
           Only work for cisco standard output.

            Args:

                root (`obj`): ElementTree Object, point to top of the tree
                namespace (`str`): Namesapce. Ex. {http://www.cisco.com/nxos:8.2.0.SK.1.:rip}
                expect_command (`str`): expected command.

            Returns:
                None

            Raises:
                AssertionError: xml tag cli and command is not matched
                Exception: No mandatory tag __readonly__ in output

            example:

                >>> compose_compare_command(
                        root=<Element '{urn:ietf:params:xml:ns:netconf:base:1.0}rpc-reply' at 0xf760434c>,
                        namespace='{http://www.cisco.com/nxos:8.2.0.SK.1.:rip}',
                        expect_command='show bgp all dampening flap-statistics')
        '''
        # get to data node
        cmd_node = root.getchildren()[0]
        # compose command from element tree
        # ex.  <nf:data>
        #        <show>
        #         <bgp>
        #          <all>
        #           <dampening>
        #            <flap-statistics>
        #             <__readonly__>
        cli = ''
        while True:
            # get next node
            try:
                cmd_node = cmd_node.getchildren()
                if len(cmd_node) == 1:

                    # when only have one child
                    cmd_node = cmd_node[0]

                    # <__XML__PARAM__vrf-name>
                    #  <__XML__value>VRF1</__XML__value>
                    # </__XML__PARAM__vrf-name>
                    if '__XML__value' in cmd_node.tag:
                        cli += ' ' + cmd_node.text

                elif len(cmd_node) > 1:

                   # <__XML__PARAM__interface>
                   #   <__XML__value>loopback100</__XML__value>
                   #   <vrf>
                   for item in cmd_node:
                       if '__XML__value' in item.tag:
                           cli += ' ' + item.text
                       else:
                           cmd_node = item
                           break
                else:
                    break
            except:
                pass

            # get tag name
            tag = cmd_node.tag.replace(namespace, '')

            # __readonly__ is the end of the command
            if '__readonly__' not in tag:
                if '__XML__PARAM__' not in tag and \
                   '__XML__value' not in tag and \
                   'TABLE' not in tag:
                    cli += ' ' + tag
            else:
                break

            # if there is no __readonly__ but the command has outputs
            # should be warining
            if 'TABLE' in tag:
            	warnings.warn('Tag "__readonly__" should exsist in output when '
            		          'there are actual values in output')
            	break

        cli = cli.strip()
        # compare the commands
        assert cli == expect_command, \
            'Cli created from XML tags does not match the actual cli:\n'\
            'XML Tags cli: {c}\nCli command: {e}'.format(c=cli, e=expect_command)