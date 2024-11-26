from gameobjects.event import Event
from catalog import Catalog
import os

class Start(Event):

    me = ""

    @classmethod
    def execute(cls):

        os.system('cls')

        name = input("What is your name?\n")


        cls.me = Catalog.find(name)

        me = cls.me

        print(f"Welcome back {me.name}")
        print(f"You are currently at {me.location}")