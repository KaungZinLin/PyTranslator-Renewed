# Imports
import tkinter
from tkinter import *
from tkinter import messagebox
import pyttsx3
from translate import Translator

# Functions
def translate():
    try:
        language_data = language_entry.get()
        text_data = text_entry.get()

        if text_data == "":
            messagebox.showerror("Error!", "Error: Please type in a text to translate!")
            text_entry.focus()
        elif language_data == "":
            messagebox.showerror("Error!", "Error: Please type in a language to translate!")
            language_entry.focus()
        else:
            translator = Translator(to_lang=language_data)
            translation = translator.translate(text_data)

            messagebox.showinfo("Info", "Translated Text: \n" + translation)
            # pyttsx3.speak(translation)
    except:
        messagebox.showerror("Error!", "Error: Cannot translate your text")

def about_app():
    messagebox.showinfo("About", "PyTranslator (Renewed) \n\nIs used to translate texts from one langauge to another. \n\nApp version: v0.1 for macOS (Stable) \n\nHUGE THANKS FOR USING THIS APP!")

# GUI Setup
window = Tk()

window.title("PyTranslator (Renewed)")
window.resizable(False, False)
window.config(padx=50, pady=50)

# Labels
py_translator_label = Label(text="PyTranslator (Renewed)", font=('Areal', 25))
py_translator_label.grid(row=0, column=0, sticky='w')

translator_label = Label(text="\nTRANSLATOR")
translator_label.grid(row=1, column=0, sticky='w')

text_input_label = Label(text="Text:")
text_input_label.grid(row=2, column=0, sticky='w')

language_input_label = Label(text="Language:")
language_input_label.grid(row=3, column=0, sticky='w')

placeholder_label = Label(text="")
placeholder_label.grid(row=4, column=0)

# Buttons
translate_button = Button(text="Translate", width=8, command=translate)
translate_button.grid(row=5, column=0, sticky='w')

about_button = Button(text="About", width=8, command=about_app)
about_button.grid(row=6, column=0, sticky='w')

# Entries - Text
text_entry = tkinter.Entry(window, width=35)
text_entry.grid(row=2, column=1, columnspan=2, sticky='w')
text_entry.insert(0, 'e.g.: Hello!')

text_data = text_entry.get()

def clear_text_2(event):
    if text_entry.get() == 'e.g.: Hello!':
        text_entry.delete(0, 'end')

text_entry.bind('<FocusIn>', clear_text_2)

#Entries - Language
language_entry = tkinter.Entry(window, width=35)
language_entry.grid(row=3, column=1, columnspan=2, sticky='w')
language_entry.insert(0, 'e.g.: Italian, Spanish')

language_data = language_entry.get()

def clear_text(event):
    if language_entry.get() == 'e.g.: Italian, Spanish':
        language_entry.delete(0, 'end')

language_entry.bind('<FocusIn>', clear_text)

# GUI Loop
window.mainloop()