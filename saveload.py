import json, os, glob

class Saveload:
    
    #protected files can't be deleted and won't be purged
    protected_files = []

    #saves a dictionary to a save file with the specified name. Overwrites the file if it already exists
    @staticmethod
    def save(data, file_name):
        with open(file_name + ".json", "w") as file:
            json.dump(data, file, indent=4)

    #loads a save file with the specified name as a dictionary. Will return an error if the file doesn't exist
    @staticmethod
    def load(file_name):
        with open(file_name + ".json", "r") as file:
            return json.load(file)

    @classmethod
    def delete(cls, file_name):
        if file_name not in cls.protected_files:
            os.remove(file_name)

    #adds a new protected file
    @classmethod
    def protectFile(cls, file_name):
        cls.protected_files.append(file_name)

    #deletes all save files in working directory. WARNING: There is no undoing this.
    @classmethod
    def purge(cls):
        json_files = glob.glob("*.json")
        for file in json_files:
            if file not in cls.protected_files:
                os.remove(file)