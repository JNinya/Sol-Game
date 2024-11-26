from gameobjects.event import Event
from catalog import Catalog
from savedata.events.start import Start

class Input(Event):
    
    def execute():
        me = Start.me
        
        destination_str = input("Where do you want to go?\n")

        destination_obj = Catalog.find(destination_str)

        me.travel(destination_obj)
        