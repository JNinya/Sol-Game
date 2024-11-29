from util.catalog import Catalog
from gui import gui
from gameloop.start import Start
from gameloop.input import Input
from gameloop.update import Update
from gameloop.render import Render

Catalog.load()

Start.execute()

while Start.running:
    Input.execute()
    Update.execute()
    Render.execute()


Catalog.save()