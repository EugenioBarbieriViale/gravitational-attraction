import pygame, math, sys

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")


sun = [screenx//2,screeny//2]

a = 200
b = 200

e = math.sqrt(a**2 - b**2)/a
p = b**2/a

theta = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))

    theta += 0.01

    r = p/(1 + e*math.cos(theta))

    x = r * math.cos(theta) + sun[0]
    y = r * math.sin(theta) + sun[1]

    pygame.draw.circle(window, (100,0,255), (x,y), 10)
    pygame.draw.circle(window, (255,0,0), sun, 20)

    pygame.draw.line(window, (0,255,0), sun, (x,y), 2)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

