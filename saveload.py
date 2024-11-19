import json, os, glob

#saves a dictionary to a save file with the specified name
def save(data, file_name):
    with open(file_name + ".json", "w") as file:
        json.dump(data, file, indent=4)

#loads a save file with the specified name as a dictionary
def load(file_name):
    with open(file_name + ".json", "r") as file:
        return json.load(file)

#deletes all save files in working directory. WARNING: There is no undoing this.
def purge():
    json_files = glob.glob("*.json")
    for file in json_files:
        os.remove(file)