import enum
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ORE_PATH = os.path.join(ROOT_DIR, r'Ores')
UI_PATH = os.path.join(ROOT_DIR, r'UI')
ICON_PATH = os.path.join(ROOT_DIR, r'ItemIcons')
LOOT_PATH = os.path.join(ROOT_DIR, r'Loot')


class Loot(enum.Enum):
    MediumPotion = os.path.join(LOOT_PATH, "MediumPotion.PNG")
    LargePotion = os.path.join(LOOT_PATH, "LargePotion.PNG")
    GlacialBlade = os.path.join(LOOT_PATH, "GlacialBlade.PNG")


class Ores(enum.Enum):
    Copper = os.path.join(ORE_PATH, "Copper.PNG")
    Iron = os.path.join(ORE_PATH, "Iron.PNG")
    Coal = os.path.join(ORE_PATH, "Coal.PNG")
    Crimsteel = os.path.join(ORE_PATH, "Crimsteel.PNG")
    Gold = os.path.join(ORE_PATH, "Gold.PNG")
    Mythan = os.path.join(ORE_PATH, "Mythan.PNG")


class UI(enum.Enum):
    Bank = os.path.join(UI_PATH, "Bank.PNG")
    Last_item_box = os.path.join(UI_PATH, "LastItemBox.PNG")
    Full_inv_box = os.path.join(UI_PATH, "InvFull.PNG")
    Ore_depleted = os.path.join(UI_PATH, "OreDepleted.PNG")
    UseIcon = os.path.join(UI_PATH, "UseIcon.PNG")
    Smelt = os.path.join(UI_PATH, "Smelting.PNG")


class Icons(enum.Enum):
    CrimSteelIconBank = os.path.join(ICON_PATH, "CrimSteelIconBank.PNG")
    CrimSteelIconInventory = os.path.join(ICON_PATH, "CrimSteelIconInventory.PNG")
    CrimSteelBarSmelter = os.path.join(ICON_PATH, "CrimSteelBarSmelt.PNG")
    CrimSteelBarInventory = os.path.join(ICON_PATH, "CrimSteelBarInventory.PNG")
    CrimSteelBarBank = os.path.join(ICON_PATH, "CrimSteelBarBank.PNG")

    CrimSteelCap = os.path.join(ICON_PATH, "CrimSteelCap.PNG")

    HammerBank = os.path.join(ICON_PATH, "HammerBank.PNG")

    CoalIconBank = os.path.join(ICON_PATH, "CoalIconBank.PNG")
    CoalIconInventory = os.path.join(ICON_PATH, "CoalIconInventory.PNG")

    GoldOreIconBank = os.path.join(ICON_PATH, "GoldIconBank.PNG")
    GoldNuggetSmelter = os.path.join(ICON_PATH, "GoldNuggetSmelter.PNG")
    GoldNuggetInventory = os.path.join(ICON_PATH, "GoldNuggetInventory.PNG")
    GoldBarInventory = os.path.join(ICON_PATH, "GoldBarInventory.PNG")
    GoldNuggetBank = os.path.join(ICON_PATH, "GoldNuggetBank.PNG")
    GoldBarSmelter = os.path.join(ICON_PATH, "GoldBarSmelter.PNG")



