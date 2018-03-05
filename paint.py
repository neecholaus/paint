from tkinter import *


class Paint:
    def __init__(self):
        print('Starting up...')

        self.window = Tk()

        self.canvas = Canvas(self.window, width="500", height="500", bg="white")
        self.canvas.pack()

        nav = Frame(self.window, relief="sunken")
        nav.pack(side=BOTTOM, fill=X)

        quitBtn = Button(nav, text="Quit", command=self.window.destroy)
        quitBtn.pack(side=RIGHT)

        self.window.bind('<Button-1>', self.paint)

        self.window.mainloop()

    def paint(self, event):
        x = event.x
        y = event.y
        self.canvas.create_rectangle(x, y, x+1, y+1, fill="black")



app = Paint()
