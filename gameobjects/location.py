from gameobjects.gameobject import GameObject

class Location(GameObject):

    dir_name = "locations"
    save_path = "gamedata/savedgameobjects/locations"
    
    def __init__(self, object_name = ""):
        super().__init__(object_name)