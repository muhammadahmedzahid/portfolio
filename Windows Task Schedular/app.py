import shutil
import os


def copy_file(src_file_path, dest_dir_path):
    """
    Let say if you have a directory and a file and if you want to move the files from one directory to another
    then you can use the below directory.
    :param src_file_path:
    :param dest_dir_path:
    :return:
    """
    try:
        # Ensure the source file exists
        if not os.path.isfile(src_file_path):
            raise FileNotFoundError(f"Source file not found: {src_file_path}")

        # Ensure the destination directory exists, if not, create it
        if not os.path.exists(dest_dir_path):
            os.makedirs(dest_dir_path)

        # Copy the file
        shutil.copy(src_file_path, dest_dir_path)
        print(f"File copied from {src_file_path} to {dest_dir_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
src_file_path = '/path/to/source/file.txt'
dest_dir_path = '/path/to/destination/directory'
copy_file(src_file_path, dest_dir_path)
