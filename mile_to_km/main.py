from tkinter import *


# Function to Calculate miles to km -- button action
def calculate():
    miles = miles_entry.get()
    kms = float(miles) * 1.609
    km_output_label.config(text=kms)


# Creating window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Creating label for write out "is equal to"
is_equal_label = Label(text="Is equal to: ")
is_equal_label.grid(column=0, row=1)

# Creating entry label for values in miles
miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)

# Creating output label
km_output_label = Label(text="0")
km_output_label.grid(column=1, row=1)

# Creating button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# Creating "Miles" label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Creating "Km" label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

window.mainloop()
