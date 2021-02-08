import pygame
import sys

Map_width = 800
Map_length = 520
num = 50

class PopUp:
    def __init__(self,title,surface,screen):
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.title = font.render(title, True, (0,0,0), (211,211,211))
        self.titleRect = self.title.get_rect()
        self.titleRect.center = (Map_width//2,Map_length//2)
        self.surface = surface
        self.screen = screen

    def run(self):
        user_cursor = Cursor()
        clock = pygame.time.Clock()
        while True:
            output = user_cursor.handle_keys()
            if output is not None:
                return output
            clock.tick(100)
            self.drawBackground(self.surface)
            self.surface.blit(self.title, self.titleRect)
            font = pygame.font.Font('freesansbold.ttf', 32)
            NoText = font.render("No", True, (0,0,0), (255,0,0))
            YesText = font.render("Yes", True, (0,0,0), (0,255,0))
            rectTextYes = YesText.get_rect()
            rectTextNo = NoText.get_rect()
            rectTextNo.center = (200,395)
            rectTextYes.center = (600,395)
            self.surface.blit(YesText,rectTextYes)
            self.surface.blit(NoText,rectTextNo)
            user_cursor.draw(self.surface)
            self.screen.blit(self.surface, (0,0))
            pygame.display.update()

    def drawBackground(self,surface):
        rect2 = pygame.Rect((num,num), (Map_width-num*2,Map_length-num*2))
        pygame.draw.rect(surface, (211,211,211), rect2)
        rect2 = pygame.Rect((150,370), (100,50))
        pygame.draw.rect(surface, (255,0,0), rect2)
        rect2 = pygame.Rect((550,370), (100,50))
        pygame.draw.rect(surface, (0,255,0), rect2)

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
                if user_input.key == pygame.K_LEFT:
                    self.move(-1)
                elif user_input.key == pygame.K_RIGHT:
                    self.move(1)
                #goes in when the user pressed x
                elif user_input.key == 120:
                    if self.position == 1:
                        return True
                    return False

    def move(self,direction):
        if self.position+direction <= 1 and self.position+direction >= 0:
            self.position+=direction

    def draw(self,surface):
        s = pygame.Surface((100,50))
        s.set_alpha(128)
        s.fill(self.color)
        if self.position == 0:
            surface.blit(s, (150,370))
        if self.position == 1:
            surface.blit(s, (550,370))
