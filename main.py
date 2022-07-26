from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ----------------------------SEARCH ------------------------------------------#

def find_password():
    try:
        with open("password_manager.json", "r") as file:
            # reading the data
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(message="Hey! it looks like you have not saved any passwords yet")
    else:
        if website_entry.get() in data:
            messagebox.showinfo(message=f"Website: {data[website_entry.get()]['email']}\n Password: {data[website_entry.get()]['password']}")
        else:
            messagebox.showinfo(message="Hey! the record for this website is not present")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    gen_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, gen_password)
    pyperclip.copy(gen_password)
    # gen_password = ""
    # for char in password_list:
    #  gen_password += char


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    user_pass = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": user_pass
        }
    }
    if len(website) == 0 or len(username) == 0 or len(user_pass) == 0:
        messagebox.showinfo(message="Hey there! Don't leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Is is information correct? \n Email: "
                                                              f"{username}\n Password: {user_pass}\n Are you ok with saving these details?")
        if is_ok:
            try:
                with open("password_manager.json", "r") as f:
                    # reading the data
                    data = json.load(f)

            except FileNotFoundError:
                with open("password_manager.json", "w") as f:
                    # saving the updated data
                    json.dump(new_data, f, indent=4)
            else:
                with open("password_manager.json", "w") as f:
                    # updating old data with new data
                    data.update(new_data)
                    # saving the updated data
                    json.dump(data, f, indent=4)
            finally:
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                username_entry.insert(END, "@gmail.com")
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=24)
website_entry.grid(column=1, row=1)
website_entry.focus()
# website = website_entry.get()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "@gmail.com")
# username = username_entry.get()

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)
# password = password_entry.get()

# buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(width=33)

window.mainloop()
