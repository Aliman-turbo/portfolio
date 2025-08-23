
# import pygame
#
# pygame.init()
# WIDTH, HEIGHT = 900, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Пинг-Понг")
# white = (255, 255, 255)
# black = (0, 0, 0)
# green = (0, 255, 0)
# clock = pygame.time.Clock()
# fps = 120
# fonts = pygame.font.Font("freesansbold.ttf", 20)
#
# class Box:
#     def __init__(self, posx, posy, width, height, speed, color):
#         self.posx = posx
#         self.posy = posy
#         self.width = width
#         self.height = height
#         self.speed = speed
#         self.color = color
#         self.boxrect = pygame.Rect(posx, posy, width, height)
#         self.boxrect2 = pygame.Rect(posx, posy, width, height)
#
#     def display(self):
#         pygame.draw.rect(screen, self.color, self.boxrect)
#         pygame.draw.rect(screen, self.color, self.boxrect)
#
#
#     def update(self, yfac):
#         self.posy += self.speed * yfac
#         if self.posy <= 0:
#             self.posy = 0
#         elif self.posy + self.height >= HEIGHT:
#             self.posy = HEIGHT - self.height
#         self.boxrect = pygame.Rect(self.posx, self.posy, self.width, self.height)
#         self.boxrect2 = pygame.Rect(self.posx, self.posy, self.width, self.height)
#
#     def displayScore(self, text, score, x, y, color):
#         text_surface = fonts.render(text + str(score), True, color)
#         textRect = text_surface.get_rect(center=(x, y))
#         screen.blit(text_surface, textRect)
#
#     def getRect(self):
#         return self.boxrect
#         return self.boxrect2
#
#
#
# class Player:
#     def __init__(self, posx, posy, width, height, color,up,down):
#         self.posx = posx
#         self.posy = posy
#         self.width = width
#         self.height = height
#         self.speed = 5
#         self.color = color
#         self.up = up
#         self.down = down
#
#
#
#     def draw(self):
#         pygame.draw.rect(screen, self.color, (self.posx, self.posy, self.width, self.height))
#         pygame.draw.rect(screen, self.color, (self.posx, self.posy, self.width, self.height))
#
#     def move(self, keys):
#         if keys[self.up]:
#             self.posy -= self.speed
#         if keys[self.down]:
#             self.posy += self.speed
#
#
#         if self.posy < 0:
#             self.posy = 0
#         if self.posy + self.height > HEIGHT:
#             self.posy = HEIGHT - self.height
# class Ball():
#     def __init__(self,posx,posy,speed,color,radius):
#         self.posx = posx
#         self.posy = posy
#         self.speed = speed
#         self.color = color
#         self.radius = radius
#         self.xfac = 1
#         self.yfac = -1
#         self.ball = pygame.draw.circle(screen,self.color(self.posx,self.posy),self.radius)
#         self.first = None
#     def display(self):
#         self.ball = pygame.draw.circle(screen, self.color(self.posx, self.posy), self.radius)
#     def update(self):
#         self.posx += self.speed*self.xfac
#         self.posy += self.speed * self.yfac
#         if self.posy<=0 or self.posy >=HEIGHT:
#             self.yfac*=-1
#         if self.posy <= 0 and self.first:
#             self.first = 0
#             return 1
#         elif self.posx >= WIDTH and self.first:
#             self.first = 0
#             return -1
#         else:
#             return 0
#     def reset(self):
#         posx = WIDTH//2
#         posy = HEIGHT // 2
#         self.xfac *= -1
#         self.first = 1
#     def hit(self):
#         self.xfac *=-1
#     def getRect(self):
#         return self.ball
# def main():
#     running = True
#     player = Player(50, 250, 20, 100, white, pygame.K_UP, pygame.K_DOWN)
#     player2 = Player(800, 250, 20, 100, white, pygame.K_w, pygame.K_s)
#     listoplayer = [player,player2]
#     ball = Ball(WIDTH//2,HEIGHT//2,7,7,white)
#     playerscore = 0
#     player2score = 0
#     player_y = 0
#     player2_y = 0
#     while running:
#
#         screen.fill(green)
#         player.draw()
#         player2.draw()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#         keys = pygame.key.get_pressed()
#         player.move(keys)
#         player2.move(keys)
#
#         pygame.display.update()
#         clock.tick(fps)
#         for player in listoplayer:
#             if pygame.Rect.colliderect(ball.getRect(),player.getRect()):
#                 ball.hit()
#         player.update()
#         player2.update()
#         point =ball.update()
#         if point==-1:
#             playerscore+=1
#         elif point ==1:
#             player2score+=1
#         if point:
#             ball.reset()
#         player.display()
#         player2.display()
#         ball.display()
#     if __name__ == "__main__":
#         main()
#         pygame.quit()
import pygame

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

