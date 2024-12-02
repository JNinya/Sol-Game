import glob
from gameobjects.character import Character
from gameobjects.location import Location

#the catalog contains references to all the gameobjects
class Catalog():
    #characters = []
    #locations = []

    """characters = {
        "members":[],
        "object":Character,
        "save_path":"characters"
    }"""


    path = "gamedata/savedgameobjects" # NOTE: removed end slash, BE CAREFUL!

    stored_objects = {
        Character: [],
        Location: [],
    }

    #save catalog to json files in gamedata
    @classmethod
    def save(cls):
        for list in cls.stored_objects.values():
            for item in list:
                item.save()


    #load catalog from json files in gamedata
    @classmethod
    def load(cls):
        for obj_type, objs in cls.stored_objects.items():
            subpath = f"{cls.path}/{obj_type.dir_name}/*.json"

            files = glob.glob(subpath)

            for file in files:
                file = file.split("\\")[-1]
                file = file.split(".")[0]

                game_obj = obj_type()

                try:
                    game_obj.load(file)
                    #obj_type.load(file) # for debugging exceptions; this doesn't work
                except Exception as ex:
                    print(f"Error loading json file: {ex}")
                
                objs.append(game_obj)
                

    #find object by name
    @classmethod
    def find(cls, name):
        #print(cls.stored_objects)
        for objs in cls.stored_objects.values():
            for obj in objs:
                if hasattr(obj, "name"):
                    if obj.name == name:
                        return obj
                else:
                    print("Error loading json file: name attribute missing")
        #print(f"Object with name {name} not found!")
        raise NameError("No object found")

    @classmethod
    def search(cls, search_dict):

        return_list = []

        # iterate through each object type
        for objs in cls.stored_objects.values():
            for obj in objs:
                #for each item in list of type
                
                #iterate through each requirement given by the search dict
                for attribute, value in search_dict.items():
                    
                    #print(f"type: {type}, item: {item}, key: {attribute}, value: {value}")

                    # Filter out objects if they don't contain all attributes in search_dict
                    if not hasattr(obj, attribute):
                        break

                    # Filter out objects that don't have the requested value in search_dict
                    if not getattr(obj, attribute) == value:
                        break

                else:
                    return_list.append(obj)

        return return_list
        
        

        
        


        
