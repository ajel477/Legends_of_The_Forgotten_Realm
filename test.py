from core.armor_manager import ArmorManager

armors = ArmorManager.load_armors()

for armor in armors:
    print(armor)
    print("-" * 40)