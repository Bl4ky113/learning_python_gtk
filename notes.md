# Python with GTK 

Start: 13/06/2022
End: 

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
- 22/07/2022 13:03 | 
 
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

It's a container which only shows one of its children, generaly another container. We can 
change the shown children with a StackSwitcher, combining this two, we can recreate a 
menu navbar. We can customise the transition between the stack children with the method 
set_transition_type().
We can have multiple Stackwitches assiciated with one Stack.

To add contents to an stack, use method: add_tilted(widget, "name widget", "label to show")
And we can set a Stack to a StackSwitcher using its method: set_stack(stack_widget)
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
or at any time with .set_text(text) or .set_markup(pango_markups). We can make it selectable to 
the user by using .set_selectable(). 
We can style the text if we use markups, or we can use differents properties and methods to style,
such as:
- set_justify(): justify to left, right, center o fill.
- use_underline: bool, to set it.
- set_line_wrap(): breaking the text if its widths is bigger than the widget's size. 
- set_lime_wrap_mode(): A way to wrap the text, by using Pango.WrapModes
- set_max_width_chars(num): Set the max width, in chars, of the label

When we use the mackup syntax, we are not using html5 markup, we are using pango markups, which are a 
series of tags to style the text, generaly pango uses spans with a bunch of properties to style the 
text, but it counts with the general \<b\>, \<i\>, and others.

Labels also can have a reference to press a key and do an action, called mnemonic. They 
show as a underlined, generaly, a letter to activate a widget. They can be set set_text__with_mnemonic,
we also have to pass the content of the label with it, just like set_text. 
These widgets generaly get assiciated with the widget which contains the label text, in case 
contary, we hace to use set_mnemonic_widget, and pass the widget to associate them with the label.

## Entries in GTK

Entries are a way for the users to enter data, using text inputs. This input can be set and get with
set/get_text(). We can filter the data of the entry with some properties and methods, such as set_max_length()
or we can make it no/editable with set_editable() or make invisible the content of the entry using set_visibility()

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
We can se the status of the btn, as a bool, using get_active(). Or change the status
with set_active(). Whenever it's toggled, it sends a toggled signal. So we can 
add a function to it.

The event behaves just like a clicked event.

### Check Btn

It's an inherit from Toggle btn, the main change is that the status of the btn gets 
displayed as a checkbox.

### Radio Btn

It's an inherit from Toggle Btn, but these work in groups, also have a weird way to create themselfs and 
create groups. We can set their group when we create them or with join_group(radiowidget).

- We can create them without a label with: new_from_widget(group)
- With a label with: new_with_label_from_widget(group)
- With a mnemonic label: new_with_mnemonic(group)

Each method takes a group to add the radio btn, it can be a RadioWidget Instance or None, when you want to 
add it to no group or if it's the first radio btn instance created.

Can be set or check activated with set/get_activate()

### Link / HyperLink Btn

It's a btn which behaves like a link to the web. We can set/get the url with set/get_uri().
We can create it with only the link or with a label:
- new(url)
- new_with_label(url, label)


### Spin Button

It's the best way to make a number input, it has two btns to increment or decrement the value. 
The main properties of the widget can se seted with Gtk.Adjustment. We can set the value to be an
int or a float. We can set how many decimals we want to se with set_digits(). 

The input not only can get number, but strings on default, to avoid it we can use set_numeric() to true.
We can set an update_policy() so the value only updates if its valid.

We can get/set the data normaly with set/get_value(), but we can also get_value_as_int()
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
set_fraction(float from 0 to 1). 
Or if we dont know how long or much is it gonna take, we can use pulse() to update
the bar whenever it makes any progress. We can also change the size of these steps with
set_pulse_step

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
treeiter instance where we can get the data appended by using get_iter in our model.

We can access the data of the treemodel by using the treeiter like a list: store[tree iter][column index]
As this behaves like a list, 2we can use splitters on the columns, and len().
And we can iterate through every row, of the top level, by using the model instance in a for. 
Being the top level rows the ones we normaly append in the lists but not he child ones in trees.
We have to use .foreach() in the tree models in order to iterate for every one, top and child.
For each is a high order function which returns the model instance, the tree path (looks like the path of the 
data in a document db), and the treeiter instance of the row.

We can get the path of a row by making a TreePath Instance and passing the number of the row 
as a parameter, and using the TreePath instance we can us it to get the treeiter instance of that 
row with model.get_iter().

These TreePath Instances will look like "0" for lists and "0:12:123" for trees with depth, 
we can see the depth of the path by using len(path) and we can access the child index by accessing the 
level of depth like a list path[level].

### Tree View

Now that we have the data on the treemodel, we can display it with a TreeView,
we just add it to the treeview by passing it as a karg model=my_model,
but we have to display it using columns and these must use cell renders. 
WE can use a render for a toggle, images & icons or text. And we can create our
own using the CellRender Class using the properties of GObject.Property().

We are going to create a instance of this render and pass it as a argument, cell_render or 2 property if positional,
to a TreeViewColumn instance. Which can have a title or a header for the column. The columns has more properties 
but the guide doesnt say which ones. 
We can add multiple model data to a column we can use pack_start() and add the data with add_atribute()

Then we can add the column to the tree view using add_column().

### Tree Select 

We can use the selection of an user by making a instance of the method of the treeview.
With this we can connect the "changed" event. this will return the selected rows, if 
he multiple option is on, so we can use get_selected/selected_rows().

### Tree Sorting

We can sort the models on a treeview by setting a column to sort the rows, 
this is done by passing the index of the column in the view to the method set_sort_column
of the column. Generaly an 0.

We can create our own sort function and use it with set_sort_funct()

### Tree Filtering

We can filter the treemodel data by using filters with
model.filter_new() making a filter instance, and we can add 
more filters to these ones. And filter it by a filter_function seted with 
set_visible_func on the filter obj.

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

Display text with its given properties. We can change them with set_property(), one of them 
is editable, when its on true, we can edit the text of the cell. We can an edited event to the 
render cell if we make it editable. Generally this envent will change the content of the Cell, which 
doesn't do by default.

### CellR. Toggle

Displays the value of an Checkbox, or radio btn, we can add a toggled event to the cell.
And we can make the toggle a radio btn by using the set_radio(True) method, but this will not make the 
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
IDs, and others, we can change the entry text with set_entry_text_column(column_id). But we can let 
the user enter a value by providing an enter by making a entry with new_with_model_and_entry(model_data)

We can connect the widget to the changed event, although with the enter it'll trigger 
whenever you change the text. You can set the max width of the text with set_wrap_width(), 
and add a default value with set_active(row_index), this will trigger the changed event 
when the program starts or the widget gets shown.

## IconView

IconView is a way to diplay pixbuf icons in a grid view, these can support 
drag and drop, multiple selections, and item reordering. It uses a ListStore to 
store the icons, it requires to atleast have one column with a pixbuf obj.

We can set the multiple selection with set_selection_mode(), just like the TreeViews.

And in the model we add another columns, such as names of the icon and others, we can 
use the set_pixbuf/text_column(column_id).
