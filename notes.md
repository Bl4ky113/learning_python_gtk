# Python with GTK 

Start: 13/06/2022
End: 26/07/2022

Sessions:
- 17/06/2022 12:49 | 14:48
- 19/06/2022 20:10 | 22:26
- 21/06/2022 21:28 | 22:02
- 23/06/2022 13:57 | 19:08
- 06/07/2022 16:16 | ...
- 07/07/2022 16:15 | ...
- 11/07/2022 19:48 | 21:50
- 12/07/2022 20:22 | 21:58
- 13/07/2022 14:53 | ...
- 17/07/2022 18:29 | 20:56
- 21/07/2022 13:22 | 15:30
- 22/07/2022 13:03 | 20:11
- 23/07/2022 16:28 | ...
- 25/07/2022 13:52 | 15:53
- 26/07/2022 13:56 | 14:29

src: https://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html
 
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
with the method require\_version("Gtk", "3.0"). Then we export Gtk from a submodule 
of gi.

Now we create a Gtk.Window Instance, and define that the quit btn of the window closes the program 
entirely and safely. We show the window, which has nothing. And start the main gtk loop.

## GTK Basics

GTK is GUI which needs an event driven programming model. It waits until a input or interruption 
ocurrs, then executes code as a response. 

### Callbacks
These responses are called CallBacks, we can make different 
functions in order to response to these callbacks by using:

handler\_id = widget.connect(event, callback, info=None)

we can use the handler\_id to disconect the callback to the event.
& if we somehow lost the h\_id, we can disconect it by the callback 
function name.

widget.disconect(handler\_id)
widget.disconect\_by\_func(callback)

info arg is just a way to pass any information or context to the callback

### Widgets
Widgets are intances of objects for the user to interact with.
Each object have different events, such as clicked on btns or typing on text inputs.
And different properties, these are the ones who can configure the widgets, by giving
them labels to display, some style properties and others.

### Widget Properties

We can set most of theses properties by giving them when we create the widget instance.
But if we need to set a property after the creation of the widget, we can use:
widget.props.property\_name = value # for setting and getting the value
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
box.pack\_start(widget, expand, fill, padding)
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
attach\_next\_to, it takes:
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

It's a container which only shows one of its children, generaly another container. We can 
change the shown children with a StackSwitcher, combining this two, we can recreate a 
menu navbar. We can customise the transition between the stack children with the method 
set\_transition\_type().
We can have multiple Stackwitches assiciated with one Stack.

To add contents to an stack, use method: add\_tilted(widget, "name widget", "label to show")
And we can set a Stack to a StackSwitcher using its method: set\_stack(stack\_widget)
It'll get the added children to the stack and show the labels of each one.

### Header Bar

Headers Bars aren't common layouts containers, but they are design for 
the header of the window. We can add general window header items, min,
max, close window btns, and general btns.

We should use Icons that GTK provides and use them as a image for our custom 
btns, in order to everything look nice and symetric.

### FlowBox

Flowbox behaves like the flex displays in the web, placing its children in rows from left
to right, and when there's no more space for the child, break the row and make another.
It's sorta flexible with the displays. Its children can be listed and sorted. You can add children
with add() method, although these children should be a FlowBoxChild, but if they aren't, they are going 
to get wrapped in a FlowBoxChild.

It has a bunch of properties which remind me of flexbox. And in order to grow normally vertically, 
it should be wrappend in a ScrolledWindow layout. Which isn't explained in the layout page.

### Notebook

Notebook works just like a stack layout, but using pages insted of stacks, doesn't use stackswitchers, 
but it can modify, and hide, the page selector.

## Labels in GTK

Are the main way to write non-editable text in our apps, we can declare it on the constructor 
or at any time with .set\_text(text) or .set\_markup(pango\_markups). We can make it selectable to 
the user by using .set\_selectable(). 
We can style the text if we use markups, or we can use differents properties and methods to style,
such as:
- set\_justify(): justify to left, right, center o fill.
- use\_underline: bool, to set it.
- set\_line\_wrap(): breaking the text if its widths is bigger than the widget's size. 
- set\_lime\_wrap\_mode(): A way to wrap the text, by using Pango.WrapModes
- set\_max\_width\_chars(num): Set the max width, in chars, of the label

When we use the mackup syntax, we are not using html5 markup, we are using pango markups, which are a 
series of tags to style the text, generaly pango uses spans with a bunch of properties to style the 
text, but it counts with the general \<b\>, \<i\>, and others.

