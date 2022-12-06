# Delete_duplicates

This Python script can remove duplicate files in a directory, even if they have different names. It uses the os and hashlib libraries to calculate the hash of each file and then compares them to identify and delete the duplicates.

Usage
To use this script, you need to modify the folder_path variable to point to the directory where your files are located. Then you can run the script and it will automatically delete any duplicate files it finds.

Example
Here is an example of how the script would work on a directory with some duplicate files:

Copy code
C:/mis_archivos/file1.txt
C:/mis_archivos/file2.txt
C:/mis_archivos/file3.txt
C:/mis_archivos/file4.txt
C:/mis_archivos/file5.txt
C:/mis_archivos/file6.txt
If file1.txt and file4.txt have the same content, and file2.txt and file5.txt have the same content, but different from the other files, the script would delete file4.txt and file5.txt and the final directory would look like this:

Copy code
C:/mis_archivos/file1.txt
C:/mis_archivos/file2.txt
C:/mis_archivos/file3.txt
