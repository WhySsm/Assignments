class Time:
    def __init__(self,h,m,s) :
        self.hour=h
        self.minute=m
        self.second=s

    
    


    def add(self,other):
            extra_m=0
            extra_h=0
            t_s=self.second + other.second 
            if (t_s>=60):
                extra_m=int(t_s/60)
                t_s=t_s%60
           


            t_m=self.minute + other.minute + extra_m
            if (t_m>=60):
                extra_h=int(t_m/60)
                t_m=t_m%60

            t_h=self.hour + other.hour + extra_h
            self.show(t_h,t_m,t_s)

    def sub(self,other):
            if self.hour< other.hour:
                    change=0
                    change=self
                    self=other
                    other=change
            elif self.hour==other.hour and self.minute<other.minute:
                    change=0
                    change=self
                    self=other
                    other=change
            elif self.hour==other.hour and self.minute==other.minute and self.second<other.second:
                    change=0
                    change=self
                    self=other
                    other=change
            extra_m=0
            extra_h=0
            t_s=self.second - other.second 
            if (t_s<0):
                extra_m=-1
                t_s=t_s+60
           


            t_m=self.minute - other.minute + extra_m
            if (t_m<0):
                extra_h=-1
                t_m=t_m+60

            t_h=self.hour - other.hour + extra_h
            self.show(t_h,t_m,t_s)

    def mul(self):
        t=0
        t=self.hour*3600+self.minute*60+self.second
        self.show(0,0,t)

    def div(self):
        
        new_h=0 
        new_m=0 
        new_s=0
        new_s=self.second%60
        new_m=int(self.second/60)
        if(new_m>=60):
           new_h=int(new_m/60)
           new_m=new_m%60
        self.show(new_h,new_m,new_s)


    def show(self,x,y,z):
        self.hour=x
        self.minute=y
        self.second=z
        if(self.second<60):
            print(f"{self.hour:02}",":",f"{self.minute:02}",":",f"{self.second:02}")
        else:
            print(self.second)



def input_value():
    x1=int(input())
    if(x1<0):
        while(1):
            print ("please enter postive number")
            x1=int(input())
            if(x1<0):
                pass
            else:
                break
    x2=int(input())
    if(x2<0 or x2>59):
        while (1):
        
            print ("please enter between 0-60")
            x2=int(input())
            if(x2<0 or x2>59):
                pass
            else:
                break
    x3=int(input())
    if(x3<0 or x3>59):
        while (1):
        
            print ("please enter between 0-60")
            x3=int(input())
            if(x3<0 or x3>59):
                pass
            else:
                break
    return x1,x2,x3



print ("please choose what do you want to do\n",
"1.addition\n",
"2.Submission\n",
"3.Multiplication\n",
"4.Division\n")

x=0
x=int(input())


if(x==1):
    print ("please enter hour,minute ,second for 1")
    h,m,s=input_value()
    t1=Time(h,m,s)

    print ("please enter hour,minute ,second for 2")
    h,m,s=input_value()
    t2=Time(h,m,s)

    Time.add(t1,t2)
elif(x==2):
    print ("please enter hour,minute ,second for 1")
    h,m,s=input_value()
    t1=Time(h,m,s)

    print ("please enter hour,minute ,second for 2")
    h,m,s=input_value()
    t2=Time(h,m,s)

    Time.sub(t1,t2)
elif(x==3):
    print ("please enter hour,minute ,second")
    h,m,s=input_value()    
    t1=Time(h,m,s)

    t1.mul()
elif(x==4):
    print ("please enter second")
    s=int(input())
    t1=Time(0,0,s)

    t1.div()