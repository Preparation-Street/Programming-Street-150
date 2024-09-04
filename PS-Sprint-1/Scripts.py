import os
import re

def sanitize_filename(filename):
    """
    Sanitize the filename by removing or replacing invalid characters.
    """
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def create_files_from_data(data_file):
    # Read the data from the file
    with open(data_file, 'r') as file:
        content = file.read()

    # Split content into problems based on headers (assuming double newlines as separator)
    problems = content.strip().split('\n\n')

    # Ensure the output directory exists
    output_dir = 'problems'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for problem in problems:
        lines = problem.split('\n')
        if len(lines) < 5:
            continue
        
        # Extract problem name and code
        problem_name = lines[0].strip()
        sanitized_problem_name = sanitize_filename(problem_name)
        problem_code = '\n'.join(lines[4:]).strip()
        
        # Create a file for each problem
        file_name = os.path.join(output_dir, f"{sanitized_problem_name}.py")
        with open(file_name, 'w') as file:
            file.write(f"# Problem: {lines[0]}\n")
            file.write(f"# **Problem Description:** {lines[1]}\n")
            file.write(f"# **Problem Example:** {lines[2]}\n")
            file.write(f"# **Example Explanation:** {lines[3]}\n\n")
            file.write(f"# **Python Code:**\n")
            file.write(problem_code + '\n')  # Ensure the code is written as is with proper indentation

    print(f"Files have been created in the '{output_dir}' directory.")

# Execute the script
create_files_from_data('F:/Programming Street - 150/Programming-Street-150/PS-Sprint-1/Data.txt')