Labels also can have a reference to press a key and do an action, called mnemonic. They 
show as a underlined, generaly, a letter to activate a widget. They can be set set\_text\_\_with\_mnemonic,
we also have to pass the content of the label with it, just like set\_text. 
These widgets generaly get assiciated with the widget which contains the label text, in case 
contary, we hace to use set\_mnemonic\_widget, and pass the widget to associate them with the label.

## Entries in GTK

Entries are a way for the users to enter data, using text inputs. This input can be set and get with
set/get\_text(). We can filter the data of the entry with some properties and methods, such as set\_max\_length()
or we can make it no/editable with set\_editable() or make invisible the content of the entry using set\_visibility()

Entries can also display progress such as a ProgressBar, using and seting the fractions of the progres, the steps of 
each pulse, and see the progress. It can be used to do different things other than just a progres bar

I can also use icons beside the entry to do different accions. And these can be styled with the icons of the icontheme.

## Buttons Widgets

Are widgets which the user use to set o turn a value on, off, set a value, etc. Is a semi restricted 
input, where the user can choose in a certian range of options.

### Simple or Just Button

Just a regular button where you pressit and sends a clicked event, use this to 
attach the button to an action. It can contain any other widget, generally icons or labels.

### Toggle Btn 

A Btn which looks like the last and normal one, but it remains presed or toggled.
We can se the status of the btn, as a bool, using get\_active(). Or change the status
with set\_active(). Whenever it's toggled, it sends a toggled signal. So we can 
add a function to it.

The event behaves just like a clicked event.

### Check Btn

It's an inherit from Toggle btn, the main change is that the status of the btn gets 
displayed as a checkbox.

### Radio Btn

It's an inherit from Toggle Btn, but these work in groups, also have a weird way to create themselfs and 
create groups. We can set their group when we create them or with join\_group(radiowidget).

- We can create them without a label with: new\_from\_widget(group)
- With a label with: new\_with\_label\_from\_widget(group)
- With a mnemonic label: new\_with\_mnemonic(group)

Each method takes a group to add the radio btn, it can be a RadioWidget Instance or None, when you want to 
add it to no group or if it's the first radio btn instance created.

Can be set or check activated with set/get\_activate()

### Link / HyperLink Btn

It's a btn which behaves like a link to the web. We can set/get the url with set/get\_uri().
We can create it with only the link or with a label:
- new(url)
- new\_with\_label(url, label)


### Spin Button

It's the best way to make a number input, it has two btns to increment or decrement the value. 
The main properties of the widget can se seted with Gtk.Adjustment. We can set the value to be an
int or a float. We can set how many decimals we want to se with set\_digits(). 

The input not only can get number, but strings on default, to avoid it we can use set\_numeric() to true.
We can set an update\_policy() so the value only updates if its valid.

We can get/set the data normaly with set/get\_value(), but we can also get\_value\_as\_int()
Also the widget has a value-changed event in order to check or trigger a function.

### Switch 

It's just like a Toggle Btn fork or inherit, but it recommends to use the event notiffy::active insted 
of active. Also it's displayed like a switch, the user can change the value by clicking the empty space 
or by draging the btn to the space.

## Expander

Expanders are a way to hide or compres our app hiding elements until the user clicks on the 
expander, and shows the widgets. It generaly can only contain one widget, but by using a 
box or anther layout, we can add many more.

## Progress Bar

Progress bars show us the status of completion of an action. If the program knows 
how long or much is it gonna take. We can use percentages, uptating the bar with 
set\_fraction(float from 0 to 1). 
Or if we dont know how long or much is it gonna take, we can use pulse() to update
the bar whenever it makes any progress. We can also change the size of these steps with
set\_pulse\_step

We can also modify the style of the progress bar adding some text and change the direction of 
the bar in percentage mode. Right to Left.

## Spiners 

They are a widget to show a indefinity activity, being a alternative to the progressbar. 
It can be started or stoped in basic functionality.
We can add a timeout function using GLi to the spiner, so the GTK loop will run a function 
until it returns False. Generaly this function will we a timer or the checker of a 
function.

## Tree and List Widgets

Tree Elements are ways to display data in a table format, without using grids. It's a bunch of 
widgets to do this layout. It has some nice features, such as:
- Update the layout if the data is added or removed
- Drag and Drop
- Sort and filter of data
- USe other widhgets such as inputs
- Styled columns

But this nice way to display data is rather complex when it comes to build and use it.

