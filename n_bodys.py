import pygame, math, sys, random

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

class Body:
    def __init__(self, x, y, mass, color, gravity):
        self.mass = mass
        self.radius = int(mass/100)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0)

        self.color = color

        self.gravity = pygame.math.Vector2(0, gravity)

    def update(self, other):
        self.distance = other.pos - self.pos
        self.dir = self.distance.normalize()
  
        magn = self.gravity.magnitude()*((self.mass*other.mass)/(self.distance.magnitude()**2))
        self.force = self.dir*magn

        self.acc = self.force/self.mass
        self.vel += self.acc

        self.pos += self.vel
        self.pos += self.gravity

        print(self.vel)

    def collide(self, other):
        dist = self.distance.magnitude()
        if dist <= self.radius or dist <= other.radius:
            return True

    def display(self):
        pygame.draw.circle(window, self.color, (self.pos.x, self.pos.y), self.radius)


gravity = 0.5

objs = []
n = 2

for i in range(n):
    x = random.randint(20, 700)
    y = random.randint(20, 700)

    mass = random.randint(600,1000)
    
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

    for j in range(len(objs)):
        for i in range(len(objs)):
            if j != i:
                objs[j].update(objs[i])
                if objs[j].collide(objs[i]):
                    objs[j].vel *= -1
                    objs[i].vel *= -1
                
        objs[j].display()

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

