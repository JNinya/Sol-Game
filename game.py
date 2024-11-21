from saveload import Saveload
from gameobjects.character import Character

save_directory = "savedata/"
Saveload.setDir(save_directory)

test = {
    "test":"test"
}


Saveload.save(test, "test", "characters")