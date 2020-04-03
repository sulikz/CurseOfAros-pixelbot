from tkinter import Tk, Button
from Bot import Bot


class Gui(Tk):
    root = None
    frame = None
    w = 100
    h = 250
    toggle_run_btn = None
    b = None

    def __init__(self):
        Tk.__init__(self)
        self.b = Bot()
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, -2 * self.w, 140))
        self.toggle_run_btn = Button(self.root, text="Stopped.", command=lambda: self.toggle())
        self.toggle_run_btn.grid(row=1, column=1, )
        self.update_toggle()

    def toggle(self):
        if self.b.running:
            self.b.running = False
        else:
            self.b.running = True

    def update_toggle(self):
        if self.b.running:
            self.toggle_run_btn.config(text="Running!")
        else:
            self.toggle_run_btn.config(text="Stopped.")
        self.after(500, self.update_toggle)
