import tkinter
import random
from functools import partial
from PIL import Image, ImageTk


InGame = False
StartingText = "Welcome to the Vending Machine! Click to begin!"
SelectText = "Select an item using the keypad"
VendingText = SelectText
ButtonChoice = []
ItemChoice = None


# to resize images if window resized (create copy for other images)
def resize_image(event):
    new_width = event.width
    new_height = event.height
    guy = copy_of_image.resize((new_width, new_height))
    thing = ImageTk.PhotoImage(guy)
    VendButton.config(image=thing)
    VendButton.image = thing


class GridManager:
    def __init__(self, Frame, colour="gray94"):
        self.Frame = Frame
        self.Colour = colour

    def set_grid(self, numofRows, numofColumns, borderwidth=0):
        self.numofRows = numofRows
        self.numofColumns = numofColumns
        self.borderwidth = borderwidth
        for i in range(numofRows):
            for j in range(numofColumns):
                canvas = tkinter.Canvas(self.Frame)
                # canvas.config(relief="raised", borderwidth=self.borderwidth)   #comment out to hide grid layout
                canvas.grid(row=i, column=j)
                canvas.config(background=self.Colour)
                self.Frame.columnconfigure(j, weight=1)
            self.Frame.rowconfigure(i, weight=1)


class Item:
    items = []

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.items.append(self)

    # def updateStock(self, stock):
    #    self.stock = stock

    def buyFromStock(self):
        if self.stock == 0:
            # raise not item exception
            pass
        self.stock -= 1


class VendingMachine:
    def __init__(self):
        self.amount = 0
        self.items = []
        self.couldshake = False

    def addItem(self, item):
        self.items.append(item)

    def showItems(self):
        # keep for debugging

        for item in self.items:
            if item.stock == 0:
                self.items.remove(item)
        for item in self.items:
            print(item.name, item.price)

    def addCash(self, money):
        self.amount = self.amount + money

    def buyItem(self, item):
        if self.amount < item.price:
            print('You can\'t buy this item. Insert more coins.')
        else:
            self.amount -= item.price
            item.buyFromStock()
            print('Cash remaining: ' + str(self.amount))

    def containsItem(self, wanted):
        ret = False
        for item in self.items:
            if item.name == wanted.lower():
                ret = True
                break
        return ret

    def getItem(self, wanted):
        ret = None
        for item in self.items:
            if item.name == wanted.lower():
                ret = item
                break
        return ret


    def insertAmountForItem(self, item):
        price = item.price
        line = "Insert ${0:.2f}: ".format(price)
        TestButton(line)

    def tooPoor(self, item):
        price = item.price
        if self.amount < price:
            return True

def vend():
    #machine = VendingMachine()
    item1 = Item('goldfish', 1.5, 3)
    item2 = Item('carrot', 1.75, 3)
    item3 = Item('tomatos', 2.0, 3)
    item4 = Item('spaghtie', 3.0, 3)
    item5 = Item('nasty flavor lays bag', 0.75, 3)
    item6 = Item('burger', 2.50, 3)
    item7 = Item('hot diggy dog', 0.75, 3)
    item8 = Item('semi alive chicken', 4.0, 3)
    item9 = Item('coka cola', 1.25, 3)
    item10 = Item('crunch bar', 1.0, 3)
    item11 = Item('almond hershey bar', 0.75, 3)
    item12 = Item('king size reeses', 2.25, 3)
    item13 = Item('weird yellow candy', 0.25, 3)
    item14 = Item('jelly beans', 0.50, 3)
    item15 = Item('king size hershey bar', 2.0, 3)
    item16 = Item('king size oreo', 2.25, 3)
    item17 = Item('skittles', 1.5, 3)
    item18 = Item('gummy worm', 1.25, 3)
    item19 = Item('red lolliepop', 0.50, 3)
    item20 = Item('cotton candy', 1.25, 3)
    item21 = Item('pringles', 1.75, 3)
    item22 = Item('cheetoes', 1.75, 3)
    item23 = Item('cheese', 1.50, 3)
    item24 = Item('pop tarts', 1.75, 3)

    for item in Item.items:
        machine.addItem(item)


