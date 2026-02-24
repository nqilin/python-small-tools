# Password Generator
A lightweight, secure password generator with custom character options and strict input validation. Designed for daily use and Python basic development practice.

## 📋 Features
- Support password length range: 8-20 characters (with validation)
- Customizable character types:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special symbols (!@#$%^&*)
- Complete input validation (prevent invalid length/empty selection)
- Loop execution with manual exit
- Modular code structure (separate functions for different logic)

## 🛠️ How to Run
1. Ensure Python 3.8+ is installed on your system
2. Navigate to the tool directory:
   ```bash
   cd Daily-Tools/Password-Generator
   ```
3. Run the script:
   ```bash
   python password_generator.py
   ```
4. Follow the interactive prompts to configure your password

## 📸 Running Example
```
===== Python Password Generator v1.0 =====
Enter password length (8-20 characters): 12

Select character types to include (at least one required):
1. Include uppercase letters (Y/N): Y
2. Include lowercase letters (Y/N): Y
3. Include digits (Y/N): Y
4. Include special symbols (!@#$%^&*) (Y/N): N

✅ Generated password: 8s9K7m8L2p7X

Generate another password? (Y/N): N

👋 Thank you for using Password Generator!
```

## 📝 Development Details
- Uses Python built-in `random` module for secure random selection
- Strict input validation to ensure password security and usability
- Follows modular programming principles (single responsibility per function)
- Cross-platform compatible (Windows/macOS/Linux)

## 📌 Dependencies
- No external dependencies (only Python standard library)
- Python Version: 3.8+ (recommended)
