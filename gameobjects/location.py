from gameobjects.gameobject import GameObject

class Location(GameObject):

    save_directory = "savedata/locations"
    
    def __init__(self):
        self.members = []