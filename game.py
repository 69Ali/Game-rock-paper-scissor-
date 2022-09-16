import random
user_choice= int(input("what do you want to choose. type 0 for rock 1 for paper and 2 for scissor\n"))
computer_choice= random.randint(0,2)
print(f"computer choses {computer_choice}")
if user_choice == 0 and computer_choice == 2 :
    print("you win !")
elif computer_choice == 0 and user_choice ==2:
    print("you lose !")
elif user_choice >=3 or user_choice < 0 :
    print("you typed an invalid number. you lose !")
elif user_choice > computer_choice :
    print("you win !")
elif computer_choice > user_choice :
    print("you lose !")    