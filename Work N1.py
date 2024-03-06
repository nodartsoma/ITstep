import random


lives = 5
def hiddenNumber():
    hidden_number = random.randint(0, 20)
    return hidden_number

number = hiddenNumber()

print("Let's play!")
def guess_the_number():
    hearts = lives

    number = hiddenNumber()
    print(number)
    while hearts > 0:
        guess = int(input("Enter the number between 0 and 20: "))
        if guess > 20 or guess < 0:
            print("I said, between 0 and 20!")
            guess_the_number()
        elif guess == number:
            print("You won! Congratulations!\nWant again?")
            yes_or_no = input("Y/N\n")
            if yes_or_no.lower() == "y":
                hiddenNumber()
                guess_the_number()
            else:
                print("Well, it was a good game! Goodbye!")
                break
        elif guess > number:
            hearts -= 1
            if hearts > 0:
                print(f"Oops, you're wrong! You have {hearts} hearts left... Now try something lower. ")
            else:
                print("Tiime toooo say gooodbyeeeee... (in Andrea Bocelli's voice)\nAnyways, good game! BTW... Want again?")
                yes_or_no = input("Y/N\n")
                if yes_or_no.lower() == "y":
                    hiddenNumber()
                    guess_the_number()
                else:
                    print("Well, it was a good game! Goodbye!")
                    break
        elif guess < number:
            hearts -= 1
            if hearts > 0:
                print(f"Oops, you're wrong! You have {hearts} hearts left... Now try something higher. ")
            else:
                print("Tiime toooo say gooodbyeeeee... (in Andrea Bocelli's voice)\nAnyways, good game! BTW... Want again?")
                yes_or_no = input("Y/N\n")
                if yes_or_no.lower() == "y":
                    hiddenNumber()
                    guess_the_number()
                else:
                    print("Well, it was a good game! Goodbye!")
                    break

guess_the_number()


