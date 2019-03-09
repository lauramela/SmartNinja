secret = "10"
guess = input("What is the secret number? ")

if guess == secret:
    print(f"Congratulations, the number {guess} is correct!")
else:
    print("Oeps, please try again!")
