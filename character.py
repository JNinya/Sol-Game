import saveload

class Prompts:
    places = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    
    @property
    def origin(self):
        return ('Where are you from?\n' + '\n'.join(f"{i + 1}. {place}" for i, place in enumerate(self.places)) + '\n')


class Character:
    def __init__(self, **character_data):
        for key, value in character_data.items():
            setattr(self, key, value)

    #returns all the attributes of the character represented as a dictionary
    @property
    def dict(self):
        return self.__dict__
    

    def save(self):
        saveload.save(self.dict, self.__class__.__name__)
    
    def promptDataFromUser(self):
        prompts = Prompts()
        self.origin = prompts.places[int(input(prompts.origin))-1]
        self.money = int(input("How much money do you have?\n"))


