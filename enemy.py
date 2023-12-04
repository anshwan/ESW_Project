from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import random
import numpy as np

class Asteroid:
    def __init__(self):
        self.image = Image.open('./images/asteroid.png')
        self.appearance = self.image.resize((64,64))
        self.position_x = random.randint(-44,166)
        self.position_y = -128
        self.state = 'alive'
        self.speed = 3
        self.is_alive = True

    def move(self):
        self.position_y += self.speed

    def draw_asteroid(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)
        #print("Asteroid Position:", self.position_x, self.position_y)
        #draw.bitmap((self.position_x, self.position_y), self.appearance, fill = (255,255,255,255))

class Meteor:
    def __init__(self):
        self.image = Image.open('./images/meteor.png')
        self.appearance = self.image.resize((80,80))
        self.position_x = random.randint(-44,166)
        self.position_y = -128
        self.speed = 4
        self.is_alive = True
    
    def move(self):
        self.position_y += self.speed

    def draw_meteor(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)
        #print("Meteor Position:", self.position_x, self.position_y)
        #draw.bitmap((self.position_x, self.position_y), self.appearance, fill = (255,255,255,255))

class Missile:
    def __init__(self):
        self.image = Image.open('./images/missile.png')
        self.appearance = self.image.resize((64,64))
        self.position_x = random.randint(-44,166)
        self.position_y = -128
        self.speed = 5
        self.is_alive = True

    def move(self):
        self.position_y += self.speed

    def draw_missile(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)
        #print("Missile Position:", self.position_x, self.position_y)
        #draw.bitmap((self.position_x, self.position_y), self.appearance, fill = (255,255,255,255))

                

