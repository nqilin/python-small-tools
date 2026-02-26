import os
import time
import shutil
from datetime import datetime, timedelta

def get_file_attributes(file_path):
    """Get detailed file attributes (size, creation/modification time)"""
    try:
        # Get file stats
        stats = os.stat(file_path)
        
        # File size in MB (human-readable)
        file_size_mb = round(stats.st_size / (1024 * 1024), 2)
        
        # Convert timestamps to readable format
        create_time = datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
        modify_time = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "path": file_path,
            "size_mb": file_size_mb,
            "create_time": create_time,
            "modify_time": modify_time,
            "extension": os.path.splitext(file_path)[1].lower(),
            "name": os.path.basename(file_path)
        }
    
    except Exception as e:
        print(f"❌ Failed to get attributes for {file_path}: {e}")
        return None

def filter_files_by_size(file_list, min_size_mb=0, max_size_mb=float('inf')):
    """Filter files by size (MB)"""
    filtered = []
    for file_path in file_list:
        attr = get_file_attributes(file_path)
        if attr and min_size_mb <= attr["size_mb"] <= max_size_mb:
            filtered.append(file_path)
    return filtered

def filter_files_by_extension(file_list, extensions):
    """Filter files by extension (case-insensitive)"""
    filtered = []
    extensions = [ext.lower() for ext in extensions]
    for file_path in file_list:
        attr = get_file_attributes(file_path)
        if attr and attr["extension"] in extensions:
            filtered.append(file_path)
    return filtered

def filter_files_by_time(file_list, time_type="modify", days=7):
    """Filter files by creation/modification time (last N days)"""
    filtered = []
    cutoff_time = datetime.now() - timedelta(days=days)
    
    for file_path in file_list:
        attr = get_file_attributes(file_path)
        if not attr:
            continue
        
        # Parse time from file attributes
        if time_type == "create":
            file_time = datetime.strptime(attr["create_time"], "%Y-%m-%d %H:%M:%S")
        else:  # modify
            file_time = datetime.strptime(attr["modify_time"], "%Y-%m-%d %H:%M:%S")
        
        # Check if file is newer than cutoff time
        if file_time >= cutoff_time:
            filtered.append(file_path)
    
    return filtered

def get_all_files_in_directory(dir_path):
    """Get all files in directory (recursive)"""
    file_list = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

def perform_action_on_files(file_list, action="list", target_dir="filtered_files"):
    """Perform action on filtered files (list/copy/move)"""
    if not file_list:
        print("❌ No files match the filter criteria!")
        return 0
    
    # Create target directory if needed
    if action in ["copy", "move"] and not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    success_count = 0
    print(f"\n📋 Found {len(file_list)} files matching criteria:")
    
    for file_path in file_list:
        try:
            if action == "list":
                # Just list the file with attributes
                attr = get_file_attributes(file_path)
                print(f"- {attr['name']} | Size: {attr['size_mb']}MB | Modified: {attr['modify_time']}")
                success_count += 1
            
            elif action == "copy":
                # Copy file to target directory
                dest_path = os.path.join(target_dir, os.path.basename(file_path))
                # Handle duplicate filenames
                counter = 1
                while os.path.exists(dest_path):
                    name, ext = os.path.splitext(os.path.basename(file_path))
                    dest_path = os.path.join(target_dir, f"{name}_{counter}{ext}")
                    counter += 1
                shutil.copy2(file_path, dest_path)
                print(f"✅ Copied: {file_path} → {dest_path}")
                success_count += 1
            
            elif action == "move":
                # Move file to target directory
                dest_path = os.path.join(target_dir, os.path.basename(file_path))
                # Handle duplicate filenames
                counter = 1
                while os.path.exists(dest_path):
                    name, ext = os.path.splitext(os.path.basename(file_path))
                    dest_path = os.path.join(target_dir, f"{name}_{counter}{ext}")
                    counter += 1
                shutil.move(file_path, dest_path)
                print(f"✅ Moved: {file_path} → {dest_path}")
                success_count += 1
        
        except Exception as e:
            print(f"❌ Failed to process {file_path}: {e}")
    
    return success_count

