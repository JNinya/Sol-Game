from saveload import Saveload
from gameobjects.character import Character

#save_directory = "savedata"
#Saveload.setDir(save_directory)

me = Character()
me.createNewFromUser()
me.save("characters")
print(me.dict)