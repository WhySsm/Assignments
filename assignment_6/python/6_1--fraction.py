1



from fractions import Fraction



    
class fraction():
    def __init__(self,n,d) :
       self.numerator = n
       self.denominator = d

    def common_denominator(self,other):
            coefficient=1
           
            
            if(self.denominator==other.denominator):
                return self.denominator
            else:
                 while(1):
                    if(((self.denominator*coefficient)%(other.denominator))==0):
                        return self.denominator*coefficient
                        break
                    else:
                         coefficient += 1
            

            
    
    def add(self,other):
        new_denominator=self.common_denominator(other)
        n=(( new_denominator/self.denominator)*self.numerator)+((new_denominator/other.denominator)*other.numerator)
        self.show( int(n),new_denominator  )
        
    def sub(self,other):
        new_denominator=self.common_denominator(other)
        n=(( new_denominator/self.denominator)*self.numerator)-((new_denominator/other.denominator)*other.numerator)
        #if(n<0):
            #n=n*-1
        self.show( int(n),new_denominator  )

    def mul(self,other):
        n=self.numerator*other.numerator
        d=self.denominator*other.denominator
        self.show(n,d)

  
    def div(self,other):
        n=self.numerator*other.denominator
        d=self.denominator*other.numerator
        self.show(n,d)

    
    

    def simp(self):
        Divisor1=[]
        Divisor2=[]
        Divisor=[]
        check=False
        if self.numerator <0 and self.denominator<0:
            self.numerator=self.numerator*-1
            self.denominator=self.denominator*-1
            check=False
        elif self.numerator<0 and self.denominator>0:
            self.numerator=self.numerator*-1
            check=True
        elif self.numerator>0 and self.denominator<0:
            self.denominator=self.denominator*-1
            check=True

        for i in range (2,self.numerator+1):
            if (self.numerator%i==0):
              Divisor1.append(i)
        for i in range (2,self.denominator+1):
            if (self.denominator%i==0):
              Divisor2.append(i)

        


        if(len(Divisor1)>=len(Divisor2)):
           for i in range(len(Divisor1)):
               for j in range (len(Divisor2)):
                   if(Divisor1[i]==Divisor2[j]):
                       Divisor.append(Divisor1[i])
            
        else:
            for i in range(len(Divisor2)):
               for j in range (len(Divisor1)):
                   if(Divisor1[j]==Divisor2[i]):
                       Divisor.append(Divisor2[i])
        max=0
        for i in range(len(Divisor)):
            if (Divisor[i]>max):
                max=Divisor[i]
      
        if(max!=0):
            if check==False:
                print(int(self.numerator/max),"/",int(self.denominator/max))
            else:
                print(-1*(int(self.numerator/max)),"/",int(self.denominator/max)) 
        else:
            if check == False:
                print(int(self.numerator),"/",int(self.denominator))
            else:
                print(-1*(int(self.numerator)),"/",int(self.denominator))


    def show(self,n,d):
        self.numerator=n
        self.denominator=d
        print(Fraction(self.numerator,self.denominator))



def input_value_(x):
    if  x>0 and x<5 :
        print ("please enter  numerator/denominator ")
        print("n1 : ")
        n1=int(input())
        print("d1 : ")
        d1=int(input())
        print("n2 : ")
        n2=int(input())
        print("d2 : ")
        d2=int(input())
        return n1,d1,n2,d2
    elif(x==5):
        print ("please enter  numerator/denominator ")
        print("n : ")
        n1=int(input())
        print("d : ")
        d1=int(input())
        return n1,d1
        
print ("please choose what do you want to do\n",
"1.addition\n",
"2.Submission\n",
"3.Multiplication\n",
"4.Division\n",
"5.fraction simplification\n")

x=int(input())

if (x==1) :
    n1,d1,n2,d2=input_value_(1)
    f1=fraction(n1,d1)
    f2=fraction(n2,d2)
    fraction.add(f1,f2)
elif (x==2) :
    n1,d1,n2,d2=input_value_(2)
    f1=fraction(n1,d1)
    f2=fraction(n2,d2)
    fraction.sub(f1,f2)
elif (x==3) :
    n1,d1,n2,d2=input_value_(3)
    f1=fraction(n1,d1)
    f2=fraction(n2,d2)
    fraction.mul(f1,f2)
elif (x==4) :
    n1,d1,n2,d2=input_value_(4)
    f1=fraction(n1,d1)
    f2=fraction(n2,d2)
    fraction.div(f1,f2)
elif (x==5) :
    n1,d1=input_value_(5)
    f1=fraction(n1,d1)
    f1.simp()

#f1=fraction(48,18)
#f2=fraction(14,3)
