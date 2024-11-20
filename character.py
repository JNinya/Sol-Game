from saveload import saveload

class Prompts:
    
    def createPrompts(self):
        prompts = saveload.load('config')
        for key, prompt_data in prompts.items():
            prompt = prompt_data["prompt"] + "\n"
            
            if prompt_data["type"] == "str":
                value = input(prompt)
            elif prompt_data["type"] == "int":
                value = int(input(prompt))
            elif prompt_data["type"] == "option":
                options = eval(prompt_data["options"])
                options = '\n'.join(f"{i + 1}. {item}" for i, item in enumerate(options))
                n = int(input(prompt + options + '\n'))-1
                value = options[n]
                
            setattr(self, key, value)


class Character:
    def __init__(self):
        pass

    #returns all the attributes of the character represented as a dictionary
    @property
    def dict(self):
        return self.__dict__
    
    #saves current instance of Character class as a .json file
    def save(self):
        saveload.save(self.dict, self.name)
    
    #loads selected json file into current object
    def load(self, name):
        character_data = saveload.load(name)
        for key, value in character_data.items():
            setattr(self, key, value)
        
    def createNewFromUser(self):
        prompts = Prompts()
        prompts.createPrompts()
        self.name = prompts.name
        self.origin = prompts.origin
        self.money = prompts.money
        self.age = prompts.age


