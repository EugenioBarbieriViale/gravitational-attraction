import pygame, math, sys, random

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

class Body:
    def __init__(self, mass, gravity):
        self.mass = mass
        self.radius = int((self.mass / 3.14) ** (1/3))

        self.x = random.randint(self.radius, screenx - self.radius)
        self.y = random.randint(self.radius, screeny - self.radius)
        self.pos = pygame.math.Vector2(self.x,self.y)

        self.vel = pygame.math.Vector2(0)

        self.gravity = pygame.math.Vector2(0, gravity)

    def move(self, x1, y1, mass1):
        attr = pygame.math.Vector2(x1,y1)

        self.distance = attr - self.pos
        self.dir = self.distance.normalize()
  
        magn = self.gravity.magnitude()*((self.mass*mass1)/(self.distance.magnitude()**2))
        force = self.dir*magn

        self.acc = force/self.mass
        self.vel += self.acc

        self.pos += self.vel
        self.pos += self.gravity

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

gravity = 1

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
