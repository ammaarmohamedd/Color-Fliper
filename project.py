

import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# Function to generate a random color
def random_color():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

# Function to flip the color randomly
def flip_color():
    new_color = random_color()
    update_color(new_color)

# Function to update the background color and label
def update_color(color):
    window.config(bg=color)
    color_label.config(text=color, bg=color, fg="white" if is_dark_color(color) else "black")
    add_to_history(color)

# Function to check if a color is dark or light
def is_dark_color(hex_color):
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return luminance < 128

# Function to add color to history
def add_to_history(color):
    if len(color_history) >= 5:
        color_history.pop(0)
    color_history.append(color)
    update_history_display()

# Function to update history display
def update_history_display():
    for idx, label in enumerate(history_labels):
        label.config(text=color_history[idx] if idx < len(color_history) else "", bg=color_history[idx] if idx < len(color_history) else "white")

# Function to copy color code to clipboard
def copy_color():
    pyperclip.copy(color_label.cget("text"))
    messagebox.showinfo("Copied!", "Color code copied to clipboard.")

# Function to save the current color to favorites
def save_favorite():
    favorites.append(color_label.cget("text"))
    update_favorites_display()

# Function to update favorites display
def update_favorites_display():
    favorites_label.config(text=", ".join(favorites) if favorites else "No favorites yet")

# Function to reset to the default color
def reset_color():
    update_color("#ffffff")

# Function to apply custom RGB color
def apply_custom_color():
    r, g, b = red_slider.get(), green_slider.get(), blue_slider.get()
    custom_color = f"#{r:02x}{g:02x}{b:02x}"
    update_color(custom_color)

# Initialize the main window
window = tk.Tk()
window.title("Enhanced Color Flip")
window.geometry("500x600")
window.config(bg="white")

# Initialize data
color_history = []
favorites = []

# Widgets
color_label = tk.Label(window, text="Click a button or adjust sliders", font=("Helvetica", 16), bg="white")
color_label.pack(pady=20, fill=tk.X)

flip_button = tk.Button(window, text="Flip Random Color", font=("Helvetica", 14), command=flip_color)
flip_button.pack(pady=10)

copy_button = tk.Button(window, text="Copy Color Code", font=("Helvetica", 14), command=copy_color)
copy_button.pack(pady=10)

save_button = tk.Button(window, text="Save to Favorites", font=("Helvetica", 14), command=save_favorite)
save_button.pack(pady=10)

reset_button = tk.Button(window, text="Reset", font=("Helvetica", 14), command=reset_color)
reset_button.pack(pady=10)

# Sliders for custom RGB color
slider_frame = tk.Frame(window, bg="white")
slider_frame.pack(pady=20)

red_slider = tk.Scale(slider_frame, from_=0, to=255, orient="horizontal", label="Red", bg="white")
red_slider.pack(pady=5)

green_slider = tk.Scale(slider_frame, from_=0, to=255, orient="horizontal", label="Green", bg="white")
green_slider.pack(pady=5)

blue_slider = tk.Scale(slider_frame, from_=0, to=255, orient="horizontal", label="Blue", bg="white")
blue_slider.pack(pady=5)

apply_button = tk.Button(slider_frame, text="Apply Custom Color", font=("Helvetica", 12), command=apply_custom_color)
apply_button.pack(pady=10)

# History display
history_frame = tk.Frame(window, bg="white")
history_frame.pack(pady=20)

tk.Label(history_frame, text="Color History (Last 5):", font=("Helvetica", 14), bg="white").pack(anchor="w")
history_labels = [tk.Label(history_frame, text="", font=("Helvetica", 12), bg="white", width=10) for _ in range(5)]
for label in history_labels:
    label.pack(anchor="w")

# Favorites display
favorites_frame = tk.Frame(window, bg="white")
favorites_frame.pack(pady=20)

tk.Label(favorites_frame, text="Favorites:", font=("Helvetica", 14), bg="white").pack(anchor="w")
favorites_label = tk.Label(favorites_frame, text="No favorites yet", font=("Helvetica", 12), bg="white")
favorites_label.pack(anchor="w")

# Run the Tkinter event loop
window.mainloop()


