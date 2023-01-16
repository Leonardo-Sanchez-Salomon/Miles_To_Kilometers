from tkinter import *

window = Tk()
window.minsize(width=300, height=100)
window.config(padx=50, pady=25)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

kilo_meter = Label(text="Kilometers")
kilo_meter.grid(row=1, column=2)

kilo_num = Label(text=0)
kilo_num.grid(row=1, column=1)

in_put = Entry(width=10)
in_put.grid(row=0, column=1)


def calc():
    calculation = float(in_put.get()) * 1.60934
    kilo_num.config(text=calculation)


calculate = Button(text="Calculate", command=calc)
calculate.grid(row=3, column=1)

window.mainloop()
