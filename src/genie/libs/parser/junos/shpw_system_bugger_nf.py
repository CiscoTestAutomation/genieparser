
class ShowSystemBufferNoForwarding(ShowSystemBuffer):
    """ Parser for:
            - 'show system buffer no-forwarding'
    """

    cli_command = "show system buffers no-forwarding"

     def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)