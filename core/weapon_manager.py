from core.data_loader import DataLoader
from core.factory import Factory

class WeaponManager:

    @staticmethod
    def load_weapons():

        weapon_data = DataLoader.load_json(
            "data/weapons.json"
        )

        weapons = []

        for weapon in weapon_data:

            weapons.append(
                Factory.create_weapon(weapon)
            )

        return weapons