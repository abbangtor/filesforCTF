def shift_character(character, position):
    if character.isalpha():
        base = ord('a') if character.islower() else ord('A')
        shifted = (ord(character) - base + position) % 26 + base
        return chr(shifted)
    elif character.isdigit():
        return str(int(character) + position)
    else:
        return character

def mirror_character(character):
    if character.isalpha():
        if character.islower():
            return chr(ord('z') - (ord(character) - ord('a')))
        else:
            return chr(ord('Z') - (ord(character) - ord('A')))
    else:
        return character

def invert_text(text):
    return text[::-1]

def encrypt_textfile(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read()

    encrypted_content = ''
    for index, char in enumerate(content, start=1):  # Start index at 1
        encrypted_char = shift_character(char, index)
        encrypted_char = mirror_character(encrypted_char)
        encrypted_content += encrypted_char

    inverted_content = invert_text(encrypted_content)

    with open(output_file_path, 'w') as file:
        file.write(inverted_content)

# Example usage:
input_file_path = r'C:\filesforCTF\UnEncryptedFile.txt'
output_file_path = r'C:\filesforCTF\EncryptedFile.txt'
encrypt_textfile(input_file_path, output_file_path)
