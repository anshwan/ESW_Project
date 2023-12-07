from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import random
import numpy as np

class Asteroid:
    def __init__(self):
        self.image = Image.open('./images/asteroid.png')
        self.appearance = self.image.resize((64,64))
        self.position_x = random.randint(-44,166)
        self.position_y = -128

        self.speed = 3
        self.state = 'alive'
        self.is_alive = True

    def move(self):
        self.position_y += self.speed

    def draw(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)
        

class Meteor:
    def __init__(self):
        self.image = Image.open('./images/meteor.png')
        self.appearance = self.image.resize((80,80))
        self.position_x = random.randint(-44,166)
        self.position_y = -128
        self.speed = 4
        self.state = 'alive'
        self.is_alive = True
    
    def move(self):
        self.position_y += self.speed

    def draw(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)


class Missile:
    def __init__(self):
        self.image = Image.open('./images/missile.png')
        self.appearance = self.image.resize((64,64))
        self.position_x = random.randint(-44,166)
        self.position_y = -128
        self.speed = 5
        self.state = 'alive'
        self.is_alive = True

    def move(self):
        self.position_y += self.speed

    def draw(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)

                

