#mile to KM converter.
from tkinter import *


def miles_to_KM():
    miles =float(miles_entry.get())
    km = miles * 1.689
    km_result.config(text=f"{km}")


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500,height=500)


#entry
miles_entry = Entry()
miles_entry.grid(column=1,row=0)


#label
label = Label(text="miles")
label.grid(column=2,row=0)

# is equal to label
isequaltolabel = Label(text="is equal to")
isequaltolabel.grid(column=0,row=1)


km_result = Label(text="0")
km_result.grid(column=1,row=1)

km_label =Label(text="KM")
km_label.grid(column=2,row=1)

#calculate Button
calculate_button = Button(text="Calculate",command=miles_to_KM)
calculate_button.grid(column=1,row=2)


window.mainloop()