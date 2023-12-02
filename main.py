from PIL import Image, ImageDraw, ImageFont
from Character import Stars
from MyBoard import Display

def main(Display):
    my_image = Image.new("RGBA", (Display.width, Display.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, Display.width, Display.height))
    Display.disp.image(my_image)

    # 잔상이 남지 않는 코드
    my_star = Stars(Display.width, Display.height)  # Character 대신에 my_star로 이름 변경

    while True:
        command = None
        if not Display.button_U.value:  # up pressed
            command = 'up_pressed'
        elif not Display.button_D.value:  # down pressed
            command = 'down_pressed'
        elif not Display.button_L.value:  # left pressed
            command = 'left_pressed'
        elif not Display.button_R.value:  # right pressed
            command = 'right_pressed'
        else:
            command = None

        my_star.move(command)

        # 그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데
        # 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
        my_draw.rectangle((0, 0, int(Display.width), int(Display.height)), fill=(0, 0, 0, 100))
        my_star.draw_star(my_draw, my_image)  # my_circle 대신에 my_star로 변경
        Display.disp.image(my_image)

if __name__ == '__main__':
    disp = Display()

    main(disp)