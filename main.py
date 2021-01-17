import pygame
import worldmap
import ShopGUI
import battle
import battleprep
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

        #GUI = battleprep.BattlePrep(surface,screen)
        #GUI = ShopGUI.Shop(surface,screen)
        #GUI = worldmap.WorldMap(surface,screen)
        GUI = battle.BattleMap(surface,screen,1)
        user_response = " "
        while user_response != "":
            if user_response == "shop":
                user_response = ShopGUI.Shop()
            #I can setu more GUI in the future, and go in there using if statements
        pygame.quit()
        sys.exit()
gui = Game()
