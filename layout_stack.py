
import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class LayoutWindow (Gtk.Window):
    def __init__ (self) -> None:
        super().__init__(title="Layout Stack")
        self.props.border_width = 10
        
        base = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.add(base)

        stack = Gtk.Stack()

        btn_1 = Gtk.Button(label="Don't Click Me")
        stack.add_titled(btn_1, "btn 1", "Click Him")
        btn_2 = Gtk.Button(label="Click Me")
        stack.add_titled(btn_2, "btn 2", "Don't Click Him")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

        base.pack_start(stack_switcher, True, True, 10)
        base.pack_start(stack, True, True, 0)

win = LayoutWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
