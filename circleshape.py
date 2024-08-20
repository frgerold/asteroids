import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

    containers: tuple = ()

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers") and self.containers != (None):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self, other):
        if pygame.math.Vector2.distance_to(self.position, other.position) <= (self.radius + other.radius):
            return True
        return False
        #print((pygame.math.Vector2.distance_to(self.position, other.position)))
        #print(self.radius)
        #print(other.radius)
       # print(self.radius + other.radius)
