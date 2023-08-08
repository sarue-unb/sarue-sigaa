# This code formats every special character from the generated database

# def format_special_char(file_name):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as input_file:
#             file_text = input_file.read()

#         transformed_text = _transform_quotation_marks(file_text)
#         transformed_text = transformed_text.encode('utf-8').decode('unicode_escape')
        
#         with open(file_name + '_formatted', 'w', encoding='utf-8') as output_file:
#             output_file.write(transformed_text)
#     except:
#         print("Error formatting file, please try again")
    
# def _transform_quotation_marks(unaltered_text):
#     return unaltered_text.replace('\\"', '"')

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