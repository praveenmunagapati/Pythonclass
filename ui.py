# 🧩 Tkinter Fundamentals (Python GUI)

## 1. What is Tkinter?

# **Tkinter** is Python’s built-in library for
#     creating graphical user interfaces (GUIs).
#     It provides widgets like windows, buttons, labels, text boxes, etc.


## 2. Basic Structure of a Tkinter Program

# Every Tkinter app follows this pattern:

import tkinter as tk

root = tk.Tk()          # Create main window
root.title("My App")    # Set window title
root.geometry("300x200") # Set size

root.mainloop()         # Run the app

# 👉 `mainloop()` keeps the window running and responsive.


## 3. Widgets (Core Components)

### Example: Label

import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()


### Example: Button

import tkinter as tk

def say_hello():
    print("Hello!")

root = tk.Tk()

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

root.mainloop()


### Example: Entry (Text Input)

import tkinter as tk

def show_text():
    print(entry.get())

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Submit", command=show_text)
btn.pack()

root.mainloop()


## 4. Layout Managers

# Tkinter has 3 layout systems:

### (a) pack() Simple stacking layout

tk.Label(root, text="Top").pack()
tk.Label(root, text="Bottom").pack()


### (b) grid()

# Table-like layout

import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Age").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)

root.mainloop()


### (c) place()

#Absolute positioning (less used)

tk.Label(root, text="Hello").place(x=50, y=50)


## 5. Event Handling Events are user actions (clicks, typing, etc.).

import tkinter as tk

def clicked():
    print("Button clicked!")

root = tk.Tk()

btn = tk.Button(root, text="Click", command=clicked)
btn.pack()

root.mainloop()


## 6. Working with Frames Frames help organize widgets.

import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Inside Frame").pack()

root.mainloop()


## 7. Message Box Example

import tkinter as tk
from tkinter import messagebox

def show_msg():
    messagebox.showinfo("Info", "Hello User!")

root = tk.Tk()

tk.Button(root, text="Show Message", command=show_msg).pack()

root.mainloop()


## 8. Simple Standalone Project (Mini App)

### Example: Counter App

import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    label.config(text=str(count))

root = tk.Tk()
root.title("Counter App")

label = tk.Label(root, text="0", font=("Arial", 20))
label.pack()

btn = tk.Button(root, text="Increase", command=increase)
btn.pack()

root.mainloop()


# ## 9. Key Concepts Summary
#
# * `Tk()` → main window
# * `Widget` → UI element (Label, Button, Entry)
# * `pack()/grid()/place()` → layout
# * `command` → attach function to widget
# * `mainloop()` → runs app


## 10. Tips for Beginners
#
# * Don’t mix `pack()` and `grid()` in the same container
# * Always call `mainloop()`
# * Use functions for button actions
# * Start with small apps (calculator, to-do list)