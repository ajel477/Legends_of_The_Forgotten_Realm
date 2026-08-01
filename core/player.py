class Player:

    def __init__(self, name, player_class, stats):

        self.name = name
        self.player_class = player_class

        self.level = 1
        self.experience = 0
        self.gold = 100

        self.max_hp = stats["max_hp"]
        self.hp = self.max_hp

        self.max_mana = stats["max_mana"]
        self.mana = self.max_mana

        self.attack = stats["attack"]
        self.defense = stats["defense"]

        self.crit_chance = stats["crit_chance"]
        self.crit_damage = 150

        self.weapon = None
        self.armor = None

        self.inventory = []

        self.potions = []

        self.bosses_defeated = 0
        self.enemies_defeated = 0

    def display_stats(self):

        print("\n========== PLAYER ==========")

        print(f"Name           : {self.name}")
        print(f"Class          : {self.player_class}")
        print(f"Level          : {self.level}")
        print(f"Experience     : {self.experience}")

        print(f"HP             : {self.hp}/{self.max_hp}")
        print(f"Mana           : {self.mana}/{self.max_mana}")

        print(f"Attack         : {self.attack}")
        print(f"Defense        : {self.defense}")

        print(f"Critical Chance: {self.crit_chance}%")

        print(f"Gold           : {self.gold}")

        print("============================")