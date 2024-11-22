import json, os, glob

#saveload saves everything as .json files. Because of this, the file_name parameter should be input without the file extension. Ex: "max" instead of "max.json"

class Saveload:
    
    #protected files can't be deleted and won't be purged
    _protected_files = ["config", "Honri", "max", "aidan"]
    
    #default directory to save the data in if not specified in the function call
    _default_dir = "savedata"

    #generate the file name with the directory used by the functions according to the file_name, the dir, and the default_dir
    @classmethod
    def generateFileName(cls, file_name, dir):
        return cls._default_dir + "/" + dir + "/" + file_name + ".json"

    @classmethod
    def setDir(cls, directory):
        cls._default_dir = directory

    #saves a dictionary to a save file with the specified name. Overwrites the file if it already exists
    #parameters: File data, File name, Save Directory within default_dir (optional)
    @classmethod
    def save(cls, data, file_name, dir = ""):
        with open(cls.generateFileName(file_name, dir), "w") as file:
            json.dump(data, file, indent=4)

    #loads a save file with the specified name as a dictionary. Will return an error if the file doesn't exist
    @classmethod
    def load(cls, file_name, dir = ""):
        with open(cls.generateFileName(file_name, dir), "r") as file:
            return json.load(file)

    #deletes a file
    @classmethod
    def delete(cls, file_name, dir = ""):
        if file_name not in cls._protected_files:
            os.remove(cls.generateFileName(file_name, dir))

    #adds a new protected file
    @classmethod
    def protectFile(cls, file_name):
        cls._protected_files.append(file_name)

    #deletes all save files in working directory. WARNING: There is no undoing this.
    @classmethod
    def purge(cls, dir = ""):
        json_files = glob.glob(cls.generateFileName("*", dir))
        for file in json_files:

            file = file.split("\\")[-1]
            file = file.split(".")[0]

            if file not in cls._protected_files:
                os.remove(cls.generateFileName(file, dir))