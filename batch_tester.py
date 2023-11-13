import subprocess
import os

# Contains the relative path to the input folder
io_folder = os.path.join(os.path.dirname(__file__), "INPUT")

def run_main(input_text, output_file):
    # Run main.py as a subprocess, passing input_text as input
    process = subprocess.Popen(
        ['python', 'main.py'], 
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )

    output, _ = process.communicate(input_text)
    
    # Print the output of main.py
    print(output)
    
    # Write the output to a file
    with open(output_file, 'w') as file:
        file.write(output)

if __name__ == "__main__":
    # Check if the input/output folder exists
    if not os.path.exists(io_folder):
        print(f"Input folder {io_folder} does not exist.")
        exit(1)

    # Check each folder in the input folder
    folders = os.listdir(io_folder)
    folders_paths = [os.path.join(io_folder, folder) for folder in folders]

    # 2D list of input files per folder

    # For each folder, and each input in that folder, run the main.py
    # Create an /output folder in each folder to output corresponding output

    for folder in folders_paths:
        # Check if the output folder exists
        output_folder = os.path.join(folder, "output")
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        # Get all the input files in the folder under /input
        input_files = os.listdir(os.path.join(folder, "input"))
        input_files_paths = [os.path.join(folder, "input", input_file) for input_file in input_files]

        # For each input file, run the main.py
        for input_file in input_files_paths:
            # Get the output file name based on the input file (first two digits)
            # e.g.: 00input.txt -> 00output.txt
            output_file = os.path.join(output_folder, input_file.split('/')[-1][:2] + "output.txt")

            # Read the input file
            with open(input_file, 'r') as file:
                input_text = file.read()

            # Run the main.py
            run_main(input_text, output_file)

