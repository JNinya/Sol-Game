import glob
from gameobjects.character import Character
from gameobjects.location import Location

#the catalog contains references to all the gameobjects
class Catalog():
    characters = []
    locations = []

    save_paths = {
        "Character":"characters",
        "Location":"locations"
    }

    #save catalog to json files in savedata
    @classmethod
    def save(cls):
        for list in cls.save_paths.values():
            for item in eval("cls."+list):
                item.save()


    #load catalog from json files in savedata
    @classmethod
    def load(cls):
        path = "savedata/"

        for object_type, folder in cls.save_paths.items():
            subpath = path + folder + "/*.json"

            files = glob.glob(subpath)

            for file in files:
                file = file.split("\\")[-1]
                file = file.split(".")[0]

                game_object = eval(object_type + "()")

                game_object.load(file)
                
                eval("cls."+folder).append(game_object)

    #find object by name
    @classmethod
    def find(cls, name):
        for list in cls.save_paths.values():
            for item in eval("cls."+list):
                if item.name == name:
                    return item
        print(f"Object with name {name} not found!")
        
        


        
