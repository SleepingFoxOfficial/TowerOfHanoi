import pygame


class Disk:
    def __init__(self, coordX, coordY, color, radius):
        self.coordX = coordX - radius
        self.coordY = coordY + 10
        self.color = color
        self.width = radius * 2
        self.height = 20
        self.radius = radius

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.coordX, self.coordY, self.width, self.height))
