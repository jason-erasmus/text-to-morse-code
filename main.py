from alphabets import morse_code_dict

# Get user message
user_message = input("Type your message here: ").lower()

# Initialise empty list to store morse code
morse_code = []

# Iterate over characters in the message
for letter in user_message:
    # Get the character from the dictionary and convert to morse code
    #'' handles any unknown characters
    character = morse_code_dict.get(letter, "")
    morse_code.append(character)

# Joins morse code list into a string with space between each letter
morse_code_string = " ".join(morse_code)

print(morse_code_string)
