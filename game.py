from saveload import Saveload
from gameobjects.character import Character
from gameobjects.location import Location


"""me = Character()
me.createNewFromUser()
me.save()
print(me.dict)

mars = Location()
mars.createNewFromUser()
mars.save()
print(mars.dict)"""

luna = Location()
luna.load("Luna")
print(luna.dict)