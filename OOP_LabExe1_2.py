#create a subroutine function for decrption of user's input string
def decrypt_str(e_text):
#create a dictionary of character substitutes for decryption
    code = {'*': 'a', '&': 'e', '#': 'i', '+': 'o', '!': 'u'}
#variable for decrypted text
    d_text = ''
#check every character from user input
    for i in user_input:
#if character from user input is in dictionary then append original character
        if i in code:
             d_text += code[i]
#else append the decrypted character
        else:
             d_text += i
#returns final decrypted text
    return d_text
#ask user for string input to decrypt
user_input = input('Enter the encrypted text that you wanted to decrypt: ')
#decrypting user input
d_text = decrypt_str(user_input)
#print output
print(f'\033[92m{d_text}')

#Enter a string to decrypt: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g.
#The Plain Text:  the quick brown fox jumps over the lazy dog.