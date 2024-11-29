from util.catalog import Catalog
from gameobjects.character import Character
from gameobjects.location import Location


class ObjectCreator():
    
    def createCharacter():
        new_character = Character()
        new_character.createNewFromUser()
        Catalog.characters.append(new_character)
        return new_character

    def createLocation():
        new_location = Location()
        new_location.createNewFromUser()
        Catalog.characters.append(new_location)
        return new_location