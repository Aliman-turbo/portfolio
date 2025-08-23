
# import pygame
# pygame.init()
# screen_width = 800
# screen_height = 400
# win = pygame.display.set_mode((screen_width, screen_height))
# white = (255, 255, 255)
# black = (0, 0, 0)
# green = (0,255,0)
# clock = pygame.time.Clock()
# fps = 60
# dino_width, dino_height = 50, 50
# dino_x, dino_y = 50, screen_height - dino_height - 20
# dino_val_y = 0
# gravity = 1
# dino_jump = -15
# is_jumping = False
# obstacle_width, obstacle_height = 20, 50
# obstacle_width_2,obstacle_height_2 = 15,45
# obstacle_x = screen_width
# obstacle_x_2 = screen_width + 20
# obstacle_y_2 = screen_height - obstacle_height_2 - 20
# obstacle_y = screen_height - obstacle_height - 20
# obstacle_val = 10
# obstacle_val_2 = 10
# score = 0
# game_over = False
# font = pygame.font.SysFont("Arial", 30)
# run = True
# def reset_game():
#     global dino_y, dino_val_y, is_jumping
#     global obstacle_x, obstacle_x_2, obstacle_val, obstacle_val_2
#     global score, game_over
#
#     dino_y = screen_height - dino_height - 20
#     dino_val_y = 0
#     is_jumping = False
#
#     obstacle_x = screen_width
#     obstacle_x_2 = screen_width + 200
#     obstacle_val = 10
#     obstacle_val_2 = 10
#
#     score = 0
#     game_over=False
# while run:
#     clock.tick(fps)
#     win.fill(white)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#         if not game_over and event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE and not is_jumping:
#                 is_jumping = True
#                 dino_val_y = dino_jump
#         if game_over and event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 reset_game()
#
#
#     if not game_over:
#         dino_val_y += gravity
#         dino_y += dino_val_y
#
#         if dino_y >= screen_height - dino_height - 20:
#             dino_y = screen_height - dino_height - 20
#             is_jumping = False
#
#         obstacle_x -= obstacle_val
#         obstacle_x_2 -= obstacle_val_2
#         if obstacle_x < -obstacle_width:
#             obstacle_x = screen_width
#             score += 1
#         if obstacle_x_2 < -obstacle_width_2:
#             obstacle_x_2 = screen_width
#             score+= 1
#
#         if (dino_x < obstacle_x + obstacle_width and dino_x + dino_width > obstacle_x and
#                 dino_y < obstacle_y + obstacle_height and dino_y + dino_height > obstacle_y):
#             game_over = True
#
#
#
#         if (dino_x < obstacle_x_2 + obstacle_width_2 and dino_x + dino_width > obstacle_x_2 and
#                 dino_y < obstacle_y + obstacle_height_2 and dino_y + dino_height > obstacle_y_2):
#             game_over = True
#         def speed():
#             global obstacle_val
#             global obstacle_val_2
#             global score
#             for i in range(1,101):
#                 if i > 1:
#                     obstacle_val += 5
#                     obstacle_val_2 += 5
#
#         pygame.draw.rect(win, black, (dino_x, dino_y, dino_width, dino_height))
#         pygame.draw.rect(win, black, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
#         pygame.draw.rect(win,green,(obstacle_x_2,obstacle_y_2,obstacle_width_2,obstacle_height_2))
#
#         score_text = font.render("Очки: " + str(score), True, black)
#         win.blit(score_text, (10, 10))
#     else:
#         f_text = font.render("Нажми Bakspace для продолжения ",True,black)
#         win.blit(f_text,(12,12))
#
#     pygame.display.update()
#
# pygame.quit()

# import pygame
# pygame.init()
# screen_width = 800
# screen_height = 400
# screen = pygame.display.set_mode((screen_width, screen_height))
# white = (255,255,255)
# black = (0,0,0)
# clock = pygame.time.Clock()
# fps = 30
# class Dino:
#     def __init__(self):
#         self.x = 50
#         self.y = 300
#         self.width, self.height = 50, 50
#         self.is_jump = False
#         self.jump_count = 10
#         self.gravity = 1
#     def draw(self,screen):
#         pygame.draw.rect(screen,black,(self.x,self.y,self.width,self.height))
#     def jumping(self):
#         if self.is_jump:
#             if self.jump_count >=-10:
#                 neg = 1
#                 if self.jump_count< 0:
#                     neg = -1
#                 self.y -=(self.jump_count**2)*0.5*neg
#                 self.jump_count -=1
#             else:
#                 self.is_jump = False
#                 self.jump_count = 10
# class Obstacle:
#     def __init__(self,x,y,width,height,speed):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.speed = speed
#     def draw(self,screen):
#         pygame.draw.rect(screen,black,(self.x,self.y,self.width,self.height))
#     def move(self):
#         self.x -= self.speed
#         if self.x < -screen_width:
#             self.x = screen_width
#
#     def display_score(score, screen):
#         font = pygame.font.Font(None, 36)
#         score_text = font.render(f"Score: {score}", True, black)
#         screen.blit(score_text, (10, 10))
# dino = Dino()
# obstacle = Obstacle(800, 300, 40, 60, 5)
# score = 0
# running = True
#
# while running:
#     screen.fill(white)
#     dino.draw(screen)
#     obstacle.draw(screen)
#     obstacle.move()
#
#     # Проверка на столкновение
#     if obstacle.x < dino.x + dino.width and obstacle.x + obstacle.width > dino.x:
#         if dino.y + dino.height > obstacle.y:
#             print("Столкновение!")
#             running = False
#
#     # Обработка событий
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#
# def draw_obstacle(x, y, width, height, screen):
#     pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
#
#
# obstacle_x = 800
# obstacle_y = 300
# obstacle_width = 40
# obstacle_height = 60
# obstacle_speed = 5
#
# while running:
#     screen.fill(white)
#     draw_obstacle(obstacle_x, obstacle_y, obstacle_width, obstacle_height, screen)
#     obstacle_x -= obstacle_speed
#
#     if obstacle_x + obstacle_width < 0:
#         obstacle_x = 800
#
#     pygame.display.update()
import pygame
pygame.mixer.init()
pygame.init()
width,height = 900,450
win = pygame.display.set_mode((width,height))
dino_img = pygame.image.load("Dinosaur.png")
obstacle_img = pygame.image.load("Cactus.png")
ground_img = pygame.image.load("road.png")

