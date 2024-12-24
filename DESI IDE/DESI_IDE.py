from tkinter import *

window = Tk()
window.minsize(500, 500)
window.title("DESI IDE")
window.config(cursor="plus")

new_logo = PhotoImage(file="logo.png")
logo = PhotoImage(file="logo.png")

window.iconphoto(False, logo, new_logo)

IDE = Text(insertwidth=2)
IDE.insert(INSERT, "ADD THE CODE HERE")
IDE.place(x=0, y=50)

def Run():
    text = IDE.get(1.0, "end-1c")
    exec(text)

def Clear():
    IDE.delete(1.0, "end-1c")

run = Button(text="RUN", command=Run)
run.place(x=100, y=0)

clear = Button(text="CLEAR", command=Clear)
clear.place(x=50, y=0)

exit = Button(text="EXIT", command=window.destroy)
exit.place(x=0, y=0)

window.mainloop()
