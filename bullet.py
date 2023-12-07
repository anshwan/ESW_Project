import numpy as np

class Bullet:
    def __init__(self, position, command):
        self.appearance = 'rectangle'
        self.speed = 10
        self.damage = 10
        self.direction = {'up': True, 'down': False, 'left': False, 'right': False}
        self.state = None
        self.outline = "#0000FF"

        # 초기 방향 설정
        if command['up_pressed']:
            self.direction['up'] = True
        if command['down_pressed']:
            self.direction['down'] = True
            self.direction['up'] = False
        if command['right_pressed']:
            self.direction['right'] = True
        if command['left_pressed']:
            self.direction['left'] = True

        # 초기 위치 설정
        self.position = np.array([position[0] - 3, position[1] - 3, position[0] + 3, position[1] + 3])

    def move(self):
        if self.direction['up']:
            self.position[1] -= self.speed
            self.position[3] -= self.speed

        if self.direction['down']:
            self.position[1] += self.speed
            self.position[3] += self.speed

        if self.direction['left']:
            self.position[0] -= self.speed
            self.position[2] -= self.speed

        if self.direction['right']:
            self.position[0] += self.speed
            self.position[2] += self.speed

    def collision_check(self, enemys, bullets):
        for enemy in enemys:
            collision = self.overlap(self.position, enemy)

            if collision and enemy.speed == 3:
                enemy.state = 'die'
                self.state = 'hit'
                if enemy in enemys:
                    enemys.remove(enemy)

                if self in bullets:
                    bullets.remove(self)
                


    def overlap(self, ego_position, other_position):
        return (
            ego_position[0] < other_position[2]
            and ego_position[2] > other_position[0]
            and ego_position[1] < other_position[3]
            and ego_position[3] > other_position[1]
        )

    def overlap(self, ego_position, enemy):
        return (
                ego_position[0] < enemy.position_x + enemy.appearance.width // 2
                and ego_position[2] + 3 // 2 > enemy.position_x 
                and ego_position[1] < enemy.position_y + enemy.appearance.height // 2
                and ego_position[3] + 3 // 2 > enemy.position_y 
        )
    
            