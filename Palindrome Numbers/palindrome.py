palindrome_input = input("Enter number ") #takes input from user
reverse_palindrome = palindrome_input[::-1]
if palindrome_input == reverse_palindrome:
    print("Palindrome ye")