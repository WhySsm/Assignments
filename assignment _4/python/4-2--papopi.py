import random

user_score=0
computer1_score=0
computer2_score=0
max=0
max_char=""

print ("please choose : \n","1 = 🤚\n","2 =🖐" )

for i in range (5) :
    computer1=random.choice(["🤚" , "🖐"])
    computer2=random.choice(["🤚" , "🖐"])
    n= int(input())
    if (n==1):
     user="🤚"
    elif (n==2):
     user = "🖐"


    if (user != computer1 and user!= computer2 and computer1==computer2 ):
        user_score += 1
        if user_score>max :
            max=user_score
            max_char="user"
    elif (user != computer1 and computer1!= computer2 and user==computer2 ):
        computer1_score += 1
        if computer1_score>max :
            max=computer1_score
            max_char="computer1"
    elif (computer2 != computer1 and user!= computer2 and user==computer1 ):
        computer2_score += 1
        if computer2_score>max :
            max=computer2_score
            max_char= "computer2"
    
    print (user," ",computer1," ",computer2) 
    
print ("the winner is : ",max_char,max)
