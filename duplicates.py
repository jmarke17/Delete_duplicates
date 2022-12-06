# Import the os library to work with files and directories
import os

# Import the hashlib library to calculate the hash of the files
import hashlib

# Define the path of the directory where the files are located
folder_path = "C:/my_files"

# Create a dictionary to store the hash of each file and its name
file_hashes = {}

# Loop through all the files in the directory
for file_name in os.listdir(folder_path):
    # Build the full path of the file
    file_path = os.path.join(folder_path, file_name)

    # Check if the file is a regular file (not a directory or a symbolic link)
    if os.path.isfile(file_path):
        # Open the file in binary reading mode
        with open(file_path, "rb") as f:
            # Calculate the hash of the file
            file_hash = hashlib.sha256(f.read()).hexdigest()

        # Check if the hash of the file already exists in the dictionary
        if file_hash in file_hashes:
            # If the hash already exists, remove the current file
            os.remove(file_path)

            # Show a message on the screen
            print("The file {} is a duplicate and has been deleted".format(file_name))
        else:
            # If the hash does not exist, add it to the dictionary along with the file name
            file_hashes[file_hash] = file_name

# Show a final message
print("All duplicate files in the directory have been deleted")
