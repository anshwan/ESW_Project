from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import random
import numpy as np

class Stars:
    def __init__(self, width, height):
        self.stand = Image.open('./images/star.png').convert("RGBA")
        #self.appearance = self.stand.transform(self.stand.size, Image.AFFINE, (1,0,0,0,1,-70))
        self.appearance = self.stand.resize((128,128))
        #self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        self.position_x = int(width // 2 - self.appearance.width/2)
        self.position_y = int(height // 2 - self.appearance.height/2 + 90)
        self.state = None

    def move(self, command = None):
        if command == None:
            self.state = None
        
        else:
            self.state = 'move'

            if command == 'up_pressed':
                self.position_y -= 5
                

            elif command == 'down_pressed':
                self.position_y += 5
                

            elif command == 'left_pressed':
                self.position_x -= 5
               
                
            elif command == 'right_pressed':
                self.position_x += 5
            

    def draw_star(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)
        #draw.bitmap((self.position_x, self.position_y), self.appearance, fill=(255,255,255,100), mask = self.appearance)
