from tkinter import *
FONT=("Arial", 24, "bold")
from tkinter import messagebox
from  random import choice, randint, shuffle
import pyperclip
import json
from settings import MY_EMAIL

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters=[choice(letters) for char in range(randint(8, 10))]
    symbols=[choice(symbols) for char in range(randint(2, 4))]
    numbers=[choice(numbers) for char in range(randint(2, 4))]

    password_list=letters+symbols+numbers
    shuffle(password_list)
    password = ''.join(password_list)
    input_password.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    my_data=[]
    my_data.append(input_website.get())
    my_data.append(input_email.get())
    my_data.append(input_password.get())
    my_string='|'.join(map(str, my_data)) + '\n'
    print(my_string)
    new_data={input_website.get():{
                  "email":input_email.get(),
                  "password":input_password.get()
        }
    }

    if len(input_website.get())==0 or len(input_password.get())==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty")
    else:
        try:
            with open("password.json", "r") as f:
                data=json.load(f)

        except FileNotFoundError:
            with open("password.json", "w") as f:
              json.dump(new_data, f, indent=4)
              input_website.delete(0,'end')
              input_password.delete(0,'end')
        else:
            data.update(new_data)
            with open("password.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            input_website.delete(0,'end')
            input_password.delete(0,'end')

# ---------------------------- SEARCH ------------------------------- #

def find_password():
    website_value=input_website.get()
    try:
        with open("password.json", "r") as f:
            data=json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Info", message="No data")
    else:
        if website_value in data:
            email = data[website_value]["email"]
            password=data[website_value]["password"]
            messagebox.showinfo(title="Info", message=f"Email: {email}, Password:{password}")
        else:
               messagebox.showinfo(title="Info", message=f"No details for {website_value} website exist")



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas=Canvas(width=200, height=200, highlightthickness=0)
lock_img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#labels
website_label=Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

email_label=Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)

password_label=Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

#Inputs
input_website=Entry(width=21)
input_website.focus()
input_website.grid(column=1, row=1)

input_email=Entry(width=35)
input_email.insert(0, MY_EMAIL)
input_email.grid(column=1, row=2, columnspan=2, sticky=EW)

input_password=Entry(width=21)
input_password.grid(column=1, row=3)

#Buttons
button_gen=Button(text="Generate Password", command=generate_password, width=14)
button_gen.grid(column=2, row=3)

button_search=Button(text="Search", width=14, command=find_password)
button_search.grid(column=2, row=1)

button_add=Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky=EW)

window.mainloop()
