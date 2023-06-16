# This code formats every special character from the generated database

def format_special_char():
    try:
        with open('extension_activity_database', 'r', encoding='utf-8') as input_file:
            file_text = input_file.read()

        transformed_text = _transform_quotation_marks(file_text)
        transformed_text = transformed_text.encode('utf-8').decode('unicode_escape')
        
        with open('extension_activity_database_formatted', 'w', encoding='utf-8') as output_file:
            output_file.write(transformed_text)
    except:
        print("Error formatting file, please try again")
    

def _transform_quotation_marks(unaltered_text):
    return unaltered_text.replace('\\"', "'")