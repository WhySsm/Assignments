

n = int(input())
n=n*2-1


Check = True
a=int(n/2)
b=a

for i in range (n) :
   
    for j in range (n):
     if j >= a and j<=b :
         
       print ("*",end="")

     else:
        print(" ",end="")
   
    print ()
    
    if(a==0):
        Check = False
 
    if (Check == True):
     a=a-1
     b=b+1
    
    else:
     a=a+1
     b=b-1

    
