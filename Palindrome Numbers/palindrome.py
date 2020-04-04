palindrome_input = input("Enter number ") #takes input from user
reverse_palindrome = palindrome_input[::-1] #reverses input

if palindrome_input==reverse_palindrome: #checks if input and reverse are equal
    print("This number is a palindrome")