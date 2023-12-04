from PIL import Image, ImageDraw
import time
import random

class RedStarCandy:
    def __init__(self):
        self.image = Image.open('./images/starcandy_red.png').convert("RGBA")
        self.position_x = random.randint(-60,180)
        self.position_y = -128
        self.speed = int(random.uniform(2,5))
        self.appearance = self.image.resize((64,64))

    def move(self):
        self.position_y += self.speed
        
            
    def draw(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)

class BlueStarCandy:
    def __init__(self):
        self.image = Image.open('./images/starcandy_blue.png').convert("RGBA")
        self.position_x = random.randint(-60,180)
        self.position_y = -128
        self.speed = int(random.uniform(2,5))
        self.appearance = self.image.resize((64,64))

    def move(self):
        self.position_y += self.speed
        
            
    def draw(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)

class YellowStarCandy:
    def __init__(self):
        self.image = Image.open('./images/starcandy_yellow.png').convert("RGBA")
        self.position_x = random.randint(-60,180)
        self.position_y = -128
        self.speed = int(random.uniform(2,5))
        self.appearance = self.image.resize((64,64))

    def move(self):
        self.position_y += self.speed
        
            
    def draw(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)






        