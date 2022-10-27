import pygame, math, sys

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

earth = [500,200]

sun = [300,screeny//2]
focus = [700,screeny//2]

a = 100
b = 70

e = math.sqrt(a**2 - b**2)/a
p = b**2/a

theta = 30
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))

    #d = math.sqrt((earth[0]-sun[0])**2 + (earth[1]-sun[1])**2)
    #cos = (earth[0] - sun[0])/d
    #theta = math.acos(cos)

    theta += 0.01
    
    r = p/(1 + e*math.cos(theta))

    polars = [r, theta]

    x = r * math.cos(theta) + sun[0]
    y = r * math.sin(theta) + sun[1]

    pygame.draw.circle(window, (255,0,0), (x,y), 10)
    
    pygame.draw.circle(window, (100,100,100), sun, 5)
    pygame.draw.circle(window, (100,100,100), focus, 5)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

