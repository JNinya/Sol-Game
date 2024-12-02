from util.catalog import Catalog
from gui.gui import Gui
from gameloop.start import Start
from gameloop.input import Input
from gameloop.update import Update
from gameloop.render import Render

#initalize everything
Catalog.load()

Gui.init()

#Start.execute()

while Gui.running:
    Input.execute()
    Update.execute()
    Render.execute()


Catalog.save()