from alphabets import morse_code_dict

user_message = input("Type your message here: ")


user_message_lst = list(user_message)

morse_code = []

for letter in user_message_lst:
    morse_code_dict.get(letter)
    morse_code.append(morse_code_dict.get(letter))


morse_code_string = " ".join(morse_code)

print(morse_code_string)
