
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow (Gtk.Window):
    def __init__ (self) -> None:
        super().__init__(title="Hello World")

        self.button:Gtk.Button = Gtk.Button(label="click here")
        self.button.connect("clicked", self.on_btn_clicked)
        self.add(self.button)

    def on_btn_clicked (self, widget) -> None:
        print("Hello World")
        print(widget)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
