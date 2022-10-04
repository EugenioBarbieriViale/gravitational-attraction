import pygame, math, sys, random

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

class Body:
    def __init__(self, x, y, mass, color, gravity):
        self.mass = mass
        self.radius = int(self.mass/100)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0)

        self.color = color

        self.gravity = pygame.math.Vector2(0, gravity)

    def update(self, other):
        self.distance = other.pos - self.pos
        self.dir = self.distance.normalize()
  
        magn = self.gravity.magnitude()*((self.mass*other.mass)/(self.distance.magnitude()**2))
        force = self.dir*magn

        self.acc = force/self.mass
        self.vel += self.acc

        self.pos += self.vel
        self.pos += self.gravity

        other.acc = force/other.mass
        other.vel -= other.acc

        other.pos -= other.vel
        other.pos -= other.gravity

    def bounce(self, screenx, screeny):
        if self.pos.x - self.radius < 0 or self.pos.x + self.radius > screenx:
            self.vel.x *= -0.5

        if self.pos.y + self.radius > screeny or self.pos.y - self.radius < 0:
            self.vel.y *= -0.5

    def display(self):
        pygame.draw.circle(window, self.color, (self.pos.x, self.pos.y), self.radius)



gravity = 1

objs = []
n = 2
for i in range(n):
    x = random.randint(20, screenx-20)
    y = 300

    mass = random.randint(800, 1400)
    
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

    for j in range(n):
        for i in range(n):
            if j != i:
                objs[j].update(objs[i])
                objs[j].bounce(screenx, screeny)
        objs[j].display()

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()