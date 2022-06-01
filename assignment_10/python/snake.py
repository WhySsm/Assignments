
import random
from turtle import color, down, up, update
import arcade
from time import sleep
class snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.color1=arcade.color.YELLOW
        self.color2=arcade.color.ARMY_GREEN
        self.width = 30
        self.height=30
        self.speed=8
        self.score=0
        self.center_x=game.width/2
        self.center_y=game.height/2
        self.body=[]
        self.head=[]
    def move(self):
        
        self.center_x += self.change_x*self.speed
        self.center_y += self.change_y*self.speed
        self.body.append([self.center_x,self.center_y])
        self.body.pop(0)
        if len (self.body)>0:
            self.head.append(self.body[-1])
            del self.head[0:-1]
            #print (self.head[0][0])  
           
    def eat(self):
        self.body.append([self.center_x,self.center_y])        
        self.score += 1
    
        
    def draw (self):
        
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,arcade.color.RED_DEVIL) 
        
        #self.head.append([self.center_x,self.center_y])
        check=False
        check1=True
        
        for part in self.body:
            if (check==True):
                arcade.draw_rectangle_filled(part[0],part[1],self.width,self.height,self.color1)
                arcade.draw_rectangle_filled(self.head[0][0],self.head[0][1],self.width,self.height,arcade.color.RED_DEVIL) 
                 
                #print (part[0])
                check=False
                check1=True
                #if(self.head[0][0]=part[0]):
                    #self.sna
            elif(check1==True):
                arcade.draw_rectangle_filled(part[0],part[1],self.width,self.height,self.color2)           
                check1=False
                check=True
                if len (self.head)>0:
                      arcade.draw_rectangle_filled(self.head[0][0],self.head[0][1],self.width,self.height,arcade.color.RED_DEVIL) 
class Apple(arcade.Sprite):
    def __init__(self,game) :
        super().__init__()
        self.color=arcade.color.ORANGE_PEEL
        self.r=18
        self.center_x=random.randint(self.r*2,game.width-self.r*2)
        self.center_y=random.randint(self.r*2,game.width-self.r*2)
        self.width=10
        self.height=10
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)


class game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=1000,title="Snake game")
        self.background_color=arcade.color.WHITE
        self.food=Apple(self)#important
        self.snake=snake(self)
        self.pressed_up=False
        self.pressed_down=False
        self.pressed_right=False
        self.pressed_left=False
    def on_key_press(self, symbol,modifier):
        
        if symbol == arcade.key.UP and self.pressed_down== False   :
             self.pressed_up=True
             self.pressed_right=False
             self.pressed_left=False
            
             self.snake.change_y=1
             self.snake.change_x=0
             
        elif symbol == arcade.key.DOWN and self.pressed_up ==False :
            self.pressed_down=True
            self.pressed_right=False
            self.pressed_left=False
            
            self.snake.change_y=-1
            self.snake.change_x=0
        elif symbol == arcade.key.LEFT  and self.pressed_right==False:
            self.pressed_left=True 
            self.pressed_down=False
            self.pressed_up=False
            
           
            self.snake.change_y=0
            self.snake.change_x=-1

        elif symbol == arcade.key.RIGHT and self.pressed_left == False:
            self.pressed_right=True 
            self.pressed_down=False
            self.pressed_up=False
            

            self.snake.change_x=1
            self.snake.change_y=0
    def on_update(self,delta_time):#logical shoulde set here
        
        self.snake.move()    
        if (arcade.check_for_collision(self.food,self.snake)):
            self.snake.eat()
            self.food=Apple(self)
        #snake hit wall
        if ( self.snake.center_y>self.width or self.snake.center_x>self.height 
            or self.snake.center_y<0 or self.snake.center_x<0):
            self.snake=snake(self)
            self.pressed_down=False 
            self.pressed_right=False
            self.pressed_up=False
            self.pressed_left=False
        #snake hit its body
        if (len (self.snake.body)>1):
            
            check3=False
            for i in range(0,len(self.snake.body)-2):
                
                if  (self.snake.body[i][0]==self.snake.head[0][0] and 
                self.snake.body[i][1]==self.snake.head[0][1]):
                    check3 = True
                    break
            if check3== True:
                self.snake=snake(self) 
                self.pressed_down=False 
                self.pressed_right=False
                self.pressed_up=False
                self.pressed_left=False
    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.snake.draw()
        score_text = f"Score: {self.snake.score}"
        arcade.draw_text(score_text,self.width/6,self.height-30,arcade.color.BLACK,25,
                         font_name=(
                             "Times New Roman",  # Comes with Windows
                             "Times",  # MacOS may sometimes have this variant
                             "Liberation Serif"  # Common on Linux systems
                         ))
    

    
        
my_game=game()

arcade.run()