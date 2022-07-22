from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print(website_entry)
    with open("password_manager.txt", "a") as f:
        f.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    username_entry.insert(END, "@gmail.com")
    password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1,columnspan=2)
website_entry.focus()
#website = website_entry.get()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "@gmail.com")
#username = username_entry.get()

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)
#password = password_entry.get()

#buttons

generate_button = Button(text="Generate")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(width=33)


window.mainloop()