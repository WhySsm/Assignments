

a=[]
check=True
n = int(input("Enter number of elements : "))
print("Enter number of elements :")
for i in range(0, n):
    elements = int(input())
    a.append(elements)

for i in range(0, n):
    print (a[i],end = " ")

for i in range(0, n-1):
     if a[i]<a[i+1] :
        check=True
     else:
        check=False
        break
        

if(check==False):
    print("unsorted")
else:
    print("sorted")