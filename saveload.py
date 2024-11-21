import json, os, glob

#saveload saves everything as .json files. Because of this, the file_name parameter should be input without the file extension. Ex: "max" instead of "max.json"

class Saveload:
    
    #protected files can't be deleted and won't be purged
    protected_files = ["config.json", "Honri.json", "max.json"]
    
    #default directory to save the data in if not specified in the function call
    default_dir = "savedata/"

    #saves a dictionary to a save file with the specified name. Overwrites the file if it already exists
    #parameters: File data, File name, Save Directory (optional)
    @classmethod
    def save(cls, data, file_name, dir = default_dir):
        with open(dir + file_name + ".json", "w") as file:
            json.dump(data, file, indent=4)

    #loads a save file with the specified name as a dictionary. Will return an error if the file doesn't exist
    @classmethod
    def load(cls, file_name, dir = default_dir):
        with open(dir + file_name + ".json", "r") as file:
            return json.load(file)

    #deletes a file
    @classmethod
    def delete(cls, file_name, dir = default_dir):
        file_name = file_name + ".json"
        if file_name not in cls.protected_files:
            os.remove(dir + file_name)

    #adds a new protected file
    @classmethod
    def protectFile(cls, file_name):
        cls.protected_files.append(file_name + ".json")

    @classmethod
    def setDir(cls, directory):
        cls.default_dir = directory

    #deletes all save files in working directory. WARNING: There is no undoing this.
    @classmethod
    def purge(cls, dir = default_dir):
        json_files = glob.glob(dir + "*.json")
        for file in json_files:
            if file not in cls.protected_files:
                os.remove(file)