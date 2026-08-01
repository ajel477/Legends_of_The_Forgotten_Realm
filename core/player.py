from core.constants import (
    STARTING_GOLD,
    STARTING_LEVEL,
    STARTING_EXP,
    DEFAULT_CRIT_DAMAGE
)


class Player:
    """
    Represents the player character.
    Stores all player-related information including stats,
    inventory, equipment, and progression.
    """

    def __init__(self, name: str, player_class, stats: dict):

        # ==========================
        # Basic Information
        # ==========================
        self.name = name
        self.player_class = player_class

        # ==========================
        # Progression
        # ==========================
        self.level = STARTING_LEVEL
        self.experience = STARTING_EXP
        self.gold = STARTING_GOLD

        self.bosses_defeated = 0
        self.enemies_defeated = 0

        # ==========================
        # Base Stats
        # (Never modified directly)
        # ==========================
        self.max_hp = stats["max_hp"]
        self.hp = self.max_hp

        self.max_mana = stats["max_mana"]
        self.mana = self.max_mana

        self.base_attack = stats["attack"]
        self.base_defense = stats["defense"]

        self.crit_chance = stats["crit_chance"]
        self.crit_damage = DEFAULT_CRIT_DAMAGE

        # ==========================
        # Current Stats
        # (Can change due to equipment,
        # buffs, skills, etc.)
        # ==========================
        self.attack = self.base_attack
        self.defense = self.base_defense

        # ==========================
        # Equipped Items
        # ==========================
        self.equipped_weapon = None
        self.equipped_armor = None

        # ==========================
        # Inventory
        # ==========================
        self.inventory = {
            "weapons": [],
            "armors": [],
            "potions": [],
            "materials": [],
            "quest_items": []
        }

    def __str__(self):
        return (
            f"{self.name} "
            f"({self.player_class.value}) "
            f"- Level {self.level}"
        )

    def display_stats(self):
        """
        Display all current player statistics.
        """

        weapon_name = (
            self.equipped_weapon.name
            if self.equipped_weapon
            else "None"
        )

        armor_name = (
            self.equipped_armor.name
            if self.equipped_armor
            else "None"
        )

        print("\n========== PLAYER STATS ==========")

        print(f"Name             : {self.name}")
        print(f"Class            : {self.player_class.value}")

        print(f"Level            : {self.level}")
        print(f"Experience       : {self.experience}")

        print(f"\nHP               : {self.hp}/{self.max_hp}")
        print(f"Mana             : {self.mana}/{self.max_mana}")

        print(f"\nAttack           : {self.attack}")
        print(f"Defense          : {self.defense}")

        print(f"\nCritical Chance  : {self.crit_chance}%")
        print(f"Critical Damage  : {self.crit_damage}x")

        print(f"\nGold             : {self.gold}")

        print(f"\nWeapon           : {weapon_name}")
        print(f"Armor            : {armor_name}")

        print("\n==================================")