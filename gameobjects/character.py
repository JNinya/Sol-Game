from gameobjects.gameobject import GameObject

class Character(GameObject):

    save_directory = "savedata/characters"

    def __init__(self):
        #save directory of this class
        #self.save_directory = "savedata/characters"
        pass

    #move the location of this character
    def travel(self, destination):
        #set object attribute
        self.location = destination

        #raise NotImplementedError
        #not implemented
        #update local location object