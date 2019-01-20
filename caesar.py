import string
lower = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def alphabet_position(letter):
    for ch in letter: 
        index = lower.find(ch)
        return index
    
def rotate_character(char, rot):
    encrypted = ''
    for ch in char:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            if char.isalpha() == True:
                rotated_index = int(alphabet_position(ch)) + int(rot)
                #if char == char.lower():
                if rotated_index < 26:
                    encrypted = encrypted + lower[rotated_index]
                    return encrypted
                else:
                    encrypted = encrypted + lower[rotated_index % 26]
                    p = encrypted.upper()
                    return (p)

def main():
    User_text = input("Type a message :")
    User_rotation = input("Rotate by :")
    print(encrypt1(User_text, User_rotation))
    
if __name__ == "__main__":
    main()
      