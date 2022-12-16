from tkinter import *


class Paint(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.brush_size = 7
        self.color = "cyan"
        self.canvas = None
        self.set_ui()

    def set_ui(self):
        # setting a name for the window
        self.parent.title("Paint Program")
        self.pack(fill=BOTH, expand=1)

        # expand the rows and columns
        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        # configure the canvas -> white font
        self.canvas = Canvas(self, bg="white")

        # position the canvas directions
        self.canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)
        self.canvas.bind("<B1-Motion>", self.draw)

        # button brush change names and position
        color_lab = Label(self, text="Colors: ")
        color_lab.grid(row=0, column=0, padx=6)

        # manage the buttons configuration
        red_button = Button(self, text="Red", width=10, command=lambda: self.set_color("red"))
        red_button.grid(row=0, column=1)

        green_button = Button(self, text="Green", width=10, command=lambda: self.set_color("green"))
        green_button.grid(row=0, column=2)

        blue_button = Button(self, text="Blue", width=10, command=lambda: self.set_color("blue"))
        blue_button.grid(row=0, column=3)

        black_button = Button(self, text="Black", width=10, command=lambda: self.set_color("black"))
        black_button.grid(row=0, column=4)

        yellow_button = Button(self, text="Yellow", width=10, command=lambda: self.set_color("yellow"))
        yellow_button.grid(row=0, column=5)

        # configure brush size text button
        size_lab = Label(self, text="Sizes: ")
        size_lab.grid(row=1, column=0, padx=5)

        two_button = Button(self, text="2x", width=10, command=lambda: self.set_brush_size(2))
        two_button.grid(row=1, column=1)

        five_button = Button(self, text="5x", width=10, command=lambda: self.set_brush_size(5))
        five_button.grid(row=1, column=2)

        seven_button = Button(self, text="7x", width=10, command=lambda: self.set_brush_size(7))
        seven_button.grid(row=1, column=3)

        ten_button = Button(self, text="10x", width=10, command=lambda: self.set_brush_size(10))
        ten_button.grid(row=1, column=4)

        twenty_button = Button(self, text="20x", width=10, command=lambda: self.set_brush_size(20))
        twenty_button.grid(row=1, column=5)

        clear_button = Button(self, text="Clear", width=10, command=lambda: self.canvas.delete('all'))
        clear_button.grid(row=0, column=6, sticky=S)

    def draw(self, event):
        self.canvas.create_oval(event.x - self.brush_size,
                                event.y - self.brush_size,
                                event.x + self.brush_size,
                                event.y + self.brush_size,
                                fill=self.color, outline=self.color)

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size


def main():
    root = Tk()
    root.resizable(False, False)
    root.geometry("800x600+200+200")
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()
