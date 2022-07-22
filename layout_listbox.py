
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ListBoxRow (Gtk.ListBoxRow):
    def __init__ (self, data):
        super().__init__()
        self.data = data
        self.add(Gtk.Label(label=data))

class LayoutWindow (Gtk.Window):
    def __init__ (self):
        super().__init__()
        self.props.border_width = 10

        listbox = Gtk.ListBox()
        items = [i + 1 for i in range(10)]
    
        for item in items:
            listbox.add(ListBoxRow(item))

        listbox.connect("row_activated", self.row_activated)

        self.add(listbox)
        listbox.show_all()

    def row_activated (self, widget, row):
        print(row.data)

win = LayoutWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
