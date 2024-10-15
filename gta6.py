import random


def play_game():
    print("Welcome to the Endless Number Guessing Game!")

    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 0

        print("\nI've selected a number between 1 and 100. Try to guess it!")

        while True:
            try:
                guess = int(input("Enter your guess : "))

                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                    break
            except ValueError:
                print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    play_game()
