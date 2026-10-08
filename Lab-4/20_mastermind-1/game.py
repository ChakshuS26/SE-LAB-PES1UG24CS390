import random
from logic import feedback


class Mastermind:
    DIFFICULTIES = {
        "easy": {
            "length": 3,
            "max_symbol": 4,
            "turns": 12,
        },
        "medium": {
            "length": 4,
            "max_symbol": 6,
            "turns": 10,
        },
        "hard": {
            "length": 5,
            "max_symbol": 8,
            "turns": 8,
        },
    }

    def __init__(self, difficulty="medium"):
        difficulty = difficulty.lower()

        if difficulty not in self.DIFFICULTIES:
            raise ValueError("Invalid difficulty.")

        settings = self.DIFFICULTIES[difficulty]

        self.difficulty = difficulty
        self.code_length = settings["length"]
        self.max_symbol = settings["max_symbol"]
        self.code = [
            str(random.randint(1, self.max_symbol))
            for _ in range(self.code_length)
        ]

        self.history = []
        self.turns = settings["turns"]
        self.game_over = False
        self.won = False

    def show_history(self):
        print("\n========== GUESS HISTORY ==========")

        if not self.history:
            print("No valid guesses were made.")
            print("===================================")
            return

        for number, (guess, exact, partial) in enumerate(
            self.history, start=1
        ):
            print(
                f"Guess {number}: {guess} | "
                f"Exact: {exact} | "
                f"Partial: {partial}"
            )

        print("===================================")

    def run(self):
        if self.game_over:
            print("The game has already ended.")
            return

        print(
            f"Mastermind — {self.difficulty.capitalize()} mode."
        )
        print(
            f"Enter {self.code_length} digits from "
            f"1 to {self.max_symbol}."
        )

        while self.turns > 0 and not self.game_over:
            raw = input(
                f"{self.turns} turns left > "
            ).strip()

            # Quit without consuming a turn.
            if raw.lower() == "q":
                self.game_over = True
                print("Game quit.")
                return

            # Reject malformed guesses without consuming a turn.
            valid_symbols = "123456789"[:self.max_symbol]

            if (
                len(raw) != self.code_length
                or any(ch not in valid_symbols for ch in raw)
            ):
                print(
                    f"Enter exactly {self.code_length} "
                    f"digits from 1 to {self.max_symbol}."
                )
                continue

            # This is an accepted guess.
            guess = list(raw)

            exact, partial = feedback(
                self.code,
                guess
            )

            # Store only accepted guesses.
            self.history.append(
                (raw, exact, partial)
            )

            # One accepted guess consumes exactly one turn.
            self.turns -= 1

            print(
                f"Exact: {exact}  Partial: {partial}"
            )

            # Win condition.
            if exact == self.code_length:
                self.won = True
                self.game_over = True

                print("Cracked the code!")
                self.show_history()
                return

        # Loss condition.
        if self.turns == 0 and not self.won:
            self.game_over = True

            print("Out of turns!")
            print("The code was", "".join(self.code))
            self.show_history()