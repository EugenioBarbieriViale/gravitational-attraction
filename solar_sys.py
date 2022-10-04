import pygame, math, sys, random

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1300,700

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

class Body:
    def __init__(self, x, y, mass, color, diameter):
        self.mass = mass
        self.diameter = diameter
        self.radius = self.diameter/2

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0)

        self.color = color

        self.gravity = pygame.math.Vector2(0, 0)

    def update(self, other):
        self.distance = other.pos - self.pos
        self.dir = self.distance.normalize()
  
        magn = self.gravity.magnitude()*((self.mass*other.mass)/(self.distance.magnitude()**2))
        force = self.dir*magn

        self.acc = force/self.mass
        self.vel += self.acc

        self.pos += self.vel
        self.pos += self.gravity

    def display(self):
        pygame.draw.circle(window, self.color, (self.pos.x, self.pos.y), self.radius)


planets = [
    Body(screenx/2, screeny/2, 2000, (0,255,0), 70), # sun
    Body(6+screenx+100, screeny/2, 5, (100,255,200), 5), # mercury
    Body(11+screenx+100, screeny/2, 50, (100,255,200), 12), # venus
    Body(15+screenx+100, screeny/2, 60, (100,255,200), 12), # earth
    Body(23+screenx+100, screeny/2, 10, (100,255,200), 6), # mars
    Body(80+screenx+100, screeny/2, 1000, (100,255,200), 25), # jupiter
    Body(143+screenx+100, screeny/2, 568, (100,255,200), 22), # saturn
    Body(288+screenx+100, screeny/2, 90, (100,255,200), 16), # uranus
    Body(450+screenx+100, screeny/2, 100, (100,255,200), 15) # neptune
]

n = len(planets)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))

    for j in range(n):
        for i in range(n):
            if j != i:
                planets[j].update(planets[i])

        planets[j].display()

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()