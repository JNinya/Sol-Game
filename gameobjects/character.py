from gameobjects.gameobject import GameObject

class Character(GameObject):

    #default save folder for objects of this class
    #save_directory = "savedata/characters"
    
    def __init__(self):
        self.save_directory = "savedata/characters"

    #move the location of this character
    def travel(self, destination):
        #set object attribute
        self.location = destination

        #raise NotImplementedError
        #not implemented
        #update local location object

    """#creates a new object in the command line
    def createNewFromUser(self):
        p = GameObject()
        p.createNewObjectFromUser(self.__class__.__name__)
        p.setAttributes(self)"""