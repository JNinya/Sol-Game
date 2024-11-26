from catalog import Catalog

Catalog.load()

name = input("What is your name?\n")

me = Catalog.find(name)

print(f"Welcome back {me.name}")
print(f"You are currently at {me.location}")






#--------------------------------
Catalog.save()