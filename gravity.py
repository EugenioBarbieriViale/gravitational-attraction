import pygame, math, sys, random

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

# variables
class Body:
    def __init__(self, mass, gravity):
        self.mass = mass
        self.radius = int((self.mass / 3.14) ** (1/3))

        self.x = random.randint(self.radius, screenx - self.radius)
        self.y = random.randint(self.radius, screeny - self.radius)
        self.pos = pygame.math.Vector2(self.x, self.y)

        self.acc = pygame.math.Vector2(0,0)
        self.vel = pygame.math.Vector2(0,0)

        self.gravity = pygame.math.Vector2(0, -gravity)

    def move(self, x1, y1, mass1):
        self.distance = round(math.sqrt((x1-self.pos.x)*(x1-self.pos.x)+(y1-self.pos.y)*(y1-self.pos.y)),3)

        force = pygame.math.Vector2(self.gravity*((self.mass*mass1)/(self.distance**2)),3)

        self.acc = pygame.math.Vector2(force/self.mass)
        self.vel += self.acc

        self.pos += self.vel

        pygame.draw.circle(window, (0,255,255), (self.pos.x, self.pos.y), self.radius)

    def bounce(self, radius1, screenx, screeny):
        if self.pos.x - self.radius < 0 or self.pos.x + self.radius > screenx:
            self.vel.x *= -0.5

        if self.pos.y + self.radius > screeny or self.pos.y - self.radius < 0:
            self.vel.y *= -0.5

atr_mass = 1000
atr_radius = 30
atr_x = screenx/2
atr_y = screeny/2

gravity = 0.5

obj = Body(800, gravity)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))

    obj.move(atr_x, atr_y, atr_mass)
    obj.bounce(atr_radius, screenx, screeny)

    pygame.draw.circle(window, (255,255,0), (atr_x, atr_y), atr_radius)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
