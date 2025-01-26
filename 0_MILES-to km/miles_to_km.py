from tkinter import *
FONT=("Arial", 24, "bold")


def button_clicked():
    miles=float(input.get())
    km = miles * 1.60934
    my_label_result.config(text=km)


window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50,pady=50)

my_label_1=Label(text="is equal to", font=FONT)
my_label_1.grid(column=0, row=1)

my_label_2=Label(text="Miles", font=FONT)
my_label_2.grid(column=2, row=0)

my_label_3=Label(text="Km", font=FONT)
my_label_3.grid(column=2, row=1)

my_label_result=Label(text="0", font=FONT)
my_label_result.grid(column=1, row=1)

input=Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

button=Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()

