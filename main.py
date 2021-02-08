import pygame

import ShopGUI
import battle
import battleprep
import worldmap
import battle2
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))

Map_width = 800
Map_length = 520

print("G "*20)
map = []

battles_index = {}

class Game:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((Map_width, Map_length),pygame.RESIZABLE,32)

        surface = pygame.Surface(screen.get_size())
        surface = surface.convert()
        user_response = "worldmap"
        GUIshop = ShopGUI.Shop(surface,screen)
        GUIworld = worldmap.WorldMap(surface,screen)
        GUIprep = battleprep.BattlePrep(surface,screen)
        GUIbattle1 = battle.BattleMap(surface,screen,0)
        GUIbattle2 = battle2.BattleMap(surface,screen,1)
        while True:
            if user_response == "shop":
                user_response = GUIshop.run()
            if user_response == "worldmap":
                user_response = GUIworld.run()
            if isinstance(user_response,int):
                chapter = user_response
                user_response = GUIprep.run()
                if user_response == "battle":
                    if chapter == 0:
                        user_response = GUIbattle1.run()
                    if chapter == 1:
                        user_response = GUIbattle2.run()
        pygame.quit()
        sys.exit()
gui = Game()
