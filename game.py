from saveload import Saveload
from gameobjects.character import Character
from gameobjects.location import locations


me = Character()
me.createNewFromUser()
print(me.dict)
me.save()