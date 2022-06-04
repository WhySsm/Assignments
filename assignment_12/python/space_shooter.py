from email.policy import default
import random
from symtable import Symbol
import arcade
import threading
import time
class Space_Shooter(arcade.Sprite):
    def __init__(self ):
        super().__init__("shooter2.png") 
        self.center_x=100
        self.center_y=75
        self.height=65
        self.width=55
        self.speed=5
        self.heart=3
        self.score=0
        self.game_over=False
    def move(self):
        self.center_x += self.change_x*self.speed
        

class Fire(arcade.Sprite):
    def __init__(self ,x,y):
        super().__init__("shot.png") 
        self.center_x=x
        self.center_y=y
        self.height=15
        self.width=15
        self.speed=4
        self.shoot_sound=arcade.load_sound('shooting.wav',False)
        arcade.play_sound(self.shoot_sound,2.0,1.0,False)
    def move(self):
        self.center_y += self.speed
class Enemy(arcade.Sprite):
   def __init__(self ):
        super().__init__("enemy.png") 
        self.center_x=random.randint(10,690)
        self.center_y=550
        self.height=30
        self.width=30
        self.speed=3
   def move(self):
       self.center_y -= self.speed


class Game(arcade.Window):
    def __init__( self):
        super().__init__( width = 800, height = 600, title= "space_shooter")

        self.background_color=arcade.color.BLACK
        self.image=arcade.load_texture("star.png")
        self.image1=arcade.load_texture("heart.png")
        self.lose_heart=arcade.load_sound('lose_heart.wav',False)
        self.explosion=arcade.load_sound('explosion.wav',False)
        self.game_oover=arcade.load_sound('Game_over.wav',False)
        self.shooter=Space_Shooter()
        #self.first_shot=False
        self.enemies=[]
        self.shots=[]
        self.my_thread=threading.Thread(target=self.enemy_generator)
        self.my_thread.start()
        self.game_over=False
        self.game_over_sound=False
        #self.explosion=["1.png","2.png","3.png","shooter.png"]
    def on_key_press(self,symbol,modifier):
        if symbol==arcade.key.LEFT:
            if self.shooter.center_x>49 :
                self.shooter.change_x = -1
        elif symbol==arcade.key.RIGHT:
            if self.shooter.center_x<751 :
                self.shooter.change_x = 1
        elif symbol== arcade.key.SPACE:
            
            self.shots.append(Fire(self.shooter.center_x,self.shooter.center_y+self.shooter.height/2))
            self.first_shot=True
    
    def on_key_release(self,symbol,modifier):
        if symbol == arcade.key.LEFT:
           
            self.shooter.change_x = 0

        elif symbol == arcade.key.RIGHT:

            self.shooter.change_x = 0
        
    def enemy_generator(self):
        while True:
            self.enemies.append(Enemy())
            time.sleep(random.randint(1,10))

    def on_update(self, delta_time: default):
        
        if self.game_over==False:
            self.shooter.move()
            if(self.shooter.center_x>750):
                self.shooter.change_x=0
            if(self.shooter.center_x<50):
                self.shooter.change_x=0
            #if self.first_shot==True:
            
            
            
            for shot in self.shots:
                    
                for enemy in self.enemies:
                    
                    if (arcade.check_for_collision(shot,enemy)):
                        self.shots.remove(shot)
                        self.enemies.remove(enemy)
                        self.shooter.score += 1
                        arcade.play_sound(self.explosion,2.0,1.0,False)
                        break
            
            for enemy in self.enemies:
                if (arcade.check_for_collision(self.shooter,enemy)):
                    self.enemies.remove(enemy)
                    self.shooter.heart -= 1
                    arcade.play_sound(self.lose_heart,2.0,1.0,False)
                    break
        
        for shot in self.shots:
            shot.move()
        
        for enemy in self.enemies:
            enemy.move()

        for shot in self.shots:
            if (shot.center_y>600):
                self.shots.remove(shot)

        for enemy in self.enemies:
            if (enemy.center_y<0):
                self.enemies.remove(enemy)
        
        
        if self.shooter.heart==0:
            self.game_over=True
            if (self.game_over_sound==False):  
                arcade.play_sound(self.game_oover,2.0,1.0,False) 
                self.game_over_sound=True
          
            
                      
    def on_draw(self):
        arcade.start_render()
        if self.game_over==False:
            arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.image)
            
            #if self.first_shot==True:
            for shot in self.shots:
                    shot.draw()
                
            for enemy in self.enemies:
                enemy.draw()
        
            self.shooter.draw()    
            for i in range (1,self.shooter.heart+1):
                arcade.draw_texture_rectangle(i*40,20,35,35,self.image1)
            score_text = f"Score: {self.shooter.score}"
        
        
            arcade.draw_text(score_text,self.width-120,10,arcade.color.YELLOW_ROSE,25,
                         font_name=(
                             "Times New Roman",  # Comes with Windows
                             "Times",  # MacOS may sometimes have this variant
                             "Liberation Serif"  # Common on Linux systems
                         ))
        else:

            arcade.draw_text("Game_Over",self.width/2-100,self.height/2,arcade.color.RED_DEVIL,45,
                         font_name=(
                             "Times New Roman",  # Comes with Windows
                             "Times",  # MacOS may sometimes have this variant
                             "Liberation Serif"  # Common on Linux systems
                         ))
        
        
game=Game()
arcade.run()