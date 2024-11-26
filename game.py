from catalog import Catalog
from savedata.events.start import Start
from savedata.events.input import Input
from savedata.events.update import Update
from savedata.events.render import Render

Catalog.load()

running = True

Start.execute()

while running:
    Input.execute()
    Update.execute()
    Render.execute()


Catalog.save()