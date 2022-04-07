import random

option = ["Rock","Paper","Scissor"]
computer_score=0
user_score=0

for i in range (10):
    computer_choice=random.choice(option)
    user_choice=input()

    if user_choice == "Paper" and computer_choice =="Rock":
        user_score +=1
    elif user_choice=="Paper" and computer_choice == "Scissor":
        computer_score +=1
    elif user_choice=="Paper" and computer_choice == "Paper":
        computer_score +=1 
        user_score +=1
    
    elif user_choice=="Rock" and computer_choice == "Paper":
        computer_score +=1
    elif user_choice=="Rock" and computer_choice == "Scissor":
        user_score +=1
    elif user_choice=="Rock" and computer_choice == "Rock":
        user_score +=1
        computer_score +=1

    elif user_choice=="Scissor" and computer_choice == "Paper":   
        user_score +=1
    elif user_choice=="Scissor" and computer_choice == "Rock":
        computer_score +=1
    elif user_choice=="Scissor" and computer_choice == "Scissor":
        user_score +=1
        computer_score +=1

print("User:",user_score)
print("Computer:",computer_score)