### Tree Model

Its the data that the treevies shows, it behaves like a table on a db, and it can be used in different ways
to display diferent columns of the main data. Just like a query with two different vies of the same data.

Generaly we store the data using Lists or Trees, lists just like lists and trees behaves like a table,
you can add data with a column header. When you create a Model you have to specify the type of data of each column.

We can add data to the models using append. For Lists we just send the data as a parameter, and for 
trees we can send the data as a parameter, and if we want a child row, we can send it like a iterable. The method will return a 
treeiter instance where we can get the data appended by using get\_iter in our model.

We can access the data of the treemodel by using the treeiter like a list: store[tree iter][column index]
As this behaves like a list, 2we can use splitters on the columns, and len().
And we can iterate through every row, of the top level, by using the model instance in a for. 
Being the top level rows the ones we normaly append in the lists but not he child ones in trees.
We have to use .foreach() in the tree models in order to iterate for every one, top and child.
For each is a high order function which returns the model instance, the tree path (looks like the path of the 
data in a document db), and the treeiter instance of the row.

We can get the path of a row by making a TreePath Instance and passing the number of the row 
as a parameter, and using the TreePath instance we can us it to get the treeiter instance of that 
row with model.get\_iter().

These TreePath Instances will look like "0" for lists and "0:12:123" for trees with depth, 
we can see the depth of the path by using len(path) and we can access the child index by accessing the 
level of depth like a list path[level].

### Tree View

Now that we have the data on the treemodel, we can display it with a TreeView,
we just add it to the treeview by passing it as a karg model=my\_model,
but we have to display it using columns and these must use cell renders. 
WE can use a render for a toggle, images & icons or text. And we can create our
own using the CellRender Class using the properties of GObject.Property().

We are going to create a instance of this render and pass it as a argument, cell\_render or 2 property if positional,
to a TreeViewColumn instance. Which can have a title or a header for the column. The columns has more properties 
but the guide doesnt say which ones. 
We can add multiple model data to a column we can use pack\_start() and add the data with add\_atribute()

Then we can add the column to the tree view using add\_column().

### Tree Select 

We can use the selection of an user by making a instance of the method of the treeview.
With this we can connect the "changed" event. this will return the selected rows, if 
he multiple option is on, so we can use get\_selected/selected\_rows().

### Tree Sorting

We can sort the models on a treeview by setting a column to sort the rows, 
this is done by passing the index of the column in the view to the method set\_sort\_column
of the column. Generaly an 0.

We can create our own sort function and use it with set\_sort\_funct()

### Tree Filtering

We can filter the treemodel data by using filters with
model.filter\_new() making a filter instance, and we can add 
more filters to these ones. And filter it by a filter\_function seted with 
set\_visible\_func on the filter obj.

### Subtract

In order to understand everything:

TreeViews a series of objs that let us create a table to display data, 
this data is from a TreeModel, in order to append data to the model we have to 
declate the type of data that it will store, this could be done on a List or Tree Model,
it will add a level of depth. To access any data we have to use & get a treeiter instance of 
the data, which will be obtainable while we add the data, & with a treepath.
Which can be use by many TreeViews, and can be filtered by a TreeFilter. This information will be displayed using a CellRender, 
having different ones for different data, on a TreeViewColumn, which will have an
index, and title. The data on the TreeView can be sorted using a column of reference, be providing the index of it. 
And the data can be selectable by the user, sigle row or a group of rows. Triggering an event in the process.

## Cell Renders 

Cell Renders are a way to display data on TreeViews and ComboBox, theres a bunch of types,
and many of them have events, these will return the widget, the path of the cell and other stuff.

### CellR. Text

Display text with its given properties. We can change them with set\_property(), one of them 
is editable, when its on true, we can edit the text of the cell. We can an edited event to the 
render cell if we make it editable. Generally this envent will change the content of the Cell, which 
doesn't do by default.

### CellR. Toggle

Displays the value of an Checkbox, or radio btn, we can add a toggled event to the cell.
And we can make the toggle a radio btn by using the set\_radio(True) method, but this will not make the 
radio btns act as a group, they will allow more than one radio btn on true.

### CellR. PixBuf

Displays a given image, generally an GTK icon. 

### CellR. Combo

Display a text input with a list of options to choose from, these must be a treemodel, and defined setting the property model.
Other than that, it is almost equal to the Cellrender text.

### CellR. ProgressBar

Displays a number as a % of a progress bar. You can make it a percentage progress bar or a active bar.

