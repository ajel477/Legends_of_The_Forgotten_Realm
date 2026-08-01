from core.weapon import Weapon
from core.enums import WeaponRarity
from core.armor import Armor
from core.enums import ArmorRarity

class Factory:

    @staticmethod
    def create_weapon(data):

        rarity = WeaponRarity(data["rarity"])

        return Weapon(
            item_id=data["id"],
            name=data["name"],
            rarity=rarity,
            damage=data["damage"],
            crit_bonus=data["crit_bonus"],
            price=data["price"],
            required_level=data["required_level"]
        )

    @staticmethod
    def create_armor(data):

        rarity = ArmorRarity(data["rarity"])

        return Armor(
            item_id=data["id"],
            name=data["name"],
            rarity=rarity,
            defense_bonus=data["defense_bonus"],
            hp_bonus=data["hp_bonus"],
            mana_bonus=data["mana_bonus"],
            crit_resistance=data["crit_resistance"],
            price=data["price"],
            required_level=data["required_level"]
        )