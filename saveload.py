import json, os, glob

"""#saves a dictionary to a save file with the specified name. Overwrites the file if it already exists
def save(data, file_name):
    with open(file_name + ".json", "w") as file:
        json.dump(data, file, indent=4)

#loads a save file with the specified name as a dictionary. Will return an error if the file doesn't exist
def load(file_name):
    with open(file_name + ".json", "r") as file:
        return json.load(file)

#deletes all save files in working directory. WARNING: There is no undoing this.
blacklist = ["config.json","Honri.json"]
def purge():
    json_files = glob.glob("*.json")
    for file in json_files:
        if file not in blacklist:
            os.remove(file)"""



class saveload:
    
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

    #protected files can't be deleted and won't be purged
    protected_files = []
    
    #adds a new protected file
    @classmethod
    def protectFile(cls, file_name):
        cls.protected_files.append(file_name)

    #deletes all save files in working directory. WARNING: There is no undoing this.
    def purge(self):
        json_files = glob.glob("*.json")
        for file in json_files:
            if file not in self.protected_files:
                os.remove(file)