import pygame
import sys
import popup

Map_width = 800
Map_length = 520

column_height = 60

list = ["Lvl.15 Infantry","Lvl.15 Archer","Lvl.13 Ballista"]
list2 = [["Iron Spear","Healing Potion"],["Wooden Bow","Steel Sword","Healing Potion"],["Iron Ballista","Strength Potion"]]
#health attack magic speed defense resistance
list3 = [["37/40","14","6","11","18","8"],["25/25","16","4","16","10","6"],["20/20","23","2","5","8","7"]]
list4 = ["Health ","ATK ","MAG ","SPD ","DEF ","RES "]

class BattlePrep:
    def __init__(self,surface,screen):
        self.surface = surface
        self.screen = screen

    def run(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        font2 = pygame.font.Font('freesansbold.ttf', 20)
        font3 = pygame.font.Font('freesansbold.ttf', 25)
        clock = pygame.time.Clock()
        user_cursor = Cursor(self.surface,self.screen)
        while True:
            output = user_cursor.handle_keys()
            if output is not None:
                if not output:
                    return "worldmap"
                return "battle"
            clock.tick(100)
            drawShop(self.surface)
            user_cursor.draw(self.surface)
            self.screen.blit(self.surface, (0,0))
            for x in range(len(list)):
                text = font.render(list[x], 1, (0,0,0))
                self.screen.blit(text, (20,x*60+15))
            if user_cursor.position1 < 3:
                for y in range(len(list2[user_cursor.position1])):
                    text = font2.render(list2[user_cursor.position1][y], 1, (0,0,0))
                    self.screen.blit(text, (320,y*60+240))
                text = ""
                for stats in range(len(list3[user_cursor.position1])):
                    text = font3.render(list4[stats]+list3[user_cursor.position1][stats], 1, (0,0,0))
                    self.screen.blit(text, (320,stats*30))
            text = font.render("BATTLE PREPARATION", 1, (255,0,0))
            self.screen.blit(text, (420,470))
            pygame.display.update()

class Cursor:
    def __init__(self,surface,screen):
        self.surface = surface
        self.screen = screen
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
                    if self.current == 2:
                        pop = popup.PopUp("would you like to start the battle",self.surface,self.screen)
                        output = pop.run()
                        if output is not None:
                            if output:
                                return True
                    if self.current+1 <= 2:
                        self.current+=1
                elif user_input.key == 122:
                    if self.current == 1:
                        pop = popup.PopUp("would you like exit the battle preparations",self.surface,self.screen)
                        output = pop.run()
                        print(output)
                        if output is not None:
                            if output:
                                return False
                    if self.current-1 <= 1:
                        self.current-=1

    def move(self,direction):
        if self.current == 1:
            if self.position1+direction >= 0 and self.position1+direction <= Map_length/column_height:
                self.position1+=direction
        if self.current == 2:
            if self.position2+direction >= 0 and self.position2+direction <= (300/column_height)-1:
                self.position2+=direction

    def draw(self,surface):
        s = pygame.Surface((300,column_height))
        s.set_alpha(128)
        s.fill(self.color)
        surface.blit(s, (0, self.position1*column_height))
        s = pygame.Surface((Map_width,column_height))
        s.set_alpha(128)
        s.fill(self.color)
        surface.blit(s, (300, (self.position2*column_height)+220))

def drawShop(surface):
    line_color = (85,52,43)
    rr = pygame.Rect((0,0), (Map_width,Map_length))
    pygame.draw.rect(surface, (255,255,255), rr)
    for y in range(1, int(Map_length/column_height)+1):
        pygame.draw.line(surface,line_color,(0, (y*column_height)-1),(300, (y*column_height)-1),4)
    pygame.draw.line(surface,line_color,(300, 0),(300, Map_length),4)
    pygame.draw.line(surface,line_color,(300, 220),(Map_width, 220),4)
    for y in range(1,int(300/column_height)+1):
        pygame.draw.line(surface,line_color,(300, ((y*column_height)-1)+220),(Map_width, (y*column_height)-1+220),4)
