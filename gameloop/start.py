from util.catalog import Catalog
from util.objectCreator import ObjectCreator
import os

class Start():


















    """me = ""

    @classmethod
    def execute(cls):

        os.system('cls')

        name = input("What is your name?\n")

        try:
            cls.me = Catalog.find(name)
            print(f"Welcome back {cls.me.name}")
        
        except NameError:
            choice = input(f"Character {name} does not exist. Would you like to create it (y/n)?")
            if choice == "y":
                cls.me = ObjectCreator.createCharacter()
                print(f"Welcome {cls.me.name}")

        
        print(f"You are currently at {cls.me.location}")
        print("Where do you want to go?")"""