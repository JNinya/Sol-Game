from character import Character
from saveload import saveload

saveload.protectFile("config.json")
saveload.protectFile("Honri.json")
saveload.purge()






#create a new character called player
player = Character()

#prompt the user to create a new character
player.createNewFromUser()

#save the character to a json file
#player.save()


print(player.dict)

#player.save()
