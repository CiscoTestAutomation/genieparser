'''show_post.py

IOSXE c9200 parsers for the following show commands:
   * show post
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

from genie.libs.parser.iosxe.cat9k.c9300.show_post import(
    ShowPostSchema as ShowPostSchema_92,
    ShowPost as ShowPost_92 )

class ShowPostSchema(ShowPostSchema_92):
    ...

# ============================
#  Parser for 'show post'
# ============================

class ShowPost(ShowPost_92):
    ...