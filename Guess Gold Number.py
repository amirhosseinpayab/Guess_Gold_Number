import random
guess = 0
print('Hello\nwelcome to Guess Gold Number game\nYou have three chance to guess :)')
number = int(input("Game is from 1 to : "))
gold_number = random.randint(1,number)
for i in range(3):
    guess = int(input("Guess the gold number : "))
    if guess == gold_number:
        print(f"You fond the gold number :)")
        break
    elif guess < gold_number:
        print(f"It is lower than gold number! {3-(i+1)} times you can guess.")
    elif guess > gold_number:
        print(f"It is highter than gold number! {3-(i+1)} times you can guess.")
print(f"The Gold number was : {gold_number}")
