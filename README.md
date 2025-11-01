# Miles to Kilometers Converter (Tkinter GUI)

## 📘 Overview
A simple and interactive **Miles to Kilometers Converter** built using **Python’s Tkinter** library.  
This GUI app allows users to enter a distance in miles and instantly convert it to kilometers with a single click.  
Perfect for beginners learning GUI programming with Python.

---

## 🧮 Conversion Formula
1 Mile = 1.60934 Kilometers

## 🖥️ GUI Preview

<img width="557" height="348" alt="Screenshot 2025-11-01 183129" src="https://github.com/user-attachments/assets/a7918436-8e20-44ea-895e-0d4bcd07f1b1" />


---

## 🧰 Technologies Used
- 🐍 **Python 3.x**
- 🪟 **Tkinter** (built-in GUI library)

---

## ✨ Features
✅ Simple and easy-to-use interface  
✅ Real-time conversion from miles to kilometers  
✅ Beginner-friendly and lightweight  
✅ Works on Windows, macOS, and Linux  

---

CODE:-
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

