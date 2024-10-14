import tkinter as tk
from tkinter import Text, Frame, Scrollbar
from tkinter import ttk
import ccnp  # Import your original module
import json

# Load configuration from a JSON file
with open('config.json') as config_file:
    config = json.load(config_file)

# Define the files dictionary from the JSON config
files = config['files']

# Define colors for the keywords
keyword_colors = config['keyword_colors']
title_color = config['title_color']

def read_file_content(file_name):
    """Read the content of a specified text file and return it as a list of lines."""
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]  # Strip whitespace from each line
    except FileNotFoundError:
        return ["Error: File not found."]
    except Exception as e:
        return [f"Error reading file: {str(e)}"]

def format_content(lines):
    """Format the content for better readability."""
    formatted_lines = []
    for line in lines:
        stripped_line = line.strip()
        formatted_lines.append(stripped_line + "\n")  # Preserve content
    return "\n".join(formatted_lines)

def show_content(file_choice):
    # Clear the text area
    text_area.delete(1.0, tk.END)

    # Get the selected file and read its content
    if file_choice in files:
        lines = read_file_content(files[file_choice])
        formatted_content = format_content(lines)  # Format the content

        # Insert the formatted content into the text area
        for line_num, line in enumerate(formatted_content.splitlines()):
            text_area.insert(tk.END, line + "\n")

            # Color keywords
            for keyword, color in keyword_colors.items():
                start_index = line.find(keyword)
                while start_index != -1:
                    end_index = start_index + len(keyword)
                    text_area.tag_add(keyword, f"{line_num + 1}.{start_index}", f"{line_num + 1}.{end_index}")
                    start_index = line.find(keyword, end_index)

            # Apply title color if it matches specific patterns
            if line.startswith("###") or line.startswith("--"):
                text_area.tag_add("title", f"{line_num + 1}.0", f"{line_num + 1}.end")

    else:
        text_area.insert(tk.END, "Invalid choice.")

# Create the main window
window = tk.Tk()
window.title("CCNP File Viewer")
window.geometry("600x400")
window.configure(bg="#282828")

# Create a frame for the text area and scrollbar
frame = Frame(window)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Configure the text area with a more modern font
text_area = Text(frame, wrap=tk.WORD, bg="#1d2021", fg="#ebdbb2", font=("Verdana", 13), bd=0, insertbackground='white')
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a ttk scrollbar
scrollbar = ttk.Scrollbar(frame, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)

# Style the scrollbar
style = ttk.Style()
style.theme_use('default')
style.configure("TScrollbar", background="#504945", troughcolor="#3c3836", arrowcolor="#ebdbb2")

# Configure text tags for keywords
for keyword, color in keyword_colors.items():
    text_area.tag_configure(keyword, font=("Verdana", 14, "bold"), foreground=color)

# Configure text tag for titles
text_area.tag_configure("title", font=("Verdana", 14, "bold"), foreground=title_color)

# Create buttons for file selection
buttons_frame = Frame(window, bg="#282828")
buttons_frame.pack(pady=10)

for choice, name in files.items():
    button = tk.Button(buttons_frame, text=name[:-4],  # Display name without ".txt"
                       command=lambda c=choice: show_content(c),
                       bg="#504945", fg="#ebdbb2", activebackground="#3c3836", activeforeground="#ebdbb2")
    button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
window.mainloop()
