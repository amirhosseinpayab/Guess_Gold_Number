import random
guess = 0
print('Hello\nwelcome to Guess Gold Number game\nYou have three chance to guess :)')
number = int(input("Game is from 1 to : "))
gold_number = random.randint(1,number)
for i in range(3):
    guess = int(input("Guess the gold number : "))
    if guess == gold_number:
        print(f"You fond the gold number :)))))))))) {gold_number}")
        break
    elif guess < gold_number:
        print("It is lower than gold number !")
    elif guess > gold_number:
        print("It is highter than gold number !")
