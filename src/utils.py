def standardize_name(name):
    if type(name) != str:
        standardized_name = name 
    else:   
        lowercase_name = name.lower()
        standardized_name = lowercase_name.replace(" ","_")
    
    return standardized_name

def clean_dictionary (dictionary):
    """
    Function to standardize the values in a dict.

    Inputs: {dict}
    """
    for key, value in dictionary.items():
        # value = standardize_name(value)
        dictionary[key] = standardize_name(value)

def parse_dictionary(new_keys, dictionary):
    """
    Function to create a dictionary from an existing dictionary.

    Inputs: [list]; new_keys - a list of keys
            {dict}; row - a row dict from DictReader
    Output: {dict} 
    """
    parsed_dictionary = {}
    for key in dictionary:
        if key in new_keys:
            value = dictionary[key]
            if value:
                parsed_dictionary.update({key:value}) 
            
    if parsed_dictionary:
        return parsed_dictionary