### CellR. Spiner

Displays a normal text, but its also a number spinner, just like the input.

## ComboBox

Combox are ways to display a list of options for the user to choose from. It's better than a 
large number of radio btns. 

It uses a datamodel, just like treeview, as values, it can have a bunch of subvalues, such as
IDs, and others, we can change the entry text with set\_entry\_text\_column(column\_id). But we can let 
the user enter a value by providing an enter by making a entry with new\_with\_model\_and\_entry(model\_data)

We can connect the widget to the changed event, although with the enter it'll trigger 
whenever you change the text. You can set the max width of the text with set\_wrap\_width(), 
and add a default value with set\_active(row\_index), this will trigger the changed event 
when the program starts or the widget gets shown.

## IconView

IconView is a way to diplay pixbuf icons in a grid view, these can support 
drag and drop, multiple selections, and item reordering. It uses a ListStore to 
store the icons, it requires to atleast have one column with a pixbuf obj.

We can set the multiple selection with set\_selection\_mode(), just like the TreeViews.

And in the model we add another columns, such as names of the icon and others, we can 
use the set\_pixbuf/text\_column(column\_id).

## Mutline Text Editor

TextView is an object that let us see large cuantities of formated text. And also can be used to 
edit this large text, just like a text editor. It uses a TextBuffer Model for the text, just like 
the tree view.

### TextView

It desplays a textbuffer info, we can get this buffer with get\_buffer(). 
The editable mode can be setted with set\_editable(), and we can make visible the 
text cursor with set\_cursor\_available(). 

We can add justification to the text with set\_justification(GTK.justification). 
The normal ones for text. And we can make a text wrap of the screen is to small with
set\_wrap\_mode().

### TextBuffer

The textbuffer is the model for the textview, we can set or get the text with get/set\_text()

We can use TextIterators to get a reference of a space between to chars, generaly words. But these
changes anytime the text does. So we can peserve the position of those chars with a TextMark, this 
mark is where the the cursor is located on the text or a selection of this. We can get the content 
of these with get\_insert()/selection\_bound(). It isn't visible by default, but we can do it by using 
set\_visible().

We can get the starting Textiter and the last one by using get\_start/end\_iter().

We can also add text on a specific text iter with insert(), or add text where the cursor is with insert\_at\_cursor().
If we want to delete the space between to iters with delete().

We can use a method to search on the text a match of a given text. It uses the start or end textiters, 
using foward/barckward\_search()

### TextTags

We can use tags to change the text format on the space of two text\_iters, adding efects such as: 
- background;
- foreground
- underline
- bold
- italics
- striketrough
- justification
- size
- text wrapping 

Add them to a text buffer by using apply\_tag() & create\_tag(), and remove them with remove\_tag() or remove\_all\_tags()

## Dialogs 

Dialogs are a type of window, which behaves just like the main window. But are used for showing or getting info from/to 
the user. Just like messages, yes or no dialogs, or choosing a file. WE can also create or own dialog to contain 
anything, just like a normal window.

### DIY Dialog

We can create our own dialog by making a inherit from GTK.Dialog, this will take self, and the parent window.

The window will only have a box layout, and it has to be accesed by using get\_content\_area(). There we can add 
any widget. But if we want to use the btns of the right or left corner, we can use add\_button and 
pass as arguments the btn, and then the response of the btn. 

We can make our dialog to freeze or stop the rest of the windows, for a login as an example. by passing the 
flag MODAL on the constructor or using set\_modal().

We can also make our code wait until the dialog sends a response by getting the response of the dialog by 
running the dialog with run(). Stoping the wait until the response is retruned.

The dialog can be removed with hide(), which removes the dialog, but keeps it stored in memory if we need it 
after. And destroy() which removes the dialog from the user view and memory, if we need it again it has to load 
everything again.

### Message Dialog

This is a inherit of Dialog pre made to display simple messages with, or without, btns. Theres 
different types of messages, warning, error, info, questions, etc. We can display a simple text, 
a seccondary text if needed and icons. Most of the content will be passed in the constructor, but for the 
secondary text we have to use format\_secondary\_text(), which will apear with a different style to the 
main text.

### FileChooser Dialog

Can open files or folders, or save files with/out a different name. When the user sends the response 
we can access the file or folder with get\_filename, or the uri with get\_uri. We can select multiple 
files by using set\_select\_multiple(), and get their data by adding a s to the get methods from before.