dino_img = pygame.transform.scale(dino_img,(60,60))
obstacle_img = pygame.transform.scale(obstacle_img,(30,60))
ground_img = pygame.transform.scale(ground_img,(width,90))
jump_sound = pygame.mixer.Sound("прыжок.mp3")
obstacke_sound = pygame.mixer.Sound("столкновение.mp3")
pygame.mixer.music.load("ikson-merry.mp3")
pygame.mixer.music.play()


class Dino:
    def __init__(self):
        self.img = dino_img
        self.x = 50
        self.y = height - self.img.get_height() - 50
        self.val_y = 0
        self.gravity = 1
        self.jump_height =- 20
        self.is_jumping = False
        self.rect = pygame.Rect(self.x,self.y,self.img.get_height(),self.img.get_height())


    def update(self):
        if self.is_jumping:
            self.val_y += self.gravity
            self.y += self.val_y
            if self.y>= height-self.img.get_height()-50:
                self.y = height - self.img.get_height() - 50
                self.is_jumping = False
        self.rect.topleft = (self.x,self.y)
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.val_y = self.jump_height
            jump_sound.play()
    def draw (self,win):
        win.blit(self.img,(self.x,self.y))

class Obstacle:
    def __init__(self):
        self.image = obstacle_img
        self.x = width
        self.y = height-self.image.get_height()-50
        self.vel = 12
        self.rect = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
    def update(self):
        self.x -= self.vel
        if self.x <-self.image.get_width():
            self.x=width
        self.rect.topleft=(self.x,self.y)
    def draw(self,win):
        win.blit(self.image,(self.x,self.y))
class Ground:
    def __init__(self):
        self.image = ground_img
        self.x = 0
        self.vel = 6
        self.rect = pygame.Rect(self.x,height-100,width,50)

    def update(self):
        self.x -=self.vel
        if self.x <=-width:
            self.x = 0
        self.rect.topleft = (self.x,height-100)
    def draw(self,win):
        win.blit(self.image,(self.x,height-100))
        win.blit(self.image,(self.x+width,height-100))
@property
def vel(self):
    return self.vel

def main():
    clock = pygame.time.Clock()
    font = pygame.font.Font("TDAText.ttf", 30)
    run = True
    game_active = False
    initial_start = True
    score = 0
    record = 0
    while run:
        clock.tick(30)
        win.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_active:
                        dino = Dino()
                        obstacle = Obstacle()
                        ground = Ground()
                        score = 0
                        game_active = True
                        initial_start = False
                    else:
                        dino.jump()
        if game_active:
            dino.update()
            obstacle.update()
            ground.update()
            if dino.rect.colliderect(obstacle.rect):
                obstacke_sound.play()
                game_active = False
            if obstacle.x<0:
                score+=1
                ground.vel+=1
                ground.update()
                if score>record:
                    record=score
                obstacle=Obstacle()
            ground.draw(win)
            dino.draw(win)
            obstacle.draw(win)
            score_text = font.render("Score:"+str(score),True,(0,0,0))
            record_text = font.render("Record:"+str(record),True,(0,0,0))
            win.blit(score_text,(10,10))
            win.blit(record_text,(width-290,10))
        else:
            if initial_start:
                start_text = font.render("Это стартовое меню To start Press Space",True,(0,0,0))
                win.blit(start_text,(width//2-start_text.get_width()//2,height//2-start_text.get_height()//2))
            else:
                game_over_text = font.render("Wanna try againg?",True,(0,0,0))
                game_over_text2 = font.render("Press Space to Start",True,(0,0,0))
                win.blit(game_over_text,(width//2 - game_over_text.get_width()//2 , height//2 - game_over_text.get_height()//2))
                win.blit(game_over_text2,( width // 2 - game_over_text.get_width() // 2,
                         height // 3 - game_over_text.get_height() // 2))
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()




