from character import Character
import saveload


player = Character()

player.createFromUser()

print(player.dict)

saveload.save(player.dict, "player")