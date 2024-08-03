import random
print("Guessing Game!")
number =  random.randint(1,100)
guessing_Stat = "Not guessed"
while guessing_Stat == "Not guessed":
    guess = int(input("What is the number"))
    guessing_Stat == "guessed"
    if guess == number:
        print("You win!!")
    elif guess >  number:
        print("Number is lesser than")
    elif guess < number:
        print("number greater than")