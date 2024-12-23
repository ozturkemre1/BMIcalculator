from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=200)

#weight label
weight_label = Label(text="Enter Your Weight (kg)")
weight_label.pack(pady=(15, 0))

#weight entry
weight_entry = Entry(width=20)
weight_entry.pack()

#height label
height_label = Label(text="Enter Your Height (cm)")
height_label.pack()

#height entry
height_entry = Entry(width=20)
height_entry.pack()

#calculate button
def button_clicked():
    if not weight_entry.get() or not height_entry.get():
        result_label.config(text="Please enter both weight and height!")
        return
    try:
        weight_value = float(weight_entry.get())
        height_value = float(height_entry.get()) / 100
        if height_value <= 0 or weight_value <= 0:
            result_label.config(text="Values must be greater than zero!")
            return
        bmi = round(weight_value / (height_value ** 2))
        if bmi <=18.4:
            result_label.config(text=f"Your BMI is {bmi}. You are underweight.")
        elif bmi <= 24.9:
            result_label.config(text=f"Your BMI is {bmi}. You are normal.")
        elif bmi <= 39.9:
            result_label.config(text=f"Your BMI is {bmi}. You are overweight.")
        else:
            result_label.config(text=f"Your BMI is {bmi}. You are obese.")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


calculate_button = Button(text="Calculate",command=button_clicked)
calculate_button.pack(pady=(5, 0))

#result label
result_label = Label()
result_label.pack(pady=(5, 0))

window.mainloop()