import json
from core.player import Player

def load_classes():
    """
    Load all playable classes from the JSON file.
    """

    with open("data/classes.json", "r") as file:
        return json.load(file)


def create_character():
    """
    Creates and returns a new Player object.
    """

    classes = load_classes()

    print("\n========== CHARACTER CREATION ==========\n")

    while True:

        player_name = input("Enter Player Name: ").strip()

        if player_name:
            break

        print("Player name cannot be empty.\n")

    print("\nChoose Your Class")
    print("-----------------------")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Assassin")

    class_choices = {
        "1": "Warrior",
        "2": "Mage",
        "3": "Archer",
        "4": "Assassin"
    }

    while True:

        choice = input("\nEnter choice (1-4): ")

        if choice in class_choices:

            selected_class = class_choices[choice]
            break

        print("Invalid choice!")

    stats = classes[selected_class]

    player = Player(
        player_name,
        selected_class,
        stats
    )

    print("\nCharacter Created Successfully!")

    return player