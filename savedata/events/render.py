from gameobjects.event import Event
from catalog import Catalog
from savedata.events.start import Start
import os

class Render(Event):
    
    def execute():
        me = Start.me
        
        os.system('cls')

        print(f"You are at {me.location}")