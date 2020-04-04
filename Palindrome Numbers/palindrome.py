checked = False
while checked == False:
    palindrome_input = input("Enter number ") #takes input from user
    if len(palindrome_input)<=20: #checks if palindrome is an integer up to 20 digits
        checked = True

nextPalindrome = False

while nextPalindrome == False:
    palindrome_input = int(palindrome_input) + 1 #increments number by 1
    palindrome_input = str(palindrome_input) #converts back to a string so that it can be reversed below
    reverse_palindrome = palindrome_input[::-1] #reversed
    if palindrome_input == reverse_palindrome: #checks if it is a palindrome
        print("Next Palindrome is " + palindrome_input) #if palindrome then outputs it to the user
        nextPalindrome = True #breaks loop