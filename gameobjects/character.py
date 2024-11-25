from gameobjects.gameobject import GameObject

class Character(GameObject):

    save_path = "savedata/characters"

    def __init__(self, object_name = ""):
        super().__init__(object_name)

    #move the location of this character
    def travel(self, destination):
        
        self.location = destination.name

        raise NotImplementedError
        #destination.addMember(self.name)