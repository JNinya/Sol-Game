import pygame
from gui.gui import Gui
from gui.menu import Menu
from gui.button import Button
import random
import os

from gameloop.start import Start
from util.catalog import Catalog

class Render():
    
    def execute():

        Gui.screen.fill("black")

        x = random.randint(0,Gui.width)
        y = random.randint(0,Gui.height)

        myb = Button((x,y,50,50),"blue")

        myb.blit()

        
        pygame.display.flip()

        Gui.clock.tick(60)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """me = Start.me
        
        os.system('cls')


        characters_at_location = Catalog.search({
            "type":"Character",
            "location":me.location
        })

        characters_at_location.remove(me)

        characters_at_location_str = ""

        for item in characters_at_location:
            characters_at_location_str += "\n" + item.name


        print(f"You are at {me.location}")
        print(f"Other people at {me.location}: {characters_at_location_str}")
        print("Where do you want to go?")"""