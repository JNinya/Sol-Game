from catalog import Catalog

Catalog.load()

name = input("What is your name?\n")

me = Catalog.find(name)

print("Welcome back " + me.name)
print("Here is your secret data:")
print(me.dict)

#Catalog.save()