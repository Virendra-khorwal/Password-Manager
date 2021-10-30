from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generate():
    #Password Generator Project
    password_input.delete(0, 'end')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]
    password_sym = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letter + password_num + password_sym

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    web = website_input.get()
    mail = email_input.get()
    passw = password_input.get()
    new_data = {
        web : {
            "email": mail,
            "password": passw,
        }
    }

    if len(web)>0 or len(passw)>0:

        is_ok = messagebox.askokcancel(title="Input Details", message=f"These are the details you filled.\n Website: {web} \n Email: {mail} \n Password: {passw}\n")

        if is_ok:
            try:
                with open("login_data.json", "r") as file:
                    data = json.load(file)
        
            except FileNotFoundError:
                with open("login_data.json", 'w') as file:
                    json.dump(new_data, file, indent=4) 

            else :
                data.update(new_data) 
                with open("login_data.json", 'w') as file:
                    json.dump(data, file, indent=4)   

    else:
        messagebox.showwarning(title="Error", message="Input field is empty!")

    website_input.delete(0, 'end')
    password_input.delete(0, 'end')

# ---------------------------- SEARCH ------------------------------- #

def search_data():
    website = website_input.get()
    try:
        with open("login_data.json", 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data in file")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website} login Data", message=f"These are the login Details. \n Email: {email} \n Password: {password}")

        else :
            messagebox.showinfo(title=f"{website} login Data", message=f"No data found for {website}.")
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50,pady=50, bg="white")
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0 )
image_lock = PhotoImage(file="./logo.png")
canvas.create_image(100,100, image=image_lock)
canvas.grid(column=1,row=0)

#Label
website = Label(text="Website:")
website.config(padx=10,pady=5, bg="white")
website.grid(column=0, row=1)
email = Label(text="Username/Email:")
email.config(padx=10,pady=5,bg="white")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.config(padx=10,pady=5,bg="white")
password.grid(column=0, row=3)


#Input
website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=55)
email_input.grid(column=1, row=2,columnspan=2)
email_input.insert(0,"virendrakhorwalvk@gmail.com" )
password_input = Entry(width=32)
password_input.grid(column=1, row=3)


# Button
search_btn = Button(text="Search", width=18,relief="flat", command=search_data)
search_btn.grid(column=2, row=1)
generate_btn = Button(text="Generate Password", width=18,relief="flat", command=pass_generate)
generate_btn.grid(column=2, row=3)
add_button = Button(text="Add", width=47,relief="flat", command=save_data)
add_button.grid(column=1, row=4,columnspan=2)





window.mainloop()