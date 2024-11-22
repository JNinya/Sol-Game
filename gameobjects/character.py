from saveload import Saveload
from gameobjects.gameobject import Gameobject

class Character:

    #default save folder for objects of this class
    save_directory = "characters"
    
    def __init__(self):
        pass

    #returns all the attributes of the character represented as a dictionary
    @property
    def dict(self):
        return self.__dict__
    
    #saves current instance of Character class as a .json file
    def save(self, dir = save_directory):
        Saveload.save(self.dict, self.name, dir)
    
    #loads selected json file into current object
    def load(self, name, dir = save_directory):
        character_data = Saveload.load(name, dir)
        for key, value in character_data.items():
            setattr(self, key, value)
        
    def createNewFromUser(self):
        p = Gameobject()
        p.promptUser()
        p.setAttributes(self)