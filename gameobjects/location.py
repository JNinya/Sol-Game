from gameobjects.gameobject import GameObject

class Location(GameObject):

    save_path = "savedata/locations"
    
    def __init__(self, object_name = ""):
        super().__init__(object_name)