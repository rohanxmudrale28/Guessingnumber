import random

def number_guessing_game():
    secret_number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0  

    print("🔥 Welcome to the Hot & Cold Number Guessing Game created by Rohan Mudrale❄️")
    print("I have selected a number between 1 and 100.")
    print("If your guess is within ±10 of the number, you're HOT! Otherwise, you're COLD!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit when guessed correctly

            # Check Hot or Cold
            if abs(secret_number - guess) <= 10:
                print("🔥 HOT! You're close.")
            else:
                print("❄️ COLD! You're far away.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
