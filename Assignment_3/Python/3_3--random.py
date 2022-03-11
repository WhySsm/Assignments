
import random
a=[]
count=0
n=int(input("enter number of elemnts : "))

while(True):
    rand=random.randrange(0,100000)
    if rand  not in a:
            a.append(rand)
            count += 1
    if (count==n):
        break

print(a)