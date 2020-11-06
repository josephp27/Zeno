import re


def merge_dictionaries(base, primary):
    """
    :param base: dictionary to replace values with
    :param primary: dictionary whose values we care about most
    :return: merged dictionary
    """
    # create the dictionary if we pass a None
    base = base or {}
    primary = primary or {}

    merged = base.copy()
    merged.update(primary)
    return merged


def to_snake_case(section):
    """Transforms input to snake_case from formats like CamelCase

    Required Args:
        section (str) - Name of String to be converted

    Returns:
        (str) section in snake_case
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', section).lower()


def traverse_dictionary(dictionary, keys):
    """Searches dictionary for all keys in order

    Required Args:
        dictionary (dict) - Dictionary to be searched
        keys (list) - list of keys to be searched in order

    Returns:
        (str) value
    """
    curr_key = keys[0]
    curr_dictionary = dictionary[curr_key]

    for i in range(1, len(keys)):
        curr_key = keys[i]
        curr_dictionary = curr_dictionary[curr_key]

    return curr_dictionary


def convert_section_to_keys(section):
    """Splits section into its keys to be searched in order

    Required Args:
        section (str) - Period delimited str

    Returns:
        (list) keys
    """
    return section.split('.')
