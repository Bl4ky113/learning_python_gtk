# Python with GTK 

Start: 13/06/2022
End: 

Sessions:
- 17/06/2022 12:49 | 14:48
 
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

### Destroy Window, and Gtk loop.

When we destroy, quit or close the top level, or main window, the program should stop. 
As this isn't include in Gtk by deafult, we have to declare by doing a main loop quit 
whenever the top-level gets destroyed.

If we don't do this, Gtk will still be running even if we close all the program windows.
We can close it in the terminal o killing it with its process id.

We can set most of theses properties by giving them when we create the widget instance.
But if we need to set a property after the creation of the widget, we can use:
widget.props.property_name = value # for setting and getting the value
Avoiding the Setting and Getting functions.

If we want to see which properties does any widget have, we can use the builtin function dir()
