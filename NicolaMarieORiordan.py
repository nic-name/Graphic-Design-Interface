from tkinter import *
from tkinter.ttk import *
from turtlefigure import *

#Uncomment for debugging
#print("I'm the first line!")

# contruct the Tk window
root = Tk()
root.geometry("320x300+300+300")
root.title("Turtle Interface")

# define handlers
def OnClear():
    #clear the entry-s
    angleInt.set(0)
    lengthInt.set(0)    
#end onClear

def OnNew():
    clear()
#end onNew


#define the figure execution functions
def executeSpiro(length, angle):
    spiro = spirograph(length, angle)
    spiro.drawSpiroGraph()
#end executeSpiro

def executeBinaryTree(length, angle):
    tree = binarytree()
    tree.drawBinaryTree(length, angle)
#end executeTree

def executeSpike(length, angle):
    s = spike()
    s.drawSpike(length, angle)
#end executeTree

def executeFernTree(length, angle):
    fern = fernTree()
    fern.drawFern(length, angle)
#end executeTree

def executeSnowFlake(length, angle):
    flake = snowFlake()
    flake.drawFlake(length, angle)
#end executeTree

def executeAntiSnowFlake(length, angle):
    antiFlake = antiSnowFlake()
    antiFlake.drawAntiFlake(length, angle)
#end executeAntiSnowFlake

def executeCircleCeption(length, angle):
    circleC = circleCeption()
    circleC.drawCircleCeption(length, angle)
#end executeCircleCeption

def executeTriangleFractal(length, angle):
    triangle = triangleFractal()
    triangle.drawTriangle(length, angle)
#end executeTriangleFractal

def executePolySpiral(length, angle):
    poly = polySpiral()
    poly.drawPolySpiral(length, angle)
#end executePolySpiral

def executeJaggedEdge(length, angle):
    jagged = jaggedEdge()
    jagged.drawJaggedEdge(length, angle)
#end executeJaggedEdge

def OnDraw():
    
    length = lengthInt.get()
    angle = angleInt.get()
    print (length, angle)
    
    selectionList = listbox.curselection()
    if selectionList.__len__() == 0:
        print ("Nothing selected") 
        
    elif selectionList[0] == 0:
        #uncomment for debugging
        #print ("executeSpiro is selected")
        executeSpiro(length, angle)
        
    elif selectionList[0] == 1:
        #uncomment for debugging
        #print("binaryTree is selected")
        executeBinaryTree(length, angle)

    elif selectionList[0]==2:
        #uncomment for debugging
        #print("spike is selected")
        executeSpike(length, angle)

    elif selectionList[0]==3:
        #uncomment for debugging
        #print("Fern tree is selected")
        executeFernTree(length, angle)

    elif selectionList[0]==4:
        #uncomment for debugging
        #print("Snowflake is selected")
        executeSnowFlake(length, angle)

    elif selectionList[0]==5:
        #uncomment for debugging
        #print("AntiSnowflake is selected")
        executeAntiSnowflake(length, angle)

    elif selectionList[0]==6:
        #uncomment for debugging
        #print("ExecuteCircleCeption is selected")
        executeCircleCeption(length,angle)

    elif selectionList[0]==7:
        #uncomment for debugging
        #print("ExecuteTriangleFractal is selected")
        executeTriangleFractal(length, angle)

    elif selectionList[0]==8:
        #uncomment for debugging
        #print("ExecutePolySpiral is selected")
        executePolySpiral(length, angle)

    elif selectionList[0]==9:
        #uncomment for debugging
        #print("ExecuteJaggedEdge is selected")
        executeJaggedEdge(length, angle)        
        
    else:
        print("Unknown error has occurred")
        
    #end if
#end onDraw

def updateDescriptionLabel(evt):
    w = evt.widget
    index = int(w.curselection()[0])
        
    if index == 0:
        DescriptionText.set("Draws swirls of quadrilateral shapes")
        
    elif index == 1:
        DescriptionText.set("Uses recursion to draw binary trees")

    elif index==2:
        DescriptionText.set("Draws a swirl of lines and spikes")

    elif index==3:
        DescriptionText.set("Draws an image of a fern tree")

    elif index==4:
        DescriptionText.set("Uses the koch curve to draw a snowflake")

    elif index==5:
        DescriptionText.set("Uses the koch curve to draw an inverse snowflake")

    elif index==6:
        DescriptionText.set("Circles created on the points found on the circumference of other circles")

    elif index==7:
        DescriptionText.set("A popular fractal of triangles within triangles")

    elif index==8:
        DescriptionText.set("A spiral created using the angles of a polygon")

    elif index==9:
        DescriptionText.set("A spiral of jagged edges")        
        
    else:
        print("Unknown error has occurred")
# end updateDescriptionLabel

#add all components as self.widget
Label(root, text = " ").grid(row = 0, column = 2, columnspan = 3)

#labels
angleLabel = Label(root, text = "Order")
angleLabel.grid(row = 1, column = 0)

Label(root, text = " ").grid(row = 1, column = 2)

lengthLabel = Label(root, text = "Length")
lengthLabel.grid(row = 2, column = 0)

Label(root, text = " ").grid(row = 2, column = 3)

PatternLabel = Label(root, text = "Pattern")
PatternLabel.grid(row = 3, column = 0)

DescriptionText = StringVar()
DescriptionLabel = Label(root, textvariable = DescriptionText, wraplength = 80, justify = "left")
DescriptionLabel.grid(row = 3, column = 2)

Label(root, text = " ").grid(row = 4, column = 0, columnspan = 3)

#inputs
angleInt = IntVar()
angleEntry = Entry(root, textvariable= angleInt)
angleEntry.grid(row = 1, column = 1)

lengthInt = IntVar()
lengthEntry = Entry(root, textvariable= lengthInt)
lengthEntry.grid(row = 2, column = 1)

#ListBox attributes
listbox = Listbox(root)
listbox.insert(END, "Spiro Graph")
listbox.insert(END, "Binary Tree")
listbox.insert(END, "Spike")
listbox.insert(END, "Fern Tree")
listbox.insert(END, "Snowflake")
listbox.insert(END, "Anti Snowflake")
listbox.insert(END, "Circle-Ception")
listbox.insert(END, "Triangle Fractal")
listbox.insert(END, "Polygon Spiral")
listbox.insert(END, "Jagged Edge")
listbox.grid(row = 3, column = 1)
listbox.bind('<<ListboxSelect>>', updateDescriptionLabel)

#Functional buttons
clearButton = Button(root, text = "Clear", command = OnClear)
clearButton.grid(row = 5, column = 0)

drawButton = Button(root, text = "Draw", command = OnDraw)
drawButton.grid(row = 5, column = 1)

newButton = Button(root, text = "New", command = OnNew)
newButton.grid(row = 5, column = 2)


    
    
mainloop()  

