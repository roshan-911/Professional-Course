"""
Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters: 3
No. of Lower case Characters : 12

Note: If you can take string input from user you can do it .
"""
def countUpperLower(paragraph):
    # Create a dictionary 'count' to store the count of upper and lower case characters
    count = {
      "UPPER_CASE": 0,
      "LOWER_CASE": 0
            }
    # Loop through the string 
    for character in paragraph:
        if character.isupper():
            count["UPPER_CASE"] += 1
        elif character.islower():
            count["LOWER_CASE"] += 1
        else:
            pass
    
    print("Original String: ", paragraph)
    print("No. of Upper case characters: ", count["UPPER_CASE"])
    print("No. of Lower case Characters: ", count["LOWER_CASE"])

userInput = input ("Please Enter string to count upper or lower case:")
# Call the 'string_test' function with the input string 'The quick Brown Fox'
countUpperLower(userInput)