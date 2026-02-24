import random
import string

def get_password_length():
    """Get password length from user with input validation"""
    while True:
        try:
            length = int(input("Enter password length (8-20 characters): "))
            if 8 <= length <= 20:
                return length
            else:
                print("❌ Password length must be between 8 and 20 characters!")
        except ValueError:
            print("❌ Please enter a valid number!")

def get_password_options():
    """Get user-selected password character options"""
    options = {
        "uppercase": False,
        "lowercase": False,
        "digits": False,
        "symbols": False
    }
    
    print("\nSelect character types to include (at least one required):")
    while True:
        options["uppercase"] = input("1. Include uppercase letters (Y/N): ").strip().upper() == "Y"
        options["lowercase"] = input("2. Include lowercase letters (Y/N): ").strip().upper() == "Y"
        options["digits"] = input("3. Include digits (Y/N): ").strip().upper() == "Y"
        options["symbols"] = input("4. Include special symbols (!@#$%^&*) (Y/N): ").strip().upper() == "Y"
        
        # Check if at least one option is selected
        if any(options.values()):
            return options
        else:
            print("❌ At least one character type must be selected!\n")

def generate_password(length, options):
    """Generate random password based on user options"""
    # Build character pool
    char_pool = ""
    if options["uppercase"]:
        char_pool += string.ascii_uppercase
    if options["lowercase"]:
        char_pool += string.ascii_lowercase
    if options["digits"]:
        char_pool += string.digits
    if options["symbols"]:
        char_pool += "!@#$%^&*"
    
    # Generate password with random selection
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    """Main function: run password generator"""
    print("===== Python Password Generator v1.0 =====")
    
    # Get user configuration
    length = get_password_length()
    options = get_password_options()
    
    # Generate and display password
    password = generate_password(length, options)
    print(f"\n✅ Generated password: {password}")
    
    # Ask to continue
    while True:
        choice = input("\nGenerate another password? (Y/N): ").strip().upper()
        if choice == "Y":
            length = get_password_length()
            options = get_password_options()
            password = generate_password(length, options)
            print(f"\n✅ Generated password: {password}")
        elif choice == "N":
            print("\n👋 Thank you for using Password Generator!")
            break
        else:
            print("❌ Please enter Y or N!")

if __name__ == "__main__":
    main()
