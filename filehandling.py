# File Read & Write Challenge with Error Handling

def modify_file(input_file, output_file):
    try:
        # Try to open and read the input file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (example: make everything uppercase)
        modified_content = content.upper()

        # Write modified content into a new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"File processed successfully! Modified file saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for file '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Ask the user for input filename
input_file = input("Enter the name of the file to read: ")
output_file = "modified_" + input_file

modify_file(input_file, output_file)
