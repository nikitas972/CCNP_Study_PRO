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

def color_keywords(text_area, line, line_num):
    """Apply color to keywords in the given line."""
    for keyword, color in keyword_colors.items():
        start_index = line.find(keyword)
        while start_index != -1:
            end_index = start_index + len(keyword)
            text_area.tag_add(keyword, f"{line_num + 1}.{start_index}", f"{line_num + 1}.{end_index}")
            start_index = line.find(keyword, end_index)

def apply_title_color(text_area, line, line_num):
    """Apply title color if it matches specific patterns."""
    if line.startswith("###") or line.startswith("--"):
        text_area.tag_add("title", f"{line_num + 1}.0", f"{line_num + 1}.end")
    elif line.startswith("**") or line.startswith("***"):
        text_area.tag_add("title", f"{line_num + 1}.0", f"{line_num + 1}.end")