def main():
    """Main function: run file filter tool"""
    print("===== Python File Filter Tool v1.0 =====")
    print("Filter files by size/extension/modified time and perform actions (list/copy/move)\n")
    
    # Get target directory
    while True:
        dir_path = input("Enter target directory path: ").strip()
        if os.path.isdir(dir_path):
            break
        print("❌ Invalid directory path! Please try again.")
    
    # Get all files in directory
    print(f"\n🔍 Scanning directory: {dir_path}")
    all_files = get_all_files_in_directory(dir_path)
    print(f"✅ Found {len(all_files)} total files")
    
    # Filter options
    filtered_files = all_files
    
    # 1. Size filter
    while True:
        use_size_filter = input("\nFilter by file size? (Y/N): ").strip().upper()
        if use_size_filter == "Y":
            try:
                min_size = float(input("Minimum size (MB, enter 0 for no limit): "))
                max_size = float(input("Maximum size (MB, enter 0 for no limit): "))
                if max_size == 0:
                    max_size = float('inf')
                filtered_files = filter_files_by_size(filtered_files, min_size, max_size)
                print(f"✅ Filtered to {len(filtered_files)} files (size: {min_size}-{max_size}MB)")
                break
            except ValueError:
                print("❌ Please enter valid numbers!")
        elif use_size_filter == "N":
            break
        else:
            print("❌ Please enter Y or N!")
    
    # 2. Extension filter
    while True:
        use_ext_filter = input("\nFilter by file extension? (Y/N): ").strip().upper()
        if use_ext_filter == "Y":
            exts = input("Enter extensions (comma-separated, e.g., .txt,.jpg): ").strip().split(",")
            exts = [ext if ext.startswith(".") else f".{ext}" for ext in exts]  # Ensure dot prefix
            filtered_files = filter_files_by_extension(filtered_files, exts)
            print(f"✅ Filtered to {len(filtered_files)} files (extensions: {', '.join(exts)})")
            break
        elif use_ext_filter == "N":
            break
        else:
            print("❌ Please enter Y or N!")
    
    # 3. Time filter
    while True:
        use_time_filter = input("\nFilter by modified time? (Y/N): ").strip().upper()
        if use_time_filter == "Y":
            try:
                days = int(input("Files modified in last N days (enter number): "))
                filtered_files = filter_files_by_time(filtered_files, "modify", days)
                print(f"✅ Filtered to {len(filtered_files)} files (modified in last {days} days)")
                break
            except ValueError:
                print("❌ Please enter valid number!")
        elif use_time_filter == "N":
            break
        else:
            print("❌ Please enter Y or N!")
    
    # Select action
    while True:
        print("\nSelect action to perform on filtered files:")
        print("1. List files (default)")
        print("2. Copy files to filtered_files/")
        print("3. Move files to filtered_files/")
        try:
            action_choice = int(input("Enter choice (1-3): ").strip())
            if action_choice == 1:
                action = "list"
                break
            elif action_choice == 2:
                action = "copy"
                break
            elif action_choice == 3:
                action = "move"
                break
            else:
                print(f"❌ Please enter 1, 2, or 3!")
        except ValueError:
            action = "list"
            break
    
    # Perform action
    print("\n🚀 Processing files...")
    success_count = perform_action_on_files(filtered_files, action)
    
    # Summary
    print(f"\n🎉 Processing completed!")
    print(f"✅ Successfully processed: {success_count}/{len(filtered_files)} files")
    if action in ["copy", "move"]:
        print(f"📂 Target directory: {os.path.abspath('filtered_files')}")
    print("\n👋 Thank you for using File Filter Tool!")

if __name__ == "__main__":
    main()
