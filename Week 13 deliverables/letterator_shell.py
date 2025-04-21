# IMPORTing content into source
import tkinter as tk
# the combobox dropdown is in a different module
from tkinter import ttk

# LIST, with STRINGS -- GLOBAL variable :(
paras = ["I would really like to touch base, I have not seen you in such a long time, dear friend", "The weather here in Indiana is great now - good time for a walk or a coffee.", "I hear Foil, Arms and Hog are playing at the Murat and would love to book us some seats.","I hope you and your family are doing well!"]

# FUNCTIONS!
# Note, Positional parameters
def save_greeting(dropdown_greeting, entry_greeting, text_display):
    greeting = dropdown_greeting.get() + " " + entry_greeting.get()
    text_display.insert(tk.END, greeting + "\n")

# Note, DEFAULT VALUE
def write_greeting_to_letter(dropdown_greeting, entry_greeting="Friend"):
    try:
        with open("letter.txt", "w") as letter:
            letter.write(dropdown_greeting.get() + " " + entry_greeting.get() + "\n")
    except PermissionError as e:
        print(f"This user does not have permission to write to disk in this folder location, {e}")
    except IOError as e:
        print(f"Input/Output issue - check for disk failure or interruption, {e}")
    except OSError as e:
        print(f"A system related error has occurred, {e}")
    else: # if there are no exceptions
        print("On track to write that letter to file!")


def save_paragraphs(vars, text_display):
    paragraphs = ""
    for check_box_num in range(len(vars)):
        if vars[check_box_num].get():
            paragraphs += paras[check_box_num] + "\n"
    text_display.insert(tk.END, paragraphs)

def append_paragraphs_to_letter(vars):
    try:
        with open("letter.txt", "a") as file:
            # "a" means to append
            for check_box_num in range(len(vars)):
                if vars[check_box_num].get():
                    file.write(paras[check_box_num] + "\n")
    except FileNotFoundError as e:
        print(f"Cannot continue writing to letter, file no longer available! {e}")
       

def save_salutation(dropdown_salutation, entry_salutation, text_display):
    salutation = dropdown_salutation.get() + " " + entry_salutation.get()
    text_display.insert(tk.END, salutation + "\n")

def append_salutation_to_letter(dropdown_salutation, entry_salutation):
    try:
        with open("letter.txt", "a") as file:
            file.write(dropdown_salutation.get() + " " + entry_salutation.get() + "\n")
    except Exception as e:
        print(f"Tried to add letter salutation, but there was an issue... {e}")

def write_to_letter(text_display):
    # Since the file is open to write, it will overwrite any existing content
    try:
        fh = open("letter.txt", "w")
    except Exception as e:
        print(f"Tried to write panel content to letter, but there was an issue...{e}")
    else:
        # This happens as long as there were no exceptions
        fh.write(text_display.get("1.0", tk.END))

