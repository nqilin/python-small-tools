# batch_rename.py
import os

def batch_rename(folder_path, prefix, start_num=1):
    """
    Core Function: Batch rename all files in the specified folder to "prefix + sequence number"
    :param folder_path: Absolute/relative path of the target folder
    :param prefix: Prefix for the renamed files
    :param start_num: Starting number of the sequence, default is 1
    """
    # Input Validation: Check if the folder exists
    if not os.path.isdir(folder_path):
        print("Error: Folder path does not exist!")
        return
    
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if not file_list:
        print("Error: No files in the folder!")
        return
    
    # Core Logic: Traverse files and rename in batch
    for idx, file_name in enumerate(file_list, start=start_num):
        # Split file name and extension
        file_ext = os.path.splitext(file_name)[1]
        new_name = f"{prefix}_{idx}{file_ext}"
        # Build old and new paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        # Execute rename
        os.rename(old_path, new_path)
        print(f"Renamed successfully: {file_name} → {new_name}")

if __name__ == "__main__":
    # Example: Rename files in "test" folder with prefix "file"
    target_folder = input("Enter the folder path to rename: ")
    name_prefix = input("Enter the rename prefix: ")
    batch_rename(target_folder, name_prefix)
