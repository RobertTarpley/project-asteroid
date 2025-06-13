import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        #always remove the asteroid that just got hit
        self.kill()

        #if already at min size, dont split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

            # Calculate new radius (e.g., shrink it by the minimum allowed)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors, splitting apart in opposite directions
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Create two new asteroids at the same position, with the new radius and velocities
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
