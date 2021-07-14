import pygame


class Head:
    def __init__(self, window, color, pos_x, pos_y, width, height):
        self.window = window
        self.Color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(self.window, self.Color, (self.pos_x, self.pos_y, self.width, self.height))

    def movement(self, key_pressed):
        width, height = pygame.display.get_surface().get_size()
        if self.pos_y <= 0:
            self.pos_y = height
        if self.pos_x <= 0:
            self.pos_x = width
        if self.pos_y >= height:
            self.pos_y = 0
        if self.pos_x >= width:
            self.pos_x = 0

        if key_pressed == pygame.K_w:  # UP
            self.pos_y -= 15

        if key_pressed == pygame.K_s:  # DOWN
            self.pos_y += 15

        if key_pressed == pygame.K_a:  # LEFT
            self.pos_x -= 15

        if key_pressed == pygame.K_d:  # RIGHT
            self.pos_x += 15
