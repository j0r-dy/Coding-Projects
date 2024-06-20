import random
import tkinter as tk
import string


def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))

    # enable text widget for editing
    result_text.config(state="normal")
    # clear previous content
    result_text.delete("1.0", tk.END)
    # insert new text
    result_text.insert(tk.END, password)
    # disable text widget again to make it read only
    result_text.config(state="disabled")


def start():
    # retrieve text from the entry field
    password_length = int(length_entry.get())

    # retrieve th state of the checkbox
    include_uppercase = checkbox_upp.get()
    include_lowercase = checkbox_low.get()
    include_digits = checkbox_num.get()
    include_special_chars = checkbox_spec.get()

    generate_password(
        length=password_length,
        uppercase=include_uppercase,
        lowercase=include_lowercase,
        digits=include_digits,
        special_chars=include_special_chars
    )


# create the main window
root = tk.Tk()
root.title("Generatore password di jordyno")

# set initial size
root.geometry("400x300")

# widgets

# greetings labels
greetings_label = tk.Label(root, text="Puoi customizzare la password in base a questi criteri")
greetings_label.pack()

# entry label for lenght
length_label = tk.Label(root, text="Enter the lenght of the password")
length_label.pack()

# entry field for lenght input
length_entry = tk.Entry(root)
length_entry.pack()

# checkbox
checkbox_spec = tk.BooleanVar(value=True)
special_checkbox = tk.Checkbutton(root, text="Include special chars", variable=checkbox_spec)
special_checkbox.pack()

checkbox_upp = tk.BooleanVar(value=True)
upper_checkbox = tk.Checkbutton(root, text="Include uppercase letters", variable=checkbox_upp)
upper_checkbox.pack()

checkbox_low = tk.BooleanVar(value=True)
lower_checkbox = tk.Checkbutton(root, text="include uppercase letters", variable=checkbox_low)
lower_checkbox.pack()

checkbox_num = tk.BooleanVar(value=True)
numb_checkbox = tk.Checkbutton(root, text="include numbers", variable=checkbox_num)
numb_checkbox.pack()



# button
button = tk.Button(root, text="Generate password", command=start)
button.pack()


# text widget
result_text = tk.Text(root, wrap="word", height=5, state="disabled")
result_text.pack()

# run the application
root.mainloop()