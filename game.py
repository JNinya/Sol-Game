from saveload import Saveload
from character import Character

#protect the files I need
Saveload.protectFile("config.json")
Saveload.protectFile("Honri.json")
Saveload.purge()



#create a new character called player
player = Character()

#prompt the user to create a new character
player.createNewFromUser()

#save the character to a json file
#player.save()


print(player.dict)

#player.save()
