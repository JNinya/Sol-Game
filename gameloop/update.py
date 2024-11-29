from util.catalog import Catalog
from gameloop.start import Start
from gameloop.input import Input
from util.objectCreator import ObjectCreator

class Update():
    
    def execute():
        me = Start.me
        user_input = Input.user_input

        if user_input == "save":
            Catalog.save()
            return

        if user_input == "exit":
            Start.running = False
            return

        try:
            destination_obj = Catalog.find(user_input)
            me.travel(destination_obj)
        
        except NameError:
            choice = input(f"Location {user_input} does not exist. Would you like to create it (y/n)?")
            if choice == "y":
                destination_obj = ObjectCreator.createLocation()
                me.travel(destination_obj)

        