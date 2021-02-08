import pygame
import sys
import random
import popup

Map_width = 800
Map_length = 520

Grid_size = 40

Grid_width = int(Map_width/Grid_size)
Grid_length = int(Map_length/Grid_size)

blocks = {
    "G":{"name":"grass","passable":True,"color":(126, 200, 80)},
    "W":{"name":"water","passable":False,"color":(0, 159, 225)},
    "M":{"name":"mountain","passable":False,"color":(151,145,144)},
    "F":{"name":"fort","passable":True,"color":(149,148,139)}
}

motion = {
    "up":(0,-1),
    "down":(0,1),
    "left":(-1,0),
    "right":(1,0)
}

map = []

enemies = {}
allies = {}

class BattleMap:
    def __init__(self,surface,screen,battlenum):
        self.screen = screen
        self.surface = surface
        with open("game_data/"+str(battlenum)+"battle.txt","r") as file:
            for y in range(Grid_length):
                map.append([])
                array = file.readline().split(" ")
                for x in range(len(array)):
                    block_name = array[x]
                    block_name = block_name.replace("\n", "")
                    map[y].append(blocks[block_name])
            enemyspawn = [int(x) for x in file.readline().split(" ")]
            alliedspawn = [int(x) for x in file.readline().split(" ")]
        self.generate(battlenum,enemyspawn,alliedspawn)

        file.close()

    def run(self):
        clock = pygame.time.Clock()
        font = pygame.font.Font('freesansbold.ttf', 32)
        drawGrid(self.surface)

        user_cursor = Cursor(self.surface,self.screen)

        generated = []

        while True:
            output = user_cursor.handle_keys()
            if output is not None:
                if output == False:
                    return "worldmap"
                elif output[1] in generated:
                    self.move_allied_unit(output[0],output[1])
            clock.tick(100)
            drawGrid(self.surface)
            self.draw_units()
            if user_cursor.selected:
                if len(generated) == 0:
                    generated = self.generate_path(4,user_cursor.position)
                self.draw_path(generated)
            if not user_cursor.selected:
                generated = []
            user_cursor.draw(self.surface)
            self.screen.blit(self.surface, (0,0))
            text = font.render("BATTLE MENU", 1, (255,0,0))
            self.screen.blit(text, (550,470))
            pygame.display.update()


    def generate(self,level,enemyspawn,alliedspawn):
        #stats [name,health,attack,defense,movement]
        enemyTroops = [["generic infantry",(7,7),2,4,3]]*(level+3)
        potential_coordinates = []
        for x in range(enemyspawn[0],enemyspawn[1]):
            for y in range(enemyspawn[2],enemyspawn[3]):
                potential_coordinates.append((x,y))
        random.shuffle(potential_coordinates)
        while len(enemyTroops) != 0:
            coordinates = potential_coordinates.pop(0)
            enemies[coordinates] = enemyTroops.pop(0)
        alliedTroops = [["generic infantry",(7,7),2,4,3]]*(3)
        potential_coordinates = []
        for x in range(alliedspawn[0],alliedspawn[1]):
            for y in range(alliedspawn[2],alliedspawn[3]):
                potential_coordinates.append((x,y))
        random.shuffle(potential_coordinates)
        while len(alliedTroops) != 0:
            coordinates = potential_coordinates.pop(0)
            allies[coordinates] = alliedTroops.pop(0)

    def draw_units(self):
        for coordinates in enemies.keys():
            rr = pygame.Rect((coordinates[0]*Grid_size, coordinates[1]*Grid_size), (Grid_size,Grid_size))
            pygame.draw.rect(self.surface, (255,0,0), rr)
        for coordinates in allies.keys():
            rr = pygame.Rect((coordinates[0]*Grid_size, coordinates[1]*Grid_size), (Grid_size,Grid_size))
            pygame.draw.rect(self.surface, (0,0,255), rr)

    def generate_path(self,movement,starting):
        queue = [(starting,movement)]
        ans = set()
        while len(queue) != 0:
            current_val = queue.pop(0)
            current = current_val[0]
            if current not in ans:
                ans.add(current)
            if current_val[1] > 0:
                for thing in motion.values():
                    potential_coordinate = (current[0]+thing[0],current[1]+thing[1])
                    if potential_coordinate not in ans and self.possible(potential_coordinate):
                        queue.append((potential_coordinate,current_val[1]-1))
        return list(ans)

    def draw_path(self,coordinates):
        s = pygame.Surface((Grid_size,Grid_size))
        s.set_alpha(128)
        s.fill((128,128,128))
        for coord in coordinates:
            self.surface.blit(s, (coord[0]*Grid_size,coord[1]*Grid_size))

    def possible(self,coordinate):
        if coordinate[0] >= 0 and coordinate[0] < Grid_width:
            if coordinate[1] >= 0 and coordinate[1] < Grid_length:
                if map[coordinate[1]][coordinate[0]]["passable"]:
                    return True
        return False

    def move_allied_unit(self,position_before,position_after):
        if position_before in allies and self.possible(position_after) and position_after not in enemies:
            value = allies.pop(position_before)
            allies[position_after] = value


class Cursor:
    def __init__(self,surface,screen):
        self.position = (6,6)
        self.color = (255,255,0)
        self.selected = False
        self.selected_positon = (0,0)
        self.surface = surface
        self.screen = screen

    def handle_keys(self):
        for user_input in pygame.event.get():
            if user_input.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_UP:
                    self.move(motion["up"])
                elif user_input.key == pygame.K_DOWN:
                    self.move(motion["down"])
                elif user_input.key == pygame.K_LEFT:
                    self.move(motion["left"])
                elif user_input.key == pygame.K_RIGHT:
                    self.move(motion["right"])
                #goes in when the user pressed x
                elif user_input.key == 120:
                    if self.selected == True:
                        self.selected = False
                        return (self.selected_positon,self.position)
                    if self.position in allies:
                        self.selected = True
                        self.selected_positon = self.position
                elif user_input.key == 122:
                    if self.selected == False:
                        pop = popup.PopUp("would you like exit the battle",self.surface,self.screen)
                        output = pop.run()
                        if output is not None:
                            if output:
                                return False
                    self.selected = False
                    self.selected_positon = (0,0)

    def move(self,direction):
        moved_position = (self.position[0]+direction[0],self.position[1]+direction[1])
        if 0 <= moved_position[0] < Grid_width and 0 <= moved_position[1] < Grid_length:
            if map[moved_position[1]][moved_position[0]]["passable"]:
                self.position = moved_position

    def draw(self,surface):
        s = pygame.Surface((Grid_size,Grid_size))
        s.set_alpha(128)
        s.fill(self.color)
        surface.blit(s, (self.position[0]*Grid_size, self.position[1]*Grid_size))


def drawGrid(surface):
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            rr = pygame.Rect((x*Grid_size, y*Grid_size), (Grid_size,Grid_size))
            pygame.draw.rect(surface, map[y][x]["color"], rr)