There's a buch of options to choose, such as:
- set\_local\_only(): can only use local files
- show\_hidden(): shows hidden files
- set\_do\_overwrite\_confirmation(): send a confirmation dialog whenever the user saves a file that already exists.

We can add filters with add\_filter() to the dialog to show only a type of the files.

## Pop overs 

Popovers are a way to display a semi dropmenu, or just simple information.
We can add widgets to them by using add(), generaly layout widgets in order to 
display more than one. They can be used by passing popover=the\_pop\_over as a karg 
on the constructor of a menu btn.

We can create popovers using XML tags in a string, using a builder to build it from the xml string, 
and then pass the menu to the menubtn constructor as a menu\_model karg. Weird.

## Clipboard

We can create a clipboard instance to use and get the content of our clipboard. It works with text and 
images. 
- For text 
	we can copy with set\_text(text, -1); wait or check if we have a current text copied with wait\_for\_text();
	this wait will return the text to paste and use it.
- For Images
	copy with set\_image(pixbuf); wait & check wait\_for\_image(), wait will return the image to paste and use.
We can see the type of storage of an element using get\_storage\_type()

## Drag and Drop

Drag and drop is a way to use some elements, generally icons from icon view. 
These work with a source with elements to drag, and a destination where the elements are going to get draged.
In the source widget we have to enable\_model\_drag\_source() and connect it to some events:
- drag-begin: user stars drag
- drag-data-get: pass data to the destination
- drag-data-delete: delete the element on the source when the drag is done
- drag-end: the drag ends.

In the destination widget we have to drag\_dest\_set() and connect it to some events:
- drag-motion: the source moves into the destination
- drag-drop: the source is droped in the destination
- drag-data-recived: the destination gets the data of the source

Theres a bunch of details on the get and pass data of the elements, but i dont want to write them down.

## Builder & Glade

The GTK Builder is a way to make our proyect with GTK without writing almost any line of code, 
by generating the stucture of the app by using a GTK XML template. In this templates we can add 
the elements as tags with its properties, signals and others. We can also add them in a 
child order. We can get the elements by adding them an id and using it in get\_object(id).

We can add signals with the signals tag, and in these tags we have to add a handler 
property, which is going to be the name of the function where we are going to handle the 
event. 
We can pass a dict with the key as the handler name, and the value as a function name in our code. 
Or we can create a class with the handlers functions.
Passing the handlers with connect\_signals()

We can also use templates and use a decorator to use an class obj to a part of that template.
Using this obj we can add the handlers with some decorators.

## Objects

The base of the GTK objects is the GObject.GObject. Where we can create our own object if we use as inheritance.
We have to init with the \_\_init\_\_ GObject's method, on the \_\_init\_\_ of the class.

We can add signals by adding them to the dict \_\_gsignals\_\_, where the key is the name of the 
signal, the value is a tuple with the way to invoke a handler for the signal, the return of the signal handler, 
and the args of the signal handler.
We can emit this signals by using emit(name, \*args)

We can add new properties by making them as a normal property with the GObject.Property class.
They can have a type, default, flags for read write. We can make properties by using the 
decorator @GObject.Property on a method, works just like the @property decorator, we can 
make a readonly or with write.
We can use the dict \_\_gproperties\_\_ to set the property data (type, nickname, blurb, min-val, max-val, default-val, flag)
But the properties defined in this dict have to be handled in do\_get/set\_property(self, prop).
We can see if a property is changed by connecting a signal to it, with notify::"property".

## Aplication

Aplications with GTK must e able to handle multiple instances, tasks and repetitive tasks.
We can make an apliation with Gtk.Application. We have to pass on the super\_\_init\_\_ the args and kargs of
the app, and then some of our own, such as:
- app\_id
- flags: for usage mostly

We can state what can our app do with defining the actions with Gio.Actions. These can be turned on or off, 
and are a nice way to include some actions menu to the desktop enviroment.

Sincerly, i didn't understand anythind. I'll read the code. Semi understandment

Actions and SimpleActions are the listed options on the window menu. 

The best thing that i can do is read tbe gnome guide of how to do an app with GTK.

### Aplication - GNOME How To Do

An Aplication is the base of the Gtk Program, in order to separate it from main(). 
This allows Gtk to only change and function when its needed. 

Theres a bunch of functions that the app needs for some events: 
- startup : app starts
- shutdown : app closes
- activate : normally launch the app
- open : open a file with the app

We need to avoid using main() on our code, if we need to init something we should use 
startup and not anything else.

Thats it.
