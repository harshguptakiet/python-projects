import re

def extract_pattern(s):
    # Regular expression pattern to match the required substrings
    pattern = r'(.).\1'
    matches = re.findall(pattern, s)
    return matches

# Example usage
s = "abacabaacacacacacac"
result = extract_pattern(s)
print(result)  # Output: ['a', 'a']
