import pygame
from pygame import mixer, image, transform

mixer.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,400))

bg = image.load('fondio.jpg')
bg = transform.scale(bg, (800,400)) #rescala el fondo

class Key():
    def __init__(self, x, y, color1, color2, key):
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.key = key
        self.rect = pygame.Rect(self.x, self.y, 100, 20)
        self.handled = False

#4 teclas A S D F
keys = [
    Key(100,350,(255,0,0),(200,0,0),pygame.K_a),
    Key(250,350,(0,255,0),(0,200,0),pygame.K_s),
    Key(400,350,(0,0,255),(0,0,200),pygame.K_d),
    Key(550,350,(255,255,0),(200,200,0),pygame.K_f)
    ]

def load(map):
    # lee mapa
    rects = []
    mixer.music.load('music.mp3')
    mixer.music.play()
    f = open(map + '.txt', 'r')
    data = f.readlines()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                rects.append(pygame.Rect(keys[x].rect.centerx - 25, y*-100, 50, 25))
    return rects

map_rect = load('text')
score = 0
life = 5

while True:
    #set font
    font = pygame.font.Font(None, 36)
    font_vida = pygame.font.Font(None, 36)
    font_gameover = pygame.font.Font(None, 100)
    #set screen
    screen.fill([0, 0, 0])
    screen.blit(bg, (0,0))
    
    score_text = font.render(f'COMBO: {score}', True, (255, 255, 255))
    score_text1 = font.render(f'Life: {life}', True, (255, 255, 255))

    screen.blit(score_text, (650, 10))
    screen.blit(score_text1, (50, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    k = pygame.key.get_pressed()

    for key in keys:
        if k[key.key]:
            pygame.draw.rect(screen, key.color1, key.rect)
            key.handled = False
        if not k[key.key]:
            pygame.draw.rect(screen, key.color2, key.rect)
            key.handled = True
    for rect in map_rect:
        pygame.draw.rect(screen, (200,0,0), rect)
        rect.y += 4
        for key in keys:
            if key.rect.colliderect(rect) and not key.handled:
                map_rect.remove(rect)
                key.handled = True
                score += 1
                break
            if rect.y == 400:
                score = 0
                life -= 1
                break
    
    if life == 0:
        score_text2 = font.render('Game Over', True, (0, 0, 0))
        screen.blit(score_text2, (350, 180))
        break

    pygame.display.update()
    clock.tick(120)
