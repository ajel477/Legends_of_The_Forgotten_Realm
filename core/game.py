from core.char_creation import create_character

class Game:

    def __init__(self):

        self.player = None
        self.running = True

    def start(self):

        while self.running:

            self.main_menu()

    def main_menu(self):

        print("\n===============================")
        print(" LEGENDS OF THE FORGOTTEN REALM")
        print("===============================")

        print("1. New Game")
        print("2. Continue")
        print("3. Instructions")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            self.new_game()

        elif choice == "2":

            print("\nContinue Game (Coming Soon)")

        elif choice == "3":

            self.instructions()

        elif choice == "4":

            print("\nThanks for playing!")

            self.running = False

        else:

            print("\nInvalid choice!")

    def new_game(self):

        self.player = create_character()

        self.player.display_stats()

        input("\nPress Enter to continue...")

    def instructions(self):

        print("\n========== HOW TO PLAY ==========")

        print("Defeat enemies.")
        print("Collect equipment.")
        print("Defeat bosses.")
        print("Reach Level 100.")
        print("Defeat the Ancient Demon King.")

        input("\nPress Enter to continue...")