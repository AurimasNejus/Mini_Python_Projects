import random
guesses = 0
random_number = random.randint(1,20)
print("Hi, what's your name?")
name = str(input("Enter your name here:"))
print(f"Nice to meet you {name}. I am thinking of number between 1 and 20. Can you guess it?")
while True:
    number_guess = int(input("Please guess a number in range 1-20:"))
    if number_guess == random_number:
        guesses+=1
        print(f"Congrats {name}! You've guessed the number correctly from {guesses} guesses!")
        break
    
    elif number_guess < random_number:
        guesses+=1 
        print("This number is lower than the correct one! Please try again")
        continue
    elif number_guess > random_number:
        guesses+=1 
        print("This number is higher than the correct one! Please try again")
        continue
    else:
       print("Please write the number between 1 and 20!")
       continue
# play_again = str(input("Do you want to play again? Y/N"))
# if play_again == "Y":

