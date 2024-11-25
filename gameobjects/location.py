from gameobjects.gameobject import GameObject

class Location(GameObject):

    save_path = "savedata/locations"
    
    def __init__(self, object_name = ""):
        super().__init__(object_name)
        self.members = []

    def addMember(self, member):
        self.members.append(member)

    def removeMember(self, member):
        self.members.remove(member)