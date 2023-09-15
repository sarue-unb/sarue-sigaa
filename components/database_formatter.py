def decode_unicode_escape(text):
    return bytes(text, 'utf-8').decode('unicode_escape')

def format_special_char(input_file_name, output_file_name):
    try:
        with open(input_file_name, 'r', encoding='utf-8') as input_file:
            file_text = input_file.read()

        decoded_text = decode_unicode_escape(file_text)

        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(decoded_text)
    except:
        print("Error formatting file, please try again")