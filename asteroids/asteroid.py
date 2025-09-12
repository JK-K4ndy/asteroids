import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

import pygame # type: ignore

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(200,200,200),self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    #ahead of time
    #def split(self):
#        self.kill()
 #       if self.radius <= ASTEROID_MIN_RADIUS:
  #         return
   #     else:
    #        pass
     #       offset = random.uniform(20, 50)
      #      angle_pos = self.velocity.rotate(offset)
       #     angle_neg = self.velocity.rotate(-offset)
        #    radius = self.radius - ASTEROID_MIN_RADIUS
         #   Asteroid()

            