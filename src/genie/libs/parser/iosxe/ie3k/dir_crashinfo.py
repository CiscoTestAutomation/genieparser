""" dir_crashinfo.py

Parser for the following command:
    ** 'dir crashinfo:'

This parser extracts structured information about the files and directories
in the `crashinfo` directory, including details such as type (file or directory),
size, modification date, and time.
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

# =============================================
# Schema for `dir crashinfo:` command
# =============================================
class DirCrashInfoSchema(MetaParser):
    """Schema for `dir crashinfo:` command
    Defines the structure of the parsed output.
    The `files` key holds details about each file in the `crashinfo` directory, such as:
    - type: Whether the entry is a file or directory.
    - size: The size of the file or directory in bytes.
    - date: The date the file or directory was last modified.
    - time: The time the file or directory was last modified.
    """
    schema = {
        'files': {  # A dictionary of files
            Any(): {  # Any filename can be a key
                'type': str,  # Type of entry (file or directory)
                'size': str,  # Size of the file in bytes
                'date': str,  # Date of last modification
                'time': str,  # Time of last modification
            }
        }
    }

# =============================================
# Parser for `dir crashinfo:`
# =============================================
class DirCrashInfo(DirCrashInfoSchema):
    """Parser for `dir crashinfo:` command
    Extracts file details from the CLI output of `dir crashinfo:`.
    """

    def cli(self, output=None):
        """
        Parses the CLI output for `dir crashinfo:`.
        
        Args:
            output (str): The raw CLI output as a string. If `None`, the command
                          will be executed on the device.
        Returns:
            dict: A structured dictionary containing parsed file details.
        """
            # Execute the CLI command on the device
        output = self.device.execute(self.cli_command)

        # Initialize the parsed result with the required schema structure
        parsed_result = {}

        # Regex pattern to match file details in the CLI output
        # Example CLI Output Pattern:
        # 1  drwx          4096  Jan  1 2023  12:00:00 +00:00  directory1
        # 2  -rw-        123456  Feb 15 2023  08:30:45 +00:00  file1.txt
        p0 = re.compile(
            r'^\s*\d+\s+'  # Example: "1" or "2"
            r'(?P<type>[-\w]{3,4})\s+'  # Example: "drwx" (directory) or "-rw-" (file)
            r'(?P<size>\d+)\s+'  # Example: "123456" (file size in bytes)
            r'(?P<date>\w{3}\s+\d{1,2}\s+\d{4})\s+'  # Example: "Feb 15 2023" (date)
            r'(?P<time>\d{2}:\d{2}:\d{2})\s+\+\d{2}:\d{2}\s+'  # Example: "08:30:45 +00:00" (time with timezone)
            r'(?P<filename>\S+)$'  # Example: "file1.txt" (filename or directory name)
        )

        # =============================================
        # Process each line in the CLI output
        # =============================================
        for line in output.splitlines():
            line = line.strip()  # Remove leading/trailing whitespace

            # Example CLI Output being processed:
            # 1  drwx          4096  Jan  1 2023  12:00:00 +00:00  directory1
            # 2  -rw-        123456  Feb 15 2023  08:30:45 +00:00  file1.txt

            # Attempt to match the line with the regex pattern
            m = p0.match(line)
            if m:
                # Example line: "2  -rw-        123456  Feb 15 2023  08:30:45 +00:00  file1.txt"
                # Extracted result: {'type': '-rw-', 'size': '123456', 'date': 'Feb 15 2023', 'time': '08:30:45', 'filename': 'file1.txt'}

                # Extract file details as a dictionary
                file_data = m.groupdict()

                # Add the file details to the result dictionary
                parsed_result['files'][file_data['filename']] = {
                    'type': 'directory' if file_data['type'] == 'drwx' else 'file',  # Determine if it's a file or directory
                    'size': file_data['size'],  # Size in bytes
                    'date': file_data['date'],  # Last modified date
                    'time': file_data['time'],  # Last modified time
                }

        return parsed_result