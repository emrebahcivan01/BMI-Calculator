from tkinter import *

def calculate_bmi():
    weight = my_entry.get()
    height = my_entry_2.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both height and weight")
        category_label.config(text="")
        return

    if not weight.isdigit() or not height.isdigit():
        result_label.config(text="Enter a valid number!")
        category_label.config(text="")
        return

    weight = float(weight)
    height = float(height) / 100  # cm to m conversion

    bmi = weight / (height ** 2)

    result_label.config(text=f"Your BMI: {bmi:.2f}")

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25.0:
        category = "Normal"
    elif 25.0 <= bmi < 30.0:
        category = "Overweight"
    elif 30.0 <= bmi < 35.0:
        category = "Obese"
    elif 35.0 <= bmi < 40.0:
        category = "Severely Obese"
    else:
        category = "Morbidly Obese"

    category_label.config(text=f"Category: {category}")

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=250)

my_label = Label(text="Enter your weight (kg)")
my_label.config(fg="black")
my_label.config(padx=10, pady=10)
my_label.pack()

my_entry = Entry(width=20)
my_entry.pack()
my_entry.focus()

my_label_2 = Label(text="Enter your height (cm)")
my_label_2.config(fg="black")
my_label_2.config(padx=10, pady=10)
my_label_2.pack()

my_entry_2 = Entry(width=20)
my_entry_2.pack()


my_button = Button(text="Calculate", command=calculate_bmi)
my_button.config(padx=10, pady=10)
my_button.pack()

result_label = Label(text="")
result_label.pack()

category_label = Label(text="")
category_label.pack()

window.mainloop()
