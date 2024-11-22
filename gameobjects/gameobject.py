from saveload import Saveload

class Gameobject:
    
    #Prompts the user using the template provided in config.json and sets the attributes of this object to the user's answers
    def promptUser(self, prompt_file):
        prompts = Saveload.load(prompt_file)
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

    #sets the attributes of the provided object to whatever is on this object
    def setAttributes(self, object):
        attribute_dictionary = self.__dict__
        for key, value in attribute_dictionary.items():
            setattr(object, key, value)
