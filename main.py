from tkinter import messagebox
import random
import pyperclip

user_name = ""
website = ""
password = ""
command = ""
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CAPITAL_LETTERS = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
small_letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
digits = [1,2,3,4,5,6,7,8,9,0]
symbols = ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','/','.','"',':',';',',','<','>','{','[','}',']','|','?',"'",' ']
characters_list = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','/','.','"',':',';',',','<','>','{','[','}',']','|','?',"'",' ']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    generated_password = []

    password_length = random.randint(8,12)

    password_entry.delete(0, END)

    generated_password.append(random.choice(CAPITAL_LETTERS))
    generated_password.append(random.choice(small_letters))
    generated_password.append(str(random.choice(digits)))
    generated_password.append(random.choice(symbols))

    for _ in random.choices(characters_list, k=(password_length-4)):
        generated_password.append(_)

    generated_password = ''.join(generated_password)
    password_entry.insert(0, string=generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    global user_name, website, password

    password_file = open(file="PasswordManager.txt", mode="a")

    website = website_entry.get()
    user_name = user_name_entry.get()
    password = password_entry.get()

    if website != "" and user_name != "" and password != "":
        save_button.config(bg=GREEN)

        result = messagebox.askokcancel(message=f"These are the details entered:\nEmail/Username: {user_name}\nPassword: {password}\nIs it ok to save?", title=website)

        if result:
            password_file.writelines(f"URL: {website}\nUsername: {user_name}\nPassword: {password}\n\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(message='Password saved', title='PassKey Manager')
        else:
            messagebox.showinfo(message='Password not saved', title='PassKey Manager')

    elif website == "" and user_name == "" and password == "":
        save_button.config(bg=RED)
        messagebox.showwarning(message='Please fill all the required fields', title='Required Field Empty')

    else:
        save_button.config(bg=YELLOW)

        if user_name == '':
            messagebox.showwarning(message='Please fill username', title='User Name Error')

            result = messagebox.askquestion(message='Do you want to use default username?', title='User Name Error')
            if result == 'yes':
                choice = messagebox.askquestion(message='Default User Name is "example@email.com"', title='Assigning Default User')
                if choice == 'yes':
                    user_name_entry.insert(END, string="example@email.com")
                else:
                    messagebox.showwarning(message="Please fill the user name", title='User Name Error')
            else:
                messagebox.showwarning(message="Please fill the user name", title='User Name Error')
        elif password == '':
            messagebox.showwarning(message='Please fill password', title='Password Error')
        elif website == '':
            messagebox.showwarning(message='Please fill URL', title="URL Missing")

    password_file.close()

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()

Font = ("Courier",16,'bold')

window.minsize(width=600, height=400)
window.title("Password Manager By Tejvir Chauhan")
window.config(pady=20,padx=20)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200,height=200)

canvas.create_image(100, 100, image= logo)
canvas.grid(column=1,row=0)

# Creating Labels for Website Name, User Name, Password

website_label = Label(text="Website:", font=Font)
website_label.grid(column=0,row=1)
website_label.config(padx=5,pady=5)

user_name_label = Label(text="Email/Username:", font=Font)
user_name_label.grid(column=0, row=2)
user_name_label.config(padx=5,pady=5)

password_label = Label(text="Password:", font=Font)
password_label.grid(column=0, row=3)
password_label.config(padx=5,pady=5)

# Text Boxes to take input from user

website_entry = Entry(width=40, font=('Courier',12), borderwidth=2)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

user_name_entry = Entry(width=40, font=('Courier',12), borderwidth=2)
user_name_entry.insert(END, string="")
# user_name_entry.insert(END, string="example@email.com")
user_name_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=22, font=('Courier',12), borderwidth=2)
password_entry.grid(column=1, row=3)
# password_entry.place(x=145, y=280)

# Buttons to generate or save password in file

generate_password_button = Button(text="Generate Password", font=("Courier",12), width=16, highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3)
# generate_password_button.place(x=372, y=275)
generate_password_button.config(padx=5,pady=1)

save_button = Button(text="Save", font=('Courier',12), command=save_password, highlightthickness=0, width=39)
save_button.grid(column=1, row=4, columnspan=2)
save_button.config(padx=5,pady=5)

window.mainloop()