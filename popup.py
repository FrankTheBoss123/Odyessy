import pygame._sdl2

class PopUp:
    def __init__(self,title,message,buttons):
        self.title = title
        self.message = message
        self.buttons = buttons

    def run(self):
        return pygame._sdl2.messagebox(self.title, self.message, buttons=self.buttons)
