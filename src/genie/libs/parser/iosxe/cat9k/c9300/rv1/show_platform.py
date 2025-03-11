from genie.libs.parser.iosxe.rv1.show_platform import (
    ShowInventorySchema as XE_ShowInventorySchema,
    ShowInventory as XE_ShowInventory)

# ============================
#  Schema for 'show inventory'
# ============================
class ShowInventorySchema(XE_ShowInventorySchema):
    ...


# ============================
#  Parser for 'show inventory'
# ============================
class ShowInventory(XE_ShowInventory):
    """
    Parser for :
        * show inventory
    """
    ...
