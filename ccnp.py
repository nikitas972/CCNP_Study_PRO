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
