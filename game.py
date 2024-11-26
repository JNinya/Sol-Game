from util.catalog import Catalog
from util.gameloop.start import Start
from util.gameloop.input import Input
from util.gameloop.update import Update
from util.gameloop.render import Render

Catalog.load()

Start.execute()

while Start.running:
    Input.execute()
    Update.execute()
    Render.execute()


Catalog.save()