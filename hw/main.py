import random

# Generate a random number between 1 and 10
number_to_guess = random.randint(1, 10)

print("Guess the number I'm thinking of between 1 and 10!")

# Loop until the correct number is guessed
while True:
    guess = int(input("Your guess: "))

    if guess == number_to_guess:
        print("Congratulations! You guessed it right!")
        break
    else:
        print("Try again!")
