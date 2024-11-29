from util.saveload import Saveload

class GameObject:

    save_path = "gamedata/savedgameobjects"

    def __init__(self, object_name = ""):
        if object_name != "":
            self.load(object_name)

    #returns all the attributes of the character represented as a dictionary
    @property
    def dict(self):
        return self.__dict__
    
    #returns the current location of the object
    @property
    def where(self):
        return self.location

    #saves current instance of class as a .json file
    def save(self):
        dir = self.__class__.save_path
        Saveload.save(self.dict, self.name, dir)
    
    #loads selected json file into current object
    def load(self, name):
        dir = self.__class__.save_path
        data = Saveload.load(name, dir)
        for key, value in data.items():
            setattr(self, key, value)

    #Prompts the user using the template provided in config.json and sets the attributes of this object to the user's answers
    def createNewFromUser(self):
        game_object_file_name = self.__class__.__name__
        prompts = Saveload.load(game_object_file_name, "util/gameobjects/object_config_files")
        for key, prompt_data in prompts.items():
            prompt = prompt_data["prompt"] + "\n"
            
            if prompt_data["type"] == "str":
                value = input(prompt)
            elif prompt_data["type"] == "int":
                value = int(input(prompt))
            elif prompt_data["type"] == "option":
                options = prompt_data["options"]
                options_string = '\n'.join(f"{i + 1}. {item}" for i, item in enumerate(options))
                n = int(input(prompt + options_string + '\n'))-1
                value = options[n]
                
            setattr(self, key, value)
        setattr(self, "type", game_object_file_name)

    #Depricated
    """#sets the attributes of the provided object to whatever is on this object
    def setAttributes(self, object):
        attribute_dictionary = self.__dict__
        for key, value in attribute_dictionary.items():
            setattr(object, key, value)"""
