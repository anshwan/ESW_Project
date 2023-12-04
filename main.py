import time
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from Character import Stars
from MyBoard import Display
from bullet import Bullet
from starcandy import RedStarCandy, BlueStarCandy, YellowStarCandy
from enemy import Asteroid, Meteor, Missile

def main(Display):
    my_image = Image.new("RGBA", (Display.width, Display.height))
    my_draw = ImageDraw.Draw(my_image)

    #배경화면
    background_image = Image.open('./images/space3.png').convert('RGBA')
    re_background_image = background_image.resize((240 ,240))
    my_image.paste(re_background_image, (0,0), re_background_image)

    #my_draw.rectangle((0, 0, Display.width, Display.height))
    Display.disp.image(my_image)

    # 잔상이 남지 않는 코드
    my_star = Stars(Display.width, Display.height)  

    #불렛 추가
    bullets=[]

    # 적 추가   

    enemies = [Asteroid(), Meteor(), Missile()]

    candies = [RedStarCandy(), BlueStarCandy(), YellowStarCandy()]
    
    last_enemy_added_time = time.time()

    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

    
    while True:

        command = {'move': False, 'up_pressed': False, 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}

        if not Display.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True
        if not Display.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True
        if not Display.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True
        if not Display.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True
        if not Display.button_A.value:
            bullet = Bullet(my_star.center, command)
            bullets.append(bullet)


        current_time = time.time()
        if current_time - last_enemy_added_time >= 5:
            enemy_type = random.choice([Asteroid, Meteor, Missile])
            enemies.append(enemy_type())
            starcandy_type = random.choice([RedStarCandy, BlueStarCandy, YellowStarCandy])
            candies.append(starcandy_type())
            starcandy_type = random.choice([RedStarCandy, BlueStarCandy, YellowStarCandy])
            candies.append(starcandy_type())
            last_enemy_added_time = current_time

        my_star.move(command)

        collided_enemy = my_star.check_collision(enemies)
        if collided_enemy and collided_enemy.is_alive:
            collided_enemy.is_alive = False
            my_star.life -= 1
            print(f"현재 목숨 : {my_star.life}")
            time.sleep(0.01)

        enemies = [enemy for enemy in enemies if enemy.is_alive]


        my_draw.rectangle((0, 0, int(Display.width), int(Display.height)), fill=(0, 0, 0, 100))
        my_image.paste(re_background_image, (0,0))
        my_star.draw_star(my_draw, my_image) 



        # LIFE DISPLAY
        x_offset = -35
        for i in range(my_star.life) :
            my_image.paste(my_star.life_image_resize,(x_offset, -65) , my_star.life_image_resize)
            x_offset += 15
        my_draw.text((0, 15), "LIFE ", font=fnt, fill=(255,255,255))   


        for enemy in enemies:
            if enemy.is_alive:
                enemy.move()
                enemy.draw(my_draw, my_image)

        for candy in candies:
            candy.move()
            candy.draw(my_draw, my_image)
    
        for bullet in bullets:
            bullet.move()
        
        # 그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데
        # 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.

        #my_draw.rectangle((0, 0, int(Display.width), int(Display.height)), fill=(0, 0, 0, 100))
        #my_image.paste(re_background_image, (0,0))
        #my_star.draw_star(my_draw, my_image)  # my_circle 대신에 my_star로 변경

        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0,0,225))

        Display.disp.image(my_image)
        time.sleep(0.01)

if __name__ == '__main__':
    disp = Display()

    main(disp)