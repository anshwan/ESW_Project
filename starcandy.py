from PIL import Image, ImageDraw
import random

class StarCandy:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = 40
        self.position_x = random.randint(-60,180)
        self.position_y = -128
        self.speed = int(random.uniform(2,5))
        candy_images = ['./images/starcandy_blue.png', './images/starcandy_red.png', './images/starcandy_yellow.png' ]
        self.image_path = random.choice(candy_images)
        self.image = Image.open(self.image_path).convert("RGBA")
        self.appearance = self.image.resize((64,64))

    def move(self):
        self.position_y += self.speed
        if self.position_y > self.height:   
            self.position_y = 0
            self.position_x = random.randint(0, self.width - self.size)
            self.speed = int(random.uniform(2,5))
            
    def draw(self, draw, background):
        background.paste(self.appearance, (self.position_x, self.position_y), self.appearance)



        