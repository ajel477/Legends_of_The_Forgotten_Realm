from core.data_loader import DataLoader
from core.factory import Factory
from core.constants import DATA_DIRECTORY


class ArmorManager:

    @staticmethod
    def load_armors():

        armor_data = DataLoader.load_json(
             "data/armors.json"
        )

        armors = []

        for armor in armor_data:
            armors.append(
                Factory.create_armor(armor)
            )

        return armors