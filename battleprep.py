import pygame
import sys

Map_width = 800
Map_length = 520

column_height = 60

class BattlePrep:
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
        self.position1 = 0
        self.position2 = 0
        self.current = 1
        self.color = (255,255,0)

    def handle_keys(self):
        for user_input in pygame.event.get():
            if user_input.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if user_input.type == pygame.KEYDOWN:
                print(user_input.key)
                if user_input.key == pygame.K_UP:
                    self.move(-1)
                elif user_input.key == pygame.K_DOWN:
                    self.move(1)
                #goes in when the user pressed x
                elif user_input.key == 120:
                    self.current = 2
                elif user_input.key == 122:
                    self.current = 1

    def move(self,direction):
        if self.current == 1:
            if self.position1+direction >= 0 and self.position1+direction <= Map_length/column_height:
                self.position1+=direction
        if self.current == 2:
            if self.position2+direction >= 0 and self.position2+direction <= (300/column_height)-1:
                self.position2+=direction

    def draw(self,surface):
        rect = pygame.Rect((0, self.position1*column_height), (200,column_height))
        pygame.draw.rect(surface, self.color, rect)
        rect2 = pygame.Rect((200, (self.position2*column_height)+220), (Map_width,column_height))
        pygame.draw.rect(surface, self.color, rect2)

def drawShop(surface):
    line_color = (85,52,43)
    rr = pygame.Rect((0,0), (Map_width,Map_length))
    pygame.draw.rect(surface, (202,164,114), rr)
    for y in range(1, int(Map_length/column_height)+1):
        pygame.draw.line(surface,line_color,(0, (y*column_height)-1),(200, (y*column_height)-1),4)
    pygame.draw.line(surface,line_color,(200, 0),(200, Map_length),4)
    pygame.draw.line(surface,line_color,(200, 220),(Map_width, 220),4)
    for y in range(1,int(300/column_height)+1):
        pygame.draw.line(surface,line_color,(200, ((y*column_height)-1)+220),(Map_width, (y*column_height)-1+220),4)
