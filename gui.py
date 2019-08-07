import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        self.face = Face(self, width = 125, height = 175, bg = "#76F015")
        self.face.pack()

        btn = tk.Button(self, text="Smile", command=self.face.smile)
        btn.pack()

        btn = tk.Button(self, text="Normal", command=self.face.normal_mouth)
        btn.pack()

        btn = tk.Button(self, text="Quick smile", command=self.quick_smile)
        btn.pack()

    def quick_smile(self):
        self.face.smile()
        self.after(500, self.face.normal_mouth) # return to normal after .5 seconds

class Face(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        tk.Canvas.__init__(self, master, **kwargs)

        # make outside circle
        self.create_oval(25, 40, 105, 120)

        # make eyes
        self.create_oval(40, 55, 60, 75)
        self.create_oval(70, 55, 90, 75)

        # make initial mouth
        self.mouth = [] #list of things in the mouth
        self.normal_mouth()

    def smile(self):
        self.clear(self.mouth) # clear off the previous mouth
        self.mouth = [
            self.create_arc(45, 80, 85, 100, start=180, extent=180)
            ]

    def normal_mouth(self):
        self.clear(self.mouth) # clear off the previous mouth
        self.mouth = [
            self.create_line(45, 100, 85, 100),
            self.create_arc(25, 95, 45, 105, extent=90, start=-45, style='arc'), # dimple
            self.create_arc(85, 95, 105, 105, extent=90, start=135, style='arc') # dimple
            ]

    def clear(self, items):
        '''delete all the items'''
        for item in items:
            self.delete(item)

def main():
    root = tk.Tk()
    win = App(root)
    win.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
