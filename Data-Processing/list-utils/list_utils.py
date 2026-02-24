# Python List Utils - Duplicate Remover & Sorter
# Supports: input multiple numbers, remove duplicates, sort (asc/desc)
# With input validation and user-friendly interaction
# Author: nqilin
# Date: 2026

def get_user_numbers():
    """Get multiple numbers from user input, return a list of floats"""
    while True:
        user_input = input("Enter multiple numbers separated by spaces: ")
        # Split input into string list, remove empty strings
        str_list = [s for s in user_input.split() if s]
        if not str_list:
            print("Error! No input detected. Please enter at least one number.")
            continue
        
        # Convert string to float, handle invalid input
        num_list = []
        valid = True
        for s in str_list:
            try:
                num = float(s)
                num_list.append(num)
            except ValueError:
                print(f"Error! '{s}' is not a valid number. Please try again.")
                valid = False
                break
        if valid:
            return num_list

def remove_duplicates(num_list):
    """Remove duplicates from list, return a new list (keep order)"""
    # Convert to set for deduplication, then back to list (Python 3.7+ keeps order)
    deduplicated_list = list(set(num_list))
    return deduplicated_list

def sort_list(num_list):
    """Sort the list by user's choice (ascending/descending), return sorted list"""
    while True:
        sort_choice = input("Sort order - Enter 'a' for ascending, 'd' for descending: ").lower()
        if sort_choice == 'a':
            num_list.sort()  # Ascending sort
            return num_list
        elif sort_choice == 'd':
            num_list.sort(reverse=True)  # Descending sort
            return num_list
        else:
            print("Error! Invalid input. Please enter 'a' or 'd'.")

def main():
    print("===== Python List Utils - Duplicate Remover & Sorter =====")
    # Step 1: Get valid numbers from user
    original_list = get_user_numbers()
    print(f"\nOriginal List: {original_list}")
    
    # Step 2: Remove duplicates
    deduplicated_list = remove_duplicates(original_list)
    print(f"Deduplicated List: {deduplicated_list}")
    
    # Step 3: Sort the list
    sorted_list = sort_list(deduplicated_list)
    print(f"Final Sorted List: {sorted_list}")
    
    print("\nOperation completed successfully!")

if __name__ == "__main__":
    main()
