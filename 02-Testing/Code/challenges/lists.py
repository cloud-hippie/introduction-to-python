

def is_in_list(value, list_of_values):
    """
    This function checks if a value is in a list.

    arguments:
        value: An integer within a list
        list_of_values: A list of values
    """
    for x in list_of_values:
        # If the value in the for loop matches value
        if x == value:
            return True
    
    return False


def longest_string_in_list(list_of_strings):
    """
    Takes a list of strings and returns the longest string.

    arguments:
        list_of_strings: list of strings
    """
    placeholder = ""
    for string in list_of_strings:
        # Check if the length of string is > placeholder
        if len(string) >= len(placeholder):
            placeholder = string
    
    return placeholder
        
    