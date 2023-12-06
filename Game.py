import time
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def game_start(draw, image, Display):
        game_start_fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30 )  
        bg_image = Image.open('./images/space.png').convert('RGBA')
        bg_image_resize = bg_image.resize((240 ,240))
        draw.text((10,50), "STARCANDY", font=game_start_fnt, fill=(255,255,0))
        draw.text((40,80), "ADVENTURE", font=game_start_fnt, fill=(255,255,255))
        draw.text((70,170), "PRESS A TO START", font=ImageFont.load_default(), fill=(0,0,0))
        Display.disp.image(image)
        while Display.button_A.value:
            time.sleep(0.1) 



def game_over(draw, image, Display):
    game_over_fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 38)   
    bg_image = Image.open('./images/space.png').convert('RGBA')
    bg_image_resize = bg_image.resize((240 ,240))
    while True:
        draw.rectangle((0, 0, Display.width, Display.height))
        image.paste(bg_image_resize, (0,0), bg_image_resize)
        draw.text((3, 100), "GAME OVER", font=game_over_fnt, fill=(255,255,255))
        Display.disp.image(image)

def stage_clear(stage, get_candy, stage_candy):
    if(get_candy[0] >= stage_candy[0] and get_candy[1] >= stage_candy[1] and get_candy[2] >= stage_candy[2]):
        return True
    return False

def stage_clear_display(draw, image, Display, star, stage):
    stage_clear_fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    bg_image = Image.open('./images/space.png').convert('RGBA')
    bg_image_resize = bg_image.resize((240 ,240))
    #star_image = Image.open('./images/starcandy_red.png').convert("RGBA")
    #star_resize = star_image.resize((150,150))
    draw.rectangle((0, 0, Display.width, Display.height))
    image.paste(bg_image_resize, (0,0), bg_image_resize)
    star.draw_star(draw, image)
    draw.text((3, 100), f"STAGE {stage} CLAER", font=stage_clear_fnt, fill=(255,255,255))
    Display.disp.image(image)
    time.sleep(2)

def new_stage_display(my_image, my_draw, stage, get_candy, stage_candy, red_candy, blue_candy, yellow_candy, fnt):
    my_draw.text((0, 0), f"STAGE {stage}", font=fnt, fill=(255, 255, 255))
    my_image.paste(red_candy.appearance, (-35, 15), red_candy.appearance)
    my_draw.text((10, 30), f"{get_candy[0]}/{stage_candy[0]}", font=fnt, fill=(255, 255, 255))
    my_image.paste(blue_candy.appearance, (0, 15), blue_candy.appearance)
    my_draw.text((45, 30), f"{get_candy[1]}/{stage_candy[1]}", font=fnt, fill=(255, 255, 255))
    my_image.paste(yellow_candy.appearance, (35, 15), yellow_candy.appearance)
    my_draw.text((80, 30), f"{get_candy[2]}/{stage_candy[2]}", font=fnt, fill=(255, 255, 255))

def addcandy(stage, stage_candy):
    stage_candy=[]
    if(stage == 2):
        for _ in range(3):
            random_number = random.randint(5, 7)
            stage_candy.append(random_number)

    if(stage == 3):
        for _ in range(3):
            random_number = random.randint(7, 9)
            stage_candy.append(random_number)
    
    return stage_candy

