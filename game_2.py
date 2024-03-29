import pygame
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 1200, 700
SCREEN = pygame.display.set_mode(SIZE)

#rgb color code
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255
BLACK = 0,0,0
GREEN = 0,255,0
XYZ = 128,220,141

bulletSound = pygame.mixer.Sound("assets/Shoot.wav")
enemySound = pygame.mixer.Sound("assets/casino.wav")
def homeScreen ():
    font = pygame.font.Font("assets/fontss/ARCADECLASSIC.TTF", 150)
    text = font.render(f"SPACE  SHOOTER", True, RED)

    font_2 = pygame.font.SysFont(None, 150)
    text_2 = font_2.render(f"Press Space To Start", True, WHITE)

    while True:
        evenList = pygame.event.get()
        for event in evenList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        SCREEN.blit(text, (100, 200))
        SCREEN.blit(text_2, (100, 450))
        pygame.display.flip()

def updateHealth(count):
    font = pygame.font.SysFont(None, 60)
    text = font.render(f"Health : {count}", True , RED)
    SCREEN.blit(text, (50, 500))


def gameOver():
    font = pygame.font.SysFont(None, 150)
    text = font.render(f"GAME_OVER", True, RED)
    while True:
        evenList = pygame.event.get()
        for event in evenList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        SCREEN.blit(text,(245, 400))
        pygame.display.flip()



def gameWin():
    SCREEN.fill(BLACK)
    font = pygame.font.SysFont(None, 270)
    text = font.render(f"GAME_WIN", True, XYZ)
    while True:
        evenList = pygame.event.get()
        for event in evenList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        SCREEN.blit(text,(150, 250))
        pygame.display.flip()

def main():
    move_x =0

    ship = pygame.image.load("assets/ship5.png")
    ship_w = ship.get_width()
    ship_h = ship.get_height()
    ship_x = WIDTH // 2 - ship_w // 2
    ship_y = (HEIGHT - ship_h)

    enemyShip = pygame.image.load("assets/newship.jpg")
    eship_w = enemyShip.get_width()
    eship_h = enemyShip.get_height()

    enemyList = []
    nrow = 2
    ncols = WIDTH // eship_w

    for i in range (nrow):
        for j in range (ncols):
            enemyX = eship_w * j
            enemyY = eship_h * i
            enemyRect = pygame.Rect(enemyX, enemyY, eship_w, eship_h)
            enemyList.append(enemyRect)

    #BulletCode
    bullet_w = 8
    bullet_h = 15
    bullet_y = ship_y
    moveBullet = 0

    # enemy bullets
    random_enemy = random.choice(enemyList)
    enemy_bullet_w = 5
    enemy_bullet_h = 10
    enemy_bullet_x = random_enemy.x + eship_w//2
    enemy_bullet_y = random_enemy.bottom - 10

    playerHealthCount = 100
    while True:
        bullet_x = ship_x + ship_w // 2
        evenList = pygame.event.get()
        for event in evenList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 0.8
                elif event.key == pygame.K_LEFT:
                    move_x = -0.8
                elif event.key == pygame.K_SPACE:
                    moveBullet = -5
                    bulletSound.play()
            else:
                move_x =0

        SCREEN.fill(BLACK)
        bullet_rect = pygame.draw.rect(SCREEN, GREEN, [bullet_x, bullet_y, bullet_w, bullet_h])
        bullet_y += moveBullet
        SCREEN.blit(ship, (ship_x, ship_y))
        ship_x += move_x

        # player ship
        ship_rect = pygame.Rect(ship_x, ship_y, ship_w, ship_h)
        enemyBullet = pygame.draw.rect(SCREEN, WHITE, [enemy_bullet_x, enemy_bullet_y, enemy_bullet_w,enemy_bullet_h])
        enemy_bullet_y += 5

        for i in range (len(enemyList)):
            # enemyShip - image
            SCREEN.blit(enemyShip , (enemyList[i].x, enemyList[i].y))

        for i in range(len(enemyList)):
            if bullet_rect.colliderect(enemyList[i]):
                bullet_y = ship_y
                moveBullet = 0
                del enemyList[i]
                break

        if bullet_y < 0:
            bullet_y = ship_y
            moveBullet = 0

        if enemy_bullet_y > HEIGHT:
            random_enemy = random.choice(enemyList)
            enemy_bullet_x = random_enemy.x + eship_w // 2
            enemy_bullet_y = random_enemy.bottom - 10
            enemySound.play()


        if enemyBullet.colliderect(ship_rect):
            playerHealthCount -= 5
            enemy_bullet_y = HEIGHT + 10

        if playerHealthCount == 0:
            gameOver()

        if (len(enemyList) ==0):
            gameWin()

        updateHealth(playerHealthCount)
        #update the screen
        pygame.display.flip()

homeScreen()