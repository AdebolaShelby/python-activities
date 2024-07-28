# Guessing game using a while loop
# Secret number is 9 and the user input has to match the secret number to win
# user can guess 3 times

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    user_prompt = int(input("Guess the secret number: "))
    guess_count += 1
    if user_prompt == secret_number:
        print("You won")
        break
    else:
        print("Try again")