import time
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from Character import Stars
from MyBoard import Display
from bullet import Bullet

def main(Display):
    my_image = Image.new("RGBA", (Display.width, Display.height))
    my_draw = ImageDraw.Draw(my_image)

    my_draw.rectangle((0, 0, Display.width, Display.height))
    Display.disp.image(my_image)

    # 잔상이 남지 않는 코드
    my_star = Stars(Display.width, Display.height)  # Character 대신에 my_star로 이름 변경

    #불렛 추가
    bullets=[]

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
        #
        if not Display.button_A.value:
            bullet = Bullet(my_star.center, command)
            bullets.append(bullet)


        my_star.move(command)
        #
        for bullet in bullets:
            bullet.move()
        #else:
            #command = None

        #my_star.move(command)

        # 그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데
        # 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
        my_draw.rectangle((0, 0, int(Display.width), int(Display.height)), fill=(0, 0, 0, 100))
        my_star.draw_star(my_draw, my_image)  # my_circle 대신에 my_star로 변경


        #
        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0,0,225))
        


        Display.disp.image(my_image)

if __name__ == '__main__':
    disp = Display()

    main(disp)