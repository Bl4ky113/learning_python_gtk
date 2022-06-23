# Python with GTK 

Start: 13/06/2022
End: 

Sessions:
- 17/06/2022 12:49 | 14:48
- 19/06/2022 20:10 | 22:26
- 21/06/2022 21:28 | 22:02
 
## Install GTK in Python

We need to download PyGObject, which is the one who lets us access 
the GTK modules written in C.

Process:
1. Install with pacman / any other pkmanager:
	- python
	- python-object
	- cairo
	- pkgconf
	- goobject-instrospection
	- go
	- gtk3
2. Create a venv or use gtk globally
3. Install with pip:
	- pycairo
	- PyGObject
4. Ready to use

It may change depending the packet manager, but looks like it dowloads
the same things with different syntaxis.

### Other way around

There's a way to download, install and build PyGObject using something called:
jhbuild, I couldn't download & install it in my machine. But it says that it's 
the easiest way to do it.

## Hello World!!!

We're going to import the module gi and we should assure that we are using gtk 3.0
with the method require_version("Gtk", "3.0"). Then we export Gtk from a submodule 
of gi.

Now we create a Gtk.Window Instance, and define that the quit btn of the window closes the program 
entirely and safely. We show the window, which has nothing. And start the main gtk loop.

## GTK Basics

GTK is GUI which needs an event driven programming model. It waits until a input or interruption 
ocurrs, then executes code as a responce. 

### Callbacks
These responces are called CallBacks, we can make different 
functions in order to responce to these callbacks by using:

handler_id = widget.connect(event, callback, info=None)

we can use the handler_id to disconect the callback to the event.
& if we somehow lost the h_id, we can disconect it by the callback 
function name.

widget.disconect(handler_id)
widget.disconect_by_func(callback)

info arg is just a way to pass any information or context to the callback

### Widgets
Widgets are intances of objects for the user to interact with.
Each object have different events, such as clicked on btns or typing on text inputs.
And different properties, these are the ones who can configure the widgets, by giving
them labels to display, some style properties and others.

### Widget Properties

We can set most of theses properties by giving them when we create the widget instance.
But if we need to set a property after the creation of the widget, we can use:
widget.props.property_name = value # for setting and getting the value
Avoiding the Setting and Getting functions.

If we want to see which properties does any widget have, we can use the builtin function dir()

### Destroy Window, and Gtk loop.

When we destroy, quit or close the top level, or main window, the program should stop. 
As this isn't include in Gtk by deafult, we have to declare by doing a main loop quit 
whenever the top-level gets destroyed.

If we don't do this, Gtk will still be running even if we close all the program windows.
We can close it in the terminal o killing it with its process id.

## Strings, Python 3.x and GTK

The strings shown in GTK are encoded, generaly or from default in ASCII, so we should 
encode our strings when we are passing them to a GTK object, or decode when GTK object 
returns a string. 

But PyGObject helps us by enconding or decoding whenever we pass or return a string.

## Widget Gallery 

GTK counts with many widgets, some of them are entire windows, such as about dialog, file chooser and others.
It also counts with widgets to organice other contents or widgets, such as frame and grid.
A good bunch of user inputs. Working as a Layout.
Many widgets centered around UI such as scroll bars, separators, stacks with its switches.

## Layout Widgets

GTK is dyanic when it comes to laying out the content of the app. We can use a bunch of 
diferent layout containers. These are:

### Grid
They can be displayed in horizontal o vertical layout, which will determine the 
order of the widgets, left to right and top to bottom for each one. 
The Placement of the objs, with the given parameters, will strech and fit the size of 
the window.
Create a instance with:
box = GTK.Box()
Add the box to a window:
window.add(box)
Add content to the box by using pack start (left or top) or pack end (right or bottom)
box.pack_start(widget, expand, fill, padding)
Start the window, and the box with the btns will apear. 

### Grid
With Gird Layouts you can place widgets a normal way or place them using themselfs.
It works in rows and columns, each one has a number, starting in 0 and incrementing going
left to right (for columns) and top to bottom (for rows). 
On default the widgets wont strech and fit the size of the window. Nor the columns or 
rows will fit the screen.

We can add widgets with attach(). It takes:
- the widget
- left: the column number where the widget will be attach
- top: the row number where ... 
- width: span of columns that the widget will take
- height: span of rows ...

Or we can attach them with another widget, silbling, using
attach_next_to, it takes:
- the widget
- the silbling
- the side of the silbling where the widget will attach
- width: span of columns that the widget will take
- height: span of columns that the widget will take

These two are the most basic layout widgets, the other ones are more functional and especific.

## Functional Layout Widgets

### ListBox

ListBox is a layout which only accepts child ListBoxRows objects, these rows can be sorted, filtered, 
added, deleted, selected and navigated by using a mouse or a keyboard.
Altough it only takes ListBoxRows, ListBoxRows can contain any widget.
It is a replacement or an alternative to TreeViews, which are like tables.

### Stack
