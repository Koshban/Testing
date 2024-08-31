"""
**Balanced Parentheses:**
   Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid and return a boolean. 
   An input string is valid if the brackets are closed in the correct order.
   Here are the rules for a string to be balanced:

An opening parenthesis must have a corresponding closing parenthesis of the same type: ( corresponds to ), { corresponds to } and [ corresponds to ].
Opening parentheses must be closed in the correct order: the last opened parenthesis must be closed first (Last In, First Out).
To illustrate, here are some examples:

Valid (balanced) strings:

(): Single pair of parentheses, correctly closed.
{}[](): Multiple types of parentheses, correctly closed.
{[()]}: Correctly nested and closed parentheses.
Invalid (unbalanced) strings:

(]: Parentheses are not of the same type.
([): Parentheses are not closed in the correct order.
(((): A parenthesis is not closed.
"""

def find_balanced_parenthese(input: str):
    input_list = list(input)
    print(input_list)
    comparison_data = { ')':'(',
                        '}':'{',
                        ']':'['
                        }
    stack = []
    for item in input_list:
        if item in comparison_data.values():
            stack.append(item)
        elif item in comparison_data.keys():
            if stack is None or comparison_data[item] != stack.pop():
                return False
        else:
            return False
       
    return len(stack) == 0

if __name__ == "__main__":
    # Test data for balanced parentheses
    test_data = [
        ("()", True), # Example 1: Balanced
        ("()[]{}", True), # Example 2: Balanced with multiple types
        ("(]", False), # Example 3: Not balanced - different types of parentheses
        ("([)]", False), # Example 4: Not balanced - incorrect order
        ("{[]}", True), # Example 5: Balanced - correct order and type
        ("({[(", False), # Example 6: Not balanced - not all parentheses are closed
        ("", True), # Example 7: An empty string is considered balanced
    ]

    for data, result in test_data:
        # print(find_balanced_parenthese(input=data))
        assert result == find_balanced_parenthese(input=data), f"Failed for {data}"