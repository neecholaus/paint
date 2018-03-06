from tkinter import *
import io

class Paint:
    def penOn(self, event):
        self.draw = True
        self.paint

    def penOff(self, event):
        self.draw = False
        self.paint

    def paint(self, event):
        x = event.x
        y = event.y
        if(self.draw == True):
            try:
                self.canvas.create_oval(x, y, x+3, y+3, fill=self.penColor, outline=self.penColor)
            except:
                self.penColor = 'black'
                self.colorEntry.delete(0, END)
                self.colorEntry.insert(0, 'black')

    def changeColor(self):
        color = self.colorEntry.get()
        self.penColor = color

    def saveCanvas(self):
        self.canvas.postscript(file="python_paint.ps", colormode="color")

    def __init__(self):
        self.window = Tk()
        self.window.title('Python Paint')

        self.canvas = Canvas(self.window, width="500", height="500", bg="white")
        self.canvas.pack()

        nav = Frame(self.window, relief="sunken")
        nav.pack(side=BOTTOM, fill=X)

        quitBtn = Button(nav, text="Quit", command=self.window.destroy)
        quitBtn.pack(side=RIGHT)

        self.colorEntry = Entry(nav)
        self.colorEntry.pack(side=LEFT)
        self.colorEntry.insert(0, 'black')

        colorBtn = Button(nav, text="Change Color", command=self.changeColor)
        colorBtn.pack(side=LEFT)

        self.saveBtn = Button(nav, text="Save", command=self.saveCanvas)
        self.saveBtn.pack(side=RIGHT)

        self.penColor = 'black'
        self.draw = False

        self.canvas.bind('<Button-1>', self.penOn)
        self.canvas.bind('<ButtonRelease-1>', self.penOff)
        self.canvas.bind('<Motion>', self.paint)

        self.window.mainloop()


app = Paint()
