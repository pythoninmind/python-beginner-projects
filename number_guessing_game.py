import random

def number_guessing_game():
    print("========================================")
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("========================================")
    print("I am thinking of a number between 1 and 100.")
    print("You have a maximum of 7 attempts to guess it.\n")

    # Generate the secret number
    secret_number = random.randint(1, 100)
    max_attempts = 7
    current_attempt = 0

    while current_attempt < max_attempts:
        current_attempt += 1
        
        # Get user input and handle invalid entries
        try:
            guess = int(input(f"Attempt {current_attempt}/{max_attempts} | Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            current_attempt -= 1  # Does not count as a spent attempt
            continue

        # Check the guess
        if guess < secret_number:
            print("📈 Too low! Try a higher number.")
        elif guess > secret_number:
            print("📉 Too high! Try a lower number.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number}!")
            print(f"🏆 It took you {current_attempt} attempts.")
            return

    # If all attempts are used up
    print("\n😢 Game over! You have run out of attempts.")
    print(f"The correct number was: {secret_number}")

# Start the game
if __name__ == "__main__":
    number_guessing_game()
