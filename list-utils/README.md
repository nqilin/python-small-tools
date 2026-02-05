# Python List Utils
A lightweight command-line tool for Python, providing **duplicate removal** and **ascending/descending sorting** functions for numeric lists. With complete input validation and user-friendly interaction.

## Core Features
- Accept multiple numeric inputs separated by spaces
- Automatic duplicate removal (keep insertion order, Python 3.7+)
- Custom sort order: ascending (a) / descending (d)
- Comprehensive input validation (reject non-numeric values, empty input)
- Clear step-by-step output (original → deduplicated → final sorted list)

## How to Run
1. Ensure Python 3.x is installed on your computer.
2. Clone this repository or download the `list_utils.py` file.
3. Open terminal/command prompt and navigate to the `list-utils` directory.
4. Run the script with the command:
   ```bash
   python list_utils.py
   ```
5. Follow the on-screen prompts to enter numbers and select sort order.

## Code Structure
- `get_user_numbers()`: Get and validate user input, return a list of floating-point numbers
- `remove_duplicates(num_list)`: Remove duplicates using set, return deduplicated list
- `sort_list(num_list)`: Sort list by user's choice (asc/desc), return sorted list
- `main()`: Main function, control the entire tool flow and interaction

## Tech Stack
- Python 3.x (no third-party libraries, out-of-the-box)

## Usage Example
```
===== Python List Utils - Duplicate Remover & Sorter =====
Enter multiple numbers separated by spaces: 5 2 8 2 9 5 1
Original List: [5.0, 2.0, 8.0, 2.0, 9.0, 5.0, 1.0]
Deduplicated List: [1.0, 2.0, 5.0, 8.0, 9.0]
Sort order - Enter 'a' for ascending, 'd' for descending: d
Final Sorted List: [9.0, 8.0, 5.0, 2.0, 1.0]

Operation completed successfully!
```
