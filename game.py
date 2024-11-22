from saveload import Saveload
import glob
from gameobjects.character import Character
from gameobjects.location import Location



maxo = Location()
maxo.createNewFromUser()
print(maxo.dict)
maxo.save()