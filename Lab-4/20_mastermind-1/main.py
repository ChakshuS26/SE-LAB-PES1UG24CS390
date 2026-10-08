from game import Mastermind


def main():
    print("=== MASTERMIND ===")
    print("Choose a difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("Q. Quit")

    choices = {
        "1": "easy",
        "2": "medium",
        "3": "hard",
    }

    while True:
        choice = input("Enter choice: ").strip().lower()

        if choice == "q":
            print("Game quit.")
            return

        if choice in choices:
            difficulty = choices[choice]
            break

        print("Please choose 1, 2, 3, or Q.")

    game = Mastermind(difficulty)
    game.run()


if __name__ == "__main__":
    main()