def BigLoopTime():
    global ItemChoice
    global InGame
    global machine
    if InGame:
        if ItemChoice and not machine.couldshake:
            if machine.containsItem(ItemChoice):
                item = machine.getItem(ItemChoice)
                if machine.tooPoor(item):
                    machine.insertAmountForItem(item)
                else:
                    machine.buyItem(item)

                    if random.randint(0, 100) < 100:
                        TestButton('You did not get your item. '
                                        'Would you like to shake the vending machine? ')
                        machine.couldshake = True
                        # maybe yes no buttons, then logic to quit


                        # InGame = False
                        # hot mess express down below...
                        """
                                                else:
                                                    if random.randint(0, 100) < 50:

                                                        print('you died')
                                                        InGame = False

                                                    else:
                                                        a = input('would you like a refund? (y/n): ')
                                                        if a == 'n':
                                                            InGame = False

                                                        else:
                                                            a = random.randint(0, 100)
                                                            print("you got")
                                                            print((thing + a) * 0.01)
                        """

                    else:
                        # fix the print parts
                        TestButton('You got ' +item.name)
                        print('You got ' + item.name)
                        #a = input('buy something else? (y/n): ')
                        #if True:
                        #    InGame = False

                        #else:
                        #    pass
                        # ^^ changed 'continue' to 'pass' for now

            else:
                print('Item not available. Select another item.')
                #ItemChoice = None
                pass


    mainwindow.after(1000, BigLoopTime)


def StartGameButton():
    global InGame
    print('you hit the button!')
    vendingFrame.lower()
    InGame = True
    print(InGame)


# basic way to change the text displayed to user. pass w/e text is necessary as "words"
def TestButton(words):
    VendingText = words
    FootText.config(text=VendingText)


# gets the text put into the entry box (like input() method)
def get(event):
    def YesNoLogic():
        print('that\'s no float')
        if input.lower() == "cat":
            vendingFrame.lift()
        else:

          """  
        if input.lower() == "y":
            do yes stuff
            make list of "yes" and "no" for these checks
            """
    input = FootEntry.get()
    try:
        money = float(input)
        print('it a float')
        machine.addCash(money)

    except ValueError:
        YesNoLogic()
    FootEntry.delete(0, "end")
    # change the print line to something useful


# this will take the selected item and give it to the main loop to do stuff with
def ButtonSelect(selected):
    print(selected)
    print(ButtonChoice)
    ButtonChoice.append(selected)
    if selected == 1: Button1["state"] = "disabled"
    if selected == 2: Button2["state"] = "disabled"
    #continue for all keypad buttons


#clear selection and re enable all keypad buttons
def ClearSelection():
    global ButtonChoice
    ButtonChoice = []
    Button1["state"] = "normal"
    Button2["state"] = "normal"
    #continue for all keypad buttons


#checks what the selection is and does stuff based on that
def ButtonHitEnter():
    global ItemChoice
    global items
    if 1 in ButtonChoice:
        if 'A' in ButtonChoice:
            ItemChoice = "Cheese"
            print('you got cheese now')
            print(ItemChoice)
            machine.showItems()
    else:
        print('not no no')

        """
        elif 'B' in ButtonChoice:
        elif 'C' in ButtonChoice:
        elif 'D' in ButtonChoice:
    if '2' in ButtonChoice:
        if 'A' in ButtonChoice:
        elif 'B' in ButtonChoice:
        elif 'C' in ButtonChoice:
        elif 'D' in ButtonChoice:
        ClearSelection()
        """



mainwindow = tkinter.Tk()
#photo = PhotoImage(file=r"C:\Users\miche\PycharmProjects\Vending\images\icon.png")


mainwindow.title("Test")
mainwindow.geometry("640x704")
mainGrid = GridManager(mainwindow)
mainGrid.set_grid(10, 10)

