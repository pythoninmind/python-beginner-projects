import random
import string

def generate_password():
    print("========================================")
    print("🔐 Welcome to the Python Password Generator! 🔐")
    print("========================================")
    
    # Get and validate password length
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        if length < 4:
            print("⚠️ Length too short! Setting default length to 12.")
            length = 12
    except ValueError:
        print("❌ Invalid input! Using default length of 12.")
        length = 12

    # Ask user for character preferences
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols/special characters? (y/n): ").strip().lower() == 'y'

    # Base character set (always includes lowercase letters)
    character_pool = string.ascii_lowercase
    
    # Guaranteed characters (at least one of each selected type)
    guaranteed_chars = [random.choice(string.ascii_lowercase)]

    # Add optional character sets based on user choices
    if include_uppercase:
        character_pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if include_numbers:
        character_pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if include_symbols:
        character_pool += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))

    # Fill the remaining length with random choices from the total pool
    remaining_length = length - len(guaranteed_chars)
    for _ in range(remaining_length):
        guaranteed_chars.append(random.choice(character_pool))

    # Shuffle the list to make the placement unpredictable
    random.shuffle(guaranteed_chars)

    # Join the list into a single string
    password = "".join(guaranteed_chars)

    print("\n----------------------------------------")
    print(f"🔑 Generated Password: {password}")
    print("----------------------------------------\n")

if __name__ == "__main__":
    generate_password()
