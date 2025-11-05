'''
Problem Statement:

Given a sequence of integers, determine if it is valid according to these rules:
1. A sequence must have at least 2 numbers
2. A sequence is valid if it is either:
   - Strictly increasing, where each subsequent number is 1-3 units larger than the previous number
   - Strictly decreasing, where each subsequent number is 1-3 units smaller than the previous number
3. If the sequence is not valid, determine if it can become valid by removing exactly one number from any position

For example:
- [1, 3, 5] is valid (increasing with differences of 2)
- [7, 5, 3] is valid (decreasing with differences of 2)
- [1, 5, 3] is not valid (neither increasing nor decreasing)
- [1, 5, 2, 4] could become valid by removing 5, resulting in [1, 2, 4]

Write a program that determines whether a given sequence is either:
- Valid without any modifications
- Can be made valid by removing exactly one number
- Cannot be made valid even with one removal

'''
def is_valid_sequence(row):
    """Check if sequence is valid without removing any numbers"""
    if len(row) < 2:
        return False
    
    # Check if sequence is increasing
    increasing_valid = True
    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]
        if diff < 1 or diff > 3:
            increasing_valid = False
            break
    
    # Check if sequence is decreasing
    decreasing_valid = True
    for i in range(len(row) - 1):
        diff = row[i] - row[i + 1]
        if diff < 1 or diff > 3:
            decreasing_valid = False
            break
    
    return increasing_valid or decreasing_valid

def is_valid_with_removal(row):
    """Check if sequence becomes valid after removing one number"""
    for i in range(len(row)):
        test_row = row[:i] + row[i + 1:]
        print(f"Testing removal at index {i}: {test_row}")
        if is_valid_sequence(test_row):
            print(f"Valid after removing element at index {i}")
            return True
    return False

def check_sequence(row):
    """Main function to check if sequence is valid either directly or after removing one number"""
    print(f"\nChecking sequence: {row}")
    if is_valid_sequence(row):
        print("Valid without removal")
        return True
    print("Not valid without removal, trying removals...")
    return is_valid_with_removal(row)

if __name__ == "__main__":

    # Test the problematic case
    sequence = [6, 9, 10, 12, 15, 16, 15, 20]
    sequence = [6, 12, 8,9, 11]
    result = check_sequence(sequence)
    print(f"Final result: {result}")