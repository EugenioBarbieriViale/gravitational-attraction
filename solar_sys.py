import pygame, math, sys, random

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

class Body:
    def __init__(self, x, y, mass, color, gravity):
        self.mass = mass
        self.radius = int((self.mass / 3.14) ** (1/3))

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0)

        self.color = color

        self.gravity = pygame.math.Vector2(0, gravity)

    def move(self, atr, mass1):
        self.distance = atr - self.pos
        self.dir = self.distance.normalize()
  
        magn = self.gravity.magnitude()*((self.mass*mass1)/(self.distance.magnitude()**2))
        force = self.dir*magn

        self.acc = force/self.mass
        self.vel += self.acc

        self.pos += self.vel
        self.pos += self.gravity

        pygame.draw.circle(window, self.color, (self.pos.x, self.pos.y), self.radius)

    def bounce(self, radius1, screenx, screeny):
        if self.pos.x - self.radius < 0 or self.pos.x + self.radius > screenx:
            self.vel.x *= -0.5

        if self.pos.y + self.radius > screeny or self.pos.y - self.radius < 0:
            self.vel.y *= -0.5

atr_mass = 1000
atr_radius = 30
atr = pygame.math.Vector2(screenx/2, screeny/2)

gravity = 1

objs = []
n = 4
for i in range(n):
    x = (i+10) * 20
    y = screeny / 2
    mass = random.randint(650, 1300)
    
    colors = []
    for j in range(3):
        color = random.randint(0,255)
        colors.append(color)

    objs.append(Body(x, y, mass, colors, gravity))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))

    for obj in objs:
        obj.move(atr, atr_mass)
        obj.bounce(atr_radius, screenx, screeny)

    pygame.draw.circle(window, (255,255,0), (atr.x, atr.y), atr_radius)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()