def main():
    root = tk.Tk()
    root.title("Letterater")
    # Purdue colours
    root.configure(bg="black")

    # let's use a different font, comic sans here, Lucida
    # what are these? TUPLES
    comic_sans_font = ("Comic Sans MS", 10, "bold italic")
    lucida_font = ("Lucida Handwriting", 10, "bold italic")

    # Specific Purdue colours, way to signify 'should not change'
    AGED = "#8e6f3e"
    RUSH = "#daaa00"
    FIELD = "#ddb945"
    DUST = "#ebd99f"
    STEEL = "#555960"
    COOLGREY = "#6f727b"
    RAILWAYGREY = "#9d9795"
    STEAM = "#c4bfc0"
    # letter salutations
    letter_titles=["Dear", "Dearest", "Dear Associate", "Dear Friend", "Cousin", "Mr", "Ms", "Agent", "Dear Agent"]
    letter_closings = ["Kind regards", "Best", "Regards", "Sincerely", "All the best","Warm regards", "Kind wishes"]

    # Text display area - for letter content
    text_display = tk.Text(root, width=40, height=25, wrap="word", font=lucida_font, bg=COOLGREY, fg=FIELD)
    text_display.pack(side=tk.LEFT, padx=10, pady=10)

    # Right side panel - for letter controls and choices
    panel = tk.Frame(root, borderwidth=2, relief="solid", bg=AGED)
    panel.pack(side=tk.RIGHT, padx=10, pady=10)

    # Greeting section with border
    # outer frame
    frame_greeting = tk.Frame(panel, borderwidth=2, relief="solid", bg=RAILWAYGREY)  # Taupe color, Railway grey
    frame_greeting.pack(padx=5, pady=5)
    # label for greeting dropdown, and greeting dropdown
    label_salutation = tk.Label(frame_greeting, text="Salutation:")
    label_salutation.pack(side=tk.LEFT, padx=5)
    dropdown_greeting = ttk.Combobox(frame_greeting, values=letter_titles)
    dropdown_greeting.pack(side=tk.LEFT, padx=5)
    # now the name label, and the text or entry field for the name letter is being sent to
    label_name = tk.Label(frame_greeting, text="Name:")
    label_name.pack(side=tk.LEFT, padx=5)
    entry_greeting = tk.Entry(frame_greeting)
    entry_greeting.pack(side=tk.LEFT, padx=5)
    # frame around the buttons, and action buttons - save to text area, write to letter
    frame_greeting_buttons = tk.Frame(frame_greeting)
    frame_greeting_buttons.pack(padx=5, pady=5)
    button_save_greeting = tk.Button(frame_greeting_buttons, bg=DUST, text="Save", command=lambda: save_greeting(dropdown_greeting, entry_greeting, text_display))
    button_save_greeting.pack(side=tk.LEFT, padx=5)
    button_write_greeting = tk.Button(frame_greeting_buttons, bg = DUST, font=lucida_font, text="Add to Letter", command=lambda: write_greeting_to_letter(dropdown_greeting, entry_greeting))
    button_write_greeting.pack(side=tk.LEFT, padx=5)

    # Paragraph section with border and label
    frame_paragraphs = tk.Frame(panel, borderwidth=2, relief="solid", bg=FIELD)  # Gold color, field
    frame_paragraphs.pack(padx=5, pady=5)
    label_paragraphs = tk.Label(frame_paragraphs, text="Letter Content")
    label_paragraphs.pack(padx=5, pady=5)
    # checkboxes need an associated Boolean variable, to check selection status
    vars = []
    for num in range(len(paras)):
        vars.append(tk.BooleanVar())
    # saving the checkboxes in a list makes it easier to iterate through them
    # and removes dependency on a specific number
    checks = []
    for num in range(len(paras)):
        check = tk.Checkbutton(frame_paragraphs, text=paras[num], variable=vars[num], bg=FIELD, font = comic_sans_font)
        check.pack(padx=5, pady=5, anchor="w")
   
    frame_paragraph_buttons = tk.Frame(frame_paragraphs)
    frame_paragraph_buttons.pack(padx=5, pady=5)
    button_save_paragraphs = tk.Button(frame_paragraph_buttons, text="Save", bg=DUST, command=lambda: save_paragraphs(vars, text_display))
    button_save_paragraphs.pack(side=tk.LEFT, padx=5)
    button_append_paragraphs = tk.Button(frame_paragraph_buttons, text="Add to Letter", bg=DUST, font=lucida_font, command=lambda: append_paragraphs_to_letter(vars))
    button_append_paragraphs.pack(side=tk.LEFT, padx=5)

    # Salutation section with border
    frame_salutation = tk.Frame(panel, borderwidth=2, relief="solid", bg=STEAM)  # Taupe/grey color, steam
    frame_salutation.pack(padx=5, pady=5)
    label_salutation = tk.Label(frame_salutation, text="Salutation:")
    label_salutation.pack(side=tk.LEFT, padx=5)
    dropdown_salutation = ttk.Combobox(frame_salutation, values = letter_closings)
    dropdown_salutation.pack(side=tk.LEFT, padx=5)
    label_name = tk.Label(frame_salutation, text="Name:")
    label_name.pack(side=tk.LEFT, padx=5)
    entry_salutation = tk.Entry(frame_salutation)
    entry_salutation.pack(side=tk.LEFT, padx=5)
    frame_salutation_buttons = tk.Frame(frame_salutation)
    frame_salutation_buttons.pack(padx=5, pady=5)
    button_save_salutation = tk.Button(frame_salutation_buttons, text="Save", bg=DUST, command=lambda: save_salutation(dropdown_salutation, entry_salutation, text_display))
    button_save_salutation.pack(side=tk.LEFT, padx=5)
    button_append_salutation = tk.Button(frame_salutation_buttons, bg=DUST, font=lucida_font, text="Add to Letter", command=lambda: append_salutation_to_letter(dropdown_salutation, entry_salutation))
    button_append_salutation.pack(side=tk.LEFT, padx=5)

    # Write to letter button
    button_write_to_letter = tk.Button(panel, text="Write all to Letter", bg=STEEL, fg=RUSH, font=lucida_font, command=lambda: write_to_letter(text_display))
    button_write_to_letter.pack(padx=5, pady=5)

    root.mainloop()


main()
