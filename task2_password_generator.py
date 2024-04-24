from tkinter import *
import string
import random
import pyperclip

def generate_password():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    password_length = int(length_box.get())
    password = ""

    if choice.get() == 1:  # Weak Password (only lowercase letters)
        password = ''.join(random.choices(small_alphabets, k=password_length))
    elif choice.get() == 2:  # Medium Password (lowercase + uppercase letters)
        password = ''.join(random.choices(small_alphabets + capital_alphabets, k=password_length))
    elif choice.get() == 3:  # Strong Password (lowercase + uppercase + digits + special characters)
        password = ''.join(random.choices(small_alphabets + capital_alphabets + numbers + special_characters, k=password_length))

    password_field.delete(0, END)  # Clear previous content
    password_field.insert(0, password)  # Insert new password

def copy_password():
    random_password = password_field.get()
    pyperclip.copy(random_password)

# Create the main Tkinter window
root = Tk()
root.config(bg='gray20')
root.title('Password Generator')

# Variables
choice = IntVar()

# GUI Elements
font = ('Arial', 13, 'bold')

password_label = Label(root, text='Password Generator', font=('Times new roman', 20, 'bold'), bg='gray20', fg='white')
password_label.grid(pady=10)

weak_button = Radiobutton(root, text='Weak', value=1, variable=choice, font=font)
weak_button.grid(pady=5)

medium_button = Radiobutton(root, text='Medium', value=2, variable=choice, font=font)
medium_button.grid(pady=5)

strong_button = Radiobutton(root, text='Strong', value=3, variable=choice, font=font)
strong_button.grid(pady=5)

length_label = Label(root, text='Password Length', font=('Times new roman', 20, 'bold'), bg='gray20', fg='white')
length_label.grid()

length_box = Spinbox(root, from_=5, to_=20, width=5, font=font)
length_box.grid(pady=5)

generate_button = Button(root, text='Generate', font=font, command=generate_password)
generate_button.grid(pady=5)

password_field = Entry(root, width=25, bd=2, font=font)
password_field.grid(pady=5)

copy_button = Button(root, text='Copy', font=font, command=copy_password)
copy_button.grid(pady=5)

root.mainloop()
