import tkinter as tk
from tkinter import Text, Frame, Scrollbar, ttk
import ccnp  # Import your original module

# Define the files dictionary
files = {
    '1': 'VLANS.txt',
    '2': 'TRUNK.txt',
    '3': 'MAC-TABLES.txt',
    '4': 'Switching-CEF-TCAM.txt',
    '5': 'spanning-tree.txt',
    '6': 'port-states.txt'
}

# Define colors for the keywords
keyword_colors = {
    "ARP": "#fb4934",  
    "CEF": "#fabd2f",   
    "CAM": "#b8bb26",  
    "FIB": "#83a598",   
    "MAC": "#d3869b",   
    "VLANS": "#8ec07c", 
    "RIB": "#458588",   
    "TCAM": "#b16286",  
    "STP": "#fb4934",   
    "VLAN": "#fabd2f",  
    "PVST": "#b8bb26",  
    "PVST+": "#83a598",  
    "RSTP": "#d3869b",  
    "MST": "#fb4934",    
    "802.1": "#fabd2f",  
    "802.1SS": "#b8bb26",  
    "802.1D": "#83a598",  
    "802.1Q": "#d3869b",  
    "BPDU": "#fb4934",   
    "VLANs": "#8ec07c",  
    "IP": "#b8bb26",     
    "AIB": "#83a598",    
}

# Color for titles
title_color = "#8ec07c"

def format_content(lines):
    """Format the content for better readability."""
    formatted_lines = []
    for line in lines:
        stripped_line = line.strip()
        formatted_lines.append(stripped_line + "\n")  # Preserve content
    return "\n".join(formatted_lines)

def show_content(text_area, file_choice):
    # Clear the text area
    text_area.delete(1.0, tk.END)

    # Get the selected file and read its content
    if file_choice in files:
        lines = ccnp.read_file_content(files[file_choice])
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

# Create text area and scrollbar
text_area = Text(frame, wrap=tk.WORD, bg="#1d2021", fg="#ebdbb2", font=("Verdana", 13), bd=0, insertbackground='white')
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(frame, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)

# Configure text tags for keywords
for keyword, color in keyword_colors.items():
    text_area.tag_configure(keyword, font=("Verdana", 14, "bold"), foreground=color)

# Configure text tag for titles
text_area.tag_configure("title", font=("Verdana", 14, "bold"), foreground=title_color)

# Create buttons for file selection
buttons_frame = Frame(window, bg="#282828")
buttons_frame.pack(pady=10)

for choice, name in files.items():
    button = tk.Button(buttons_frame, text=name[:-4],
                       command=lambda c=choice: show_content(text_area, c),
                       bg="#504945", fg="#ebdbb2", activebackground="#3c3836", activeforeground="#ebdbb2")
    button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
window.mainloop()
