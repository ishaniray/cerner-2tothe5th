# cerner_2^5_2019

# lines of code: 29

"""
Rövarspråket (English: The Robber Language) is a Swedish language game.
Every consonant is doubled, and an 'o' is inserted in-between. Vowels are left intact.
For example, 'stubborn' in Rövarspråket would be expressed as 'sostotubobboborornon'.
"""

vowels = ['a', 'e', 'i', 'o', 'u']
punctuationMarks = [' ', ',', ';', '.', '!', '-', '"', '\'', ':', '(', ')']  

choice = int(input("ROVARSPRAKET\n------------\n\n1. Encode\n2. Decode\n\nEnter your choice (1 or 2): "))

if choice == 1:
    string = input("\nEnter a string: ")

    rs_list = []    # list to hold output

    for letter in string:
        rs_list.append(letter)
        if letter.lower() not in vowels and letter not in punctuationMarks: # letter is a consonant
            rs_list.append('o')
            rs_list.append(letter)

    rs_string = ''.join(rs_list)    # converting list to string

    if string.isupper():
        rs_string = rs_string.upper()

    print("\n" + string + " in Rövarspråket: " + rs_string)

else:
    rs_string = input("\nEnter a Rövarspråket string: ")

    str_list = [] # list to hold output

    i = 0
    while i < len(rs_string):
        str_list.append(rs_string[i])
        if rs_string[i].lower() in vowels or rs_string[i] in punctuationMarks:
            i = i + 1
        else:
            i = i + 3   # if a consonant is encountered, skip the next two letters

    string = ''.join(str_list)  # converting list to string

    if rs_string.isupper():
        string = string.upper()

    print("\nThe decoded string is: " + string)

# end of program
