
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class LayoutWindow (Gtk.Window):
    def __init__ (self) -> None:
        super().__init__(title="Grid Layout")

        self.btns = [Gtk.Button(label=f"{i + 1}") for i in range(6)]

        self.grid = Gtk.Grid()
        self.grid.add(self.btns[0])
        self.grid.attach(self.btns[1], 1, 0, 2, 1)
        self.grid.attach_next_to(self.btns[2], self.btns[0], 3, 1, 2)
        self.grid.attach_next_to(self.btns[3], self.btns[2], 1, 2, 1)
        self.grid.attach(self.btns[4], 1, 2, 1, 1)
        self.grid.attach_next_to(self.btns[5], self.btns[4], 1, 1, 1)

        self.add(self.grid)

win = LayoutWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
