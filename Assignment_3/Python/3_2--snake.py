

n=int(input ())
check=True
for i in range(n):
    
    if (check):
        print("🟥", end = "")
        check=False
    
    elif (check==False):
        print("🟨" , end = "")
        check=True
