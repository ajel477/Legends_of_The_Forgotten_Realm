from core.consumable import Consumable


class Potion(Consumable):

    def __init__(
        self,
        item_id,
        name,
        rarity,
        potion_type,
        value,
        duration,
        price,
        required_level=1
    ):

        super().__init__(
            item_id,
            name,
            rarity,
            price,
            required_level
        )

        self.potion_type = potion_type
        self.value = value
        self.duration = duration