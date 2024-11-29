import glob
from gameobjects.character import Character
from gameobjects.location import Location

#the catalog contains references to all the gameobjects
class Catalog():
    characters = []
    locations = []

    path = "gamedata/savedgameobjects/"

    save_paths = {
        "Character":"characters",
        "Location":"locations"
    }

    #save catalog to json files in gamedata
    @classmethod
    def save(cls):
        for list in cls.save_paths.values():
            for item in eval("cls."+list):
                item.save()


    #load catalog from json files in gamedata
    @classmethod
    def load(cls):


        for object_type, folder in cls.save_paths.items():
            subpath = cls.path + folder + "/*.json"

            files = glob.glob(subpath)

            for file in files:
                file = file.split("\\")[-1]
                file = file.split(".")[0]

                game_object = eval(object_type + "()")

                try:
                    game_object.load(file)
                except:
                    print("Error loading json file")
                
                eval("cls."+folder).append(game_object)

    #find object by name
    @classmethod
    def find(cls, name):
        for list in cls.save_paths.values():
            for item in eval("cls."+list):
                if hasattr(item, "name"):
                    if item.name == name:
                        return item
                else:
                    print("Error loading json file: name attribute missing")
        #print(f"Object with name {name} not found!")
        raise NameError("No object found")

    @classmethod
    def search(cls, search_dict):
        
        return_list = []

        #iterate through each object type
        for type, list in cls.save_paths.items():
            
            #iterate through each item in list
            for item in eval("cls."+list):
                #for each item in list of type
                
                #iterate through each requirement given by the search dict
                for attribute, value  in search_dict.items():
                    
                    #print(f"type: {type}, item: {item}, key: {attribute}, value: {value}")

                    #break if attribute doesn't exist
                    if not hasattr(item, attribute):
                        break

                    #break if attribute does not have the correct value
                    if not (eval(f"item.{attribute}") == value):
                        break

                #print item if the above for loop executed all the way through without breaking
                else:
                    return_list.append(item)

        return return_list
        
        

        
        


        
