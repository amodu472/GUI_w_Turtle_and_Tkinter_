import random
import pyperclip
from tkinter import *
from tkinter import messagebox
import json

# set up screen
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)


# __________________________________________________ Logic ____________________________________________________________
def save_data():
    # Get all necessary inputs
    web_input = website_entry.get()
    mail_input = email_username_entry.get()
    pass_input = password_entry.get()

    # aggregate our data above and save in JSON format (nested dict)
    all_data = {
        web_input.title(): {
            "Email": mail_input,
            "Password": pass_input
        }
    }

    # validate that an entry was made.
    if len(web_input) == 0 or len(mail_input) == 0 or len(pass_input) == 0:
        messagebox.showinfo(title="Boi!", message="You left one or more fields empty my guy!")
        return
    # ask user if their entries are correct, the save if correct
    ok_to_save = messagebox.askokcancel(title=f"{web_input} Credentials...",
                                        message=f"Credentials Entered: \nWebsite: {web_input}\nEmail: "
                                                f"{mail_input}\nPassword: {pass_input}")
    if ok_to_save:
        try:
            # Save the data to a json file
            with open("data.json", "r") as my_info:
                # first step in the json update process is to load existing data
                data = json.load(my_info)
                # Update old data with new data
                data.update(all_data)
        except FileNotFoundError:
            # First time we're opening this file
            with open("data.json", "w") as file:
                json.dump(all_data, file, indent=3)
        else:
            # write the updated data to our file
            with open("data.json", "w") as my_info2:
                json.dump(data, my_info2, indent=3)
        finally:
            # Clear entries
            website_entry.delete(0, END), password_entry.delete(0, END)
            website_entry.focus()


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    # if no password has been previously generated
    if len(password_entry.get()) == 0:
        password_entry.insert(0, "".join(password_list))
        pyperclip.copy(password_entry.get())


def search():
    query = website_entry.get()

    # user did not enter any search term/query
    if len(query) == 0:
        messagebox.showinfo(title="Try Again...", message="Please enter a search query.")
    else:
        query = query.title()
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            #   Query found. Print appropriate response
            if query in data:
                messagebox.showinfo(title=f"{query}", message=f"Email: {data[query]['Email']}\n"
                                                              f"Password: {data[query]['Password']}")
            else:
                # Query not found. Print appropriate response
                messagebox.showinfo(title=f"{query} not found!", message=f"No record for {query} yet!")
        #   No file has been saved yet
        except FileNotFoundError:
            messagebox.showinfo(title="No records yet...", message="No data saved yet.")


# ___________________________________________________ UI ______________________________________________________________
# setup image on screen
image_ = PhotoImage(file="manager.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(56, 100, image=image_)
canvas.grid(column=1, row=0)

# Lets setup our widgets
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
# once app is launched, cursor is focused inside this entry box
website_entry.focus()

email_username = Label(text="Email/Username: ")
email_username.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
# pre-populate this field with most common email
email_username_entry.insert(0, string="amodu472@gmail.com")

password = Label(text="Password: ")
password.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate = Button(text="Generate Password", width=26, command=password_generator)
generate.grid(column=1, row=4, columnspan=2)

add = Button(text="Add Info", width=26, command=save_data)
add.grid(column=1, row=5, columnspan=2)

# search
search = Button(text="Info Search", width=26, command=search)
search.grid(row=6, column=1, columnspan=2)

window.mainloop()
