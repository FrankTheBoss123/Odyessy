import pygame
import sys

Map_width = 800
Map_length = 520

Column_height = 60

class Shop:
    def __init__(self,surface,screen):
        self.surface = surface
        self.screen = screen

        clock = pygame.time.Clock()
        user_cursor = Cursor()

        while True:
            output = user_cursor.handle_keys()
            clock.tick(100)
            drawShop(surface)
            user_cursor.draw(surface)
            screen.blit(surface, (0,0))
            pygame.display.update()

class Cursor:
    def __init__(self):
        self.position = 0
        self.color = (255,255,0)

    def handle_keys(self):
        for user_input in pygame.event.get():
            if user_input.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_UP:
                    self.move(-1)
                elif user_input.key == pygame.K_DOWN:
                    self.move(1)
                #goes in when the user pressed x
                elif user_input.key == 120:
                    return self.enter()

    def move(self,direction):
        print(self.position)
        if self.position+direction >= 0 and self.position+direction <= Map_length/Column_height:
            self.position+=direction

    def draw(self,surface):
        s = pygame.Surface((Map_width,Column_height))
        s.set_alpha(128)
        s.fill(self.color)
        surface.blit(s, (0,self.position*Column_height))

def drawShop(surface):
    rr = pygame.Rect((0,0), (Map_width,Map_length))
    pygame.draw.rect(surface, (255,255,255), rr)
    for y in range(1, int(Map_length/Column_height)+1):
        pygame.draw.line(surface,(85,52,43),(0, (y*Column_height)-1),(Map_width, (y*Column_height)-1),4)
