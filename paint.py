from tkinter import *

class Paint:
    def __init__(self):
        self.window = Tk()

        self.canvas = Canvas(self.window, width="500", height="500", bg="white")
        self.canvas.pack()

        nav = Frame(self.window, relief="sunken")
        nav.pack(side=BOTTOM, fill=X)

        quitBtn = Button(nav, text="Quit", command=self.window.destroy)
        quitBtn.pack(side=RIGHT)

        self.colorEntry = Entry(nav, text="Color")
        self.colorEntry.pack()

        colorBtn = Button(nav, text="Change Color", command=self.changeColor)
        colorBtn.pack()

        self.penColor = 'black'
        self.draw = False

        self.canvas.bind('<Button-1>', self.penOn)
        self.canvas.bind('<ButtonRelease-1>', self.penOff)
        self.canvas.bind('<Motion>', self.paint)

        self.window.mainloop()

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
            self.canvas.create_oval(x, y, x+3, y+3, fill=self.penColor, outline=self.penColor)

    def changeColor(self):
        color = self.colorEntry.get()
        self.penColor = color



app = Paint()
