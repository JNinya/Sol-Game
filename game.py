from catalog import Catalog
from savedata.events.wormhole import Wormhole

Catalog.load()

location = Catalog.find('Earth')
destination = Catalog.find('Luna')

Wormhole.execute(location, destination)


search_dict = {
    'type':'Character'
}

results = Catalog.search(search_dict)

for item in results:
    print(item.location)

Catalog.save()