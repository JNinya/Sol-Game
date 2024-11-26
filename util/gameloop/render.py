from util.catalog import Catalog
from util.gameloop.start import Start
import os

class Render():
    
    def execute():
        me = Start.me
        
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
        print("Where do you want to go?")