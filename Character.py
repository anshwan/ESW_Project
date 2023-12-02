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
