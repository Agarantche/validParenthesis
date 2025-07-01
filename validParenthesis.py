class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # A dictionary to map closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:  # Iterate through each character in the string
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping.keys():  # If it's a closing bracket
                if not stack or stack.pop() != mapping[char]:
                    # If stack is empty or the popped element doesn't match
                    return False
    

        # After iterating through the entire string, the stack should be empty
        # if all brackets were properly closed.
        return not stack
