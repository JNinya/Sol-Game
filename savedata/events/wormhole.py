from gameobjects.event import Event
from catalog import Catalog

class Wormhole(Event):
    
    #take all characters at location and move them to destination
    def execute(location, destination):
        
        search_dict = {
        'type':'Character',
        'location':location.name
        }

        results = Catalog.search(search_dict)

        for item in results:
            item.travel(destination)