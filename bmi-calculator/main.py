import tkinter

screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.minsize(500, 600)
screen.config(padx=50, pady=50)


def calculate():
    weight_value = weight_entry.get()
    height_value = height_entry.get()

    if weight_value == "" or height_value == "":
        result_label.config(text="Enter both weight and height")
    else:
        try:
            bmi = float(weight_value) / (float(height_value) / 100) ** 2
            bmi = round(bmi, 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")


message_weight = tkinter.Label(text="Enter your weight (kg)")
message_weight.pack()

weight_entry = tkinter.Entry()
weight_entry.pack()

message_height = tkinter.Label(text="Enter your height (cm)")
message_height.pack()

height_entry = tkinter.Entry()
height_entry.pack()

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()


def write_result(bmi):
    result_string = f"Your bmi: {bmi}. You are  "

    if bmi <= 16:
        result_string += "Severe Thinness"
    elif 16 < bmi <= 17:
        result_string += "Moderate Thinness	"
    elif 17 < bmi <= 18.5:
        result_string += "Mild Thinness"
    elif 18.5 < bmi <= 20:
        result_string += "Normal"
    elif 25 < bmi <= 40:
        result_string += "Overweight"
    elif 30 < bmi <= 35:
        result_string += "Obese Class I"
    elif 35 < bmi <= 40:
        result_string += "Obese Class II"
    elif bmi > 40:
        result_string += "Obese Class III"


tkinter.mainloop()
