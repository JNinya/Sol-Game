from util.catalog import Catalog
from util.gameloop.start import Start
import os

class Render():
    
    def execute():
        me = Start.me
        
        os.system('cls')


        print(f"You are at {me.location}")
        print("Where do you want to go?")