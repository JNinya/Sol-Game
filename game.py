from catalog import Catalog

Catalog.load()

aidan = Catalog.find('aidan')

aidan.origin = "Earth"

Catalog.save()