
import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class LayoutWindow (Gtk.Window):
    def __init__ (self) -> None:
        super().__init__(title="Layout Box")

        self.box:Gtk.Box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.btn_1:Gtk.Button = Gtk.Button(label="Hello")
        self.btn_1.connect("clicked", self.btn_1_clicked)
        self.box.pack_start(self.btn_1, True, True, 0)

        self.btn_2:Gtk.Button = Gtk.Button(label="Goodbye")
        self.btn_2.connect("clicked", self.btn_2_clicked)
        self.box.pack_start(self.btn_2, True, True, 0)

    def btn_1_clicked (self, widget:Gtk.Button) -> None:
        print("Hello World")

    def btn_2_clicked (self, widget:Gtk.Button) -> None:
        print("Good Bye World")

window = LayoutWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
