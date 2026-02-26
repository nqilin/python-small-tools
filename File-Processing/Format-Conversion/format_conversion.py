import os
import csv
from PIL import Image
import chardet

# Supported conversion types
SUPPORTED_CONVERSIONS = {
    "txt_to_md": "Text file to Markdown",
    "csv_to_txt": "CSV file to Text",
    "jpg_to_png": "JPG image to PNG",
    "png_to_jpg": "PNG image to JPG"
}

def detect_file_encoding(file_path):
    """Detect file encoding to handle different language files"""
    with open(file_path, 'rb') as f:
        raw_data = f.read(10000)
        result = chardet.detect(raw_data)
        return result['encoding'] or 'utf-8'

def txt_to_md(input_path, output_path):
    """Convert TXT file to Markdown format"""
    try:
        # Detect file encoding
        encoding = detect_file_encoding(input_path)
        
        # Read TXT content
        with open(input_path, 'r', encoding=encoding) as f:
            content = f.read()
        
        # Add Markdown basic formatting
        md_content = f"# Converted from {os.path.basename(input_path)}\n\n{content}"
        
        # Write to MD file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"✅ Converted: {input_path} → {output_path}")
        return True
    
    except Exception as e:
        print(f"❌ Failed to convert {input_path}: {e}")
        return False

def csv_to_txt(input_path, output_path, delimiter='|'):
    """Convert CSV file to formatted Text file"""
    try:
        # Detect CSV encoding
        encoding = detect_file_encoding(input_path)
        
        # Read CSV and write to TXT
        with open(input_path, 'r', encoding=encoding) as csv_file, \
             open(output_path, 'w', encoding='utf-8') as txt_file:
            
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                # Join columns with delimiter
                txt_line = delimiter.join(row) + '\n'
                txt_file.write(txt_line)
        
        print(f"✅ Converted: {input_path} → {output_path}")
        return True
    
    except Exception as e:
        print(f"❌ Failed to convert {input_path}: {e}")
        return False

def image_conversion(input_path, output_path, target_format):
    """Convert image between JPG and PNG"""
    try:
        # Open image with Pillow
        with Image.open(input_path) as img:
            # Convert RGBA to RGB for JPG (PNG supports transparency, JPG does not)
            if target_format.lower() == 'jpg' and img.mode == 'RGBA':
                img = img.convert('RGB')
            
            # Save in target format
            img.save(output_path, target_format.upper())
        
        print(f"✅ Converted: {input_path} → {output_path}")
        return True
    
    except Exception as e:
        print(f"❌ Failed to convert {input_path}: {e}")
        return False

def get_file_list(input_dir, file_ext):
    """Get list of files with specific extension from directory"""
    file_list = []
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(file_ext):
            file_list.append(os.path.join(input_dir, filename))
    return file_list

def main():
    """Main function: run file format conversion tool"""
    print("===== Python File Format Conversion Tool v1.0 =====")
    print("Supported conversions:")
    for idx, (key, desc) in enumerate(SUPPORTED_CONVERSIONS.items(), 1):
        print(f"{idx}. {desc} ({key})")
    print()
    
    # Get user selection
    while True:
        try:
            choice = int(input("Enter conversion type (1-4): "))
            if 1 <= choice <= len(SUPPORTED_CONVERSIONS):
                conversion_type = list(SUPPORTED_CONVERSIONS.keys())[choice-1]
                break
            else:
                print(f"❌ Please enter a number between 1 and {len(SUPPORTED_CONVERSIONS)}!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Get input directory/file
    input_path = input("\nEnter input file/directory path: ").strip()
    if not os.path.exists(input_path):
        print("❌ Input path does not exist!")
        return
    
    # Create output directory
    output_dir = "converted_files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process single file or batch files
    if os.path.isfile(input_path):
        files_to_convert = [input_path]
    else:
        # Determine file extension based on conversion type
        ext_mapping = {
            "txt_to_md": ".txt",
            "csv_to_txt": ".csv",
            "jpg_to_png": ".jpg",
            "png_to_jpg": ".png"
        }
        files_to_convert = get_file_list(input_path, ext_mapping[conversion_type])
        if not files_to_convert:
            print(f"❌ No {ext_mapping[conversion_type]} files found in directory!")
            return
    
    # Convert files
    success_count = 0
    for file_path in files_to_convert:
        # Generate output filename
        filename = os.path.basename(file_path)
        name_without_ext = os.path.splitext(filename)[0]
        
        # Determine output extension
        ext_mapping = {
            "txt_to_md": ".md",
            "csv_to_txt": ".txt",
            "jpg_to_png": ".png",
            "png_to_jpg": ".jpg"
        }
        output_filename = name_without_ext + ext_mapping[conversion_type]
        output_path = os.path.join(output_dir, output_filename)
        
        # Perform conversion
        if conversion_type == "txt_to_md":
            if txt_to_md(file_path, output_path):
                success_count += 1
        elif conversion_type == "csv_to_txt":
            if csv_to_txt(file_path, output_path):
                success_count += 1
        elif conversion_type == "jpg_to_png":
            if image_conversion(file_path, output_path, "png"):
                success_count += 1
        elif conversion_type == "png_to_jpg":
            if image_conversion(file_path, output_path, "jpg"):
                success_count += 1
    
    # Conversion summary
    print(f"\n🎉 Conversion completed!")
    print(f"✅ Success: {success_count}/{len(files_to_convert)}")
    print(f"📂 All converted files saved to: {os.path.abspath(output_dir)}")
    print("\n👋 Thank you for using Format Conversion Tool!")

if __name__ == "__main__":
    main()
