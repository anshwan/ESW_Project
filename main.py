import time
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from Character import Stars
from MyBoard import Display
from bullet import Bullet
from starcandy import RedStarCandy, BlueStarCandy, YellowStarCandy, RainbowStarCandy
from enemy import Asteroid, Meteor, Missile
import Game as game


def main(Display):
    my_image = Image.new("RGBA", (Display.width, Display.height))
    my_draw = ImageDraw.Draw(my_image)

    #배경화면
    background_image = Image.open('./images/space.png').convert('RGBA')
    re_background_image = background_image.resize((240 ,240))
    my_image.paste(re_background_image, (0,0), re_background_image)

    Display.disp.image(my_image)

    # 별 캐릭터 추가  
    my_star = Stars(Display.width, Display.height)  

    # 불렛 추가
    bullets=[]

    # 적 추가   
    asteroid = Asteroid()
    meteor = Meteor()
    missile = Missile()
    enemies = [asteroid, meteor, missile]

    # 별사탕 추가
    red_candy = RedStarCandy()
    blue_candy = BlueStarCandy()
    yellow_candy = YellowStarCandy()
    rainbow_candy = RainbowStarCandy()
    candies = [red_candy, blue_candy, yellow_candy, rainbow_candy]

    # stage
    stage = 1
    # stage clear state 
    Isclear = False

    isGameStart = False
    
    end_time = time.time()

    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

    stage_candy = []   
    for _ in range(3):
        random_number = random.randint(3, 5)
        stage_candy.append(random_number)

    # 획득한 red, blue, yellow candy의 개수
    get_candy = [0, 0, 0] 
    
    while True:
        if (my_star.life <= 0):
            game.game_over(my_draw, my_image, disp)

    
        if not isGameStart:
            # 시작 화면 표시
            game.game_start(my_draw, my_image, disp)
            isGameStart = True
                

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


        # 랜덤한 적과 사탕 생성 후 떨어트리는 코드
        current_time = time.time()
        if current_time - end_time >= 3:
                enemy_type = random.choice([Asteroid, Meteor, Missile])
                enemies.append(enemy_type())

                starcandy_type = random.choice([RedStarCandy, BlueStarCandy, YellowStarCandy, RainbowStarCandy])
                candies.append(starcandy_type())
                end_time = current_time

        my_star.move(command)


        # 적과의 충돌 시 EVENT
        collided_enemy = my_star.check_collision(enemies)
        if collided_enemy:
            if isinstance(collided_enemy, Missile):
                my_star.life -= 2
            elif isinstance(collided_enemy, Meteor):
                my_star.life -= 1
            elif isinstance(collided_enemy, Asteroid):
                get_candy = [x - 1 for x in get_candy]
            time.sleep(0.01)

        # 별사탕과의 충돌 시 EVENT
        collided_candy = my_star.check_collision(candies)
        if collided_candy:
            if isinstance(collided_candy, RedStarCandy):
                get_candy[0]+= 1
            elif isinstance(collided_candy, BlueStarCandy):
                get_candy[1] += 1
            elif isinstance(collided_candy, YellowStarCandy):
                get_candy[2] += 1
            elif isinstance(collided_candy, RainbowStarCandy):
                get_candy = [x + 1 for x in get_candy]
            time.sleep(0.01)



        my_draw.rectangle((0, 0, int(Display.width), int(Display.height)), fill=(0, 0, 0, 100))
        my_image.paste(re_background_image, (0,0))
        my_star.draw_star(my_draw, my_image) 



        # 하트 DISPLAY
        x_offset = -35
        for i in range(my_star.life) :
            my_image.paste(my_star.life_image_resize,(x_offset, -65) , my_star.life_image_resize)
            x_offset += 15
        my_draw.text((0, 15), "LIFE ", font=fnt, fill=(255,255,255))  


        # 초기 stage display
        game.new_stage_display(my_image, my_draw, stage, get_candy, stage_candy, red_candy, blue_candy, yellow_candy, fnt)


        #stage를 clear 했는지 확인
        Isclear = game.stage_clear(stage, get_candy, stage_candy)

        #stage를 clear 한 경우 다음 stage로 이동
        if(Isclear):
            game.stage_clear_display(my_draw, my_image, Display, my_star, stage)
            if(stage == 3):
                complete_fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
                while True:
                    my_image.paste(re_background_image, (0,0), re_background_image)
                    my_draw.text((3, 100), "CONGRATULATION!", font=complete_fnt, fill=(255,255,255))
                    my_image.paste(my_star.appearance, (56,146), my_star.appearance)
                    Display.disp.image(my_image)
            stage += 1
            get_candy = [0,0,0]
            stage_candy = game.addcandy(stage, stage_candy)
            game.new_stage_display(my_image, my_draw, stage, get_candy, stage_candy, red_candy, blue_candy, yellow_candy, fnt)
            

        for enemy in enemies:
            if enemy.is_alive:
                enemy.move()
                enemy.draw(my_draw, my_image)

        for candy in candies:
            candy.move()
            candy.draw(my_draw, my_image) 

        for bullet in bullets:
            bullet.move()

        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0,0,225))

        Display.disp.image(my_image)
        time.sleep(0.01)

if __name__ == '__main__':
    disp = Display()

    main(disp)