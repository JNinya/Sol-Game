from saveload import Saveload

class Prompts:
    
    #Prompts the user using the template provided in config.json and sets the attributes of this object to the user's answers
    def promptUser(self):
        prompts = Saveload.load('config')
        for key, prompt_data in prompts.items():
            prompt = prompt_data["prompt"] + "\n"
            
            if prompt_data["type"] == "str":
                value = input(prompt)
            elif prompt_data["type"] == "int":
                value = int(input(prompt))
            elif prompt_data["type"] == "option":
                options = eval(prompt_data["options"])
                options_string = '\n'.join(f"{i + 1}. {item}" for i, item in enumerate(options))
                n = int(input(prompt + options_string + '\n'))-1
                value = options[n]
                
            setattr(self, key, value)

    #sets the attributes of the provided object to whatever is on this object
    def setAttributes(self, object):
        attribute_dictionary = self.__dict__
        for key, value in attribute_dictionary.items():
            setattr(object, key, value)


class Character:
    def __init__(self):
        pass

    #returns all the attributes of the character represented as a dictionary
    @property
    def dict(self):
        return self.__dict__
    
    #saves current instance of Character class as a .json file
    def save(self, dir = ""):
        Saveload.save(self.dict, self.name, dir)
    
    #loads selected json file into current object
    def load(self, name, dir = ""):
        character_data = Saveload.load(name, dir)
        for key, value in character_data.items():
            setattr(self, key, value)
        
    def createNewFromUser(self):
        p = Prompts()
        p.promptUser()
        p.setAttributes(self)