clock = pygame.time.Clock()
fps = 120
fonts = pygame.font.Font("freesansbold.ttf", 20)

class Box:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.boxrect = pygame.Rect(posx, posy, width, height)

    def display(self):
        pygame.draw.rect(screen, self.color, self.boxrect)

    def update(self, yfac):
        self.posy += self.speed * yfac
        self.posy = max(0, min(self.posy, HEIGHT - self.height))
        self.boxrect.update(self.posx, self.posy, self.width, self.height)

    def displayScore(self, text, score, x, y, color):
        text_surface = fonts.render(text + str(score), True, color)
        textRect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, textRect)

    def getRect(self):
        return self.boxrect

class Player:
    def __init__(self, posx, posy, width, height, color, up, down):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = 5
        self.color = color
        self.up = up
        self.down = down

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.posx, self.posy, self.width, self.height))

    def move(self, keys):
        if keys[self.up]:
            self.posy -= self.speed
        if keys[self.down]:
            self.posy += self.speed

        self.posy = max(0, min(self.posy, HEIGHT - self.height))

    def getRect(self):
        return pygame.Rect(self.posx, self.posy, self.width, self.height)

    def displayScore(self, param, playerscore, param1, param2, white):
        pass


class Ball:
    def __init__(self, posx, posy, speed, color, radius):
        self.posx = posx
        self.posy = posy
        self.speed = speed
        self.color = color
        self.radius = radius
        self.xfac = 1
        self.yfac = -1
        self.ball_rect = pygame.Rect(self.posx - self.radius, self.posy - self.radius, self.radius * 2, self.radius * 2)
        self.first = True

    def display(self):
        pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xfac
        self.posy += self.speed * self.yfac


        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yfac *= -1

        self.ball_rect.update(self.posx - self.radius, self.posy - self.radius, self.radius * 2, self.radius * 2)

        if self.posx <= 0 and self.first:
            self.first = False
            return 1
        elif self.posx >= WIDTH and self.first:
            self.first = False
            return -1
        return 0

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xfac *= -1
        self.first = True

    def hit(self):
        self.xfac *= -1
    def getRect(self):
        return self.ball_rect

def main():
    running = True
    player = Player(50, 250, 20, 100, white, pygame.K_UP, pygame.K_DOWN)
    player2 = Player(800, 250, 20, 100, white, pygame.K_w, pygame.K_s)
    listoplayer = [player, player2]
    ball = Ball(WIDTH // 2, HEIGHT // 2, 4, white, 7)

    playerscore = 0
    player2score = 0

    while running:
        screen.fill(green)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)
        player2.move(keys)


        for p in listoplayer:
            if ball.getRect().colliderect(p.getRect()):
                ball.hit()

        point = ball.update()
        if point == -1:
            playerscore += 1
        elif point == 1:
            player2score += 1

        if point:
            ball.reset()

        player.draw()
        player2.draw()
        ball.display()

        player.displayScore("Игрок 1: ", playerscore, WIDTH // 4, 30, white)
        player2.displayScore("Игрок 2: ", player2score, WIDTH * 3 // 4, 30, white)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
if __name__ == "__main__":
    main()