image = Image.open('C://Users//miche//PycharmProjects//Vending//images//icon.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)

# test big picture state 1
vendingFrame = tkinter.Frame(mainwindow)
vendingFrame.grid(row=0, column=0, columnspan=10, rowspan=10, sticky='nsew')
vendingGrid = GridManager(vendingFrame, "black")
vendingGrid.set_grid(10, 10)

VendButton = tkinter.Button(vendingFrame, image=photo, command=StartGameButton)
VendButton.grid(row=1, column=0, columnspan=10, rowspan=9)
VendButton.bind('<Configure>', resize_image)

VendText = tkinter.Label(vendingFrame, text=StartingText, font=("Arial", 22))
VendText.grid(row=0, column=0, columnspan=10, sticky="nsew")

#stuff for state 2

header_Frame = tkinter.Frame(mainwindow)
header_Frame.grid(row=0, column=0, columnspan=10, sticky="nsew")
headerGrid = GridManager(header_Frame, "red")
headerGrid.set_grid(1, 10)

#Footer=Text Display and Entry frames

footerFrame = tkinter.Frame(mainwindow)
footerFrame.grid(row=8, rowspan=2, column=0, columnspan=10, sticky="nsew")
footerGrid = GridManager(footerFrame)
footerGrid.set_grid(numofRows=2, numofColumns=10, borderwidth=0)

FootText = tkinter.Label(footerFrame, text=VendingText, font=("Arial", 12))
FootText.grid(row=1, column=0, columnspan=10, sticky="new")

FootEntry = tkinter.Entry(footerFrame)
FootEntry.grid(row=1, column=4, columnspan=2, sticky='ew')
FootEntry.bind('<Return>', get)

rightFrame = tkinter.Frame(mainwindow)
rightFrame.grid(row=1, column=6, rowspan=6, columnspan=4, sticky="nsew")
rightGrid = GridManager(rightFrame, "blue")
rightGrid.set_grid(numofRows=6, numofColumns=4, borderwidth=0)

ButtonA = tkinter.Button(rightFrame, text="A", command=partial(ButtonSelect, "A"))
ButtonA.grid(row=0, column=0, sticky="nsew")

ButtonB = tkinter.Button(rightFrame, text="B", command=partial(ButtonSelect, "B"))
ButtonB.grid(row=0, column=1, sticky="nsew")

ButtonC = tkinter.Button(rightFrame, text="C", command=partial(ButtonSelect, "C"))
ButtonC.grid(row=0, column=2, sticky="nsew")

ButtonD = tkinter.Button(rightFrame, text="D", command=partial(ButtonSelect, "D"))
ButtonD.grid(row=0, column=3, sticky="nsew")

Button1 = tkinter.Button(rightFrame, text="1", command=partial(ButtonSelect, 1))
Button1.grid(row=1, column=0, sticky="nsew")

Button2 = tkinter.Button(rightFrame, text="2", command=partial(ButtonSelect, 2))
Button2.grid(row=1, column=1, sticky="nsew")

Button3 = tkinter.Button(rightFrame, text="3", command=partial(ButtonSelect, 3))
Button3.grid(row=1, column=2, sticky="nsew")

Button4 = tkinter.Button(rightFrame, text="4", command=partial(ButtonSelect, 4))
Button4.grid(row=2, column=0, sticky="nsew")

Button5 = tkinter.Button(rightFrame, text="5", command=partial(ButtonSelect, 5))
Button5.grid(row=2, column=1, sticky="nsew")

ButtonEnter = tkinter.Button(rightFrame, text="Enter", command=ButtonHitEnter)
ButtonEnter.grid(row=1, column=3, sticky="nsew")

ButtonClear = tkinter.Button(rightFrame, text="Clear", command=ClearSelection)
ButtonClear.grid(row=2, column=3, sticky="nsew")

# rightLabel = tkinter.Label(rightFrame, text='look what I can do')
# rightLabel.grid(row=0, column=1, rowspan=2, columnspan=3, sticky="nsew")


#rightEntry = tkinter.Entry(rightFrame)
#rightEntry.grid(row=0, column=1, columnspan=1)
#rightEntry.bind('<Return>', get)

leftFrame = tkinter.Frame(mainwindow)
leftFrame.grid(row=1, column=0, rowspan=6, columnspan=6, sticky="nsew")
leftGrid = GridManager(leftFrame, "yellow")
leftGrid.set_grid(numofRows=6, numofColumns=6, borderwidth=0)

#Bottom Frame full of buttons

BottomFrame = tkinter.Frame(mainwindow)
BottomFrame.grid(row=7, column=0, rowspan=2, columnspan=10, sticky="nsew")
BottomGrid = GridManager(BottomFrame, "black")
BottomGrid.set_grid(2,10)

#### use class to make buttons the lazy way!!!!

machine = VendingMachine()
if InGame is False:
    vendingFrame.lift()


vend()
BigLoopTime()
#mainwindow.after(0, BigLoopTime)
mainwindow.mainloop()
