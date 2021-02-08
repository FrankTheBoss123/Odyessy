import pygame
import sys
import popup

Map_width = 800
Map_length = 520

Column_height = 60
list = ["Wooden Sword","Stone Sword","Healing Potion","Strength Potion","Iron Spear"]
list2 = ["$15","$30","$20","$40","$60"]

class Shop:
    def __init__(self,surface,screen):
        self.surface = surface
        self.screen = screen

    def run(self):
        clock = pygame.time.Clock()
        user_cursor = Cursor(self.surface,self.screen)
        font = pygame.font.Font('freesansbold.ttf', 32)
        while True:
            output = user_cursor.handle_keys()
            if output is not None:
                return output
            clock.tick(100)
            drawShop(self.surface)
            user_cursor.draw(self.surface)
            self.screen.blit(self.surface, (0,0))
            for x in range(len(list)):
                text = font.render(list[x], 1, (0,0,0))
                self.screen.blit(text, (50,x*60+15))
                text = font.render(list2[x], 1, (0,0,0))
                self.screen.blit(text, (600,x*60+15))
            text = font.render("SHOP MENU", 1, (255,0,0))
            self.screen.blit(text, (570,440))
            pygame.display.update()

class Cursor:
    def __init__(self,surface,screen):
        self.position = 0
        self.color = (255,255,0)
        self.screen = screen
        self.surface = surface

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
                    if self.position < len(list):
                        pop = popup.PopUp("would you like to buy "+list[self.position],self.surface,self.screen)
                        output = pop.run()

                elif user_input.key == 122:
                    pop = popup.PopUp("would you like to leave the shop",self.surface,self.screen)
                    output = pop.run()
                    if output is not None:
                        if output:
                            return "worldmap"

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
