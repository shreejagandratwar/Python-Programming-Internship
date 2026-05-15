# Program to check whether a string is palindrome or not

text = input("Enter a word to check palindrome: ")

reverse_text = text[::-1]

print("Original word:", text)
print("Reversed word:", reverse_text)

if text == reverse_text:
    print("Result: The entered word is a palindrome")
else:
    print("Result: The entered word is not a palindrome")