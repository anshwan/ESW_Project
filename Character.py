from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import random
import numpy as np

class Stars:
    def __init__(self, width, height):
        self.stand = Image.open('./images/star.png').convert("RGBA")
        self.appearance = self.stand.resize((128,128))
        self.position_x = int(width // 2 - self.appearance.width/2)
        self.position_y = int(height // 2 - self.appearance.height/2 + 90)
        self.center = np.array([self.position_x + self.appearance.width / 2, self.position_y + self.appearance.height / 2])
        self.state = None
        self.life =  5 # 목숨 초기값
        self.life_images = []
        self.life_image = Image.open('./images/life.png').convert("RGBA")
        self.life_image_resize = self.life_image.resize((150 ,150))
        


    #def calculate_center(self):
        #self.center_x = int(self.width  / 2)
        #self.center_y = int(self.height / 2)
        #self.position_x = int(self.center_x - self.appearance.width / 2)
        #self.position_y = int(self.center_y - self.appearance.height / 2)

    def move(self, command = None):
        if command['move'] == False:
            self.state = None
        
        else:   
            self.state = 'move' 

            if command['up_pressed']:
                self.position_y -= 5
                

            if command['down_pressed']:
                self.position_y += 5
                

            if command['left_pressed']:
                self.position_x -= 5
               
                
            if command['right_pressed']:
                self.position_x += 5
            self.center = np.array([self.position_x + self.appearance.width / 2, self.position_y + self.appearance.height / 2])

    def draw_star(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)
        #print("Star Position:", self.position_x, self.position_y, self.appearance.width, self.appearance.height)

    def check_collision(self, candies):
        collided_candy = None
        for candy in candies:
            if(
                self.position_x < candy.position_x + candy.appearance.width // 2 - 32 and 
                self.position_x + self.appearance.width // 2 > candy.position_x - 48  and
                self.position_y < candy.position_y + candy.appearance.height // 2 - 32 and
                self.position_y + self.appearance.height // 2 > candy.position_y - 32
            ):
                collided_candy = candy
                break

        if collided_candy:
            candies.remove(collided_candy)

        return collided_candy
    
    def check_collision(self, enemies):
        collided_enemy = None
        for enemy in enemies:
            if (
                self.position_x < enemy.position_x + enemy.appearance.width // 2 - 32 and
                self.position_x + self.appearance.width // 2 > enemy.position_x  and
                self.position_y < enemy.position_y + enemy.appearance.height // 2 - 32 and
                self.position_y + self.appearance.height // 2 > enemy.position_y 
            ):
                collided_enemy = enemy
                break

        if collided_enemy:
            enemies.remove(collided_enemy)

        return collided_enemy

