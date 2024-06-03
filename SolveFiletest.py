def unshift_character(character, position):
    if character.isalpha():
        base = ord('a') if character.islower() else ord('A')
        unshifted = (ord(character) - base - position) % 26 + base
        return chr(unshifted)
    elif character.isdigit():
        return str(int(character) - position)
    else:
        return character

def uninvert_text(text):
    return text[::-1]

def decrypt_textfile(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read()

    decrypted_content = ''
    for index, char in enumerate(content, start=1):  # Start index at 1
        decrypted_char = unshift_character(char, index)
        decrypted_content += decrypted_char

    original_content = uninvert_text(decrypted_content)

    with open(output_file_path, 'w') as file:
        file.write(original_content)

# Example usage:
input_file_path = r'C:\filesforCTF\EncryptedFile.txt'
output_file_path = r'C:\filesforCTF\SolvedFile.txt'
decrypt_textfile(input_file_path, output_file_path)
