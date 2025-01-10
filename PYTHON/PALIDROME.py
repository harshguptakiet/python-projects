def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

word = input("enter a word:")
if is_palindrome(word):
   print(f"{word} is a palindrome.")
else:
    print(f"{word} is no a palindrome,")
