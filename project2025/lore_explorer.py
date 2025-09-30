import json  # Imports the JSON module to work with .json files (load/save data)
import tkinter as tk  # Imports tkinter and gives it the alias "tk" for GUI creation
from tkinter import messagebox  # Imports the messagebox module for pop-up dialogs


# loads json file
with open('personal projects/project2025/lore_chars.json') as f:  # Opens the characters JSON file in read mode
    lore = json.load(f)  # Loads the file's contents into a Python dictionary called 'lore'
with open('personal projects/project2025/lore_regions.json') as f:  # Opens the regions JSON file
    area = json.load(f)  # Loads the file's contents into a dictionary called 'area'


def search_character():  # Defines a function that will run when the search button is clicked
    name = entry.get()  # Gets the text input from the entry box (user input)
    found = False  # A flag to track whether a match has been found

    # Search in characters
    for char in lore["characters"]:  # Loops through each character dictionary in the "characters" list
         if char["name"].lower() == name.lower():  # Compares input to character name if any letters are similar like ji = jicho (case-insensitive)
              info = f"Name: {char['name']}\nTitle: {char['title']}\nTraits: {', '.join(char['traits'])}\nShort Story:{ ', '.join(char['short story'])}"
              # Formats the character's details into a readable string (traits list is joined into a string)
              messagebox.showinfo("Character Found.", info)  # Shows a pop-up with character info
              found = True  # Marks that a character was found
              break  # Exits the loop once a match is found

    #search in regions   
    if not found:  # If no character was found, start looking through regions
         for char in area["regions"]:  # Loops through each region dictionary in the "regions" list
            if  char["reg"].lower() == name.lower():  # Compares input to region name if contains the same like re = rema (case-insensitive)
              infoR = f"Region: {char['reg']}\nCharacters: {', ' .join(char['characters'])}\nDescription:{ ', '.join(char['description'])}"  
              # Formats region info (characters & description lists are joined into strings)
              messagebox.showinfo("Region Found: ", infoR)  # Shows a pop-up with region info
              found = True  # Marks that a region was found
              break  # Exits the loop once a match is found
    if not found:  # If neither a character nor a region matched the input
        messagebox.showerror("Not Found", "Character or Region not found.")  # Shows an error pop-up
        return
   # #if not found:
    #    for char in lore["characters"]:
    #            info += f"- {char['name']} ({char['title']})\n"
    #            print(info)
    #    for char in area["regions"]:
    #            infoReg += f"- {char['reg']}: {', '.join(char['characters'])}\n"
    #            print(infoReg)
root = tk.Tk()  # Initializes the main window (root of your GUI)
root.title("Lore Search")  # Sets the title of the window
label = tk.Label(root, text="Enter character name or region:")  # Creates a label instructing the user
label.pack(pady=20)  # Adds the label to the window with padding
entry = tk.Entry(root)  # Creates an entry box for text input
entry.pack(pady=20)  # Adds the entry box to the window with padding
search_button = tk.Button(root, text="Search", command=search_character)  # Creates a search button and links it to the function
search_button.pack(pady=20)  # Adds the button to the window with padding
root.mainloop()  # Starts the GUI event loop, keeps the window running
